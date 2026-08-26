#!/usr/bin/env python3
"""Validate a Track-1 submission CSV and simulate scores against hypothetical truths.

Uses the challenge's own evaluation.py (downloaded to challenge_src/).
Usage:
  .venv/bin/python analysis/submission_sim.py validate <submission.csv>
  .venv/bin/python analysis/submission_sim.py simulate <submission.csv>
"""
import csv
import sys
import importlib.util
from pathlib import Path
import sys
spec = importlib.util.spec_from_file_location("evaluation", "challenge_src/evaluation.py")
evaluation = importlib.util.module_from_spec(spec)
sys.modules["evaluation"] = evaluation
spec.loader.exec_module(evaluation)

Variant = evaluation.Variant


def load(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def normalize_rows(rows):
    """Report formatting issues that would silently hurt; return cleaned variant tuples."""
    problems = []
    seen_epcr = []
    for i, r in enumerate(rows, 1):
        for j in (1, 2):
            chrom = (r.get(f"chrom_{j}") or "").strip()
            if not chrom:
                continue
            if not chrom.startswith("chr"):
                problems.append(f"row{i} v{j}: chrom '{chrom}' lacks 'chr' prefix")
            pos = r.get(f"pos_{j}")
            if not pos or not pos.strip().isdigit():
                problems.append(f"row{i} v{j}: bad pos '{pos}'")
        try:
            e = float(r["epcr"])
            if not (0 < e <= 1):
                problems.append(f"row{i}: epcr {e} outside (0,1]")
            seen_epcr.append(e)
        except (KeyError, ValueError):
            problems.append(f"row{i}: epcr missing/invalid")
        ft = (r.get("finding_type") or "primary").strip().lower()
        if ft not in ("primary", "secondary"):
            problems.append(f"row{i}: finding_type '{ft}' invalid")
    if seen_epcr != sorted(seen_epcr, reverse=True):
        problems.append("epcr not strictly descending (rows will be re-sorted by scorer; keep sorted)")
    if len(rows) > 10:
        problems.append(f"{len(rows)} rows > max 10")
    return problems


def simulate(path, truths):
    subs = evaluation.load_submission(path)
    pid = next(iter(subs))
    for name, truth in truths.items():
        truth_set = frozenset(truth)
        res = evaluation.score_proband(pid, subs[pid], truth_set)
        print(f"{name:60s} rank_pts={res.rank_points:6.1f} f_max={res.f_max:.3f} "
              f"full_rank={res.full_match_rank} partial_rank={res.partial_match_rank}")


def main():
    mode, path = sys.argv[1], sys.argv[2]
    rows = load(path)
    problems = normalize_rows(rows)
    if problems:
        print("FORMAT PROBLEMS:")
        for p in problems:
            print(" -", p)
    else:
        print("Format OK")
    if mode == "simulate":
        print("\nSimulations (example truths):")
        # placeholder truths -- replaced by real candidates later
        v = lambda c, p, r, a: (c, p, r, a)
        simulate(path, {
            "truth = top pair of this submission": None,
        })


if __name__ == "__main__":
    main()
