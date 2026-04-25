---
route: /library/create
tags:
  - library
  - assessment-definitions
  - create
  - YAML
---

# Create Assessment Definition

Assessment definitions are the templates used to create new assessments. Use the Assessment Editor to build a new definition with sections, questions, and scoring rules.

## Getting Started

To create a new assessment definition:

1. Navigate to the **Assessment Library** (Assessments > Library)
2. Click the **Design Assessment** button at the top of the Assessment List
3. The Assessment Editor will open with a blank definition ready for configuration

## Editor Overview

The Assessment Editor provides a complete interface for building assessment definitions. You'll configure:

### Top Section
- **Assessment Name** — The title of your assessment definition
- **Noun Descriptor** — The term used for respondents (e.g., "Facility", "Establishment", "Plant")
- **Scoring Method** — Choose between "Averaging" (consistent scale) or "Summing" (total points)
- **Description** — Internal documentation about the assessment's purpose
- **Summary** — Concise overview (appears in the Library list)

### Assessment Structure
- **Groups** — Organize questions into logical sections (e.g., "Leadership", "Operations", "Technology")
- **Questions** — Add questions within each group, specifying type, parameters, and scoring

### Question Configuration
Add questions within groups by selecting a question type and configuring its parameters. Each question type has different options:

- **Text** — Open-ended responses (Required, Scorable)
- **Numeric** — Single numeric values with optional units (Min/Max/Step)
- **Numeric Range** — Values matched against score ranges
- **Multiple Choice** — Single selection from predefined options
- **Multiple Select** — Multiple selections with optional limits

See the [Question Types](question-types.md) page for detailed information about each question type and its configuration options.

## Next Steps

Once you've configured your assessment definition, see [Edit Assessment Definition](edit.md) for comprehensive guidance on working with the editor, managing questions, configuring scoring, and publishing your definition.

## Related

- [Library](index.md)
- [Edit Assessment Definition](edit.md)
- [Question Types](question-types.md)
- [Scoring](scoring.md)
