"""Check documentation targets, nav coverage, and the adjacent Help Assistant index.

Run after zensical build. No database, browser, or external API is used.
"""
import ast
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
SITE = ROOT / 'site'

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        target = attrs.get('href' if tag == 'a' else 'src') if tag in ('a', 'img') else None
        if target:
            self.links.append(target)

def route(path):
    relative = path.relative_to(DOCS).with_suffix('').as_posix()
    return '/' if relative == 'index' else '/' + relative.removesuffix('/index').strip('/') + '/'

def main():
    errors = []
    pages = set(DOCS.rglob('*.md'))
    for page in pages:
        for target in re.findall(r'\]\(([^)]+)\)', page.read_text()):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            if not (page.parent / unquote(parsed.path)).exists():
                errors.append(f'{page.relative_to(ROOT)}: missing {target}')
    nav = set(re.findall(r'^\s*-\s+(?:.*?:\s*)?([\w/-]+\.md)\s*$', (ROOT/'mkdocs.yml').read_text(), re.M))
    expected = {p.relative_to(DOCS).as_posix() for p in pages}
    if nav != expected:
        errors.append(f'Navigation missing={sorted(expected-nav)}, unknown={sorted(nav-expected)}')
    backend = ROOT.parent/'schema-backend/app_tenant/views/v2/help_assistant_view.py'
    if backend.exists():
        values = {}
        for node in ast.parse(backend.read_text()).body:
            if isinstance(node, (ast.Assign, ast.AnnAssign)):
                target = node.target if isinstance(node, ast.AnnAssign) else node.targets[0]
                if isinstance(target, ast.Name) and target.id in ('DOCS_PAGES', 'SYSTEM_PROMPT_TEMPLATE'):
                    values[target.id] = ast.literal_eval(node.value)
        indexed = {p.rstrip('/') for p, _ in values['DOCS_PAGES']}
        expected_routes = {route(p).rstrip('/') for p in pages}
        if indexed != expected_routes:
            errors.append(f'Help index missing={sorted(expected_routes-indexed)}, unknown={sorted(indexed-expected_routes)}')
        values['SYSTEM_PROMPT_TEMPLATE'].format(max_turns=12, app_location='/get-started', docs_location='/', docs_pages='Links')
    if not SITE.exists():
        errors.append('Build the site with zensical before checking rendered links.')
    parsed_pages = {}
    for path in SITE.rglob('*.html'):
        parser = Links()
        parser.feed(path.read_text())
        parsed_pages[path.resolve()] = parser
    for page, parser in parsed_pages.items():
        for link in parser.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            path = unquote(parsed.path)
            target = (SITE/path.lstrip('/')) if path.startswith('/') else page.parent/path
            if not path:
                target = page
            if target.is_dir():
                target /= 'index.html'
            target = target.resolve()
            if not target.exists():
                errors.append(f'{page.relative_to(SITE)}: missing {link}')
            elif parsed.fragment and target in parsed_pages and unquote(parsed.fragment) not in parsed_pages[target].ids:
                # The theme generates its own skip link even on the 404 page.
                if page.name == '404.html' and parsed.fragment == '__skip':
                    continue
                errors.append(f'{page.relative_to(SITE)}: missing anchor {link}')
    for error in sorted(set(errors)):
        print(error)
    if errors:
        raise SystemExit(1)
    print(f'Checked {len(pages)} pages: local targets, rendered links/anchors, navigation, and Help Assistant index are consistent.')

if __name__ == '__main__':
    main()
