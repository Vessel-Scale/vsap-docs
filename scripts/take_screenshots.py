"""
Playwright screenshot script for VSAP docs.
Captures authenticated screenshots into organized subfolders.

Usage:
  uv run python scripts/take_screenshots.py                  # all sections
  uv run python scripts/take_screenshots.py account          # one section
  uv run python scripts/take_screenshots.py account library  # multiple sections

Available sections:
  dashboard, account, assessments, library, ecosystem, industries, settings, report-builder
"""
import argparse
import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright

BASE_URL = "http://testv2.localhost:3000"
ACCESS_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2NTg4ODE0LCJpYXQiOjE3NzY1NDU2MTQsImp0aSI6IjUwNTk2MTJhYWIyNTQ0YTc4MTQ0OGE0NTczYzFkMzYxIiwidXNlcl9pZCI6IjZjNjkxYjQzLTQwMGYtNGRiZi1hNWFlLTRmYWZlNmVlMDYyYyIsImZ1bGxuYW1lIjoiS2V2aW4gVGV0eiIsImVtYWlsIjoia2V2aW5AdmVzc2Vsc2NhbGUuY29tIiwidXNlcl9ncm91cHMiOlsiYWRtaW4iLCJhY2NvdW50X2V4ZWN1dGl2ZSJdfQ.lmJOAlgdBPaRdpE285gPXU5_FPpa7oBNtVF63Mm_oTw"

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "assets" / "screenshots"

COOKIES = [
    {"name": "csrftoken",    "value": "aYgogqONppu5mvxHgiwQUB2zX4ub0HiH"},
    {"name": "sessionid",    "value": "ngsidfkxqpd84m56tuu6vge6e2n73xw8"},
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
