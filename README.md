# tobiaskummer.de

Der Schirm über den Apps: Startseite, Impressum, Datenschutz der Website, ein
gemeinsames Stylesheet aus den Farben von Theme.kt, und je App ein Ordner.

Diese Seite baut nichts. Jedes App-Repo erzeugt seinen Ordner selbst, mit seinem
Erzeuger und seinen Wachen; hier wird er per Subtree in seinen Pfad geholt:

    git subtree add  --prefix=bzf-pruefung https://github.com/tobkum/BZF-Pruefung.git phase-1 --squash
    git subtree pull --prefix=bzf-pruefung https://github.com/tobkum/BZF-Pruefung.git phase-1 --squash

(Der Subtree ist `store/pages/` des App-Repos; bis zum Split-Befehl dort ist das ein
Platzhalter, siehe docs/release.md im App-Repo.)

Die beiden Spiele (noch ohne GitHub-Remote) kommen aus den lokalen Repos, jeweils aus dem
Zweig `pages`, den dort `git subtree split --prefix=store/pages -b pages` erzeugt:

    git subtree pull --prefix=probe    D:/PyDev/games/probe    pages --squash
    git subtree pull --prefix=asterism D:/PyDev/games/asterism pages --squash

Beide Ordner enthalten bisher nur die Datenschutzerklärung, englisch (`privacy.html`, die
Adresse für Google Play) und deutsch (`datenschutz.html`). Sobald die Repos einen Remote
haben, die Quelle hier auf dessen URL umstellen.

Hosting: GitHub Pages unter der Domain aus `CNAME`; DNS beim Registrar mit vier
A-Records auf GitHubs Pages-Adressen und einem CNAME für www. Kein Jekyll
(`.nojekyll`), kein JavaScript, nichts nachgeladen.

## Vor jedem Push

    python bauen.py

schreibt `sitemap.xml` (alle Seiten ohne `noindex`, letztes Commit-Datum je Datei) und die
Stand-Zeile im Fuss der Startseite. `python bauen.py --check` sagt, ob beides aktuell ist;
das ist die einzige Wache dieses Repos. Nach einem Subtree-Pull also: `bauen.py`, dann
committen, dann pushen.

