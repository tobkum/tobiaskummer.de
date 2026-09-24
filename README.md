# Probe: web pages

This folder is published at <https://tobiaskummer.de/probe/>. The site repo
(`D:/PyDev/tobiaskummer.de`) pulls it in with `git subtree`, the same way as the other apps.

- `privacy.html`: the English privacy policy. This is the URL for the Google Play listing
  (reachable on its own, no sign-in).
- `datenschutz.html`: the German twin. Keep both in sync.

The pages use the site's shared stylesheet (`/style.css`), fonts and icons.

## Publishing a change

1. Edit and commit here (in this repo).
2. Here: `git subtree split --prefix=store/pages -b pages`
3. In the site repo: `git subtree pull --prefix=probe D:/PyDev/games/probe pages --squash`,
   then `python bauen.py`, commit and push.

## Keep the policy true

The policy describes the release build as it is. Update it **before** a release that changes
any of these: permissions (today only VIBRATE, no INTERNET), the local gameplay log
(`user://telemetry.jsonl`, recorded in every build; export only in test builds via the
`playtest` feature tag), Android backup (`allowBackup="false"`), purchases (none yet), ads or
any third-party library that processes data.
