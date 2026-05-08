---
route: /library/edit/:id
tags:
  - library
  - assessment-definitions
  - edit
  - categories
  - scoring
  - preview
---

# Edit Assessment Definition

The Assessment Editor is the primary workspace for building and managing assessment definitions. This is one of the most important pages in the platform — from here you define every question, category, scoring rule, and piece of feedback that powers evaluations across the entire system.

## What you can do here

- Add, edit, reorder, and delete questions
- Organize questions into categories with descriptions
- Configure scoring sections with strengths, root causes, solutions, and recommendations
- Preview the full assessment, a single category, or check how the editor looks at a glance
- Find-and-replace text across the entire assessment at once
- Undo/redo changes freely before saving
- Save your changes or cancel to revert

## Editor Overview

![Library Editor Overview](../assets/screenshots/library/library-editor-overview.png)

The editor loads the full assessment in a single scrollable layout. The toolbar at the top contains the key action buttons — **PREVIEW**, **REPLACE**, **CANCEL**, and **SAVE CHANGES** — always visible as you work.

![Library Editor Toolbar](../assets/screenshots/library/library-editor-toolbar.png)

The toolbar provides one-click access to all major actions. The sidebar panel on the left can be expanded for navigation.

## Assessment Details

![Assessment Details](../assets/screenshots/library/library-editor-assessment-details.png)

The **Assessment Details** accordion at the top of the editor lets you set the assessment name, description, summary, icon, and other top-level metadata. Expand it to edit these fields.

## Scoring Sections

![Scoring Sections](../assets/screenshots/library/library-editor-scoring.png)

Below the assessment details, each category has a **Scoring Section** panel. This is where you define what the score means for respondents. Each scoring tier (e.g. *At Risk*, *Could Improve*, *Optimal*) can contain:

- **Strengths** — what the respondent is doing well
- **Root Causes** — why they may be in this range
- **Solutions** — specific things to address
- **Recommended Actions** — concrete next steps

![Scoring Section Feedback](../assets/screenshots/library/library-editor-scoring-feedback.png)

The **Scoring Section Feedback** accordion shows AI-generated suggestions for improving your scoring content. Use the **SYNC SCORING** button to pull in updated suggestions.

## Categories

![Categories](../assets/screenshots/library/library-editor-categories.png)

All categories are listed in order at the bottom of the editor. Each category shows its name and the number it holds. You can reorder them by dragging, add new ones with **Add Category**, or use the action buttons on each row to **preview**, **copy**, or **delete** the category.

![Category Expanded](../assets/screenshots/library/library-editor-category-expanded.png)

Expanding a category reveals all of its questions and the full editing interface for that section.

---

## Preview Functionality

The editor provides two levels of preview so you can see exactly how respondents will experience your assessment before publishing.

### Preview the Full Assessment

![Preview Full Assessment](../assets/screenshots/library/library-preview-full-assessment.png)

Click the **PREVIEW** button (`VisibilityIcon`) in the top toolbar to open a full-screen modal showing the entire assessment exactly as a respondent would see it — all categories, all questions, in order.

![Preview Full Assessment Scrolled](../assets/screenshots/library/library-preview-full-scrolled.png)

Scroll through the preview to review every question and response option. This is the recommended final check before saving or publishing.

**How to access:** Click `PREVIEW` in the top toolbar (labeled **Preview Assessment**).

---

### Preview a Single Category

![Preview Category](../assets/screenshots/library/library-preview-category.png)

Each category row has a dedicated **Preview category questions** button (`VisibilityIcon`). Clicking it opens a modal showing only the questions in that category.

![Preview Category Scrolled](../assets/screenshots/library/library-preview-category-scrolled.png)

Use this to quickly verify a specific section without scrolling through the full assessment.

**How to access:** In the categories list, click the eye icon (`👁`) on the category row you want to preview.

---

!!! tip "Preview early and often"
    Use category preview as you build each section to catch wording issues and layout problems immediately. Run a full assessment preview before every save to ensure the complete flow makes sense.

!!! warning "Impact on existing evaluations"
    Changes to a published assessment definition may affect in-progress evaluations. Review all changes carefully before clicking **SAVE CHANGES**.

!!! tip "Use Find & Replace for bulk edits"
    The **REPLACE** button lets you find and replace specific text across every question, description, and scoring section in one pass — ideal when rebranding or correcting a repeated term.

---

## Sync Scoring

The **SYNC SCORING** feature automatically refreshes and updates scoring suggestions for your assessment based on the latest AI recommendations.

### What Sync Scoring Does

When you click the **SYNC SCORING** button in the Scoring Section Feedback accordion, the platform:

- Analyzes your current questions and category structure
- Generates or updates suggested content for strengths, root causes, solutions, and recommended actions
- Provides AI-powered recommendations tailored to your assessment
- Updates the **Scoring Section Feedback** panel with the latest suggestions

### When to Use Sync Scoring

- **Initial assessment creation** — Generate starting suggestions for a new assessment
- **After making significant changes** — Refresh suggestions when you add, remove, or substantially modify questions
- **To improve feedback quality** — Get fresh AI recommendations to enhance the respondent experience
- **When updating existing assessments** — Keep your scoring content current with the latest suggestions

### How to Use Sync Scoring

1. Expand the **Scoring Section Feedback** accordion for a category
2. Review the current AI-generated suggestions
3. Click the **SYNC SCORING** button to refresh recommendations
4. The system will process your questions and generate updated suggestions
5. Review the new recommendations and manually incorporate them into your scoring sections as desired

!!! note "Manual integration"
    Sync Scoring provides suggestions — you maintain full control over your final scoring content. Review suggestions and manually update your Strengths, Root Causes, Solutions, and Recommended Actions sections with the content you want to use.

---

## Copy Scoring Sections

The **COPY SCORING SECTIONS** feature allows you to quickly duplicate an entire category with all its questions and scoring configuration, saving time when building similar assessment sections.

### What Copy Scoring Sections Does

When you copy a category, you create an exact duplicate that includes:

- All questions and their response options
- Category name and description
- Full scoring section configuration (Strengths, Root Causes, Solutions, Recommended Actions)
- All scoring tier definitions and feedback
- Question ordering and grouping

### When to Use Copy Scoring Sections

- **Repeating patterns** — Quickly create similar assessment sections with minimal editing
- **Scaling assessments** — Expand an assessment to multiple related topics using a proven template
- **A/B testing** — Duplicate a section to create variations for comparison
- **Building from templates** — Use a well-structured category as a foundation for new ones
- **Saving development time** — Avoid rebuilding similar sections from scratch

### How to Use Copy Scoring Sections

1. Navigate to the **Categories** list at the bottom of the editor
2. Locate the category you want to copy
3. Click the **Copy category** action button (copy icon) on that category row
4. A duplicate category will be created directly below the original with the name suffix "Copy"
5. Edit the copied category name, questions, and scoring content as needed
6. Save your changes when complete

!!! tip "Organize after copying"
    After copying a category, you can rename it and use the drag-to-reorder feature to place it in the correct position within your assessment structure.

!!! warning "Update all content"
    Don't forget to update the copied category's name and all scoring feedback to match its new purpose. Generic "Copy" names and duplicated content can confuse respondents.

---

## Draft vs. Published Editors

The platform distinguishes between **Draft** (unpublished) and **Published** assessment editors, each with different capabilities and use cases.

### Draft Assessment Editor

The Draft editor is where you design and refine unpublished assessments. You have full editing capabilities:

![Draft Editor Overview](../assets/screenshots/library/library-editor-draft-overview.png)

The draft editor provides complete control over your assessment structure, allowing you to add, modify, and reorganize all elements freely.

![Draft Editor Toolbar](../assets/screenshots/library/library-editor-draft-toolbar.png)

The toolbar in the draft editor includes all editing actions: **PREVIEW**, **REPLACE**, **CANCEL**, and **SAVE CHANGES**.

![Draft Assessment Details](../assets/screenshots/library/library-editor-draft-details.png)

In the draft editor, you can fully edit the **Assessment Details** accordion, including name, description, summary, and icon.

![Draft Scoring Sections](../assets/screenshots/library/library-editor-draft-scoring.png)

Scoring sections are fully editable in the draft editor, allowing you to refine feedback, strengths, root causes, solutions, and recommended actions.

![Draft Categories](../assets/screenshots/library/library-editor-draft-categories.png)

All categories are fully editable, allowing you to add, delete, reorder, and customize every aspect of your assessment structure.

### Published Assessment Editor

Once you publish an assessment, it can be used by respondents to complete evaluations. The Published editor provides a read-only or limited-edit view depending on your needs:

![Published Editor Overview](../assets/screenshots/library/library-editor-published-overview.png)

The published editor displays the assessment in a read-only or controlled mode to prevent accidental breaking changes to live evaluations.

![Published Editor Toolbar](../assets/screenshots/library/library-editor-published-toolbar.png)

The toolbar in the published editor reflects the limitations of editing a live assessment, with restricted actions to preserve assessment integrity.

![Published Assessment Details](../assets/screenshots/library/library-editor-published-details.png)

The **Assessment Details** section in the published editor may have limited editability to protect the assessment's core identity during active use.

![Published Scoring Sections](../assets/screenshots/library/library-editor-published-scoring.png)

Scoring sections in the published editor are displayed for reference, with limitations on editing to ensure consistency across active evaluations.

![Published Categories](../assets/screenshots/library/library-editor-published-categories.png)

Published assessment categories are visible for reference, with restricted editing capabilities to maintain assessment stability.

### Key Differences

| Feature | Draft Editor | Published Editor |
|---------|---|---|
| Full editing | ✓ | Limited |
| Add/remove questions | ✓ | May be restricted |
| Edit assessment details | ✓ | Limited |
| Modify scoring | ✓ | Limited |
| Preview assessment | ✓ | ✓ |
| View respondent data | View only | View with restrictions |

---

## Related

- [Library](index.md)
- [Create Assessment](create.md)
- [Question Types](question-types.md)
- [Scoring](scoring.md)
