#!/usr/bin/env python3
"""Rate-limit-aware HTTP helpers with retries, backoff, jitter, and a JSON cache."""
import json
import os
import random
import time
import urllib.error
import urllib.request
import os as _os
CACHE_DIR = _os.environ.get("NETUTIL_CACHE") or _os.path.join(
    _os.path.dirname(_os.path.abspath(__file__)), "candidates", ".cache")
MIN_INTERVAL = {"default": 1.0, "gnomad.broadinstitute.org": 3.0, "rest.ensembl.org": 0.35}
_last = {}


def _pacing(host):
    key = next((h for h in MIN_INTERVAL if host.endswith(h)), "default")
    interval = MIN_INTERVAL[key]
    wait = _last.get(host, 0) + interval - time.monotonic()
    if wait > 0:
        time.sleep(wait)
    _last[host] = time.monotonic()


def fetch_json(url, data=None, headers=None, method=None, timeout=90,
               max_retries=6, cache_key=None, cache_ttl=86400 * 7):
    """GET/POST JSON with 429/5xx/timeout handling. Returns parsed JSON or raises."""
    host = urllib.request.urlparse(url).netloc
    os.makedirs(CACHE_DIR, exist_ok=True)
    ck = os.path.join(CACHE_DIR, (cache_key or url.replace("/", "_")[:180] +
                                  ("_" + str(len(data)) if data else "")).lstrip("_") + ".json")
    if os.path.exists(ck) and time.time() - os.path.getmtime(ck) < cache_ttl:
        with open(ck) as f:
            return json.load(f)
    hdrs = {"Accept": "application/json"}
    if data is not None:
        hdrs["Content-Type"] = "application/json"
    hdrs.update(headers or {})
    delay = 2.0
    last_err = None
    for attempt in range(max_retries):
        _pacing(host)
        try:
            req = urllib.request.Request(url, data=data, headers=hdrs, method=method)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                payload = json.load(r)
            with open(ck, "w") as f:
                json.dump(payload, f)
            return payload
        except urllib.error.HTTPError as e:
            body = b""
            try:
                body = e.read(400)
            except Exception:
                pass
            last_err = f"HTTP {e.code}: {body.decode(errors='replace')[:200]}"
            if e.code == 429 or e.code >= 500:
                retry_after = e.headers.get("Retry-After") if e.headers else None
                delay = float(retry_after) if (retry_after or "").isdigit() else min(delay * 2, 60)
                time.sleep(delay + random.uniform(0, 1.5))
                continue
            raise RuntimeError(last_err) from e
        except (TimeoutError, urllib.error.URLError, OSError) as e:
            last_err = f"{type(e).__name__}: {e}"
            time.sleep(min(delay * 2, 90) + random.uniform(0, 2))
            delay *= 2
    raise RuntimeError(f"exhausted retries ({max_retries}) on {url}: {last_err}")
