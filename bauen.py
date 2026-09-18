"""Schreibt sitemap.xml und die Stand-Zeile der Startseite aus dem, was im Repo liegt.

Kein Erzeuger für Seiten (die kommen von Hand oder aus den App-Repos per Subtree), nur
die zwei Stellen, die sonst von Hand veralten: die Liste der Seiten samt letztem
Änderungsdatum aus git, und das Datum im Fuss der Startseite. `python bauen.py --check`
schlägt fehl, wenn das Ergebnis nicht dem entspricht, was im Repo steht; das läuft vor
jedem Push (README).
"""
import re
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent
DOMAIN = "https://tobiaskummer.de"


def datum(pfad: Path) -> str:
    """Letztes Commit-Datum der Datei (ISO-Tag); ungetrackt oder geändert: heute."""
    rel = pfad.relative_to(WURZEL).as_posix()
    status = subprocess.run(["git", "status", "--porcelain", "--", rel], capture_output=True, text=True, cwd=WURZEL).stdout
    if status.strip():
        return subprocess.run(["git", "log", "-1", "--format=%cs"], capture_output=True, text=True, cwd=WURZEL).stdout.strip() or heute()
    aus = subprocess.run(["git", "log", "-1", "--format=%cs", "--", rel], capture_output=True, text=True, cwd=WURZEL).stdout.strip()
    return aus or heute()


def heute() -> str:
    import datetime
    return datetime.date.today().isoformat()


def seiten() -> list[tuple[str, str]]:
    """(URL, lastmod) für jede HTML-Seite, die indexiert werden darf (kein noindex)."""
    aus = []
    for p in sorted(WURZEL.rglob("*.html")):
        if ".git" in p.parts or "vorschau" in p.parts:
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        if re.search(r'<meta name="robots" content="noindex', text):
            continue
        rel = p.relative_to(WURZEL).as_posix()
        url = DOMAIN + "/" + (rel[: -len("index.html")] if rel.endswith("index.html") else rel)
        aus.append((url, datum(p)))
    # Die Startseite zuerst, dann nach Adresse: eine Liste, die ein Mensch lesen kann.
    return sorted(aus, key=lambda e: (e[0] != DOMAIN + "/", e[0]))


def sitemap() -> str:
    zeilen = "".join(f"  <url><loc>{u}</loc><lastmod>{d}</lastmod></url>\n" for u, d in seiten())
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + zeilen + "</urlset>\n"


def stand() -> str:
    """Das jüngste Datum aller Seiten, als „TT.MM.JJJJ" für den Fuss."""
    j, m, t = max(d for _, d in seiten()).split("-")
    return f"{t}.{m}.{j}"


def startseite_mit_stand(text: str) -> str:
    neu, n = re.subn(r'(<span id="stand">Stand: )[^<]*(</span>)', rf"\g<1>{stand()}\g<2>", text)
    assert n == 1, "Startseite hat keine Stand-Zeile (<span id=\"stand\">)"
    return neu


def main() -> int:
    sm = WURZEL / "sitemap.xml"
    start = WURZEL / "index.html"
    neu_sm, neu_start = sitemap(), startseite_mit_stand(start.read_text(encoding="utf-8"))
    if "--check" in sys.argv:
        fehler = []
        if sm.read_text(encoding="utf-8") != neu_sm:
            fehler.append("sitemap.xml ist nicht aktuell")
        if start.read_text(encoding="utf-8") != neu_start:
            fehler.append("Stand-Zeile der Startseite ist nicht aktuell")
        for f in fehler:
            print(f)
        return 1 if fehler else 0
    sm.write_text(neu_sm, encoding="utf-8", newline="\n")
    start.write_text(neu_start, encoding="utf-8", newline="\n")
    print(f"{len(seiten())} Seiten in sitemap.xml, Stand {stand()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
