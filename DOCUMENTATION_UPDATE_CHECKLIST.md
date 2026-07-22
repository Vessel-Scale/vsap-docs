# Documentation Update Checklist

**Internal reference document** — NOT published as part of the docs site.

When updating the VSAP documentation, ensure you update ALL of these locations to keep everything in sync. This checklist was created after discovering mismatches between different doc systems.

---

## 📋 Checklist

- [ ] **mkdocs.yml** (`nav:` section)
  - Add/remove/rename pages in the sidebar navigation hierarchy
  - Update page titles and paths
  - Ensure all file paths match actual markdown files

- [ ] **docs/index.md** (Home page)
  - Update "Quick Navigation" section with all new pages
  - Update "Platform Overview" feature descriptions if applicable
  - Update button links to point to correct pages (check file extensions)

- [ ] **Individual markdown files**
  - Update internal links (relative paths) to point to correct locations
  - Update image paths if files are moved to different folders
  - Check that all linked pages actually exist

- [ ] **Backend Help Assistant** (`schema-backend/app_tenant/views/v2/help_assistant_view.py`)
  - Update `DOCS_PAGES` list with all new/changed doc URLs
  - Ensure URL paths match mkdocs.yml structure exactly
  - Remove URLs for pages that no longer exist
  - Add descriptions that match the page content

- [ ] **Screenshot automation** (`vsap-docs/scripts/take_screenshots.py`)
  - Add new `section_*()` functions for new features
  - Update existing functions if screenshots locations changed
  - Add new sections to `SECTIONS` dictionary
  - Verify screenshot output paths are correct

- [ ] **Build & Deploy**
  - Run `uv run zensical build` to verify no build errors
  - Check that all pages are accessible in `site/` folder
  - Test links locally before deploying
  - Hard refresh browser (Ctrl+Shift+R) to clear cache

---

## 🔧 Common Issues & Solutions

### Issue: Pages return 404 even after being created
**Cause:** mkdocs.yml not updated or files not rebuilt
**Solution:** 
1. Verify page exists in correct location
2. Check mkdocs.yml nav section includes the path
3. Run `rm -rf .cache site && uv run zensical build`

### Issue: Sidebar links are broken
**Cause:** mkdocs.yml path doesn't match actual file
**Solution:**
1. Check file extension (should be `.md`)
2. Verify path uses `/` not `\`
3. Check for typos in path
4. Test link works before committing

### Issue: AI Help Assistant doesn't know about feature
**Cause:** DOCS_PAGES list in help_assistant_view.py not updated
**Solution:**
1. Add page URL to `DOCS_PAGES` list in backend
2. Restart backend server
3. Test assistant can find the feature again

### Issue: Image paths are broken after reorganization
**Cause:** Markdown files reference old image paths
**Solution:**
1. Use relative paths: `../../assets/screenshots/...`
2. Update `../../` depth based on new folder structure
3. Verify image files exist at referenced paths

### Issue: Screenshots are outdated or missing
**Cause:** take_screenshots.py not updated for new features
**Solution:**
1. Add new section function to script
2. Add section to SECTIONS dict
3. Run script to capture new screenshots
4. Update markdown files to reference new images

---

## 📂 File Locations Reference

| Document Type | Location | Purpose |
|---|---|---|
| Navigation structure | `mkdocs.yml` (nav section) | Sidebar menu + page hierarchy |
| Home page | `docs/index.md` | Landing page with quick nav links |
| Help assistant index | `schema-backend/app_tenant/views/v2/help_assistant_view.py` | AI can find docs pages |
| Screenshot automation | `vsap-docs/scripts/take_screenshots.py` | Captures UI screenshots |
| Content pages | `docs/*/index.md` | Actual documentation |
| Assets | `docs/assets/screenshots/*` | Screenshots and images |

---

## 🚀 Update Process (Step-by-Step)

When adding a new feature to the docs:

1. **Create the markdown file** in appropriate folder under `docs/`
2. **Update mkdocs.yml** with new page in correct nav hierarchy
3. **Update docs/index.md** Quick Navigation section
4. **Update backend DOCS_PAGES** in help_assistant_view.py
5. **Add screenshot section** to take_screenshots.py if needed
6. **Capture screenshots** by running the script
7. **Update image references** in markdown files
8. **Build & test locally:** `uv run zensical build && uv run zensical serve`
9. **Verify all links work** in browser
10. **Test Help Assistant** can find the new feature
11. **Commit all changes** across both repos

---

## 📝 Last Updated

- **Date:** 2026-07-22
- **Reason:** Comprehensive docs restructure (Getting Started, Dashboards, Impact Tracker, Ecosystem, Settings)
- **Files Modified:** 10+ files across backend and docs
- **Lessons Learned:** Always update all 5 locations simultaneously when docs change
