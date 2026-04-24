"""
Playwright screenshot script for VSAP docs.
Captures authenticated screenshots into organized subfolders.

Usage:
  uv run python scripts/take_screenshots.py                        # all sections
  uv run python scripts/take_screenshots.py account                # one section
  uv run python scripts/take_screenshots.py account library        # multiple sections
  uv run python scripts/take_screenshots.py custom-data            # custom data only

Available sections:
  dashboard, account, assessments, library, ecosystem, industries, settings, report-builder, custom-data,
  email-templates, intake-forms, web-reports, branding
"""
import argparse
import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright

BASE_URL = "http://testv2.localhost:3000"
ACCESS_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MDg5MTgxLCJpYXQiOjE3NzcwNDU5ODEsImp0aSI6IjQxM2ExNGQ0ZmYxZDQ2OTA5N2U4YzMyYzZjYzU5MmE4IiwidXNlcl9pZCI6IjZjNjkxYjQzLTQwMGYtNGRiZi1hNWFlLTRmYWZlNmVlMDYyYyIsImZ1bGxuYW1lIjoiS2V2aW4gVGV0eiIsImVtYWlsIjoia2V2aW5AdmVzc2Vsc2NhbGUuY29tIiwidXNlcl9ncm91cHMiOlsiYWRtaW4iLCJhY2NvdW50X2V4ZWN1dGl2ZSJdfQ.pc9uW1gZV6CcYthcXwpO0swbhGuarR_DdGCtv45Abrw"

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "assets" / "screenshots"

COOKIES = [
    {"name": "csrftoken",    "value": "aYgogqONppu5mvxHgiwQUB2zX4ub0HiH"},
    {"name": "API_URL",      "value": "http://testv2.localhost:8000/"},
    {"name": "ACCESS_TOKEN", "value": ACCESS_TOKEN},
]

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
    print("\n[dashboard]")
    await goto(page, "/dashboard")
    await save(page, "dashboard", "dashboard")


async def section_account(page):
    print("\n[account] list")
    await goto(page, "/account")
    await save(page, "account", "account-list")

    print("[account] details - clicking first row")
    if await try_click(page,
        "tbody tr:first-child td:first-child",
        "tbody tr:first-child",
        "a[href*='/account/']",
    ):
        await save(page, "account", "account-details")

        print("[account] edit - clicking edit button")
        if await try_click(page,
            "button:has-text('Edit')",
            "a:has-text('Edit')",
            "[aria-label='edit']",
            "[data-testid='edit-btn']",
        ):
            await save(page, "account", "account-edit")


async def section_assessments(page):
    print("\n[assessments] collections")
    await goto(page, "/evaluation-assessment-list")
    await save(page, "assessments", "assessment-collections")

    print("[assessments] details - clicking first row")
    if await try_click(page,
        "tbody tr:first-child",
        "tbody tr:first-child td",
        "tbody tr:first-child td:first-child",
        "[class*='row']:first-child",
        "[class*='Row']:first-child",
        "a[href*='/evaluation']",
        "a[href*='/assessment']",
    ):
        await save(page, "assessments", "assessment-details")


async def section_library(page):
    print("\n[library] list")
    await goto(page, "/library")
    await save(page, "library", "library-list")

    print("[library] editor - clicking first card title")
    if await try_click(page,
        "h2:first-of-type",
        "h3:first-of-type",
        "[class*='card']:first-child",
        "[class*='Card']:first-child",
        "[class*='item']:first-child h2",
        "a[href*='/library/edit']",
    ):
        await save(page, "library", "library-editor")

        print("[library] editor-category - clicking second tab")
        if await try_click(page,
            "[role='tab']:nth-child(2)",
            "button[role='tab']:nth-of-type(2)",
            "[role='tablist'] button:nth-child(2)",
            "button:has-text('Category')",
            "button:has-text('Categories')",
            "button:has-text('Questions')",
            "button:has-text('Sections')",
        ):
            await save(page, "library", "library-editor-category")


async def section_ecosystem(page):
    print("\n[ecosystem] overview - map with filters panel open")
    # Map page never reaches networkidle — use domcontentloaded + long wait
    await goto(page, "/ecosystem-map", wait_ms=8000, wait_until="domcontentloaded")
    await save(page, "ecosystem", "ecosystem")

    # ── Filters panel ────────────────────────────────────────────────────────
    # Filters panel is open by default; capture it in full view
    print("[ecosystem] filters panel visible")
    await save(page, "ecosystem", "ecosystem-filters")

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

    # ── Assessment filter → Scores view ──────────────────────────────────────
    print("[ecosystem] selecting an assessment")
    if await try_click(page,
        "label:has-text('Assessment') ~ * [role='combobox']",
        "div:has(> label:has-text('Assessment')) .MuiSelect-select",
        "[id*='assessment']",
    ):
        await page.wait_for_timeout(600)
        # Pick first real assessment (index 1 skips "Any")
        if await try_click(page,
            "[role='listbox'] [role='option']:nth-child(2)",
            "[role='option']:nth-child(2)",
        ):
            await page.wait_for_timeout(2000)
            await save(page, "ecosystem", "ecosystem-assessment-selected")

            # Click the "Scores" toggle button (only appears after assessment selected)
            print("[ecosystem] switching to Scores view")
            if await try_click(page,
                "button:has-text('Scores')",
                "[role='button']:has-text('Scores')",
            ):
                await page.wait_for_timeout(3000)
                await save(page, "ecosystem", "ecosystem-scores")

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


# ── Section registry ───────────────────────────────────────────────────────────

SECTIONS = {
    "dashboard":        section_dashboard,
    "account":          section_account,
    "assessments":      section_assessments,
    "library":          section_library,
    "ecosystem":        section_ecosystem,
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
