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
- ✅ User-facing features (new capabilities, UI/UX improvements)
- ✅ Significant performance enhancements that users will notice
- ✅ New authentication methods or security improvements
- ✅ New reporting or data export capabilities
- ✅ Enhanced integrations visible to end users

**EXCLUDE:**
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
- Group related features to show interconnections
- **Minimize bullet points**: Only add separate bullets for distinct user-facing changes; combine related aspects into single bullets to improve readability
- Avoid adding fluff or redundant bullets that restate the same feature from different angles
- **Be specific**: If a change only affects one or two specific items (e.g., a single template variable, one field fix), name them explicitly rather than using vague language like "improved" or "enhanced"

### 6. **Examples of Good vs Bad**

**❌ Bad:**
> Refactor ContactCard component and remove unused imports

**✅ Good:**
> **Enhanced Contact Management**: Improved contact card interface with clearer styling and portal access indicators

---

**❌ Bad:**
> Add is_client_visible field to YamlAssessment model

**✅ Good:**
> **Client Assessment Visibility Controls**: New ability to create assessments visible exclusively to client portal users for self-service completion

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
