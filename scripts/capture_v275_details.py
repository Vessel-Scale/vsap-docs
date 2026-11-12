"""Read-only detail captures supplementing capture_v275.py (same env/auth).

Each workspace opens in a fresh tab. Only preview-data POST is permitted;
all tenant-changing API requests and generation requests are blocked.
"""
import argparse
import asyncio
import re
from playwright.async_api import async_playwright
import capture_v275 as s

async def main(selected=None):
    if not s.auth.ACCESS_TOKEN:
        raise SystemExit('Set VSAP_ACCESS_TOKEN before capturing.')
    s.OUTPUT.mkdir(parents=True, exist_ok=True)
    s.EVIDENCE.mkdir(exist_ok=True)
    failures=[]
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True)
        context=await browser.new_context(viewport={'width':1440,'height':1000})
        async def guard(route):
            r=route.request
            if 'schema-api' in r.url and r.method not in ('GET','HEAD','OPTIONS') and not (r.method=='POST' and '/web-report-configurations/preview-data/' in r.url):
                print('Blocked:',r.method,r.url.split('?')[0],flush=True)
                await route.abort()
            else:
                await route.continue_()
        await context.route('**/*',guard)
        auth_page=await context.new_page()
        await s.auth.setup_auth(auth_page,context)
        await auth_page.close()
        async def visit(path):
            page=await context.new_page()
            await page.goto(s.auth.BASE_URL+path,wait_until='domcontentloaded')
            await page.wait_for_timeout(9000)
            return page
        async def snap(page,name):
            await page.wait_for_timeout(1000)
            await s.snapshot(page,name)
        async def click(page,name):
            exact=isinstance(name,str)
            target=page.get_by_role('tab',name=name,exact=exact)
            if not await target.count():
                pattern=re.compile('^'+re.escape(name)+'$') if exact else name
                target=page.locator('button').filter(has_text=pattern)
            if not await target.count():
                target=page.get_by_role('button',name=name,exact=exact)
            await target.first.click(timeout=15000)
            await page.wait_for_timeout(2000)
        async def task(name,fn):
            try: await fn()
            except Exception as exc:
                failures.append(name)
                print('FAILED',name,str(exc)[:300],flush=True)
        async def editor():
            page=await visit('/evaluation-assessment-list/library/edit/18d301ec-bb02-4880-b004-9ce3ff8d5c5f')
            await click(page,re.compile(r'^1\. Leadership & Strategy'))
            await snap(page,'editor-category')
            await page.get_by_role('button',name=re.compile('How clearly is your organization')).click()
            await snap(page,'editor-question')
            await click(page,'Preview')
            await snap(page,'editor-preview')
            await page.close()
            page=await visit('/evaluation-assessment-list/library/edit/18d301ec-bb02-4880-b004-9ce3ff8d5c5f')
            await click(page,'Click to change icon')
            await snap(page,'editor-icons')
            await page.close()
        async def conditional_logic():
            page=await visit('/evaluation-assessment-list/library/edit/18d301ec-bb02-4880-b004-9ce3ff8d5c5f')
            await page.get_by_role('switch',name='Enable Conditional Logic').check()
            await page.get_by_role('button',name=re.compile('Leadership & Strategy')).first.click()
            await page.get_by_text("To what extent is day-to-day work aligned with your organization's strategic priorities?",exact=True).click()
            await page.wait_for_timeout(700)
            await page.get_by_role('combobox').nth(0).click()
            await page.get_by_role('option',name='Show when conditions match',exact=True).click()
            await page.wait_for_timeout(600)
            await snap(page,'conditional-logic-question-rules')
            add_group=page.get_by_role('button',name='Add condition group')
            if await add_group.count():
                await add_group.click()
                await page.wait_for_timeout(700)
                await snap(page,'conditional-logic-condition-groups')
            preview=page.get_by_role('button',name='Preview',exact=True).first
            if await preview.count():
                await preview.click()
                await page.wait_for_timeout(1800)
                await snap(page,'conditional-logic-preview')
            await page.close()
        async def reports():
            page=await visit('/evaluation-assessment-list/reports/create')
            await snap(page,'report-editor')
            await click(page,'Preview')
            await snap(page,'report-preview')
            await page.close()
            page=await visit('/report/bd3f6a72-1207-47f9-8cae-dd3394fdd4d4')
            await snap(page,'web-report')
            await page.close()
        async def dashboard():
            page=await visit('/dashboard?view=directors')
            await snap(page,'directors-dashboard')
            await click(page,'Configure')
            await snap(page,'dashboard-configure')
            await page.close()
            page=await visit('/dashboard?view=directors')
            await click(page,'Export')
            await snap(page,'dashboard-export')
            await page.close()
            page=await visit('/dashboard?view=directors')
            await click(page,'Analytics')
            await page.wait_for_timeout(8000)
            await snap(page,'dashboard-pivot')
            await page.close()
        async def account():
            page=await visit(f'/account/{s.ACCOUNT}')
            await click(page,'Assessments')
            await page.wait_for_timeout(4500)
            await snap(page,'account-assessments')
            await click(page,'Actions')
            await page.wait_for_timeout(4000)
            await snap(page,'account-actions')
            await page.close()
        async def assessment():
            page=await visit(f'/evaluation-assessment-detail/{s.ASSESSMENT}')
            await click(page,'Share Report')
            await snap(page,'share-report')
            await page.close()
        async def forms():
            page=await visit('/account/intake-form')
            await page.get_by_text('Getting Started Assessment - Intake',exact=True).click()
            await page.wait_for_timeout(6500)
            await snap(page,'intake-editor')
            await page.close()
            page=await visit('/settings/email-templates')
            await page.get_by_role('button',name=re.compile('edit',re.I)).first.click()
            await snap(page,'email-editor')
            await page.close()
        async def simple():
            for name,path in [('profile','/profile'),('account-import','/account'),('account-export','/account')]:
                page=await visit(path)
                if name=='account-import': await click(page,'Import')
                elif name=='account-export': await click(page,'Export')
                await snap(page,name)
                await page.close()
        async def maps():
            page=await visit('/ecosystem-map')
            await snap(page,'ecosystem-filters')
            await page.close()
            page=await visit('/ecosystem-map?assessment=Supplier%20Business%20Health%20Assessment&view=scores')
            await snap(page,'ecosystem-score')
            await page.close()
        for name,fn in [('editor',editor),('conditional-logic',conditional_logic),('reports',reports),('dashboard',dashboard),('account',account),('assessment',assessment),('forms',forms),('simple',simple),('map',maps)]:
            if not selected or name in selected:
                await task(name,fn)
        await browser.close()
    if failures: raise SystemExit('Review captures: '+', '.join(failures))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('sections', nargs='*', choices=['editor','conditional-logic','reports','dashboard','account','assessment','forms','simple','map'])
    asyncio.run(main(parser.parse_args().sections))
