# tobiaskummer.de

Der Schirm über den Apps: Startseite, Impressum, Datenschutz der Website, ein
gemeinsames Stylesheet aus den Farben von Theme.kt, und je App ein Ordner.

Diese Seite baut nichts. Jedes App-Repo erzeugt seinen Ordner selbst, mit seinem
Erzeuger und seinen Wachen; hier wird er per Subtree in seinen Pfad geholt:

    git subtree pull --prefix=bzf-pruefung https://github.com/tobkum/bzf-pruefung-web.git main --squash

(Das ist `store/pages/` des App-Repos BZF-Pruefung, dort mit
`git subtree push --prefix=store/pages web main` in das Repo `bzf-pruefung-web` geschoben;
siehe `store/pages/README.md` im App-Repo.)

Die Spiele und Masinop (noch ohne GitHub-Remote) kommen aus den lokalen Repos, jeweils aus
dem Zweig `pages`, den dort `git subtree split --prefix=store/pages -b pages` erzeugt:

    git subtree pull --prefix=probe    D:/PyDev/games/probe            pages --squash
    git subtree pull --prefix=asterism D:/PyDev/games/asterism         pages --squash
    git subtree pull --prefix=masinop  D:/PyDev/apps/ph-money-tracker pages --squash

Probe enthält nur die Datenschutzerklärung, englisch (`privacy.html`, die Adresse für Google Play)
und deutsch (`datenschutz.html`). Asterism dazu seit 04.11.2026 ein Pressekit (`press.html`, englisch,
immer dunkel, mit eigenem `style.css` und den Bildern in `press/`). Masinop hat nur `privacy.html`
(englisch mit tagalischer Kurzfassung). Probe ist pausiert (seit 29.09.2026): seine Seiten bleiben
online, stehen aber nicht mehr in der App-Liste von `datenschutz.html`. Sobald die Repos einen
Remote haben, die Quelle hier auf dessen URL umstellen.

`screentrackr/` ist die Ausnahme: kein Subtree, sondern **hier** gepflegt (seit 04.11.2026), weil das
App-Repo (`D:/PyDev/screentrackr`, die Web-App für overmind-studios.de) keinen Seiten-Ordner hat. Darin
nur die Nutzungsbedingungen für Googles Händlerangabe, englisch (`terms.html`, der Link für Google Play)
und deutsch (`nutzungsbedingungen.html`).

Hosting: GitHub Pages unter der Domain aus `CNAME`; DNS beim Registrar mit vier
A-Records auf GitHubs Pages-Adressen und einem CNAME für www. Kein Jekyll
(`.nojekyll`), kein JavaScript, nichts nachgeladen. Eine Ausnahme beim JavaScript: die
Seiten der BZF-Prüfung (Produktseite und die 28 Themenseiten) tragen ein kleines Skript, das eine
Frage beim Antippen aufdeckt, wie in der App; ohne Skript steht jede Antwort samt Erklärung offen
da, es fehlt also nichts und nichts ist falsch. Schriften liegen in `/fonts/` und in den
App-Ordnern (`asterism/fonts/`, `ribband/fonts/`), je mit ihrer Lizenz daneben; nichts kommt von
einem fremden Host.

## Die Gestalt des Schirms (seit 20.11.2026)

Die Startseite ist ein Werkverzeichnis, gesetzt wie ein Flugbuch: ein Raster aus zwölf Spalten,
die ersten drei sind die Randspalte, und darin stehen in B612 Mono (der Schrift aus dem Cockpit,
die schon im Repo liegt) nur die Angaben, also Abschnitt, Plattform, Art und Preis; der Text
beginnt in der vierten Spalte, auf derselben Kante wie Impressum und Datenschutz. Den Text trägt
Source Serif 4 (Adobe, SIL OFL 1.1, `fonts/SourceSerif4-OFL.txt`; aus Ribbands Leseschriften auf
Latin geschnitten), aufrecht und ruhig, die grossen Zeilen im leichtesten Schnitt; kursiv nie,
das ist Ribbands Leinen. Roboto bleibt die Schrift der Produktseiten von BZF-Prüfung und
Asterism und lädt auf den Seiten des Schirms nicht. Die neue Gestalt gilt nur unter
`<body class="schirmseite">` (Startseite, Impressum, Datenschutz); die Rechtsseiten der Apps
behalten ihre bisherige. Jede App steht in einer Zeile
zwischen Haarlinien, nicht in einer Karte: Angaben, Name, zwei Sätze, das Badge und ein
schlichter Verweis, rechts ihr Bildschirm auf einer Tafel in ihrer eigenen Grundfarbe (Amber,
Nachthimmel, Leinen), so trägt jede App ihren Akzent und der Schirm keinen. Die Texte bleiben
Sätze in der ersten Person, ohne Werbewörter; geändert wurde nur, was nach Vorlage klang.

Wer die Klassen kennt: `.zeile` und `.werk` (Raster), `.rand-titel`, `.angaben`, `.tafel` mit
`--werk`, `--werk-ink`, `--werk-grund` je App. Ribbands Produktseite hängt an `.wrap` (64rem;
das Leseband rechnet mit der halben Breite), an `header.site`, `.marke`, `nav`, `.actions`,
`.play`, `.badge` und `footer.site`; die bleiben in Mass und Bau, wie sie sind.

## Vor jedem Push

    python bauen.py

schreibt `sitemap.xml` (alle Seiten ohne `noindex`, letztes Commit-Datum je Datei) und die
Stand-Zeile im Fuss der Startseite. `python bauen.py --check` sagt, ob beides aktuell ist, und
schlägt fehl, wenn eine Seite oder ein Stylesheet etwas von einem fremden Host lädt (Schrift,
Stylesheet, Skript, Bild; auch `@import`, `url(…)` und `preconnect`; Verweise wie canonical
sind erlaubt); das ist die einzige Wache dieses Repos. Nach einem Subtree-Pull also: `bauen.py`, dann
committen, dann pushen.

