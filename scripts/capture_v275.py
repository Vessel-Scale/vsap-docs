"""Capture current demo UI without saving credentials or changing tenant data.

Set VSAP_BASE_URL and VSAP_ACCESS_TOKEN in vsap-docs/.env (with or without Bearer),
then run with the docs venv.
Screenshots go to docs/assets/screenshots/v275; inspection text goes to /tmp.
"""
import argparse
import asyncio
import json
from datetime import datetime, timezone
from urllib.parse import urlsplit
from pathlib import Path

from playwright.async_api import async_playwright
import take_screenshots as auth

OUTPUT = auth.OUTPUT_DIR / 'v275'
EVIDENCE = Path('/tmp/vsap-docs-v275')
ACCOUNT = '51899e42-31b1-4545-9574-70df220581c5'
ASSESSMENT = 'bd3f6a72-1207-47f9-8cae-dd3394fdd4d4'
PAGES = {
 'getting-started': '/get-started',
 'accounts': '/account',
 'create-account': '/create-account',
 'account-details': f'/account/{ACCOUNT}',
 'account-edit': f'/account/{ACCOUNT}/edit',
 'assessments': '/evaluation-assessment-list',
 'assign-assessment': '/create-evaluation-assessment',
 'assessment-details': f'/evaluation-assessment-detail/{ASSESSMENT}',
 'library': '/evaluation-assessment-list/library',
 'library-editor': '/evaluation-assessment-list/library/edit/18d301ec-bb02-4880-b004-9ce3ff8d5c5f',
 'reports': '/evaluation-assessment-list/reports',
 'intake-forms': '/account/intake-form',
 'dashboard': '/dashboard?view=ae',
 'directors-dashboard': '/dashboard?view=directors',
 'published-editor': '/evaluation-assessment-list/library/edit-published/aa00c4b8-080d-495e-8a66-2b6885381bc4',
 'report-builder': f'/evaluation-assessment-detail/{ASSESSMENT}/evaluation-assessment-analysis-score',
 'ecosystem': '/ecosystem-map',
 'industries': '/naics-explorer',
 'settings': '/settings',
 'branding': '/settings/branding',
 'email-templates': '/settings/email-templates',
 'users': '/settings/users',
 'custom-data': '/settings/custom-data',
 'naics': '/settings/custom-data/naics',
 'rma': '/settings/custom-data/rma',
 'regions': '/settings/custom-data/regions',
 'media-library': '/settings/custom-data/media-library',
 'profile': '/profile',
 'client-getting-started': f'/account/{ACCOUNT}/client-portal/get-started',
 'client-dashboard': f'/account/{ACCOUNT}/client-portal/dashboard',
 'client-assessments': f'/account/{ACCOUNT}/client-portal/assessments',
 'client-library': f'/account/{ACCOUNT}/client-portal/client-assessments',
 'client-account': f'/account/{ACCOUNT}/client-portal/my-account',
 'client-actions': f'/account/{ACCOUNT}/client-portal/actions',
 'client-industries': f'/account/{ACCOUNT}/client-portal/industries',
}

async def snapshot(page, name):
    await page.mouse.move(1430, 990)
    await page.wait_for_timeout(600)
    text = await page.locator('body').inner_text()
    if len(text.strip()) < 220 or any(error in text for error in ('Sign in to your account', 'Failed to load assessment', 'Network Error', 'Please select an assessment to view scores.')):
        raise RuntimeError(f'{name}: missing authenticated content')
    await page.screenshot(path=str(OUTPUT / f'{name}.png'))
    (EVIDENCE / f'{name}.txt').write_text(text)
    links = await page.locator('a[href]').evaluate_all('(els) => els.map(e => ({text:e.innerText, href:e.getAttribute("href")}))')
    (EVIDENCE / f'{name}-links.json').write_text(json.dumps(links, indent=2))
    manifest_path = Path(__file__).with_name('screenshot-manifest-v275.json')
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    url = urlsplit(page.url)
    existing = manifest.get(name, {})
    manifest[name] = {
        'file': f'docs/assets/screenshots/v275/{name}.png',
        'source_origin': f'{url.scheme}://{url.netloc}',
        'source_path': url.path,
        'captured_utc': datetime.now(timezone.utc).isoformat(),
        'viewport': page.viewport_size,
        'used_by': existing.get('used_by', []),
    }
    manifest_path.write_text(json.dumps(dict(sorted(manifest.items())), indent=2) + '\n')
    print(f'Captured {name}: {page.url}', flush=True)

async def main(selected=None):
    if not auth.ACCESS_TOKEN:
        raise SystemExit('Set VSAP_ACCESS_TOKEN before running.')
    OUTPUT.mkdir(parents=True, exist_ok=True)
    EVIDENCE.mkdir(exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width':1440,'height':1000})
        async def guard(route):
            request = route.request
            if 'schema-api' in request.url and request.method not in ('GET','HEAD','OPTIONS'):
                print(f'Blocked mutation: {request.method} {request.url.split("?")[0]}', flush=True)
                await route.abort()
            else:
                await route.continue_()
        await context.route('**/*', guard)
        page = await context.new_page()
        await auth.setup_auth(page,context)
        failures = []
        for name,path in PAGES.items():
            if selected and name not in selected:
                continue
            try:
                await page.close()
                page = await context.new_page()
                await auth.goto(page,path,wait_ms=9000,wait_until='domcontentloaded')
                if name == 'published-editor':
                    open_editor = page.get_by_role('button', name='Open Editor with Selections', exact=True)
                    if await open_editor.count():
                        await open_editor.click()
                        await page.wait_for_timeout(700)
                if name == 'client-library':
                    await page.get_by_role('heading', name='Available Assessments', exact=True).scroll_into_view_if_needed()
                await snapshot(page,name)
                if name == 'getting-started':
                    for title in ['Add an account','Design an assessment','Assign an assessment','Deliver to respondents','Build your report','Share the results','Explore your dashboard','Explore the Client Portal','Understand your ecosystem','Track and measure impact']:
                        await page.get_by_role('button',name=f'Learn more: {title}',exact=True).click()
                        await page.wait_for_timeout(300)
                        await snapshot(page,'guide-'+title.lower().replace(' ','-'))
                        await page.keyboard.press('Escape')
                if name == 'account-details':
                    for tab in ['Assessments','Reports','Contacts','Assignments','Actions']:
                        button=page.get_by_role('tab',name=tab,exact=True)
                        if not await button.count():
                            button=page.get_by_role('button',name=tab,exact=True)
                        await button.click()
                        await page.wait_for_timeout(3500)
                        await snapshot(page,'account-'+tab.lower())
                if name == 'assessment-details':
                    for tab in ['Analysis','Actions']:
                        button=page.get_by_role('tab',name=tab,exact=True)
                        if not await button.count():
                            button=page.get_by_role('button',name=tab,exact=True)
                        if await button.count():
                            await button.click()
                            await page.wait_for_timeout(3500)
                            await snapshot(page,'assessment-'+tab.lower().replace(' ','-'))
            except Exception as exc:
                failures.append({'name':name,'error':str(exc)[:300]})
                print(f'Failed {name}: {str(exc)[:180]}',flush=True)
        (EVIDENCE/'failures.json').write_text(json.dumps(failures,indent=2))
        await browser.close()
        if failures:
            raise SystemExit(f'{len(failures)} captures need review; see {EVIDENCE}/failures.json')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pages', nargs='*', choices=list(PAGES))
    asyncio.run(main(parser.parse_args().pages))
