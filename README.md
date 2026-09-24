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
any of these: permissions (today only VIBRATE, no INTERNET), what is stored
(`user://progress.json`: best ratings, solved nights by date, the puzzle in progress, the last
opened puzzle, seen rule cards, settings; nothing else),
Android backup (`allowBackup="false"`), purchases (none yet), ads, or any third-party library
that processes data. The web prototype's tester tools (survey, log export) are not in the app;
if they ever are, the policy needs a section like Probe's "Gameplay log".
