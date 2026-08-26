#!/usr/bin/env python3
"""Schema-aware Open Targets GraphQL client: resolves query fields via introspection."""
import json
import sys

sys.path.insert(0, "track1/analysis")
from netutil import fetch_json

API = "https://api.platform.opentargets.org/api/v4/graphql"
_cache = {}

def fields_of(type_name):
    if type_name in _cache:
        return _cache[type_name]
    q = ('query { __type(name: "%s") { fields { name type { name kind ofType { name kind ofType '
         '{ name kind ofType { name kind ofType { name } } } } } } } }' % type_name)
    res = fetch_json(API, data=json.dumps({"query": q}).encode(),
                     cache_key=f"ot_introspect_{type_name}")
    t = res["data"]["__type"]
    out = {} if t is None else {f["name"]: f for f in t["fields"]}
    return out

def resolve(type_name, want):
    """Build selection set from `want` spec: dict leaf=True or dict sub-spec."""
    lines = []
    for key, sub in want.items():
        fs = fields_of(type_name)
        if key not in fs:
            raise KeyError(f"{type_name} has no field '{key}'; available: {sorted(fs)[:40]}")
        if sub is True:
            lines.append(key)
        else:
            f = fs[key]
            t = f["type"]
            chain = []
            names = []
            while t:
                chain.append(f"{t.get('name')}/{t.get('kind')}")
                if t.get("name"):
                    names.append(t["name"])
                t = (t.get("ofType") or {})
            sub_type = names[-1] if names else None
            if sub_type is None:
                raise KeyError(f"field '{key}' on {type_name} has no object type; chain={chain}")
            lines.append(key + " { " + resolve(sub_type, sub) + " }")
    return " ".join(lines)

def query_target(ensembl_id, spec):
    sel = resolve("Target", spec)
    q = 'query { target(ensemblId: "%s") { %s } }' % (ensembl_id, sel)
    return fetch_json(API, data=json.dumps({"query": q}).encode(),
                      cache_key=f"ot_target_{ensembl_id}_{str(abs(hash(json.dumps(spec, sort_keys=True))))[:12]}")


if __name__ == "__main__":
    spec = {
        "id": True, "approvedSymbol": True,
        "functionDescriptions": True,
        "tractability": {"label": True, "modality": True},
        "drugAndClinicalCandidates": {"rows": {
            "maxClinicalStage": True,
            "drug": {"name": True},
            "diseases": {"diseaseFromSource": True},
        }},
        "pathways": {"pathway": True},
    }
    res = query_target("ENSG00000156970", spec)
    t = res["data"]["target"]
    json.dump(t, open("track1/analysis/candidates/ot_bub1b_profile.json", "w"), indent=1)
    print("==", t["approvedSymbol"], t["id"])
    print("function:", " ".join(t.get("functionDescriptions") or [])[:400])
    print("targetClass:", [x.get("label") for x in t.get("targetClass") or []])
    print("tractability:", sorted({(x["label"], x["modality"]) for x in t.get("tractability") or []}))
    rows = (t.get("drugAndClinicalCandidates") or {}).get("rows") or []
    print("drug/clinical candidates:", len(rows))
    for r in rows[:12]:
        print("  ", (r.get("drug") or {}).get("name"), "| stage", r.get("maxClinicalStage"),
              "|", [d.get("diseaseFromSource") for d in r.get("diseases") or []][:3])
    print("DepMap tissues:", len(t.get("depMapEssentiality") or []))
    print("pathways:", [x["pathway"] for x in t.get("pathways") or []][:10])
    gc = t.get("geneticConstraint") or []
    print("constraint:", [(g["constraintType"], g.get("obs"), g.get("oe")) for g in gc])
    print("mouse:", [(m.get("modelPhenotypeLabel"), m.get("biologicalProcess")) for m in (t.get("mousePhenotypes") or [])[:6]])
