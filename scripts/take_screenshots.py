"""
Playwright screenshot script for VSAP docs.
Captures authenticated screenshots into organized subfolders.

Usage:
  uv run python scripts/take_screenshots.py                        # all sections
  uv run python scripts/take_screenshots.py account                # one section
  uv run python scripts/take_screenshots.py account library        # multiple sections
  uv run python scripts/take_screenshots.py custom-data            # custom data only

Available sections:
  dashboard, account, assessments, library, library-question-types, ecosystem, industries, settings, report-builder, custom-data,
  email-templates, intake-forms, web-reports, branding
"""
import argparse
import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright

BASE_URL = "https://demo.schema-qa.vesselscale.com"
ACCESS_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3ODAwMjE5LCJpYXQiOjE3Nzc3NTcwMTksImp0aSI6ImQ3ZTUxYTEyNDRiNjQyZjI5N2JjNzY3YWRhOWMxMzhiIiwidXNlcl9pZCI6ImVjYTIxNzZmLTJkZjQtNDc1NC1iNDNhLTZmMDRlMWJjODA5ZCIsImZ1bGxuYW1lIjoiS2V2aW4gVGV0eiIsImVtYWlsIjoia2V2aW5AdmVzc2Vsc2NhbGUuY29tIiwidXNlcl9ncm91cHMiOlsiYWRtaW4iLCJhY2NvdW50X2V4ZWN1dGl2ZSJdfQ.MgYJjpajBmhgafVXbdkGCqNXgps0JKazRKXgkNEkRP8"

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "assets" / "screenshots"

COOKIES = [
    {"name": "API_URL",      "value": "https://demo.schema-api-qa.vesselscale.com/"},
    {"name": "ACCESS_TOKEN", "value": ACCESS_TOKEN},
]

EXTRA_HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "origin": "https://demo.schema-qa.vesselscale.com",
    "referer": "https://demo.schema-qa.vesselscale.com/",
    "sec-ch-ua": '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
}

PERSIST_ROOT = json.dumps({
    "authReducers": json.dumps({
        "user": {
            "currentUser": {
                "access": ACCESS_TOKEN.removeprefix("Bearer "),
                "refresh": "",
                "account_id": "",
                "user_type": ["admin", "account_executive"],
                "profile_image": "",
                "fullname": "Kevin Tetz",
                "first_name": "Kevin",
                "last_name": "Tetz",
                "email": "kevin@vesselscale.com",
                "is_superuser": False,
            },
            "loading": False,
            "error": False,
        }
    }),
    "_persist": json.dumps({"version": 1, "rehydrated": True}),
})


async def setup_auth(page, context):
    await context.set_extra_http_headers(EXTRA_HEADERS)
    await context.add_cookies([{**c, "url": BASE_URL + "/"} for c in COOKIES])
    await page.goto(BASE_URL, wait_until="domcontentloaded", timeout=15000)
    await page.evaluate(f"localStorage.setItem('persist:root', {json.dumps(PERSIST_ROOT)})")


async def goto(page, path, wait_ms=3000, wait_until="networkidle"):
    await page.goto(BASE_URL + path, wait_until=wait_until, timeout=30000)
    await page.wait_for_timeout(wait_ms)
    print(f"    url: {page.url}")


async def save(page, folder, name):
    out = OUTPUT_DIR / folder / f"{name}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    await page.screenshot(path=str(out), full_page=False)
    print(f"  + {folder}/{name}.png")


async def try_click(page, *selectors, timeout=5000):
    for sel in selectors:
        try:
            await page.click(sel, timeout=timeout)
            await page.wait_for_timeout(2500)
            return True
        except Exception:
            continue
    print("    (no clickable element found)")
    return False


# ── Section capture functions ──────────────────────────────────────────────────

async def section_dashboard(page):
    print("\n[dashboard] navigating to dashboard")
    await goto(page, "/dashboard", wait_ms=3000)
    
    # Select "Supplier Business Health Assessment" from the dropdown
    print("[dashboard] selecting Supplier Business Health Assessment")
    # Look for any button/select that might be the assessment selector
    dropdown_clicked = False
    for selector in [
        'button:has-text("Assessment")',
        'button:has-text("Getting Started")',
        '.MuiSelect-select',
        '[role="button"][aria-haspopup="listbox"]',
    ]:
        try:
            el = await page.query_selector(selector)
            if el:
                await el.click()
                await page.wait_for_timeout(800)
                dropdown_clicked = True
                print(f"    clicked dropdown with selector: {selector}")
                break
        except Exception as e:
            print(f"    selector {selector} failed: {e}")
            continue
    
    if dropdown_clicked:
        # Now click the Supplier Business Health Assessment option
        if await try_click(page,
            "[role='option']:has-text('Supplier Business Health')",
            "li:has-text('Supplier Business Health')",
            "[role='listbox'] [role='option']:has-text('Supplier')",
            timeout=3000
        ):
            print("    selected Supplier Business Health Assessment")
            await page.wait_for_timeout(3000)
        else:
            print("    could not find Supplier Business Health Assessment in dropdown")
    
    print("[dashboard] overview")
    await save(page, "dashboard", "dashboard")

    # Toolbar buttons (top-right area)
    print("[dashboard] toolbar buttons")
    await page.screenshot(
        path=str(OUTPUT_DIR / "dashboard" / "dashboard-toolbar.png"),
        clip={"x": 1220, "y": 110, "width": 200, "height": 55},
    )
    print("  + dashboard/dashboard-toolbar.png")

    # Screenshot each component card using element.screenshot() so scroll position doesn't matter.
    # Take the smallest (most specific) matching element to avoid capturing a parent container.
    async def screenshot_component(search_text, filename):
        el = await page.evaluate_handle(f"""
            (() => {{
                const candidates = Array.from(document.querySelectorAll('*')).filter(e => {{
                    const t = e.innerText?.trim();
                    return t?.includes({json.dumps(search_text)}) &&
                           e.children.length > 1 &&
                           e.offsetWidth > 200 && e.offsetHeight > 100;
                }});
                // Return the element with the smallest bounding area (most specific card)
                return candidates.reduce((best, e) =>
                    (!best || e.offsetWidth * e.offsetHeight < best.offsetWidth * best.offsetHeight) ? e : best
                , null);
            }})()
        """)
        el = el.as_element()
        if el:
            out = str(OUTPUT_DIR / "dashboard" / f"{filename}.png")
            await el.screenshot(path=out)
            print(f"  + dashboard/{filename}.png")
            return True
        print(f"  ✗ could not find card: {search_text!r}")
        return False

    await screenshot_component("Assessment Summary", "dashboard-assessment-summary")
    await screenshot_component("Total Resilience Score", "dashboard-resilience-score")
    await screenshot_component("Most Frequently Offered Solutions", "dashboard-solutions")
    await screenshot_component("Total Companies", "dashboard-company-size")
    await screenshot_component("Assessment Scoring by Category", "dashboard-scoring-by-category")
    await screenshot_component("Average Score by NAICS Industry", "dashboard-naics-score")
    await screenshot_component("Top Scoring Accounts", "dashboard-top-accounts")
    await screenshot_component("Assessments in progress with no responses", "dashboard-in-progress")
    await screenshot_component("Business Size Distribution by NAICS Industry", "dashboard-business-size-naics")
    await screenshot_component("Highest Scoring Statements", "dashboard-highest-scoring")
    await screenshot_component("Lowest Scoring Statements", "dashboard-lowest-scoring")

    # Configure Dashboard modal
    print("[dashboard] configure modal")
    await page.evaluate("""
        (() => {
            const el = Array.from(document.querySelectorAll('*')).find(e => {
                const s = window.getComputedStyle(e);
                return (s.overflowY === 'auto' || s.overflowY === 'scroll') && e.scrollHeight > e.clientHeight + 50;
            });
            if (el) el.scrollTop = 0;
        })()
    """)
    await page.wait_for_timeout(300)
    await page.locator('button[aria-label="Configure dashboard components"]').click()
    await page.wait_for_timeout(1500)
    await save(page, "dashboard", "dashboard-configure")

    # Scroll configure list to show all components
    await page.evaluate("""
        (() => {
            const modal = document.querySelector('[role="dialog"]');
            if (modal) {
                const scrollable = Array.from(modal.querySelectorAll('*')).find(e => {
                    const s = window.getComputedStyle(e);
                    return (s.overflowY === 'auto' || s.overflowY === 'scroll') &&
                           e.scrollHeight > e.clientHeight + 20;
                });
                if (scrollable) scrollable.scrollTop = 300;
            }
        })()
    """)
    await page.wait_for_timeout(400)
    await save(page, "dashboard", "dashboard-configure-scrolled")
    await page.keyboard.press("Escape")
    await page.wait_for_timeout(500)

    # Download CSV modal
    print("[dashboard] download CSV modal")
    await page.locator('button[aria-label="Download CSV for all assessments"]').click()
    await page.wait_for_timeout(1500)
    await save(page, "dashboard", "dashboard-download")
    await page.keyboard.press("Escape")
    await page.wait_for_timeout(500)

    # Pivot table — column selector
    print("[dashboard] pivot table")
    await page.locator('button[aria-label="Open pivot table analytics"]').click()
    await page.wait_for_timeout(3000)
    await save(page, "dashboard", "dashboard-pivot-selector")

    # Load the pivot table
    load_btn = page.locator('button:has-text("LOAD PIVOT TABLE")')
    if await load_btn.count() > 0:
        await load_btn.click()
        await page.wait_for_timeout(3000)
        await save(page, "dashboard", "dashboard-pivot-table")


async def section_account(page):
    print("\n[account] list")
    await goto(page, "/account")
    await save(page, "account", "account-list")

    VESSEL_ACCOUNT_ID = "51899e42-31b1-4545-9574-70df220581c5"
    print("[account] details - navigating to Vessel account")
    await goto(page, f"/account/{VESSEL_ACCOUNT_ID}", wait_ms=2000)
    print(f"    url: {page.url}")

    # Overview tab (default)
    print("[account] details - overview tab")
    await try_click(page, "button:has-text('Overview'), [role='tab']:has-text('Overview')", timeout=3000)
    await page.wait_for_timeout(800)
    await save(page, "account", "account-details-overview")

    # Assessments tab
    print("[account] details - assessments tab")
    if await try_click(page, "button:has-text('Assessments'), [role='tab']:has-text('Assessments')", timeout=3000):
        await page.wait_for_timeout(1000)
        await save(page, "account", "account-details-assessments")

    # Settings tab
    print("[account] details - settings tab")
    if await try_click(page, "button:has-text('Settings'), [role='tab']:has-text('Settings')", timeout=3000):
        await page.wait_for_timeout(1000)
        await save(page, "account", "account-details-settings")

    # Keep legacy screenshot name for backwards compat (overview tab)
    await try_click(page, "button:has-text('Overview'), [role='tab']:has-text('Overview')", timeout=3000)
    await page.wait_for_timeout(500)
    await save(page, "account", "account-details")

    print("[account] edit - clicking edit button")
    if await try_click(page,
        "button:has-text('Edit Details')",
        "button:has-text('Edit')",
        "a:has-text('Edit')",
        "[aria-label='edit']",
        "[data-testid='edit-btn']",
    ):
        await save(page, "account", "account-edit")

    print("[account] download/upload buttons on account list")
    await goto(page, "/account", wait_ms=2000)
    # Capture the download and upload buttons in the toolbar
    print("[account] download button")
    if await try_click(page, "button:has-text('Download')", timeout=3000):
        await page.wait_for_timeout(1500)
        await save(page, "account", "account-list-download-modal")
        await page.keyboard.press("Escape")
        await page.wait_for_timeout(500)

    print("[account] upload button")
    if await try_click(page, "button:has-text('Upload')", timeout=3000):
        await page.wait_for_timeout(1500)
        await save(page, "account", "account-list-upload-modal")
        
        # Show paste option
        print("[account] upload modal - paste option")
        if await try_click(page, "button:has-text('Paste')", timeout=3000):
            await page.wait_for_timeout(1000)
            await save(page, "account", "account-list-upload-modal-paste")
        
        # Show upload file option
        print("[account] upload modal - upload option")
        if await try_click(page, "button:has-text('Upload')", timeout=3000):
            await page.wait_for_timeout(1000)
            await save(page, "account", "account-list-upload-modal-upload")
        
        await page.keyboard.press("Escape")
        await page.wait_for_timeout(500)

    print("[account] create account form")
    await goto(page, "/create-account", wait_ms=2000)
    await save(page, "account", "account-create")
    # Scroll the main content area to show lower sections
    await page.evaluate("""
        (() => {
            const el = Array.from(document.querySelectorAll('*')).find(e => {
                const s = window.getComputedStyle(e);
                return (s.overflowY === 'auto' || s.overflowY === 'scroll') && e.scrollHeight > e.clientHeight + 50;
            }) || document.documentElement;
            el.scrollTop = 600;
        })()
    """)
    await page.wait_for_timeout(400)
    await save(page, "account", "account-create-scrolled")


async def section_assessments(page):
    print("\n[assessments] collections list")
    await goto(page, "/evaluation-assessment-list")
    await save(page, "assessments", "assessment-collections")

    # Navigate to Vessel account assessments tab to get real assessment data
    VESSEL_ACCOUNT_ID = "51899e42-31b1-4545-9574-70df220581c5"
    print("[assessments] navigating to Vessel account")
    await goto(page, f"/account/{VESSEL_ACCOUNT_ID}", wait_ms=2000)
    
    print("[assessments] clicking assessments tab")
    if await try_click(page, "button:has-text('Assessments'), [role='tab']:has-text('Assessments')", timeout=3000):
        await page.wait_for_timeout(1000)
        await save(page, "assessments", "account-assessments-list")

    # Click the first assessment to view its details
    print("[assessments] details - clicking first assessment")
    if await try_click(page,
        "tbody tr:first-child",
        "tbody tr:first-child td:first-child",
        "a[href*='/evaluation']",
        "a[href*='/assessment']",
        "[class*='row']:first-child",
    ):
        await page.wait_for_timeout(2000)
        await save(page, "assessments", "assessment-details-overview")

        # Scroll to show responses section
        print("[assessments] scrolling to responses section")
        await page.evaluate("""
            (() => {
                const el = Array.from(document.querySelectorAll('*')).find(e => {
                    const s = window.getComputedStyle(e);
                    return (s.overflowY === 'auto' || s.overflowY === 'scroll') && e.scrollHeight > e.clientHeight + 50;
                }) || document.documentElement;
                el.scrollTop = 500;
            })()
        """)
        await page.wait_for_timeout(800)
        await save(page, "assessments", "assessment-responses-section")

        # Scroll to scoring section
        print("[assessments] scrolling to scoring section")
        await page.evaluate("""
            (() => {
                const el = Array.from(document.querySelectorAll('*')).find(e => {
                    const s = window.getComputedStyle(e);
                    return (s.overflowY === 'auto' || s.overflowY === 'scroll') && e.scrollHeight > e.clientHeight + 50;
                }) || document.documentElement;
                el.scrollTop = 1200;
            })()
        """)
        await page.wait_for_timeout(800)
        await save(page, "assessments", "assessment-scoring-section")


LIBRARY_EDITOR_ID = "dcb00786-ae5a-4c6d-b91b-b46f0133c975"


async def section_library(page):
    print("\n[library] list")
    await goto(page, "/library", wait_ms=4000)
    await save(page, "library", "library-list")

    # ── Navigate directly to the "All Question Types" assessment ─────────────
    print("[library] navigating directly to All Question Types editor")
    await goto(page, f"/library/edit/{LIBRARY_EDITOR_ID}", wait_ms=4000)
    print(f"    url: {page.url}")

    # The editor uses an inner scrollable container, not window scroll.
    # Find it and use it throughout.
    async def scroll_main(y):
        await page.evaluate(f"""
            (() => {{
                // try main content scrollable container first, fallback to body
                const el = document.querySelector('main, [class*="content"], [class*="Content"], [class*="main"], [class*="Main"]');
                if (el && el.scrollHeight > el.clientHeight) {{ el.scrollTop = {y}; return; }}
                window.scrollTo(0, {y});
            }})()
        """)
        await page.wait_for_timeout(400)

    # ── Top of editor — toolbar + assessment details ───────────────────────
    await scroll_main(0)
    await save(page, "library", "library-editor-overview")

    # ── Expand sidebar panel if collapsed ──────────────────────────────────
    print("[library] editor - expanding sidebar if needed")
    sidebar_btn = await page.query_selector("button:has(svg[data-testid='KeyboardDoubleArrowRightIcon'])")
    if sidebar_btn:
        await sidebar_btn.click()
        await page.wait_for_timeout(800)
    await save(page, "library", "library-editor-toolbar")

    # ── Expand Assessment Details accordion ────────────────────────────────
    print("[library] editor - expanding Assessment Details")
    await try_click(page, "button:has-text('Assessment Details')", timeout=3000)
    await page.wait_for_timeout(600)
    await save(page, "library", "library-editor-assessment-details")

    # ── Scroll to show scoring sections ────────────────────────────────────
    print("[library] editor - scoring sections area")
    await scroll_main(400)
    await save(page, "library", "library-editor-scoring")

    # ── Expand scoring section feedback accordion ─────────────────────────
    print("[library] editor - scoring section feedback")
    await try_click(page, "button:has-text('Scoring Section Feedback')", timeout=3000)
    await page.wait_for_timeout(600)
    await save(page, "library", "library-editor-scoring-feedback")

    # ── Scroll to categories list ──────────────────────────────────────────
    print("[library] editor - categories area")
    await scroll_main(900)
    await page.wait_for_timeout(500)
    await save(page, "library", "library-editor-categories")

    # ── Click first category to expand it and show questions ──────────────
    print("[library] editor - expanding first category")
    cat_expanded = False
    for sel in [
        "[aria-label='Drag to reorder category'] ~ *",
        "button[class*='expand']",
        "button[class*='Expand']",
        "[class*='categoryName']",
        "[class*='CategoryName']",
        "h4:has-text('EXAMPLE:'):first-of-type",
    ]:
        try:
            el = await page.query_selector(sel)
            if el:
                await el.click()
                await page.wait_for_timeout(1000)
                cat_expanded = True
                break
        except Exception:
            continue

    if cat_expanded:
        await save(page, "library", "library-editor-category-expanded")
    else:
        # Just save the categories as-is
        await save(page, "library", "library-editor-category-expanded")

    # ── Preview: full assessment ───────────────────────────────────────────
    print("[library] preview - full assessment")
    await scroll_main(0)
    await page.wait_for_timeout(300)
    if await try_click(page, "button[aria-label='Preview Assessment']", timeout=5000):
        await page.wait_for_timeout(2500)
        await save(page, "library", "library-preview-full-assessment")

        print("[library] preview - full assessment scrolled")
        await page.evaluate("""
            const d = document.querySelector('[role="dialog"]');
            if (d) d.scrollTop = 500;
        """)
        await page.wait_for_timeout(400)
        await save(page, "library", "library-preview-full-scrolled")

        await try_click(page, "[aria-label='close']", "[aria-label='Close']", "button:has-text('Close')", "button:has-text('Cancel')")
        await page.wait_for_timeout(600)
    else:
        print("    (Preview Assessment button not found)")

    # ── Preview: first category ────────────────────────────────────────────
    print("[library] preview - category")
    if await try_click(page, "button[aria-label='Preview category questions']", timeout=5000):
        await page.wait_for_timeout(2500)
        await save(page, "library", "library-preview-category")

        print("[library] preview - category scrolled")
        await page.evaluate("""
            const d = document.querySelector('[role="dialog"]');
            if (d) d.scrollTop = 400;
        """)
        await page.wait_for_timeout(400)
        await save(page, "library", "library-preview-category-scrolled")

        await try_click(page, "[aria-label='close']", "[aria-label='Close']", "button:has-text('Close')", "button:has-text('Cancel')")
        await page.wait_for_timeout(600)
    else:
        print("    (Preview category questions button not found)")


async def section_ecosystem(page):
    print("\n[ecosystem] overview - map with filters panel open")
    # Map page never reaches networkidle — use domcontentloaded + long wait
    await goto(page, "/ecosystem-map", wait_ms=8000, wait_until="domcontentloaded")
    await save(page, "ecosystem", "ecosystem")

    # ── Filters panel ────────────────────────────────────────────────────────
    # Filters panel is open by default; capture it in full view
    print("[ecosystem] filters panel visible")
    await save(page, "ecosystem", "ecosystem-filters")

    # ── Assessment filter with Supplier Business Health Assessment ──────────
    print("[ecosystem] selecting Supplier Business Health Assessment")
    if await try_click(page,
        "label:has-text('Assessment') ~ * [role='combobox']",
        "div:has(> label:has-text('Assessment')) .MuiSelect-select",
        "[id*='assessment']",
    ):
        await page.wait_for_timeout(600)
        # Click "Supplier Business Health Assessment" option
        if await try_click(page,
            "[role='option']:has-text('Supplier Business Health Assessment')",
            "[role='listbox'] li:has-text('Supplier Business Health')",
        ):
            await page.wait_for_timeout(2000)

            # Click the "Scores" button to show scores view
            print("[ecosystem] switching to Scores view")
            if await try_click(page,
                "button:has-text('Scores')",
                "[role='button']:has-text('Scores')",
            ):
                await page.wait_for_timeout(3000)
                await save(page, "ecosystem", "ecosystem-scores-suppliers")

                # Capture Score Category dropdown
                print("[ecosystem] capturing Score Category dropdown")
                if await try_click(page,
                    "label:has-text('Score Category') ~ * [role='combobox']",
                    "div:has(> label:has-text('Score Category')) .MuiSelect-select",
                ):
                    await page.wait_for_timeout(1000)
                    await save(page, "ecosystem", "ecosystem-score-category-dropdown")

                    # Select Financial Stability
                    print("[ecosystem] selecting Financial Stability category")
                    if await try_click(page,
                        "[role='option']:has-text('Financial Stability')",
                        "[role='listbox'] li:has-text('Financial Stability')",
                    ):
                        await page.wait_for_timeout(2000)
                        await save(page, "ecosystem", "ecosystem-scores-financial-stability")

    # Apply a NAICS sector filter — click the Sector dropdown, pick first option
    print("[ecosystem] NAICS sector filter - opening")
    if await try_click(page,
        "[aria-label*='sector' i]",
        "label:has-text('Sector') ~ * [role='combobox']",
        "[id*='sector']",
        "div:has(> label:has-text('Sector')) [role='combobox']",
        "div:has(> label:has-text('Sector')) .MuiSelect-select",
    ):
        await page.wait_for_timeout(600)
        # Pick first real option (not "All")
        if await try_click(page,
            "[role='listbox'] [role='option']:nth-child(2)",
            "[role='option']:nth-child(2)",
        ):
            await page.wait_for_timeout(1500)
            await save(page, "ecosystem", "ecosystem-filtered-sector")

    # ── Click an account from the list panel to open account detail ──────────
    # Re-load clean so the list is in default state
    print("[ecosystem] clicking an account from the list to open account detail")
    await goto(page, "/ecosystem-map", wait_ms=8000, wait_until="domcontentloaded")
    # The account list in the middle panel renders rows with cursor:pointer.
    # Wait for account list items to appear (Virtuoso renders items with data-index)
    try:
        await page.wait_for_selector('[data-index="0"]', timeout=10000)
    except Exception:
        pass
    # Click the first Virtuoso list item (account card)
    clicked = await try_click(page, '[data-index="0"]')
    if clicked:
        await page.wait_for_timeout(2000)
        await save(page, "ecosystem", "ecosystem-account-detail")

        # ── View Legislators ────────────────────────────────────────────
        print("[ecosystem] clicking View Legislators button")
        if await try_click(page,
            "button:has-text('View Legislators')",
            "span:has-text('View Legislators')",
            "[title='View Legislators']",
            "button:has(svg[data-testid='GroupsIcon'])",
        ):
            await page.wait_for_timeout(2000)
            await save(page, "ecosystem", "ecosystem-legislators")
    else:
        print("    (no account list item found)")


async def section_industries(page):
    print("\n[industries] overview - sector level")
    await goto(page, "/naics-explorer")
    await save(page, "industries", "industries")

    # Sector detail is shown by default — capture it
    await save(page, "industries", "industries-sector")

    # Helper: click the first [role="tab"] inside the nth [role="tablist"] (0-based)
    async def click_first_tab_in_column(col_index: int) -> bool:
        clicked = await page.evaluate(f"""
            (() => {{
                const lists = document.querySelectorAll('[role="tablist"]');
                const list = lists[{col_index}];
                if (!list) return false;
                const tab = list.querySelector('[role="tab"]');
                if (!tab) return false;
                tab.click();
                return true;
            }})()
        """)
        if clicked:
            await page.wait_for_timeout(800)
        return clicked

    # Subsector column is index 1
    print("[industries] subsector level - clicking first subsector tab")
    if await click_first_tab_in_column(1):
        await save(page, "industries", "industries-subsector")

        # Group column is index 2
        print("[industries] group level - clicking first group tab")
        if await click_first_tab_in_column(2):
            await save(page, "industries", "industries-group")

            # Industry column is index 3
            print("[industries] industry level - clicking first industry tab")
            if await click_first_tab_in_column(3):
                await save(page, "industries", "industries-industry")


async def section_settings(page):
    print("\n[settings]")
    await goto(page, "/settings")
    await save(page, "settings", "settings")


async def section_report_builder(page):
    print("\n[report-builder] list")
    await goto(page, "/settings/web-reports")
    await save(page, "report-builder", "web-reports-list")

    print("[report-builder] editor - clicking first card")
    if await try_click(page,
        "h2:first-of-type",
        "h3:first-of-type",
        "[class*='card']:first-child",
        "[class*='Card']:first-child",
        "a[href*='/settings/web-reports/']",
        "button:has-text('Edit')",
    ):
        await save(page, "report-builder", "web-report-editor")


async def section_custom_data(page):
    print("\n[custom-data] hub")
    await goto(page, "/settings/custom-data")
    await save(page, "custom-data", "custom-data-hub")

    # ── NAICS list ────────────────────────────────────────────────────────────
    print("[custom-data] NAICS list")
    await goto(page, "/settings/custom-data/naics")
    await save(page, "custom-data", "naics-list")

    print("[custom-data] NAICS list - scrolled")
    await page.evaluate("window.scrollTo(0, 400)")
    await page.wait_for_timeout(500)
    await save(page, "custom-data", "naics-list-scrolled")
    await page.evaluate("window.scrollTo(0, 0)")

    print("[custom-data] NAICS edit - clicking first row")
    if await try_click(page,
        "tbody tr:first-child td:last-child button",
        "tbody tr:first-child button[aria-label='edit']",
        "tbody tr:first-child button:has-text('Edit')",
        "tbody tr:first-child [class*='edit']",
        "tbody tr:first-child td:first-child",
    ):
        await save(page, "custom-data", "naics-edit-modal")
        await try_click(page, "[aria-label='Close']", "button:has-text('Cancel')", "button:has-text('Close')")

    # ── RMA list ──────────────────────────────────────────────────────────────
    print("[custom-data] RMA list")
    await goto(page, "/settings/custom-data/rma")
    await save(page, "custom-data", "rma-list")

    print("[custom-data] RMA edit - clicking first row")
    if await try_click(page,
        "tbody tr:first-child td:last-child button",
        "tbody tr:first-child button[aria-label='edit']",
        "tbody tr:first-child button:has-text('Edit')",
        "tbody tr:first-child [class*='edit']",
        "tbody tr:first-child td:first-child",
    ):
        await save(page, "custom-data", "rma-edit-modal")
        await try_click(page, "[aria-label='Close']", "button:has-text('Cancel')", "button:has-text('Close')")

    # ── Media Library ─────────────────────────────────────────────────────────
    print("[custom-data] media library")
    await goto(page, "/settings/custom-data/media-library", wait_ms=4000)
    await save(page, "custom-data", "media-library")

    print("[custom-data] media library - upload dialog")
    if await try_click(page,
        "button:has-text('Upload')",
        "button:has-text('Add Media')",
        "button:has-text('New')",
        "[class*='upload']:not(input)",
        "[aria-label='upload']",
    ):
        await save(page, "custom-data", "media-upload-dialog")
        await try_click(page, "[aria-label='Close']", "button:has-text('Cancel')", "button:has-text('Close')")

    print("[custom-data] media preview - clicking first image")
    if await try_click(page,
        "[class*='media'] img:first-of-type",
        "[class*='Media'] img:first-of-type",
        "[class*='card'] img:first-of-type",
        "[class*='Card'] img:first-of-type",
        "img:first-of-type",
    ):
        await save(page, "custom-data", "media-preview-dialog")

        print("[custom-data] media color picker - attempting to reveal")
        if await try_click(page,
            "[aria-label='Pick color']",
            "button:has-text('Pick Color')",
            "[class*='colorPick']",
            "[class*='color-pick']",
            "[class*='eyedrop']",
        ):
            await save(page, "custom-data", "media-color-picker")

        await try_click(page, "[aria-label='Close']", "button:has-text('Cancel')", "button:has-text('Close')")


async def section_email_templates(page):
    # ── List ─────────────────────────────────────────────────────────────────
    print("\n[email-templates] list")
    await goto(page, "/settings/email-templates")
    await save(page, "email-templates", "email-templates-list")

    # ── Editor: click Edit on first template card ─────────────────────────────
    print("[email-templates] editor - clicking first edit button")
    if await try_click(page,
        "button[aria-label='Edit']",
        "button[aria-label='edit']",
        "[data-testid*='edit']",
        "svg[data-testid='EditIcon']",
        "button:has(svg[data-testid='EditIcon'])",
    ):
        await save(page, "email-templates", "email-template-editor")

        # Scroll down to see the rich-text body
        print("[email-templates] editor - scrolled to body")
        await page.evaluate("window.scrollTo(0, 500)")
        await page.wait_for_timeout(500)
        await save(page, "email-templates", "email-template-editor-body")
        await page.evaluate("window.scrollTo(0, 0)")

        # Open template variables help dialog
        print("[email-templates] variables help dialog")
        if await try_click(page,
            "button[aria-label*='variable' i]",
            "button[aria-label*='help' i]",
            "button:has(svg[data-testid='HelpIcon'])",
            "svg[data-testid='HelpIcon']",
        ):
            await save(page, "email-templates", "email-template-variables-help")
            await try_click(page,
                "[aria-label='Close']",
                "button:has-text('Close')",
                "button:has-text('Cancel')",
                "[role='dialog'] button:last-child",
            )


async def section_intake_forms(page):
    # ── List ─────────────────────────────────────────────────────────────────
    print("\n[intake-forms] list")
    await goto(page, "/settings/intake-form")
    await save(page, "intake-forms", "intake-forms-list")

    # ── Actions menu on first card ─────────────────────────────────────────────
    print("[intake-forms] actions menu - clicking ⋮ on first card")
    if await try_click(page,
        "button[aria-label='more']",
        "button[aria-label='More options']",
        "svg[data-testid='MoreVertRoundedIcon']",
        "button:has(svg[data-testid='MoreVertRoundedIcon'])",
        "[class*='card']:first-child button:last-child",
    ):
        await save(page, "intake-forms", "intake-form-actions-menu")
        # Dismiss
        await page.keyboard.press("Escape")
        await page.wait_for_timeout(500)

    # ── Editor ────────────────────────────────────────────────────────────────
    print("[intake-forms] editor - navigating to first form")
    if await try_click(page,
        "button:has-text('Edit')",
        "[class*='card']:first-child",
        "[class*='Card']:first-child",
        "h2:first-of-type",
        "h3:first-of-type",
    ):
        await save(page, "intake-forms", "intake-form-editor")

        print("[intake-forms] editor - scrolled to behavior settings")
        await page.evaluate("window.scrollTo(0, 600)")
        await page.wait_for_timeout(500)
        await save(page, "intake-forms", "intake-form-editor-behavior")

        print("[intake-forms] editor - scrolled to pages section")
        await page.evaluate("window.scrollTo(0, 1200)")
        await page.wait_for_timeout(500)
        await save(page, "intake-forms", "intake-form-editor-pages")
        await page.evaluate("window.scrollTo(0, 0)")


async def section_web_reports(page):
    # ── List ─────────────────────────────────────────────────────────────────
    print("\n[web-reports] list")
    await goto(page, "/settings/web-reports")
    await save(page, "web-reports", "web-reports-list")

    # ── Editor: click first card ──────────────────────────────────────────────
    print("[web-reports] editor - clicking first report")
    if await try_click(page,
        "h2:first-of-type",
        "h3:first-of-type",
        "[class*='card']:first-child",
        "[class*='Card']:first-child",
        "a[href*='/settings/web-reports/']",
        "button:has-text('Edit')",
    ):
        await save(page, "web-reports", "web-report-editor")

        # Scroll to first section accordion
        print("[web-reports] editor - sections area")
        await page.evaluate("window.scrollTo(0, 600)")
        await page.wait_for_timeout(500)
        await save(page, "web-reports", "web-report-sections")

        # Expand first section accordion
        print("[web-reports] editor - expanding first section accordion")
        if await try_click(page,
            "[class*='MuiAccordionSummary']:first-of-type",
            "[class*='accordion']:first-child [class*='summary']",
            ".MuiAccordion-root:first-child .MuiAccordionSummary-root",
        ):
            await page.wait_for_timeout(500)
            await save(page, "web-reports", "web-report-section-editor")

        await page.evaluate("window.scrollTo(0, 0)")

        # YAML / code preview
        print("[web-reports] editor - YAML preview")
        if await try_click(page,
            "button:has(svg[data-testid='CodeIcon'])",
            "svg[data-testid='CodeIcon']",
            "button[aria-label*='yaml' i]",
            "button[aria-label*='code' i]",
            "button[aria-label*='preview' i]",
        ):
            await page.wait_for_timeout(500)
            await save(page, "web-reports", "web-report-yaml-preview")
            # Close/dismiss
            await try_click(page,
                "button:has(svg[data-testid='CodeIcon'])",
                "svg[data-testid='CodeIcon']",
                "[aria-label='Close']",
                "button:has-text('Close')",
            )


async def section_library_question_types(page):
    print("\n[library-question-types]")
    await goto(page, f"/library/edit/{LIBRARY_EDITOR_ID}", wait_ms=4000)

    # The editor's main scrollable container
    async def scroll_container(y):
        await page.evaluate(f"""
            (() => {{
                const el = Array.from(document.querySelectorAll('*')).find(e => {{
                    const s = window.getComputedStyle(e);
                    return (s.overflowY === 'auto' || s.overflowY === 'scroll') &&
                           e.scrollHeight > e.clientHeight + 50;
                }});
                if (el) el.scrollTop = {y};
            }})()
        """)
        await page.wait_for_timeout(400)

    async def expand_category(cat_name):
        """Click the MUI accordion summary to expand a category."""
        await page.evaluate(f"""
            (() => {{
                const summaries = Array.from(document.querySelectorAll('[class*="MuiAccordionSummary"]'));
                const cat = summaries.find(s => s.innerText.includes({json.dumps(cat_name)}));
                if (cat) cat.click();
            }})()
        """)
        await page.wait_for_timeout(1500)

    async def open_question(snippet):
        """Click the question row button to expand its inline editor."""
        await page.evaluate(f"""
            (() => {{
                const btns = Array.from(document.querySelectorAll('button'));
                const q = btns.find(b => b.innerText.includes({json.dumps(snippet)}));
                if (q) q.click();
            }})()
        """)
        await page.wait_for_timeout(2000)
        # Scroll the expanded editor's textarea into center of viewport
        await page.evaluate(f"""
            (() => {{
                const ta = Array.from(document.querySelectorAll('textarea'))
                    .find(t => t.value.includes({json.dumps(snippet)}));
                if (ta) ta.scrollIntoView({{behavior: 'instant', block: 'center'}});
            }})()
        """)
        await page.wait_for_timeout(600)

    async def close_question(snippet):
        """Collapse a question editor by clicking its row again."""
        await page.evaluate(f"""
            (() => {{
                const btns = Array.from(document.querySelectorAll('button'));
                const q = btns.find(b => b.innerText.includes({json.dumps(snippet)}));
                if (q) q.click();
            }})()
        """)
        await page.wait_for_timeout(600)

    # ── Categories list (collapsed) ──────────────────────────────────────────
    print("[library-question-types] categories list (collapsed)")
    await scroll_container(900)
    await save(page, "library", "library-qt-categories")

    # ── Multiple Choice Types — expand and show question list ────────────────
    print("[library-question-types] expanding Multiple Choice Types category")
    await expand_category("EXAMPLE: Multiple Choice Types")
    await scroll_container(1300)
    await save(page, "library", "library-qt-multiple-choice-expanded")

    # ── Likert question editor ───────────────────────────────────────────────
    print("[library-question-types] Likert question editor")
    await open_question("EXAMPLE LIKERT:")
    await save(page, "library", "library-qt-editor-likert")
    await close_question("EXAMPLE LIKERT:")

    # ── Binary question editor ───────────────────────────────────────────────
    print("[library-question-types] Binary question editor")
    await open_question("EXAMPLE BINARY:")
    await save(page, "library", "library-qt-editor-binary")
    await close_question("EXAMPLE BINARY:")

    # ── Rating Qualitative question editor ───────────────────────────────────
    print("[library-question-types] Rating question editor")
    await open_question("EXAMPLE RATING:")
    await save(page, "library", "library-qt-editor-rating")
    await close_question("EXAMPLE RATING:")

    # ── Input Types — expand ─────────────────────────────────────────────────
    print("[library-question-types] expanding Input Types category")
    await expand_category("EXAMPLE: Input Types")
    await page.wait_for_timeout(500)

    # ── Text question editor ─────────────────────────────────────────────────
    print("[library-question-types] Text question editor")
    await open_question("EXAMPLE TEXT:")
    await save(page, "library", "library-qt-editor-text")
    await close_question("EXAMPLE TEXT:")

    # ── Numeric question editor (percent variant) ────────────────────────────
    print("[library-question-types] Numeric question editor")
    await open_question("EXAMPLE NUMERIC PERCENT:")
    await save(page, "library", "library-qt-editor-numeric")
    await close_question("EXAMPLE NUMERIC PERCENT:")

    # ── Numeric Range Types — expand ─────────────────────────────────────────
    print("[library-question-types] expanding Numeric Range Types category")
    await expand_category("EXAMPLE: Numeric Range Types")
    await page.wait_for_timeout(500)

    # ── Numeric Range question editor ────────────────────────────────────────
    print("[library-question-types] Numeric Range question editor")
    await open_question("EXAMPLE RANGE EMP:")
    await save(page, "library", "library-qt-editor-numeric-range")
    await close_question("EXAMPLE RANGE EMP:")

    # ── Multiple Select Types — expand ───────────────────────────────────────
    print("[library-question-types] expanding Multiple Select Types category")
    await expand_category("EXAMPLE: Multiple Select Types")
    await page.wait_for_timeout(500)

    # ── Multiple Select question editor ──────────────────────────────────────
    print("[library-question-types] Multiple Select question editor")
    await open_question("EXAMPLE MS SCORED:")
    await save(page, "library", "library-qt-editor-multiple-select")
    await close_question("EXAMPLE MS SCORED:")


async def section_branding(page):
    print("\n[branding] overview")
    await goto(page, "/settings/branding")
    await save(page, "branding", "branding")

    print("[branding] colors section")
    await page.evaluate("window.scrollTo(0, 600)")
    await page.wait_for_timeout(500)
    await save(page, "branding", "branding-colors")

    print("[branding] login page section")
    await page.evaluate("window.scrollTo(0, 1200)")
    await page.wait_for_timeout(500)
    await save(page, "branding", "branding-login-page")

    print("[branding] terminology section")
    await page.evaluate("window.scrollTo(0, 1800)")
    await page.wait_for_timeout(500)
    await save(page, "branding", "branding-terminology")

    await page.evaluate("window.scrollTo(0, 0)")


async def section_library_scoring(page):
    print("\n[library-scoring]")
    await goto(page, f"/library/edit/{LIBRARY_EDITOR_ID}", wait_ms=4000)

    async def scroll_container(y):
        await page.evaluate(f"""
            (() => {{
                const el = Array.from(document.querySelectorAll('*')).find(e => {{
                    const s = window.getComputedStyle(e);
                    return (s.overflowY === 'auto' || s.overflowY === 'scroll') &&
                           e.scrollHeight > e.clientHeight + 50;
                }});
                if (el) el.scrollTop = {y};
            }})()
        """)
        await page.wait_for_timeout(400)

    # Screenshot 1: Scoring Method dropdown
    print("[library-scoring] scoring method")
    await scroll_container(200)
    await save(page, "library", "library-editor-scoring-method")

    # Expand the Scoring Section Feedback accordion
    await scroll_container(400)
    await page.evaluate("""
        (() => {
            const summaries = Array.from(document.querySelectorAll('[class*="MuiAccordionSummary"]'));
            const el = summaries.find(s => s.innerText?.includes('Scoring Section Feedback'));
            if (el) el.click();
        })()
    """)
    await page.wait_for_timeout(1500)

    # Screenshot 2: Scoring sections expanded (also shows SYNC SCORING button)
    print("[library-scoring] scoring sections + sync scoring button")
    await scroll_container(430)
    await save(page, "library", "library-editor-sync-scoring-expanded")

    # Screenshot 3: Edit section modal
    print("[library-scoring] edit section modal")
    result = await page.evaluate("""
        (() => {
            const allEls = Array.from(document.querySelectorAll('*'));
            const atRiskRow = allEls.find(el => {
                const text = el.innerText?.trim();
                return text?.startsWith('At Risk') && text?.includes('4.750') && el.children.length > 0;
            });
            if (!atRiskRow) return {found: false};
            let container = atRiskRow;
            let editBtn = null;
            for (let i = 0; i < 10; i++) {
                editBtn = container.querySelector('button svg[data-testid="EditIcon"]');
                if (editBtn) { editBtn = editBtn.parentElement; break; }
                container = container.parentElement;
                if (!container) break;
            }
            if (editBtn) {
                const rect = editBtn.getBoundingClientRect();
                return {found: true, top: rect.top, left: rect.left, width: rect.width, height: rect.height};
            }
            return {found: false};
        })()
    """)
    if result.get('found'):
        x = result['left'] + result['width'] / 2
        y = result['top'] + result['height'] / 2
        await page.mouse.click(x, y)
        await page.wait_for_timeout(2000)
        await save(page, "library", "library-editor-scoring-edit-section")


async def section_library_icons(page):
    print("\n[library-icons] opening icon picker modal")
    # The icon picker modal is embedded in the IconPickerModal component
    # This section demonstrates how to access it via the settings/branding page
    await goto(page, "/settings/branding", wait_ms=3000)
    
    # Look for any icon or color picker buttons in the branding settings
    print("[library-icons] looking for icon/color controls in branding")
    
    # Find all buttons and look for ones that might open the icon picker
    potential_icon_buttons = await page.query_selector_all("button")
    print(f"    found {len(potential_icon_buttons)} buttons on page")
    
    # Try to find the icon picker by looking for specific attributes or text
    for btn in potential_icon_buttons:
        aria_label = await btn.get_attribute("aria-label")
        title = await btn.get_attribute("title")
        text = await btn.inner_text()
        
        # Look for buttons related to icons or colors
        if any(keyword in str(aria_label or text or title).lower() for keyword in ['icon', 'color', 'palette']):
            print(f"    found potential icon button: {aria_label or text or title}")
            try:
                await btn.click()
                await page.wait_for_timeout(1500)
                
                modal = await page.query_selector("[role='dialog']")
                if modal:
                    print("[library-icons] captured icon picker modal - overview")
                    await save(page, "library", "library-icon-picker-modal")
                    
                    # Scroll in the modal to show more options
                    await page.evaluate("""
                        (() => {
                            const scrollable = Array.from(document.querySelectorAll('[role="dialog"] *')).find(e => {
                                const s = window.getComputedStyle(e);
                                return (s.overflowY === 'auto' || s.overflowY === 'scroll') && 
                                       e.scrollHeight > e.clientHeight + 100;
                            });
                            if (scrollable) scrollable.scrollTop = 250;
                        })()
                    """)
                    await page.wait_for_timeout(800)
                    
                    print("[library-icons] captured icon picker modal - scrolled")
                    await save(page, "library", "library-icon-picker-scrolled")
                    
                    # Close modal
                    await page.keyboard.press("Escape")
                    await page.wait_for_timeout(500)
                    return
            except Exception as e:
                print(f"    error clicking button: {e}")
                continue
    
    print("    note: icon picker screenshots can be manually captured from Assessment Editor or Web Reports editor")


# ── Section registry ───────────────────────────────────────────────────────────

SECTIONS = {
    "dashboard":              section_dashboard,
    "account":                section_account,
    "assessments":            section_assessments,
    "library":                section_library,
    "library-question-types": section_library_question_types,
    "library-scoring":        section_library_scoring,
    "library-icons":          section_library_icons,
    "ecosystem":              section_ecosystem,
    "industries":       section_industries,
    "settings":         section_settings,
    "report-builder":   section_report_builder,
    "custom-data":      section_custom_data,
    "email-templates":  section_email_templates,
    "intake-forms":     section_intake_forms,
    "web-reports":      section_web_reports,
    "branding":         section_branding,
}

ALL_SECTIONS = list(SECTIONS.keys())


async def main(sections: list[str]):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await context.new_page()
        await setup_auth(page, context)

        for name in sections:
            await SECTIONS[name](page)

        await browser.close()
        print(f"\nDone! ({len(sections)} section(s))")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Take VSAP doc screenshots",
        epilog=f"Available sections: {', '.join(ALL_SECTIONS)}",
    )
    parser.add_argument(
        "sections",
        nargs="*",
        metavar="SECTION",
        help="Section(s) to capture. Omit to capture all.",
    )
    args = parser.parse_args()

    unknown = [s for s in args.sections if s not in SECTIONS]
    if unknown:
        parser.error(f"Unknown section(s): {', '.join(unknown)}. Choose from: {', '.join(ALL_SECTIONS)}")

    target = args.sections if args.sections else ALL_SECTIONS
    print(f"Capturing sections: {', '.join(target)}")
    asyncio.run(main(target))
