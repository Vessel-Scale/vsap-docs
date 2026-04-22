---
route: /settings/custom-data
---

# Custom Data

Manage organization-specific reference data used throughout the platform. Custom data includes industry classifications (NAICS codes), regional associations, and media assets that appear across assessments, reports, intake forms, and branding.

## Quick Access Menu

The Custom Data section provides centralized management for:
- **NAICS Codes** - Industry classification system
- **Regional Manufacturer Associations (RMA)** - Geographic and organizational groupings
- **Media Library** - Images and media for use in reports and content

---

## NAICS Codes

**Route:** `/settings/custom-data/naics`

NAICS (North American Industry Classification System) codes categorize business industries. This section allows you to customize which industry codes are available in your ecosystem.

### Available Filters & Settings

When managing NAICS codes, you can use the following controls:

| Filter/Setting | Description | Use Case |
|---|---|---|
| **Search Box** | Search by code number or description | Find specific industries quickly (e.g., "336111" or "automobile") |
| **Active Status Toggle** | Show/hide inactive codes | Maintain a curated list while keeping historical data |
| **MEP List Flag** | Identify codes associated with manufacturing sectors | Filter codes relevant to Manufacturing Extension Partnership (MEP) programs |
| **Bulk Actions** | Select multiple codes at once | Activate/deactivate groups of related industries; set MEP flags for multiple codes |
| **Sort Controls** | Sort by code, description, or status | Organize codes by any column |

### NAICS Code Fields

Each NAICS code record contains:
- **Code**: Six-digit industry classification code (e.g., "336111")
- **Description**: Human-readable industry name (e.g., "Automobile Manufacturing")
- **Active Status**: Whether this code is available for selection in forms and assessments
- **MEP List Flag**: Whether this code qualifies for MEP manufacturing programs

### Where NAICS Codes Are Used

NAICS codes appear throughout the platform:

- **[Intake Forms](../settings/intake-forms.md)** - Industry Type page where users select their business classification
- **[Web Reports](../settings/web-reports.md)** - Dynamically populate assessment content based on selected industry
- **[Industries](../industries/index.md)** - Reference data for ecosystem analysis and reporting
- **[Dashboard Pivots](../dashboard/pivot-table.md)** - Group and analyze accounts by industry classification
- **Account Details** - Display associated NAICS codes for filtering and segmentation

---

## Regional Manufacturer Associations (RMA)

**Route:** `/settings/custom-data/rma`

RMAs are regional organizations that support manufacturing businesses. This section lets you define which associations are relevant to your ecosystem.

### Available Filters & Settings

When managing RMAs, you can use the following controls:

| Filter/Setting | Description | Use Case |
|---|---|---|
| **Search Box** | Search by association name | Find specific RMAs quickly |
| **Active Status Toggle** | Show/hide inactive associations | Maintain a curated list while preserving historical data |
| **Sort Controls** | Sort by name or status | Organize associations alphabetically or by status |
| **Bulk Actions** | Select multiple associations | Update active status for groups of RMAs |

### RMA Fields

Each RMA record contains:
- **Name**: Organization name (e.g., "Northeast Manufacturing Association")
- **Active Status**: Whether this RMA is available for selection in forms and accounts

### Where RMAs Are Used

RMAs are referenced throughout the platform:

- **[Intake Forms](../settings/intake-forms.md)** - Regional Associations page where users select their local association
- **Account Details** - Associate accounts with specific RMAs for ecosystem mapping
- **Dashboard Pivots** - Group and analyze accounts by regional association
- **Ecosystem Analysis** - Understand geographic distribution and regional support structures

---

## Media Library

**Route:** `/settings/custom-data/media-library`

Store and manage images and other media assets used across your reports, web content, and branding. Media uploaded here can be referenced in web reports, email templates, and custom content blocks.

### Uploading Media

You can upload media files using any of these methods:

#### 1. **Drag & Drop**
Simply drag image files from your computer and drop them into the upload zone. A visual highlight appears to indicate the drop target is active.

#### 2. **Click to Browse**
Click the upload area to open your file browser and select files from your computer.

#### 3. **Paste from URL**
If you have an image hosted online, paste its URL directly into the URL input field. The system will fetch and store the image.

#### 4. **Clipboard Paste**
Copy an image to your clipboard (e.g., from a screenshot or image editor) and paste it directly into the platform.

### Supported File Formats

The following image formats are supported:
- **JPEG** - Standard compressed format
- **PNG** - Supports transparency
- **GIF** - Animated or static
- **WebP** - Modern compressed format
- **SVG** - Vector graphics (scalable)

### Media Fields

When you upload or edit a media item, you can customize these fields:

| Field | Type | Description | Example |
|---|---|---|---|
| **Title** | Text | Custom name for the media asset | "Company Logo" |
| **Alt Text** | Text | Accessibility text describing the image | "Vessel Impact company logo" |
| **Description** | Text | Longer description of the image content and purpose | "High-resolution logo for web reports" |
| **Tags** | Multiple Selection | Categorize media by type or usage | "logo", "header", "footer" |
| **File Type** | Auto-detected | Image format (JPEG, PNG, etc.) | "image/png" |
| **File Size** | Auto-detected | Size in bytes | "245 KB" |
| **Dimensions** | Auto-detected | Width × Height in pixels | "1920 × 1080" |

### Image Preview & Metadata

#### Preview Dialog

When you click on any media item, a preview dialog appears showing:
- Full-resolution image preview
- Current metadata (title, alt text, description, tags)
- Edit button to modify the metadata
- File information (type, size, dimensions, upload date)

#### Color Picker Functionality

The image preview dialog includes an **interactive color picker** overlay that lets you:
- **Click anywhere on the image** to extract a color at that location
- **View the hex code** of the selected color (e.g., "#FF5733")
- **Copy the color code** for use in design systems or reports

**Why Color Picker is Useful:**

- **Brand Consistency** - Extract exact colors from your logo or brand materials for use in report templates and web reports
- **Themed Reporting** - Match report color schemes to brand images
- **Design Planning** - Use extracted colors for section headers, backgrounds, and accent elements in web reports
- **Color Documentation** - Create a reference guide of your brand's color palette from existing assets
- **Quick Design Reference** - No need to use separate color picker tools; extract colors directly from uploaded images

### Where Media is Used

Media uploaded to the library can be referenced in:

- **[Web Reports](../settings/web-reports.md)** - Insert images into report templates and content sections
- **[Email Templates](../settings/email-templates.md)** - Add logos and images to email content
- **Report Sections** - Use as headers, backgrounds, or content illustrations
- **Branding** - Include in your organization's visual presentation
- **Content Blocks** - Add to custom content sections within assessments

---

## Related

- [Settings](index.md)
- [Web Reports](../settings/web-reports.md) - Uses custom data in report templates
- [Intake Forms](../settings/intake-forms.md) - References NAICS and RMA data
- [Industries](../industries/index.md) - NAICS code reference and explorer
- [Dashboard Pivot Table](../dashboard/pivot-table.md) - Analyze data by custom classifications
