"""Build a public-only website folder and upload ZIP using referenced files only."""
from html.parser import HTMLParser
from pathlib import Path
import re
import shutil
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist"
PAGES = ("index.html", "products.html", "rota-case-study.html", "invoice-reader.html")


class References(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.urls = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        self.urls.extend(value for key, value in attrs if key in ("src", "href") and value)


pending = [ROOT / name for name in PAGES]
files = set()
while pending:
    path = pending.pop().resolve()
    relative = path.relative_to(ROOT)
    allowed = relative.as_posix() in PAGES or relative.parts[0] in ("assets", "css", "js")
    if not allowed or not path.is_file():
        raise SystemExit(f"Missing or non-public file referenced: {relative}")
    if path in files:
        continue
    files.add(path)
    urls = []
    if path.suffix == ".html":
        urls = References(path.read_text(encoding="utf-8")).urls
    elif path.suffix == ".css":
        urls = re.findall(r"url\(\s*['\"]?([^)'\"\s]+)", path.read_text(encoding="utf-8"))
    for url in urls:
        parts = urlsplit(url)
        if not parts.scheme and not parts.netloc and parts.path:
            base = ROOT if parts.path.startswith("/") else path.parent
            pending.append(base / unquote(parts.path).lstrip("/"))

# Only remove this script's generated output within the project, never source files.
if OUTPUT.is_symlink() or OUTPUT.resolve() != ROOT / "dist":
    raise SystemExit("Unexpected output path; refusing to replace it.")
if OUTPUT.exists():
    shutil.rmtree(OUTPUT)
OUTPUT.mkdir()
with ZipFile(ROOT / "website-upload.zip", "w", ZIP_DEFLATED) as archive:
    for path in sorted(files):
        relative = path.relative_to(ROOT)
        destination = OUTPUT / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)
        archive.write(path, relative.as_posix())
print(f"Built {len(files)} public files in dist/ and website-upload.zip.")
