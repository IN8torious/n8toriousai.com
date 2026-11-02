# n8toriousai.com — site source

The public proof page for **N8toriousAi** (Nathan Brown, solo
developer, Brunswick, Ohio). Static site, no build step: open
`index.html` or serve the folder.

- `TELEMETRY.json` — machine-readable map of the package (files,
  roles, hashes, verified facts). Start there. Regenerate with
  `python tools/refresh-site-telemetry.py`.
- `.github/copilot-instructions.md` — the rules of this package
  (frozen privacy page, no-overlay hero, the world.html gaze fix,
  counted numbers, manual deploy).
- Deployment: the owner uploads the site zip to Cloudflare Pages
  by hand. This repo does not auto-deploy.

Binaries (Temple APK, CapsuleOS .apbx) and images ride in the
deployment zip, not in git — TELEMETRY.json lists them with hashes.
