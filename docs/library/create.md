---
route: /evaluation-assessment-list/library/create
tags:
  - library
---

# Design an Assessment Template

Open **Getting Started → Design an assessment** or **Assessments → Library**. Start with **Browse** to copy a Shared Template Library template into your Library as a draft, or choose **Design Assessment** to create your own.

## Prepare reusable content

1. Define the intended audience, goals, and the support your organization can offer.
2. Set the assessment’s name, terminology, internal description, and group tags.
3. Write the respondent-facing landing page and completion message; optionally add images.
4. Organize categories and questions, choose response types, and configure scoring and feedback.
5. Where enabled, choose the evidence default and opt into conditional authoring when you need follow-up questions or visibility rules.
6. Preview the full questionnaire and test relevant answer paths.
7. Save the draft and confirm the saved state, then publish when ready for reuse.

AI Creator can help draft or refine content where enabled. Review its proposed questions, scoring, and suggestions before publishing. For a first rollout, work with the Vessel team to choose a template and align the recommendations with your services and expertise.

Publishing a template and starting an account assessment are separate. After publishing, [assign an assessment](../assessments/create.md) to an account and start collection from its details.

[Design guide](../getting-started/before-you-begin/design-assessment.md) · [Editor reference](edit.md) · [Question types](question-types.md) · [Scoring](scoring.md)

## Work with the AI Assessment Creator

Open **More Actions → AI Creator** in a draft template where the feature is enabled. Describe the audience, purpose, and desired question count. Work in small steps: categories first, then questions for one category, then feedback. Review each result in the editor; chat actions change the draft immediately. Save and publish are separate steps.

For a focused revision, name the category or question and say what must stay unchanged. For example:

> Update only assessment-level scoring feedback. Keep At Risk / Could Improve / Optimal and add one recommended action per band. Preserve existing strengths, questions, category order, summary, and scoring method.

Feedback can be requested at **assessment**, **category**, or **question** level. Specify the level rather than saying only “change scoring.” Updating feedback is different from changing numeric score ranges or the averaging/summed method. Default scoring is the simplest starting point; do not ask an external agent to invent numeric ranges unless you intend to customize them.

### Use an external AI agent

Choose **Copy AI Instructions** in the creator panel and provide those instructions, the current exported YAML, and your request to the external agent. Ask for complete import-ready YAML that retains unrelated content. Do not paste external YAML into internal chat expecting an import: use the supported YAML import workflow. Preview and validate the imported draft before publishing.

External instructions describe YAML authoring; the internal creator uses editor actions. They share content and scoring principles but their output formats are different. Re-copy instructions when returning to an older conversation with an external agent.

### Get reliable results with smaller models

- Give one bounded task per message and specify an explicit question or feedback count.
- Supply the current YAML for external edits; the internal creator receives the current authoring state, including existing feedback.
- Ask to preserve unrelated content and review the actual fields, not just the chat’s success message.
- Check answer choices for gaps/overlap, question types, scoring direction, feedback level, and any conditional paths.
- If an edit is missed, restate the exact field or level. Avoid asking the agent to regenerate everything to repair one field.
- AI output is a draft. Preview, save, reopen, and verify before publishing or assigning it to accounts.

For report narrative and HTML authoring, see [Web Report Templates](../settings/web-reports.md).
