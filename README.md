# BZF-Prüfung, die Seiten der App

Der Ordner, den die Website <https://tobiaskummer.de/bzf-pruefung/> per Subtree holt.
Er wird hier gepflegt und mit `git subtree push --prefix=store/pages web main` in das
Repo `bzf-pruefung-web` geschoben, von dort zieht ihn das Site-Repo.

- `index.html`: die Produktseite. Frage 209 und ein Stück Turm-Flug stehen als Text,
  wörtlich aus Katalog (`catalogue.json`) und Erzeuger (`sprechfunk-probe.txt`).
- `datenschutz.html`: die Datenschutzerklärung der App, die Adresse, die Google Play
  verlangt (allein erreichbar, ohne Anmeldung). Seit dem 18.09.2026 teilt sie das
  Stylesheet des Schirms, weil sie auf derselben Domain liegt, und bleibt ohne Stylesheet
  lesbar: Plays Anforderung gilt der Erreichbarkeit und dem Inhalt, nicht der Gestaltung.
  Zwilling von `../privacy-de.html` (Wache test_zusagen.py).
- `widerruf.html`: die Widerrufsbelehrung, aus `../widerruf-de.md`.
- `style.css`: der Akzent der App über dem Stylesheet des Schirms (`/style.css`), Amber
  und Grün aus Theme.kt.
- `bilder/`: die acht Ladenbilder in halber Größe (540×960), aus `../assets/screenshots/`.

Schrift und Grundfarben kommen vom Schirm (`/style.css`, `/fonts/`), auf allen Seiten.

Diese App ist kein Angebot der Bundesnetzagentur und steht in keiner Verbindung zu ihr.
