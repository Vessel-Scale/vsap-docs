---
tags:
  - industries
  - NAICS
  - dashboard
  - reports
  - ecosystem
  - intake-forms
  - assessments
---

# Platform Integration

Assigning a NAICS code to an Account unlocks industry-aware features throughout the platform. Because all four levels of the hierarchy are implied by a single 6-digit code, the platform can aggregate and filter data at any level — Sector, Subsector, Group, or full Industry — without any extra configuration.

## Where NAICS Data Is Used

| Feature | How industry data is used |
|---|---|
| **Dashboard — Business Size by NAICS Sector** | Groups all accounts by their 2-digit Sector and plots company size distribution per sector |
| **Dashboard — Average Score by NAICS** | Aggregates assessment scores at the Sector or Subsector level for benchmarking |
| **Dashboard Pivot Table** | Allows pivoting by Sector, Subsector, Group, or full Industry code |
| **Ecosystem Map** | Filter the map by NAICS Sector or Subsector to visualize geographic concentration |
| **Intake Form — Industry Type page** | Lets a submitting company select their 6-digit code; the result is stored on their Account |
| **Web Reports** | Dynamically populate report content based on the account's industry classification |
| **Settings → Custom Data → NAICS** | Admins control which codes are active and which are flagged for MEP programs |

## How a Code Gets Assigned

A NAICS code is stored at the Account level and can be set in two ways:

1. **Intake form** — the Industry Type page of an intake form lets the submitting company search and select their 6-digit code. On submission, it is saved to their Account automatically.
2. **Account details** — an admin can set or update the NAICS code manually from the Account details page.

Once set, the code propagates to all features in the table above without any additional steps.

## Related

- [Industries Overview](index.md)
- [NAICS Hierarchy](hierarchy.md) — browse and understand the four levels
- [Dashboard](../dashboard/index.md) — charts that use NAICS sector/subsector data
- [Ecosystem Map → Filters](../ecosystem/filters.md) — filter by NAICS in the map
- [Settings → Intake Forms](../settings/intake-forms.md) — configure the Industry Type page
- [Settings → Custom Data](../settings/custom-data.md) — manage active NAICS codes
- [Settings → Web Reports](../settings/web-reports.md) — use industry classification in report templates
