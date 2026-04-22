"""
Playwright screenshot script for VSAP docs.
Captures authenticated screenshots into organized subfolders.

Usage:
  uv run python scripts/take_screenshots.py                        # all sections
  uv run python scripts/take_screenshots.py account                # one section
  uv run python scripts/take_screenshots.py account library        # multiple sections
  uv run python scripts/take_screenshots.py custom-data            # custom data only

Available sections:
  dashboard, account, assessments, library, ecosystem, industries, settings, report-builder, custom-data
"""
import argparse
import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright

BASE_URL = "http://demo.localhost:3000"
ACCESS_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTA5NDAwLCJpYXQiOjE3NzY4NjYyMDAsImp0aSI6IjNmZWY0Njc2Y2ZiZjQ5ODE5NzlhYTJkYjAyN2NhY2M3IiwidXNlcl9pZCI6IjU1OWE1ZmZkLThiODMtNDZhYy1hYzVlLTY3Y2EzNzE3NzU4NCIsImZ1bGxuYW1lIjoiS2V2aW4iLCJlbWFpbCI6ImtldmluQHZlc3NlbHNjYWxlLmNvbSIsInVzZXJfZ3JvdXBzIjpbImFkbWluIl19.oM-XL5DcGuSFGnigvY7IN8Tx211D608fROVXxN4Xi1U"

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "assets" / "screenshots"

COOKIES = [
    {"name": "csrftoken",    "value": "XelKhI6ztL04Xc99oHEm2ENY33AA9tBm"},
    {"name": "sessionid",    "value": "r7bt9yieyv8v8elr59chzo63mo82oxbf"},
    {"name": "API_URL",      "value": "http://demo.localhost:8000/"},
    {"name": "ACCESS_TOKEN", "value": ACCESS_TOKEN},
]

PERSIST_ROOT = json.dumps({
    "authReducers": json.dumps({
        "user": {
            "currentUser": {
                "access": ACCESS_TOKEN.removeprefix("Bearer "),
                "refresh": "",
                "account_id": "",
                "user_type": ["admin"],
                "profile_image": "",
                "fullname": "Kevin",
                "first_name": "Kevin",
                "last_name": "",
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
    print("\n[ecosystem]")
    # Map page never reaches networkidle — use domcontentloaded + long wait
    await goto(page, "/ecosystem-map", wait_ms=8000, wait_until="domcontentloaded")
    await save(page, "ecosystem", "ecosystem")


async def section_industries(page):
    print("\n[industries]")
    await goto(page, "/naics-explorer")
    await save(page, "industries", "industries")


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
    # ── Hub ──────────────────────────────────────────────────────────────────
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


# ── Section registry ───────────────────────────────────────────────────────────

SECTIONS = {
    "dashboard":      section_dashboard,
    "account":        section_account,
    "assessments":    section_assessments,
    "library":        section_library,
    "ecosystem":      section_ecosystem,
    "industries":     section_industries,
    "settings":       section_settings,
    "report-builder": section_report_builder,
    "custom-data":    section_custom_data,
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
