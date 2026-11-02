#!/usr/bin/env python3
"""Regenerate TELEMETRY.json for the n8toriousai.com package.
Run: python tools/refresh-site-telemetry.py — never hand-edit the JSON."""
import json, hashlib
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = {
    "index.html": "The page. Act 1: framed world stage (nothing overlays the world). Act 2: the proof — stats strip + one article per project.",
    "world.html": "The living 3D galaxy (Harakiri Unified build) shown in the Act 1 frame. Site copy only: gaze auto-inspect is disabled here so panels open on click, never on their own. The canonical build lives with the SI Core work, untouched.",
    "privacy.html": "Privacy policy (Temple / Play). FROZEN — do not edit; the Play listing depends on its wording.",
    "temple-1.0.apk": "Temple — Daily Bible, Android install file (binary; linked from the Temple article).",
    "capsuleos.apbx": "CapsuleOS playbook v0.1.0 (binary; linked from the Capsule Toolbox article).",
    "img/ball.png": "SI Core article image — the Ball.",
    "img/prototype.png": "PoeTchi article image — the Complete Prototype.",
    "img/altiminac.png": "Alchemedies article image — ALTIMINAC running.",
    "img/onion.png": "Spare image (the Onion), not currently placed.",
}

def main():
    files = []
    for name, role in FILES.items():
        p = ROOT / name
        if not p.exists():
            files.append({"path": name, "missing": True})
            continue
        data = p.read_bytes()
        files.append({"path": name, "bytes": len(data),
                      "sha256": hashlib.sha256(data).hexdigest()[:16],
                      "role": role})
    idx = (ROOT / 'index.html').read_text(errors='ignore')
    t = {
        "format": "site-telemetry/1",
        "generated": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        "site": {
            "domain": "n8toriousai.com",
            "owner": "Nathan Brown — a solo developer from Brunswick, Ohio (brand: N8toriousAi)",
            "hosting": "Cloudflare Pages — deployment is a MANUAL upload of the site zip by the owner. This repo being updated does not change the live site.",
            "repo": "https://github.com/IN8torious/n8toriousai.com",
        },
        "files": files,
        "pageFacts": {
            "articles": idx.count('<article'),
            "hero": "Framed stage: brand bar, world at 60svh with zero overlays, action strip below. Verified by screenshot (desktop + portrait).",
            "statsStrip": "27,811 lines (v2.0.0 release, scoped) · 19,652 PoeTchi checks / 0 failures · 10 kernels (9 packaged + Nimbusis) · 29 languages · 66 Bible books · 0 trackers",
            "plainLanguage": "Full clarity pass applied 2026-11-02 — no insider jargon without an in-line explanation.",
        },
        "hardRules": [
            "privacy.html is frozen. Do not edit it.",
            "world.html: keep gaze auto-inspect disabled (search 'gaze auto-inspect OFF'). Click-to-inspect must stay.",
            "Numbers on the page are counted, not rounded. If a number changes, recount from its source first (see TELEMETRY regen + article notes).",
            "Deploy = owner uploads the zip to Cloudflare Pages. Never claim the live site changed from a repo or zip change.",
            "The owner's own work credits the brand N8toriousAi, never a personal name, in lineage contexts.",
        ],
    }
    (ROOT / 'TELEMETRY.json').write_text(json.dumps(t, indent=2))
    print('site TELEMETRY.json written —', t['generated'])

if __name__ == '__main__':
    main()
