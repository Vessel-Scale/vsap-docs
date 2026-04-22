---
route: /settings/branding
---

# Branding

Customize the visual identity, colors, logos, and terminology for your platform instance. These settings appear throughout the application and affect how your organization is represented to all users.

## Overview

Navigate to **Settings → Branding** to configure:

- **Organization identity** — Company name, logos, and browser tab appearance
- **Color scheme** — Primary and secondary brand colors
- **Login page** — Custom headline and description text
- **Terminology** — Business terms used throughout the app (e.g., "Assessments" vs "Evaluations")
- **Report builder** — Custom names and descriptions for report sections
- **Business rules** — Employee count thresholds for company size classification

Changes take effect immediately after saving (the page will reload automatically).

---

## Organization Identity

### Company Name

The name displayed in the header sidebar and throughout the application. Leave blank to use platform defaults.

### Primary Logo

Your organization's main logo, displayed in:
- Header/sidebar
- Login page
- Navigation bars
- Assessment pages

**Recommended size:** 200×60 pixels  
**Supported formats:** PNG, JPG, GIF, WebP

### Secondary Logo

An alternative logo used in:
- Reports and document exports
- Email templates (where appropriate)

**Recommended size:** 200×60 pixels

### Favicon

The small icon displayed in browser tabs.

**Recommended size:** 32×32 or 64×64 pixels

### Browser Tab Title

The text shown in the browser tab when users view the application. If not set, defaults to "Smart Assessment Platform".

---

## Colors

### Primary Color

Your brand's main color, used for:
- Active navigation indicators (underlines, borders)
- Accent elements throughout the interface
- Links and interactive highlights

**Format:** Hex color code (e.g., `#1976d2`)

### Secondary Color

An accent color for alternative states and emphasis. Used in:
- Secondary buttons
- Alternative highlights
- Contrast elements

**Format:** Hex color code (e.g., `#dc004e`)

---

## Login Page Customization

### Login Headline

Main headline displayed above the login form. Add a welcome message or organization name.

**Example:** "Welcome to the Smart Assessment Platform"

### Login Paragraph

Description or supporting text displayed below the headline. Provide context about the platform or your organization.

**Example:** "Sign in to access assessments, reports, and performance insights."

---

## Terminology

Customize business terms used throughout the application to match your organization's language.

### Assessment Property Name

What the platform calls assessments. Default: **"Assessment"**

This term appears in:
- Navigation menus
- Page titles
- Help text
- Report headings

**Examples:** "Assessment", "Evaluation", "Review", "Survey"

### Account Executive Name

The title for administrators managing client accounts. Default: **"Manager of Client Services"**

This term appears when displaying contact information and in admin descriptions.

**Examples:** "Account Manager", "Client Advisor", "Project Manager"

---

## Report Builder Customization

When users build custom reports in the Report Builder, they work with sections organized by category. You can customize the names and descriptions of these sections.

### Category Tab Names

| Default | Use Case |
|---------|----------|
| Strengths | Positive findings and capabilities |
| Gaps, Challenges, & Threats | Areas for improvement |
| Root Causes | Underlying reasons for challenges |
| Solutions | Proposed approaches to address gaps |
| Recommended Actions | Specific next steps and recommendations |

**To customize:** Enter your preferred term or phase for each category tab.

### Category Tab Descriptions

Short help text displayed under each tab name in the Report Builder. These guide users on what content belongs in each section.

**Examples:**

- **Strengths** (default): "Highlight the team strengths for future success."
- **Gaps, Challenges, & Threats** (default): "Identify areas where team goals aren't met, cite specific opportunities, or discuss external risks."
- **Root Causes** (default): "Explain the underlying reasons for the challenges identified above."

**To customize:** Provide a brief, action-oriented description for each section.

---

## Business Rules

### Company Size Thresholds

Define the employee count boundaries used to classify companies as Small, Medium, or Large.

| Setting | Default | Purpose |
|---------|---------|---------|
| **Small Company Threshold** | 50 employees | Upper limit for "Small" classification |
| **Medium Company Threshold** | 250 employees | Upper limit for "Medium" classification |

**How it works:**
- Companies with ≤ 50 employees are classified as "Small"
- Companies with 51–250 employees are classified as "Medium"
- Companies with > 250 employees are classified as "Large"

**Impact:** Used in company size displays, filtering, and data aggregation throughout the platform.

---

## Tips & Best Practices

- **Logo dimensions** — Upload logos in the recommended sizes to avoid distortion. The platform will handle responsive scaling.
- **Color contrast** — Ensure your primary color has sufficient contrast for readability, especially for accessibility.
- **Terminology consistency** — Choose terminology that aligns with how your organization refers to assessments internally.
- **Report builder sections** — Write descriptions that clearly explain to users what content should go in each report section.
- **Page reload** — After saving branding changes, the page will reload automatically to reflect the updates.
- **Testing** — After making changes, verify the appearance in different browsers and on mobile devices.

---

## Related

- [Settings](index.md)
- [Email Templates](email-templates.md)
- [Intake Forms](intake-forms.md)
- [Custom Data](custom-data.md)
