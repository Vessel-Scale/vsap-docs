---
route: /evaluation-assessment-detail/:id
tags:
  - assessments
  - scoring
  - results
  - details
  - respondents
---

# Assessment Details

The Assessment Details page shows all data captured for a single assessment instance.

## What you can do here

- Review all question responses and scores
- See scoring summaries and breakdowns
- Edit the assessment
- Navigate to the Report Builder for this assessment

## Assessment Response Data

![Evaluation Details](../assets/screenshots/assessments/assessment-details.png)

The Assessment Details page displays the complete record of an assessment that was performed on a specific account or organization. This view shows all questions that were answered, the responses provided, and any supporting documentation or notes. The detailed data view allows you to audit the complete assessment history, verify that all questions were properly answered, and understand the basis for any scores or recommendations that were generated from this assessment.

## Sections

### Responses

The Responses section shows each question from the assessment alongside the respondent's answer. Questions are grouped by category, and scorable questions display their assigned point value next to the response. You can review all answers in one place to audit the assessment or understand the basis for its scores.

See [Assessment Question Types](question-types.md) for details on how each question type captures and scores responses.

### Scoring

The Scoring section shows how the respondent's answers translated into a final score. Category scores are broken down individually, and the overall result is displayed using the scoring method configured in the assessment definition — either **Averaged** (scores averaged across all questions) or **Summed** (scores totaled across all questions).

See [Assessment Scoring](scoring.md) for a full explanation of how scores are calculated and how scoring sections (At Risk, Could Improve, Optimal) are defined.

### Edit Assessment

![Assessment Editor](../assets/screenshots/assessments/assessment-details.png)

The assessment editor allows you to fill in or modify responses to assessment questions. This interface is used both when creating new assessments and when editing existing responses from the Assessment Details page.

Within the editor, you can:

- **View Questions**: Browse questions organized by category
- **Provide Responses**: Fill in answers, scores, and supporting information
- **Navigate Categories**: Move between different sections of the assessment
- **Track Progress**: See which questions have been answered

The editor provides a consistent experience whether you're completing a new assessment or revisiting responses to an existing assessment.

## Related

- [Getting Started: Step 4](../../getting-started/send-assessment.md) — Quick-start guide to sharing assessments
- [Getting Started: Step 5](../../getting-started/analyze-results.md) — Quick-start guide to analyzing results
- [Assessments](index.md)
- [Report Builder](report-builder.md)
