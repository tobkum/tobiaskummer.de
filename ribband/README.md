# Ribband, die Seiten der App

Der Ordner, den die Website unter <https://tobiaskummer.de/ribband/> per Subtree holt, wie die
Ordner von Asterism, BZF-Prüfung und Masinop. Er wird nicht von Hand gepflegt: jede Seite
entsteht mit `store/tools/pages.py` aus einer Markdown-Datei in `docs/release/store/`, und
nur dort wird geändert. Datum und Version stehen an einer Stelle, `store/pages.json`.

- `privacy.html`: die Datenschutzerklärung, englisch. Das ist die Adresse für Google Play,
  für den OAuth-Zustimmungsbildschirm und für die Zeile „Privacy policy“ in der App (allein
  erreichbar, ohne Anmeldung). Quelle `privacy-policy-en.md`; der Abschnitt „For the owner“
  darin wird nicht veröffentlicht.
- `datenschutz.html`: der deutsche Zwilling, Quelle `privacy-policy-de.md`. Beide gemeinsam
  ändern.
- `purchase.html` / `kauf.html`: Kauf von Pro, Erstattung und **die vollständige gesetzliche
  Widerrufsbelehrung samt Muster-Widerrufsformular**. Der deutsche Text ist Asterisms
  `kauf.html`, und der ist BZF-Prüfungs juristisch geprüfter Text (Prüfung bestanden am
  28.10.2026, Gründe und Quellen in `D:/PyDev/bzf-trainer/store/kauf-de.md`): Google Play ist
  in Deutschland Merchant of Record, aber die deutsche Lesart (IHK, eRecht24) lässt die
  Belehrungspflicht beim Anbieter, darum steht beides da. Geändert sind nur der Name des Kaufs
  (Pro), was eine Erstattung in der App bewirkt, und „Fragen zur App“. Nicht kürzen.
  **Vor der ersten Veröffentlichung vom Inhaber rechtlich prüfen lassen**, wie die Vorbilder.
  Die englische Seite ist eine Übersetzung und sagt das. Beide `noindex`, wie bei Asterism.
  Quellen `kauf-de.md`, `purchase-en.md`.
- `export-format.html` (POCKET-3): die Beschreibung des Exportformats, nur englisch und ohne
  Zwilling (die deutsche Produktseite sagt beim Verweis, dass sie englisch ist). Quelle ist
  `docs/export-format.md` selbst, die Datei, nach der sich der Code richtet; nur ihre
  HTML-Kommentare bleiben draussen. Rahmen der rechtlichen Seiten, indexierbar, ohne hreflang.
  Wache: `test_seiten.py`, Klasse `Exportformat` (aktuell, Rahmen, keine internen Notizen, Stimme).
- `terms.html` / `nutzungsbedingungen.html`: die Nutzungsbedingungen, der Link, den Google
  Play bei der Händlerangabe verlangt (Ribband verkauft Pro, also gilt derselbe Grund wie bei
  Asterism und BZF-Prüfung). Was kostenlos ist, was Pro bringt, Erstattung schliesst Pro und
  lässt die Bibliothek. Quellen `terms-en.md`, `nutzungsbedingungen-de.md`.

Die Seiten nutzen das Stylesheet, die Schriften und die Symbole des Schirms (`/style.css`),
mit Kopf, Kopfzeile und Fuss Zeichen für Zeichen wie Asterisms Seiten. Ohne Stylesheet
bleiben sie lesbar. Ribbands eigenes Aussehen trägt nur die Produktseite.

## Die Produktseite

`index.html` (englisch, <https://tobiaskummer.de/ribband/>) und `de/index.html` (deutsch,
<https://tobiaskummer.de/ribband/de/>, in
der du-Form wie die App und wie BZF-Prüfungs Produktseite; die rechtlichen Seiten bleiben beim
Sie). Von Hand geschrieben, nicht aus Markdown erzeugt (`pages.HANDGESCHRIEBEN`): sie trägt
Bilder, eine eigene Gestalt und strukturierte Daten, die der Markdown-Rahmen nicht hergibt.
Beide gemeinsam ändern; die Wache vergleicht ihren Bau Tag für Tag.

- Kopfzeile wie bei BZF-Prüfung und Asterism: der Name der App (verlinkt auf die Seite selbst),
  rechts die andere Sprache und das Impressum; die rechtlichen Seiten behalten Asterisms Rahmen.
- Aufbau: der Umschlag (Tuch, die gestapelte Marke, „Kept for later.“, das `<h1>`, Google
  Play, zwei Bildschirme halb auf dem Tuch), dann Aufheben (Teilen-Menü; der Browser am Computer mit der
  Erweiterung, ihren Badges und dem Bild ihres Fensters; Eingang, Regal, Archiv, Suche), Lesen (beginnt mit den drei Farbschemata nebeneinander, dann der Text; E-Ink),
  Deine Bibliothek (ein Satz, dann die Tatsachen als Begriffsliste: Werbung, Verbindungen,
  Synchronisierung, Import, Export), Kostenlos und Pro (zwei Spalten unter Linien wie ein
  Inhaltsverzeichnis, ohne Preis; daneben ein Satz, was hier kostenlos ist, wofür manche anderen ein Abo
  verlangen), Fragen (neun kurze Antworten, darunter die nach der Browser-Erweiterung und, POCKET-3, „Was
  ist, wenn es Ribband nicht mehr gibt?“ mit dem Verweis auf das Exportformat), der hintere Umschlag (Tagline, Google Play, die rechtlichen Seiten).
- Jede Tatsache stammt aus `docs/release/store/listing-*.md` (in `claims-check.md` am Code
  belegt), den Entscheidungen in `docs/decisions/REVIEW-3.md` (Gespeicherte Suchen, Regal,
  Leiste Eingang · Regal · Archiv, weisse E-Ink-Leisten, Schriftnamen ohne Version) und dem
  Import im Code (`ForeignImporter.kt`: Titel, Datum, Schlagwörter, Favoriten, gelesen oder
  nicht; Ordner als Regale; aus Omnivore Texte und Markierungen). Ändert sich eines davon,
  ändert sich die Seite mit.
- `style.css`: Clothbound über dem Schirm. Die Farben sind die Tokens der App
  (`core/designsystem/…/Tokens.kt`), hell und Ink night über `prefers-color-scheme`.
- `fonts/`: Literata (OFL, Lizenz daneben) als Latin-Teilmenge in WOFF2, aufrecht 400 bis 600
  mit optischer Grösse (71 KB) und kursiv 400 (42 KB), aus `design/brand/fonts/` mit fontTools
  geschnitten. Fehlt die Schrift, steht Georgia an ihrer Stelle, auf Literatas Masse gebracht.
- `bilder/`: Googles offizielle Badges (`google-play-badge-en.png`, `-de.png`), unverändert
  kopiert von der Website (`/asterism/press/`, `/bzf-pruefung/bilder/`), so gross und mit dem
  Freiraum, wie `/style.css` sie setzt (`.play`, `.badge`); die Bildschirme als WebP (540 px breit) und die Marke als SVG, geschrieben von
  `store/tools/bilder.py` aus der lokalen Screenshot-Basis und den Gerätefotos der Leseseite
  (beide nicht im Repo); dazu `ribband-1200x630.png`, das Vorschaubild für geteilte Links,
  aus der Feature-Grafik der Marke ins Mass 1200 x 630 gesetzt. Zusammen unter 1 MB; die
  Wache lässt höchstens 2 MB zu. Werden die Bildschirme der App anders, `bilder.py` neu
  laufen lassen: jede Quelle steht in einer Zeile der Tabelle `BILDER`.
  Stand der Bildschirme: die Basis von `main` 02aebb0f (20.11.2026), mit den englischen
  Beispieldaten, der dichteren E-Ink-Zeile (`eink-pages-inbox-1.png`) und der vollen Suche
  (`library-search-full.png`). Danach die Bildmasse in `index.html`/`de/index.html`
  nachziehen, falls sie sich ändern (die Wache meldet es).
- Der Unterordner `de/` reist mit: `git subtree split --prefix=store/pages` nimmt den ganzen
  Baum unter dem Präfix mit, und `bauen.py` sucht Seiten mit `rglob("*.html")`, macht aus
  `ribband/de/index.html` die Adresse `https://tobiaskummer.de/ribband/de/` und nimmt sie in
  `sitemap.xml` auf.
- Suche: Titel und Beschreibung je Sprache, canonical, hreflang en/de/x-default, Open Graph,
  JSON-LD (`MobileApplication`, Autor über die `@id` der Person auf der Startseite, ohne
  Preis und ohne Bewertung, siehe `test_produktseite.py`). Die Suchbegriffe und wo die Seite
  sie beantwortet: `docs/release/store/keywords-web.md`. Indexierbar.

### Am Tag der Veröffentlichung prüfen

Die Seite geht erst mit der App online. Sie ist die Seite für danach; nur eines hängt am
Eintrag bei Google Play und lässt sich vorher nicht prüfen (keine Wache ruft Play ab):

1. **Die Adresse bei Google Play.** Überall steht
   `https://play.google.com/store/apps/details?id=com.tobkum.ribband`, aus der
   Anwendungs-ID. Im Browser öffnen: zeigt sie Ribbands Eintrag, ist es gut. Die Wache
   `test_jeder_verweis_hat_ein_ziel` lässt nur diese eine Play-Adresse zu.
2. **Die Browser-Erweiterung** (PAGES-3). Ihre beiden Adressen gehören nach
   `store/pages.json` (`erweiterung.chrome`, `erweiterung.firefox`); `pages.py` schreibt die
   offiziellen Badges dann zwischen die Marken `<!-- erweiterung: … -->` und
   `<!-- /erweiterung -->` in beide Seiten, eine leere Adresse heisst: kein Badge. Den Platz für
   das Bild des Fensters der Erweiterung (`PLATZ`) durch das Bild ersetzen. Dann
   `python store/tools/pages.py --release` und `PAGES_RELEASE=1 python -m unittest discover -s
   store/tools/tests -t .`: beide schlagen fehl, solange eine Adresse oder das Bild fehlt
   (`docs/release/release-checklist.md` C8). Quellen und Regeln der Badges:
   `docs/decisions/PAGES-3.md`; die Markenzeilen von Google und Mozilla stehen im Fuss.
Danach im Site-Repo und in der Search Console:

- Auf der Startseite (`index.html`) und in ihrer App-Liste eine Karte für Ribband mit Link auf
  `/ribband/`, wie BZF-Prüfung und Asterism; in `datenschutz.html` die Zeile unten.
- `python bauen.py` nimmt beide Seiten von selbst in `sitemap.xml` auf (sie sind nicht
  `noindex`).
- In der Google Search Console (Property `tobiaskummer.de`) die Sitemap neu einreichen und
  `https://tobiaskummer.de/ribband/` und `…/ribband/de/` per URL-Prüfung zur
  Indexierung anmelden; in den Bing Webmaster Tools ebenso.
- Eine geteilte Vorschau einmal ansehen (etwa im Post-Inspector von LinkedIn oder in einem
  Messenger), ob `ribband-1200x630.png` erscheint.
- Auf der Play-Seite der App die Website-Adresse auf `https://tobiaskummer.de/ribband/`
  setzen.

## Ändern

    python store/tools/pages.py
    python -m unittest discover -s store/tools/tests -t .

Der Erzeuger schreibt die acht rechtlichen Seiten und das Exportformat; `--check` sagt nur, ob sie aktuell sind.
Die Produktseite wird von Hand geändert, ihre Bilder mit `python store/tools/bilder.py`
(braucht Pillow und Chrome). Die Wachen in `store/tools/tests/` (nur Standardbibliothek):

- `test_seiten.py`: Seiten aktuell zu ihren Quellen; Zwillinge mit gleich vielen und gleich
  nummerierten Abschnitten; keine eckigen Klammern im Text ausser den offenen Platzhaltern,
  die dort in `OFFEN` stehen (derzeit keiner); jeder Verweis und jedes hreflang-Ziel vorhanden; der Rahmen
  gleich dem von Asterism (setzt aus, wenn das Site-Repo nicht neben diesem liegt;
  `RIBBAND_SITE` zeigt woandershin); Datenschutz und Bedingungen indexierbar für `bauen.py`;
  keine Gedankenstriche, keine Ausrufezeichen, „ich“ statt „wir“ und Sie-Form.
- `test_produktseite.py`: die Produktseite. Zwillinge gleich gebaut; kein Skript ausser den
  JSON-LD-Daten, kein style-Attribut, nichts von einem anderen Server geladen; jeder Verweis
  vorhanden, die rechtlichen Seiten verlinkt, nur die eine Play-Adresse, das offizielle Badge
  der Website in der Sprache der Seite an beiden Stellen; jedes Bild mit
  Alternativtext und `width`/`height`, die zu seinem Mass passen, unter dem Umschlag
  `loading="lazy"`; Bilder zusammen unter 2 MB, das Vorschaubild unter 300 KB; ein `<h1>`,
  Titel 45 bis 62 und Beschreibung 120 bis 160 Zeichen; canonical, hreflang und `og:url`
  stimmig; Open Graph vollständig, Vorschaubild 1200 x 630; JSON-LD gültig, ohne Preis und
  Bewertung; indexierbar; keine Gedankenstriche, keine Ausrufezeichen, „ich“, Deutsch in der
  du-Form, die Tagline englisch, die neuen Namen (Saved searches, Regal); die Badges der
  Erweiterung unverändert (Prüfsumme), nur mit Adresse und so, wie `pages.json` sie verlangt,
  und mit `PAGES_RELEASE=1` die Wache für die Veröffentlichung.
- `test_veroeffentlicht.py`: die veröffentlichten Seiten gegen den committeten Stand, nach
  BZF-Prüfungs Wache. Ohne Netz setzt sie aus, ebenso solange die Adressen 404 geben (noch
  nie veröffentlicht), und `PAGES_OFFLINE=1` schaltet den Abruf ab. Dem frisch Committeten
  lässt sie fünfzehn Minuten.

## Veröffentlichen: zwei Sprünge

Beide lassen sich vergessen, und beim Vergessen ist im Repo alles grün; dafür gibt es
`test_veroeffentlicht.py`. Ribband hat keinen Remote für die Seiten, sie gehen wie bei
Asterism über einen lokalen Zweig `pages`.

1. In diesem Repo, auf `main` (Arbeitskopie `D:/PyDev/rl/main`), nach Erzeuger und
   Wachen:

       git subtree split --prefix=store/pages -b pages

2. Im Site-Repo `D:/PyDev/tobiaskummer.de`, **beim ersten Mal** `add`, danach `pull`:

       git subtree add  --prefix=ribband D:/PyDev/rl/main pages --squash
       git subtree pull --prefix=ribband D:/PyDev/rl/main pages --squash

   dann

       python bauen.py
       git add -A
       git commit -m "Ribband: Datenschutzerklärung, Kauf und Nutzungsbedingungen"
       git push

`D:/PyDev/rl/main` ist die Arbeitskopie, in der `main` ausgecheckt ist (`git worktree list`); der
Zweig `pages` gehört allen Arbeitskopien desselben Repos.

## Was das Site-Repo einmal braucht

- In `datenschutz.html` unter „Die Apps“ eine Zeile, in der Art der anderen (Stand der Seite
  mitziehen):

      <p><a href="/ribband/datenschutz.html">Ribband</a> (<a href="/ribband/privacy.html" hreflang="en" lang="en">English</a>): die App zum späteren Lesen speichert Links und Artikel auf dem Gerät, hat kein Konto und keine Werbung; ins Netz geht sie, um die gespeicherten Seiten zu laden, für die freiwillige Synchronisierung über das eigene Google Drive und für den Kauf über Google Play.</p>

- In `README.md` die Quelle neben Asterism und Masinop:

      git subtree pull --prefix=ribband  D:/PyDev/rl/main      pages --squash

  und ein Satz zum Inhalt: Datenschutzerklärung englisch (`privacy.html`, die Adresse für
  Google Play) und deutsch, Kauf und Erstattung, Nutzungsbedingungen, je als Zwillinge.

## Die Erklärung wahr halten

Die Erklärung beschreibt den Release-Bau, wie er ist. Sie wird **vor** einem Release
geändert, das eines davon ändert: Berechtigungen (`app/release-manifest-allowlist.txt`), was
die App ins Netz schickt und wohin (`docs/release/store/data-safety.md`, mit Datei und Zeile),
die Synchronisierung, der Kauf, Androids Sicherung und Übertragung
(`app/src/main/res/xml/data_extraction_rules.xml`), Seitenmeldungen, Vorlesen, und jede
Bibliothek, die Daten verarbeitet. Die Bedingungen und die Kaufseite ändern sich mit dem, was
Pro bringt.

Die Presseseite `press.html` (englisch, von Hand, `pages.PRESSE`) mit ihren Dateien in `press/`: Aufbau und Gründe in `docs/decisions/LAUNCH-1.md`, Bilder mit `python store/tools/presse.py`, Wache `tests/test_presse.py`. Die beiden Zips mit den Bildern in voller Grösse
(`press/ribband-press-images-en.zip`, `press/ribband-pressebilder-de.zip`) sind Bauprodukte und git-ignoriert (Renders
werden nie versioniert): `git subtree split` trägt sie nicht mit. Beim Veröffentlichen baut `presse.py` sie aus den fertigen
Store-Bildern, und sie werden von Hand nach `ribband/press/` im Site-Repo kopiert, vor `python bauen.py` und dem Commit
dort (`docs/release/release-checklist.md` C9). `python store/tools/pages.py --release` meldet, wenn sie fehlen.

Die Vergleichsseite `compare.html` (englisch, <https://tobiaskummer.de/ribband/compare.html>) und `de/vergleich.html`
(deutsch, du-Form), von Hand (`pages.VERGLEICH`), mit `compare.css` über dem Aussehen der Produktseite. Der Text ist
`docs/launch/comparison-page.md`; jede Zelle über eine andere App wird am Tag der Veröffentlichung neu gelesen. Die
Produktseiten verweisen aus der Antwort zu Instapaper und Readwise Reader und im Fuss darauf. `pages.py` schreibt in
die Seite die Karten für schmale Schirme aus der Tabelle (zwischen `<!-- karten: … -->` und `<!-- /karten -->`; unter
60rem stehen sie statt der Tabelle, so dass nichts seitwärts rollt) und die Fragen als FAQPage. Indexierbar, also
nimmt `bauen.py` beide in `sitemap.xml` auf. Wache `tests/test_vergleich.py`.
