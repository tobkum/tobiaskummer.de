# BZF-Prüfung, die Seiten der App

Der Ordner, den die Website <https://tobiaskummer.de/bzf-pruefung/> per Subtree holt.
Er wird hier gepflegt und mit `git subtree push --prefix=store/pages web main` in das
Repo `bzf-pruefung-web` geschoben, von dort zieht ihn das Site-Repo.

- `index.html`: die Produktseite. Frage 209 und ein Stück Turm-Flug stehen als Text,
  wörtlich aus Katalog (`catalogue.json`) und Erzeuger (`sprechfunk-probe.txt`).
- `datenschutz.html`: die Datenschutzerklärung der App, in sich geschlossen (Inline-CSS),
  weil Google Play sie allein erreichbar braucht; Zwilling von `../privacy-de.html`.
- `widerruf.html`: die Widerrufsbelehrung, aus `../widerruf-de.md`.
- `style.css`: der Akzent der App über dem Stylesheet des Schirms (`/style.css`), Amber
  und Grün aus Theme.kt.
- `bilder/`: die acht Ladenbilder in halber Größe (540×960), aus `../assets/screenshots/`.

Schrift und Grundfarben kommen vom Schirm (`/style.css`, `/fonts/`); nur die
Datenschutzseite trägt alles selbst.

Diese App ist kein Angebot der Bundesnetzagentur und steht in keiner Verbindung zu ihr.
