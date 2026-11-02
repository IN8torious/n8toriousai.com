# n8toriousai.com — instructions for Copilot

This repo is the source of the public site **n8toriousai.com** — the
proof page for Nathan Brown (brand: N8toriousAi), a solo developer
from Brunswick, Ohio. Read `TELEMETRY.json` first: it lists every
file, its role, size, and hash, plus the page's verified facts.
Regenerate it after changes: `python tools/refresh-site-telemetry.py`.

## Layout

- `index.html` — the whole page. Act 1 is a framed stage holding the
  world; Act 2 ("The Proof") is a stats strip + one article per
  project (Temple, Toolbox Bible, Capsule Toolbox, Capsule Ecology,
  SI Core, PoeTchi, Nimbusis, Agent Toolbox, Alchemedies).
- `world.html` — the living 3D galaxy in the Act 1 frame (Harakiri
  Unified build, site copy).
- `privacy.html` — **FROZEN.** The Google Play listing depends on its
  exact wording. Never edit it.
- Binaries (`temple-1.0.apk`, `capsuleos.apbx`) and images live in the
  deployment zip; git carries the text source. See TELEMETRY.json.

## Hard rules

- **Nothing overlays the world.** The hero is a framed stage: brand
  bar above, world in a bordered frame, names/ENTER/warning in a
  strip below. The old fullscreen veil layout was removed on the
  owner's orders — do not bring it back.
- **world.html gaze fix:** the world's gaze camera used to auto-open
  its inspector panel for whatever crossed screen center (the
  Galactic Core sits at center, so the panel opened unasked and
  covered the page). It is disabled in this copy — search for
  `gaze auto-inspect OFF`. Click-to-inspect stays. Do not re-enable.
- **Plain language.** The page passed a full clarity review: every
  number and term must be understandable by a first-time visitor.
  Gloss any technical term in-line or cut it.
- **Numbers are counted, not rounded.** Recount from the source
  before changing any stat (the strip's sources are in TELEMETRY.json).
- **Deploy is manual.** The owner uploads the site zip to Cloudflare
  Pages. A change here does NOT change the live site — say so when
  summarizing.
