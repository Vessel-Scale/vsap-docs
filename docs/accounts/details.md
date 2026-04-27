---
route: /account/:id
tags:
  - accounts
  - clients
  - contacts
  - details
---

# Account Details

The Account Details page shows all information associated with a specific account.

## What you can do here

- View contact information, industry classification, and location
- See evaluations linked to this account
- Configure which Web Reports appear in the Client Portal
- Access account editing from the edit button
- Preview the Client Portal as the client sees it

## View as Client

The **View as Client** button opens a live preview of the [Client Portal](../client-portal/index.md) for this account — exactly as the client would see it.

![View as Client button](../assets/screenshots/client-portal/cp-account-action-bar.png)

When you click **View as Client**, a **Preview Mode** banner appears at the top of the portal confirming that you are viewing on behalf of this account. You can return to the Account Details page at any time by clicking **Return to Account**.

Use this to:

- Verify the client can see the correct assessments
- Confirm which Web Reports are available in the portal
- Troubleshoot portal access issues before escalating to the client

## Overview

![Account Details](../assets/screenshots/account/account-details.png)

The Account Details view provides a comprehensive snapshot of a single organization. This page consolidates all key information about an account in one place, including company name, contact information, geographic location, NAICS industry codes, and operational details. The overview section serves as your starting point for understanding the complete profile of an account and its current status within the system.

## Web Reports Configuration

The Web Reports panel controls which assessment report templates are made available to this account's client portal view.

### What is this section for?

When you enable Web Report templates for an account, they become available for the organization's representatives to view in the **Client Portal**. This allows you to:

- **Control Portal Visibility** - Choose which report templates clients can access
- **Customize Per Account** - Different accounts can have different report templates available
- **Manage Sensitivity** - Enable only reports appropriate for a specific client
- **Streamline Navigation** - Clients only see the reports that are relevant to them

### How Web Reports configuration works

1. **Reports are created in Settings** - Administrators create and manage Web Report templates in **Settings → Web Reports**
2. **Templates are enabled per account** - On this Account Details page, you select which of the available templates should be enabled for this specific account
3. **Clients see enabled reports** - When clients log into the Client Portal, they see a **Reports** card showing only the enabled reports for their account
4. **Only active templates shown** - Only Web Report templates marked as **Active** in Settings are available for account assignment

### Enabling Reports

The Web Reports panel displays:

- **All available active report templates** from Settings
- **Checkboxes** to enable or disable each template for this account
- A list filtered to show only reports for assessment definitions with completed assessments from this account

When you check the box next to a report template, that report becomes visible to the account in the Client Portal. Unchecking removes it from the portal view.

### Important considerations

- Only **active** templates are available for assignment (inactive templates won't appear in this list)
- Only templates matching **assessment definitions** with completed assessments from this account are offered
- Changes take effect immediately - no additional save step required
- The client portal automatically shows the enabled reports in the **Reports** card

### Related documentation

For more information about creating and managing Web Report templates, see **[Web Reports](../settings/web-reports.md)** in Settings.

## Settings

The Settings section on the Account Details page controls user access and role assignments for this account.

### Account Executive Assignment

!!! note "Role Name Configuration"
	The role name displayed here (such as "Account Executive", "Account Manager", "Account Rep", etc.) is customizable and defined in your **[Branding](../settings/branding.md)** settings. The exact title shown will match what your organization has configured.

The Settings panel allows administrators to assign a user to the Account Executive role for this account. The Account Executive is responsible for:

- Managing the account relationship
- Reviewing assessment results and reports
- Coordinating with the client organization
- Ensuring proper report distribution and portal access

### How to assign an Account Executive

The Settings section displays a selector field where you can:

1. Click the **Account Executive** field (or the custom-named role)
2. Select a user from your organization
3. The assignment takes effect immediately

Only users with appropriate permissions can be assigned to this role. The current assigned user is displayed in the field, and you can change the assignment at any time.

### Related documentation

For information about customizing role names and branding settings, see **[Branding](../settings/branding.md)** in Settings.

## Geocoding

The Geocoding section allows you to assign geographic coordinates to an account based on its address.

### What is geocoding?

Geocoding converts a physical address into geographic coordinates (latitude and longitude). This enables the platform to:

- **Map accounts geographically** - Visualize where your accounts are located on maps
- **Support ecosystem analysis** - Enable location-based filtering and analysis in the Ecosystem view
- **Improve data insights** - Provide context for regional assessment trends and patterns
- **Enable location services** - Support any location-aware features in the platform

### How to geocode an account

To geocode an account:

1. Ensure the account has an **accurate and complete address** (street address, city, state/province, postal code)
2. Look for the **Geocode** button or action on the Account Details page
3. Click the button to initiate geocoding
4. The system will attempt to match the address to geographic coordinates
5. The coordinates will be saved to the account record

### Important: Address Accuracy Required

!!! warning "Address Accuracy is Critical"
	For geocoding to work correctly, the account's address **must be accurate and correctly formatted**. 
	
	- Verify the street address is complete and correct
	- Ensure the city and state/province are spelled correctly
	- Include a valid postal code
	- Correct any typos or formatting issues
	
	If geocoding fails or produces incorrect results, check the account's address in [Edit Account](edit.md) and correct any errors before attempting to geocode again.

### When geocoding fails

If geocoding cannot match an address:

- The address may be incomplete or contain errors
- The address may not exist in the geocoding service's database
- The postal code or jurisdiction may be ambiguous
- Non-standard address formatting may cause matching to fail

Always verify the account's address in **[Edit Account](edit.md)** before attempting geocoding, and make corrections as needed.

## Assessments

![Assessment Details](../assets/screenshots/assessments/assessment-details.png)

The Assessments section displays all assessments associated with this account. Here you can see the history of assessments performed on the organization, their completion status, scores, and dates. This gives you a complete audit trail of the account's assessment activity and helps track progress over time.

The Assessments section displays all assessments associated with this account. Here you can see the history of assessments performed on the organization, their completion status, scores, and dates. This gives you a complete audit trail of the account's assessment activity and helps track progress over time.

## Related

- [Edit Account](edit.md) - Update account information
- [Accounts](index.md) - Accounts overview
- [Client Portal](../client-portal/index.md) - Preview what clients see in their portal
- [Web Reports](../settings/web-reports.md) - Create and manage report templates
- [Assessments](../assessments/index.md) - Assessment overview
