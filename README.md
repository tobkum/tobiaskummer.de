# Asterism: web pages

This folder is published at <https://tobiaskummer.de/asterism/>. The site repo
(`D:/PyDev/tobiaskummer.de`) pulls it in with `git subtree`, the same way as the other apps.

- `privacy.html`: the English privacy policy. This is the URL for the Google Play listing
  (reachable on its own, no sign-in).
- `datenschutz.html`: the German twin. Keep both in sync.

The pages use the site's shared stylesheet (`/style.css`), fonts and icons.

## Publishing a change

1. Edit and commit here (in this repo).
2. Here: `git subtree split --prefix=store/pages -b pages`
3. In the site repo: `git subtree pull --prefix=asterism D:/PyDev/games/asterism pages --squash`,
   then `python bauen.py`, commit and push.

## Keep the policy true

The policy describes the release build as it is. Update it **before** a release that changes
any of these: permissions (since 12 Oct 2026: INTERNET, ACCESS_NETWORK_STATE and BILLING for Google Play Billing; no VIBRATE), what is stored
(`user://progress.json`: best ratings, solved nights by date, the puzzle in progress, the last
opened puzzle, seen rule cards incl. the swipe count, Deep Sky progress (charted skies, chosen
law/depth, deal order), the hint count of a puzzle in progress, whether the full sky is owned, settings; nothing else),
Android backup (Auto Backup on since 5 Oct 2026, `progress.json` only: release/android), purchases (the one-time "full sky" through Google Play since 12 Oct 2026), sharing (a solve's card and text line through Android's share menu since 12 Oct 2026, only to the app the player picks), ads, or any third-party library
that processes data. The web prototype's tester tools (survey, log export) are not in the app;
if they ever are, the policy needs a section like Probe's "Gameplay log".
