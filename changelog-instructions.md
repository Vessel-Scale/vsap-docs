# Changelog Update Instructions

**Purpose**: This document guides future updates to the internal changelog (`changelog.md`) for upcoming releases.

---

## Overview

The changelog is maintained as an **internal document** focused on **user-facing features and enhancements only**. It serves as a guide for updating external user-facing documentation and is NOT directly integrated into the public docs code.

---

## Process for Next Release (v2.61+)

### 1. **Identify Tags**
- Find the release tags in both `schema-backend` and `schema-frontend` repositories
- Use git commands to locate tags: `git tag -l | grep "v2.61" | sort -V`
- Combine both backend and frontend changes under a single version section (even if they have separate .0 and .1 releases)

### 2. **Extract Commit History**
From the appropriate workspace folders:

**For Frontend Changes:**
```bash
cd /home/kt/code/vessel/vsap/schema-frontend
git log <PREVIOUS_VERSION>..v<NEW_VERSION> --oneline --no-decorate
```

**For Backend Changes:**
```bash
cd /home/kt/code/vessel/vsap/schema-backend
git log <PREVIOUS_VERSION>..v<NEW_VERSION> --oneline --no-decorate
```

### 3. **Filter & Organize Changes**

**INCLUDE:**
- ✅ Totally new features and major functionality additions
- ✅ Significant UI/UX improvements (structural changes, new workflows, important visual redesigns)
- ✅ Meaningful performance enhancements that users will experience
- ✅ New authentication methods or security improvements
- ✅ New reporting or data export capabilities
- ✅ Enhanced integrations visible to end users

**EXCLUDE:**
- ❌ Minor style tweaks, spacing adjustments, or visual polish (e.g., button color changes, form padding adjustments)
- ❌ Typo fixes and wording corrections
- ❌ Dev-only refactoring and code cleanup
- ❌ Dependency updates (unless critical for user experience)
- ❌ Internal bug fixes (.0 and .1 patch versions)
- ❌ Test suite improvements
- ❌ Developer documentation updates
- ❌ Internal code restructuring

### 4. **Structure & Write**

Use this hierarchy in `changelog.md`:

```
## v<VERSION>

### Core Features & Enhancements
- Group related features under descriptive subheadings
- Use **bold** for feature titles
- Provide 1-2 sentence descriptions of user impact
- Use bullet points for clarity

### User Experience Improvements
- Quick wins and polish items
- Minor UI/UX enhancements
- Accessibility improvements

### Notes
- Mention any special considerations
- Link to related features from previous versions if relevant
```

### 5. **Guidelines for Writing Descriptions**

- Write from **user perspective** (not developer)
- Focus on *what users can do* and *how it improves their experience*
- Avoid technical jargon unless essential
- Be concise—aim for 1-2 sentences per item
- **Be specific and precise**: Name the exact component, field, or workflow affected (e.g., "Contact Email field validation" instead of "improved validation")
- **Only create bullets for significant changes**: New features, major workflows, substantial UI redesigns. Combine minor related fixes into a single concise line or exclude entirely if trivial
- Avoid vague language like "improved", "enhanced", or "updated" without explaining what specifically changed
- Avoid adding fluff or redundant bullets that restate the same feature from different angles
- Group related features to show interconnections, but only if they constitute meaningful changes

### 6. **Examples of Good vs Bad**

**❌ Bad (too vague):**
> Refactor ContactCard component and remove unused imports

**✅ Good (specific and developer-focused, exclude from changelog):**
> (Don't include internal refactoring—skip it entirely)

---

**❌ Bad (vague, minor change):**
> Improved contact card styling

**✅ Good (skip minor style tweaks, only include if major redesign):**
> (Exclude minor styling—only include if restructuring the contact card workflow itself)

---

**❌ Bad (too vague):**
> Add is_client_visible field to YamlAssessment model

**✅ Good (specific, user-facing, meaningful feature):**
> **Client-Only Assessments**: Create assessments visible exclusively to client portal users for self-service completion

---

**❌ Bad (sounds like a feature but too minor):**
> Fixed typos in assessment template

**✅ Good (exclude, not user-facing):**
> (Don't include—typos don't go in the changelog)

---

**❌ Bad (vague, sounds like minor tweaks):**
> Updated form fields and improved layout

**✅ Good (specific and significant):**
> **Redesigned Contact Intake Form**: New multi-step workflow with inline validation and progress indicators

---

## Version Format

- Use semantic versioning: `## v2.61`
- If both .0 and .1 releases occur, combine under single version section
- Move older versions below current version (newest first)
- Keep formatting consistent with existing entries

---

## Last Updated
June 2026 (Established for v2.60 release)

## Maintained By
Development & Product Team
