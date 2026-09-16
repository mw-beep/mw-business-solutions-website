"""Dependency-free checks for the static site's local links and page structure."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.tags = Counter()
        self.ids = []
        self.links = []
        self.errors = []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        self.tags[tag] += 1
        if "id" in attrs:
            self.ids.append(attrs["id"])
        for key in ("src", "href"):
            if key in attrs:
                self.links.append(attrs[key])
        if tag == "img":
            if "alt" not in attrs:
                self.errors.append("Image missing alt attribute")
            if attrs.get("src", "").endswith(".png"):
                if not attrs.get("width") or not attrs.get("height"):
                    self.errors.append("Screenshot missing intrinsic dimensions")
        if len(attributes) != len(attrs):
            self.errors.append(f"Duplicate attribute on <{tag}>")


pages = {p.resolve(): Page(p) for p in ROOT.glob("*.html")}
errors = []
checked = 0
for path, page in pages.items():
    for tag in ("html", "head", "body", "title", "main", "h1", "footer"):
        if page.tags[tag] != 1:
            page.errors.append(f"Expected one <{tag}>, found {page.tags[tag]}")
    if len(page.ids) != len(set(page.ids)):
        page.errors.append("Duplicate element IDs")
    for link in page.links:
        checked += 1
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc:
            continue
        target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        if not target.is_file():
            page.errors.append(f"Missing local destination: {link}")
        elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
            page.errors.append(f"Missing fragment: {link}")
    errors.extend(f"{path.name}: {error}" for error in page.errors)
if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: {len(pages)} pages; {checked} links/assets; page landmarks, image attributes and fragments.")
