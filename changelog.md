# Changelog

**Internal Guide for User-Facing Documentation** - Focus on features and improvements that impact end users. This document guides external documentation updates. *Latest versions appear first.*

---

## v2.68

### Core Features & Enhancements

#### **AI-Powered Assessment Creation**
- **AI Assessment Creator**: New AI-powered assistant for rapid assessment creation with chat interface, providing automated guidance and YAML generation for building assessments from scratch

#### **AI-Generated Web Reports**
- **AI Web Report Creator**: Intelligent web report generation using AI to analyze assessment data, extract website content, and automatically structure report sections with appropriate visualizations and styling

#### **Public Assessment Library**
- **Assessment Library Browser**: New public library feature for discovering and browsing community assessments with categorization and filtering capabilities
- **Assessment Copying & Versioning**: Import assessments from the public library with automatic version management and duplicate name handling
- **Bulk Assessment Import**: Ability to copy multiple assessments at once from the library into your workspace

#### **Enhanced Qualitative Insights**
- **AI-Generated Recommendations**: Integrated AI assistant for generating actionable recommendations based on qualitative insights with separated identified and AI-generated content
- **Qualitative Insights Display**: Improved visualization and organization of qualitative insights alongside quantitative assessment results

#### **Advanced Web Report Capabilities**
- **Webpage Content Integration**: Automatic extraction and processing of website content for enhanced web reports with improved image handling and context integration
- **Report Styling & Formatting**: Enhanced CSS color and font extraction from source materials with support for custom subsection headers and styling options
- **Optional Report Sections**: Ability to configure which assessment categories appear in web reports with customizable section layouts

#### **Scoring & Visualization Improvements**
- **Enhanced Score Calculations**: Improved scoring logic for Gas Gauge and Bar Chart visualizations with averaged min/max score handling
- **Response Distribution & Analytics**: Comprehensive tracking of assessment responses with duplicate submission prevention and enhanced initialization logic

### User Experience Improvements

- **Performance Optimization**: Improved component performance across Assessment Creator, Web Report Creator, and YAML Editor with memoization and debouncing
- **Help Assistant Integration**: Enhanced help assistant with guidance on scoring methods and workflow switching
- **Category & Metadata Handling**: Improved category extraction and validation from YAML assessments with better user feedback
- **Field Validation**: New character length limits and validation for assessment field names to ensure data consistency

---

## v2.67

### Core Features & Enhancements

#### **Assessment Auditor with AI Integration**
- **Assessment Auditor**: LLM-powered assessment validation service with interactive auditor modal featuring deterministic rules, severity filtering, and elapsed time tracking; includes action menu in YAML Assessment Editor for quick access to preview, audit, media library, and replace options

#### **Region Management & Enhanced Exports**
- **Region Support**: Enhanced account management with region-based organization and filtering capabilities
- **Advanced Data Export**: New export functionality for accounts, clients, and dashboard analytics with CSV/YAML downloads and configurable dataset selection

#### **Scoring & Performance Improvements**
- **Enhanced Scoring & Validation**: Improved scoring method dropdown with better styling, optimized score aggregation in dashboards, and intelligent conversion of preset questions with custom answers to multiple_choice format

### User Experience Improvements

- **Auditor & Editor Enhancements**: Improved auditor state management, severity filtering, and hover-based action menu in YAML Assessment Editor with dynamic branding integration
- **UI/UX Refinements**: Updated tab styling in NAICS Explorer and improved error handling for missing data states

---

## v2.66

### Core Features & Enhancements

#### **Assessment Workflow Guide**
- **New Workflow Guide Card**: Comprehensive guided workflow interface for managing assessment lifecycle from start to completion with status-aware navigation and built-in report management
- **Dynamic Status & Branding**: Workflow guide automatically adapts based on assessment status with styling that reflects organization branding for consistent visual experience

#### **Assessment Report Sharing**
- **Share Report Functionality**: Consilidate web/pdf share assessment reports directly from assessment details with modal interface for easy distribution

#### **NAICS Explorer Navigation**
- **Sector Grouping & Organization**: Enhanced NAICS Explorer with logical sector grouping and improved navigation structure for better data exploration
- **URL Sync & Navigation History**: Navigation state now syncs with URL parameters, enabling shareable exploration sessions and preserving user search context

#### **Link Editing & Rich Content**
- **LinkedText Component**: New component implementation enabling inline link editing and management across assessment content

#### **User & Admin Management**
- **Admin User Management**: New admin endpoints for managing tenant users with full CRUD operations (create, read, update, delete)

### User Experience Improvements
- **CreateButton Styling**: Improved CreateButton with hover effects and border radius for better visual feedback
- **Assessment Component Layout**: Various layout and styling improvements across assessment detail components for better visual hierarchy
- **Dynamic Assessment Terminology**: Assessment noun labels now dynamically updated throughout the interface for consistency

---

## v2.65

### Core Features & Enhancements

#### **Directors Dashboard**
- **New Directors Dashboard**: Comprehensive analytics and management interface for directors with configurable components
- **Dashboard Analytics Pivot**: CSV and YAML export capabilities for directors analytics data
- **Company Size & Business Distribution Analysis**: New analytics views for company size and business size distribution by NAICS code
- **Action Tracker Integration**: Integrated action tracker items view in directors dashboard with filtering and metrics display
- **Impact Metrics Dashboard**: Aggregated action tracker data visualization for ecosystem impact tracking
- **Offered Solutions Tracking**: New directors feature for tracking and managing offered solutions

#### **Ecosystem Map & Congressional Districts**
- **State Borders Selector**: Enhanced map control to highlight and customize state boundaries with color picker and line styling options
- **Congressional Districts Control**: New map control for selecting and displaying Congressional District overlays
- **Enhanced Filtering**: Improved map filter dropdowns for status and priority with better typography and visibility
- **Impact Metrics View**: New impact metrics visualization in ecosystem map with filtering and data aggregation

#### **Sidebar Navigation & Creation Flow**
- **Navigation State Persistence**: Sidebar navigation state now persists across page reloads using session storage
- **Enhanced Create Button**: Redesigned CreateButton with descriptions, icons, and assessment definition context for improved discoverability
- **Intake Form Creation**: New quick-create button in IntakeFormPickerModal when no forms exist
- **Assessment Context Navigation**: Assessment definition ID passed through navigation state for streamlined creation flow

#### **Intake Form Enhancements**
- **Email Validation & Notifications**: New email validation with user notifications for invalid or duplicate email addresses
- **EULA Footer Component**: Integrated EULA footer across intake form pages (Landing and Methodology pages)
- **Enhanced Error Handling**: Replaced failure modal with improved error modal for better error communication
- **Configuration Validation**: Enhanced intake form configuration validation and improved logging for debugging

#### **Assessment Collection Improvements**
- **No Assessments State**: Improved empty state messaging with action buttons for creating new assessments in collections
- **Assessment Noun Pluralization**: Smart pluralization helper for customizable assessment terminology across collection interfaces

#### **Account Source Tracking**
- **Source Field Standardization**: New source field for accounts created through intake form with standardized assignment in import process

### User Experience Improvements

- **Accordion Icon Animation**: Enhanced accordion expand/collapse animations across components for smoother interactions
- **Dashboard Configuration Modal**: Drag-and-drop reordering for directors dashboard components with visual improvements
- **Map Legend**: Enhanced color gradient functions for better contrast in score and impact legends
- **Component Styling**: Improved card borders, hover effects, and typography consistency across ecosystem and dashboard interfaces
- **Impact Chart Display**: Enhanced Action Tracker Impact Chart with icon styling and priority display improvements

---

## v2.64

### Core Features & Enhancements

#### **Impact Tracker Feature**
- **Action Item Management**: New Impact Tracker system (formerly Action Tracker) for managing action items, comments, and impact metrics within assessments
- **Item Prioritization**: Priority levels and status tracking for action items with WONTDO status support
- **Impact Metrics**: Track impact metrics and status breakdowns for action items with comment editing capabilities
- **Assessment Closing Integration**: Action tracker checks and validation when closing assessments
- **Assessment Filtering**: Lock assessment filter in Impact Tracker tab with ability to target specific assessment IDs

#### **Web Report Enhancements**
- **Default Report Templates**: Automatic default intake form and web report template generation for published assessments
- **Report Access Controls**: Toggle functionality for web report access with enhanced role-based visibility (showing enabled status for admins and account executives)
- **Response Distribution Control**: Enhanced configuration option to enable/disable response distribution modal visibility in web reports

#### **Assessment Form & Preview Improvements**
- **Assessment Navigation Enhancements**: Improved tab navigation and data fetching on status changes with enhanced tab styling and responsiveness
- **Content Blocks Support**: New support for rendering optional content blocks before and after various report sections
- **Form Styling Updates**: Updated button background colors to use theme palette across intake forms, PDF reports, and web reports lists for consistent visual appearance

#### **Score & Visualization Improvements**
- **Score Animation Effects**: Enhanced score animations with smooth transitions and fixed decimal formatting for better visual feedback
- **Progress Bar Animation**: Animated progress bar with CSS transitions for enhanced assessment score display
- **Question Distribution Modal**: New modal displaying response distribution charts and statistics for question responses
- **Assessment Status Indicators**: Added tooltips with descriptions for assessment status steps in the status bar

#### **Assessment Repair & Data Integrity**
- **YAML Assessment Repair Command**: Enhanced management command to repair corrupted YAML assessments with improved validation for question types, possible answers, and preset name reconstruction
- **Assessment Structure Updates**: Updated assessment structure in default intake form to use camelCase keys for consistency
- **Nested Structure Support**: Improved repair command to handle both nested and flat structures with better field merging

#### **Intake Form Configuration**
- **Definition-Based Filtering**: Enhanced intake form picker modal with ability to filter forms by assessment definition ID
- **Assessment Structure Consistency**: Automatic structure standardization across assessment definitions

### User Experience Improvements

- **Design Refinements**: Numerous usability improvements including button styling, color palette consistency, and visual feedback enhancements
- **Loading State Improvements**: Better loading state handling with Redux integration for improved user feedback during data fetching
- **Assessment Workflow**: Enhanced assessment closing process with integrated action tracker checks and clearer status transitions
- **Navigation Clarity**: Removed back button from first tab of assessment forms for streamlined navigation flow
- **Icon Consistency**: Improved visual consistency with theme-aware color palettes and icon styling

---

## v2.63

### Core Features & Enhancements

#### **Web Report Configuration Enhancements**
- **Response Distribution Modal Control**: New configuration option to enable/disable response distribution modal in web reports, providing more granular control over report presentation and user experience

### User Experience Improvements

- **Assessment Form Navigation**: Removed back button from the first tab of assessment evaluation forms for streamlined navigation and clearer user flow
- **Web Report Display**: Enhanced flexibility in web report customization and display options

---

## v2.62

### Core Features & Enhancements

#### **Email Template Improvements**
- **Email Template Format Conversion**: Enhanced markdown link support in email templates with automatic conversion to HTML format for improved email client compatibility and link reliability
- **Assessment Invitation Link Fixes**: Fixed origin sanitization in invitation links to properly handle various protocol variations and improved assessment invite endpoint routing for reliable invitation delivery

### User Experience Improvements

- **Email Delivery**: Improved email template rendering across different email clients with better link handling
- **Assessment Invitations**: More reliable assessment invitation links and delivery mechanisms

---

## v2.61

### Core Features & Enhancements

#### **Assessment Status Visualization**
- **Assessment Status Timeline**: New visual progress bar showing assessment lifecycle (Draft → In Progress → Results Review → Closed) with animated status indicators and real-time status tracking

#### **Email Tracking & Automation**
- **Email Tracking Implementation**: New email tracking system to monitor assessment invitations and reminder emails
- **Reminder Automation**: Automated reminder delivery system with configurable days before assessment close
- **Email Preview Functionality**: Preview assessment and reminder emails before they are sent to recipients

#### **Assessment Recipient Management**
- **Flexible Recipient Name Handling**: Improved recipient creation and name management with support for optional names and flexible update options
- **Contact Search Functionality**: New contact search view for quickly finding and managing contacts by account

#### **Assessment Content & Reporting**
- **Report Data Builder Bug Fix**: Fixed custom scoring threshold labels that were not being properly rendered in reports; now correctly displays category-level thresholds
- **Getting Started Assessment Seed Update**: Updated the database seed content with detailed descriptions and comprehensive scoring sections; removed assessment-level suggestions and consolidated to category-level only for clearer guidance to new users
- **Assessment Close Reminders**: Configure reminder frequency and days before assessment closure

#### **Assessment Form Improvements**
- **Responsive Assessment Forms**: Improved layout and responsiveness in Create and Edit Assessment forms for better usability across devices

#### **Email Template Improvements**
- **Fixed Expiry Date Variable**: Properly uses assessment end date in email templates instead of incorrect variable reference
- **Graceful Recipient Name Handling**: Email templates now handle missing recipient names by returning an empty string instead of breaking the template

---

## v2.60

### Core Features & Enhancements

#### **Client Portal & Self-Service Assessment Management**
- **Client-Only Assessments**: New ability to create assessments visible exclusively to client portal users for self-service completion
- **Client Assessment Delivery**: Streamlined interface for clients to access and complete assigned assessments directly in the portal
- **Draft Status Support**: Clients can now save assessments as drafts and resume work later
- **Read-Only Assessment Mode**: View-only access for clients to review completed assessments without modification
- **Improved Contact Card UI**: Enhanced contact management interface with portal access indicators and clear styling

#### **Assessment Import & Export**
- **Assessment Data Export**: Export assessments in CSV or YAML formats for flexible data sharing and integration
- **YAML Import Functionality**: Improved import tools with enhanced tooltips and better UI for importing assessment definitions
- **Streamlined Terminology**: Updated language across the platform (Download → Export, Upload → Import) for consistency

#### **Single Sign-On (SSO) Enhancements**
- **OIDC Integration**: Added support for Higher Logic OIDC SSO authentication flow
- **Improved Authentication Flow**: Smoother user authentication experience with updated SSO integration
- **Automatic User-Contact Linking**: Users are automatically linked to contact records upon account creation and recovery

#### **Assessment Reporting & Insights**
- **PDF Report Templates**: New support for PDF report configurations and template management
- **Web Report Configuration**: Ability to configure and view web-based assessment reports
- **Qualitative Insights Support**: New field for capturing and viewing qualitative insights alongside quantitative assessment data
- **Category Insights Display**: Enhanced assessment analysis with qualitative insights accordion in category analysis notes
- **Report Visibility Controls**: Options to manage PDF and web report access for different user roles

#### **Enhanced Sidebar Navigation**
- **Assessment Creation & Delivery Navigation**: Updated sidebar with clearer navigation paths for creating and delivering assessments
- **Improved Tab Layout & Styling**: Better organization of assessment preview and detail tabs for improved usability
- **Breadcrumb Navigation**: Integrated breadcrumb store for consistent navigation across assessment workflows and account management

#### **Account Executive Features**
- **Account Details Reports Tab**: New dedicated tab for viewing and managing assessment reports in account details
- **Enhanced Route Access**: Extended account executive access to YAML assessments for better assessment management
- **Account Contact Management**: Improved ability to manage contacts with cleaner UI and better visibility controls

#### **Password & Security Management**
- **Password Reset Functionality**: Users can now reset their passwords with validation rules and clear feedback
- **Enhanced Contact Updates**: Improved contact information management tied to account changes

#### **User Interface Improvements**
- **Dynamic Header Styling**: Header bars now properly render with configured colors and fallback to white if not specified
- **Improved Account Details**: Refined Overview component with enhanced contact cards and web reports selector
- **Tab Subtitle Updates**: Clearer, more descriptive subtitles for better navigation understanding
- **Assessment Card Enhancements**: Improved tooltips for private assessments and cleaner card layouts
- **Section Expansion Logic**: Smarter section expansion in assessment reports (active and parent sections)
- **Animated Page Sections**: Smoother animations and timing adjustments in dashboard cover sections

#### **Assessment Definition Management**
- **Deprecation Controls**: Ability to deprecate and undeprecate YAML assessments with visibility toggles
- **Assessment Version Tracking**: Automatic version incrementing with updated timestamps on assessment modifications
- **Field Enhancements**: Updated field detection for state change management in YAML assessments
- **Flexible Validation**: Removed overly strict validation on first name, last name, and email fields for client account creation

#### **Data Quality Improvements**
- **Question Type Handling**: Clarified default behavior for required fields in text questions
- **Assessment Definition Information**: Enhanced assessment definitions with linked YAML categories and metadata
- **Text/Image Field Merging**: Improved YAML field merge functionality for better assessment data continuity

---

### User Experience Enhancements

- **Tooltip Support**: Added helpful tooltips across import and password reset workflows
- **Consistent Terminology**: Platform-wide updates for clearer user language
- **Better Mobile Responsiveness**: Improved grid layouts for IntakeFormList and assessment cards
- **Admin Features**: New admin endpoints for accessing web reports and county data
- **Contact Row Updates**: Enhanced contact management with improved styling and accessibility

---

**Last Updated**: June 2026  
**Purpose**: Internal guide for updating external user-facing documentation  
**Scope**: Features and user-visible improvements only

---

## v2.59

### Core Features & Enhancements

#### **User Self-Service Profile Management**
- **User Profile Page**: New self-service profile page allowing users to view and manage their account information
- **Password Change Functionality**: Users can now change their own passwords directly from their profile
- **Staff Access Controls**: Profile links intelligently hidden for staff and superuser accounts

#### **Branding & Customization Enhancements**
- **Header Bar Color Configuration**: New ability to customize header bar colors in branding settings
- **Breadcrumb Theme Customization**: Control breadcrumb styling and appearance through branding settings
- **Logo Preview**: Enhanced branding settings UI with improved logo preview and color handling
- **Server-Side Cache Invalidation**: Branding changes now properly refresh cached data for immediate effect

#### **Published Assessment Improvements**
- **Assessment Text Updates**: Ability to update text directly in published assessments without full re-publication
- **Text/Image Merge Functionality**: Improved merging of text and image fields into existing published assessments
- **Sync Comparison Tool**: Enhanced reconciliation and comparison of assessment versions with sync functionality
- **YAML/Library Terminology**: Updated internal terminology for clearer user understanding

#### **Question Type Enhancements**
- **Likert Confidence Preset**: New confidence-based Likert scale preset questions for assessments
- **Preset Question Options**: Multiple preset question types now available for quick assessment creation
- **Confidence Ranking**: Enhanced Likert question types with confidence scales

#### **Assessment Editor Improvements**
- **Form Value Synchronization**: Better synchronization between form inputs and account selections
- **HTML Import Support**: Enhanced HTML import plugin to correctly insert content at cursor position
- **Long Question Text Support**: Improved editor support for assessments with lengthy question text
- **Deprecated Assessment Status Filter**: New filter to view deprecated assessments in the library

#### **Media & Content Management**
- **Media Library Access**: New MediaManagerModal for enhanced media library management in published assessments
- **Icon Style Options**: Default icon style selection now available in icon picker
- **Form Configuration**: Added formId support for improved form tracking in intake form submissions

#### **Demo Seeding & Test Data**
- **Updated Demo Accounts**: Enhanced demo seeding with updated account and contact data
- **Multiple Configuration Support**: Better support for multiple account configurations in demo environments

#### **Issue Resolution & Bug Fixes**
- **Annual Sales Format**: Clarified annual_sales format to numeric for improved data consistency
- **Optional Field Clarification**: Better guidance on optional fields in account YAML instructions
- **Message Clarity**: Updated messaging in published save confirmation modals for clarity
- **Whitespace & Code Quality**: Code improvements for readability

### User Experience Improvements

- **Assessment Editor UX**: Improved editing flow with return navigation parameters
- **Editor Initialization**: Smarter form initialization to prevent overwriting user edits
- **Long Form Handling**: Better support for assessments with long question text
- **Import/Export Refinement**: Updated terminology consistency across import/export flows
- **Modal Improvements**: Enhanced modal layouts and interactions for better UX

---

## v2.58

### Core Features & Enhancements

#### **Account Management**
- **Account Import/Export**: New comprehensive account data import and export functionality supporting CSV and YAML formats
- **Async Account Import**: Asynchronous account import with status polling for handling large batches
- **Clipboard Copy Functionality**: Quick-copy account data to clipboard for easy sharing
- **Enhanced Search**: Expanded account search to include additional fields for better discoverability
- **Duplicate Name Handling**: Support for accounts with duplicate names when previous versions are soft-deleted
- **Account Seeding**: Improved account seeding with pre-fetching for optimized data loading

#### **Assessment Targeting**
- **Target Response Management**: New form-based management of target responses for assessments
- **Account Association**: Improved ability to set accounts for assessments from assessment detail data
- **Child Assessment Filtering**: Better filtering of child assessments in assessment views

#### **Geocoding & Address Data**
- **Geocoding Backfill**: Automatic geocoding backfill triggered after assessment saves
- **Address Normalization**: Enhanced address data normalization for consistency

#### **Assessment Editor Improvements**
- **Import/Export Enhancements**: Increased timeout for large file handling with improved YAML detection
- **Responsive Layout**: Better responsive design in assessment collection and list components
- **Grid Layout Improvements**: Optimized grid layouts in IntakeFormList and related components

#### **Form Management**
- **AssessmentHeader Component**: New shared header component across assessment forms for consistency
- **Intake Form Picker Modal**: Enhanced modal with search functionality for assessment definitions
- **AssessmentDownloadModal**: New modal for flexible data export options (CSV/YAML)
- **Account Import Modal**: Dedicated modal for account import with AI-powered suggestions

#### **Sorting & Filtering**
- **Sorting Functionality**: Added to AccountListTable and ClientList for better data organization
- **Label Updates**: Improved terminology (e.g., "Account Name" vs "Company Name") for clarity

### User Experience Improvements

- **Error Handling**: Improved error handling and logging in form submissions
- **Label Consistency**: Updated labels for clarity and consistency
- **Layout Responsiveness**: Better responsive behavior across components
- **Image Load Error Handling**: Graceful handling of image load failures in tables
- **Border Styling**: Added border radius to buttons for improved visual consistency

---

## v2.57

### Core Features & Enhancements

#### **Help & Support System**
- **Help Drawer Component**: New resizable help drawer providing user assistance and support
- **Help Assistant Chat**: Integrated chat assistant for real-time help functionality
- **Help Button Integration**: New help button across the application for easy access to support
- **Drawer State Management**: Proper state management for open/close and resize behavior

#### **Assessment Scoring Features**
- **Scoring Section Copy**: Ability to copy scoring sections between categories for consistency
- **Copy Dialog Enhancements**: Improved UI and interaction in scoring copy dialog
- **Scoring Method Display**: Enhanced scoring section display with improved precision and formatting
- **Sync Scoring Method**: Fixed sync scoring to make all questions uniform

#### **Assessment Management**
- **Assessment Closed State**: New handling for closed assessment states in form submission
- **Assessment Definition Matching**: Enhanced logic for matching assessment definitions
- **Form Validation**: Improved verification of assessment definitions during submission
- **Current Version Fetching**: API enhanced to fetch current assessment versions

#### **Pagination & Large Data**
- **ClientList Pagination**: Added pagination support for client listings
- **AccountListTable Pagination**: Pagination implemented for account tables with better performance

#### **Assessment Preview**
- **Preview Functionality**: Enhanced assessment preview with close functionality
- **Layout Improvements**: Refactored preview components for improved layout and clarity
- **Category Filtering**: Assessment category filtering now available in preview tabs

#### **Data Organization**
- **Assessment Collection Detail**: Year filter added to assessment collection views
- **N Responses Display**: Showing number of responses in assessments list view
- **Deprecation Notice**: Display of deprecation notices for older assessments

#### **Settings Refinement**
- **Menu Item Refactoring**: Updated settings menu organization with removal of experimental flags
- **Email Template Flags**: Removed experimental gates for email template features
- **Intake Form Flags**: Experimental intake form flags consolidated

### User Experience Improvements

- **Field Display**: Company size input now clearly indicates required field status
- **Error Messages**: Improved error messages and logging for better user feedback
- **Help Access**: Easier access to help and support tools
- **Search Placeholders**: Updated placeholder text for clarity
- **Required Contact Info**: Clearer labeling of required contact information in intake forms

---

## v2.56

### Core Features & Enhancements

#### **Assessment Collections Feature**
- **Assessment Collections**: New ability to group related assessments into collections
- **Collection Management**: Create, organize, and manage assessment collections
- **Collection Detail View**: Comprehensive view of all assessments within a collection
- **Collection Filtering**: Filter assessments within collections by various criteria

#### **PDF & Web Report Enhancements**
- **PDF Report Configuration**: Enhanced PDF report configuration and template management
- **Web Report Optimization**: Improved web report viewing and configuration
- **Report URL Handling**: Optimized PDF URL handling in embedded and full-page views
- **HTML Structure Improvements**: Better HTML structure for proper web report rendering

#### **Scoring Improvements**
- **Score Display Enhancements**: Improved visibility and emphasis in overall score box
- **Score Precision**: Enhanced score formatting with proper rounding for readability
- **Scoring Method Terminology**: Updated "Result Chart Type" to "Scoring Method" for clarity
- **Score Range Guards**: Added validation guards against invalid score ranges
- **Sync Scoring Logic**: Fixed and improved sync scoring behavior

#### **Multiple Select Questions**
- **Multiple Select Answer Display**: New component for displaying multiple select responses
- **Selection Limits**: Enhanced validation and messaging for selection limits
- **Question Preview**: Prevented auto-advancing in preview mode for multiple select questions
- **Scoring Support**: Multiple select questions now fully supported in scoring logic

#### **Assessment Form Enhancements**
- **Legal Agreement Update**: Updated legal agreement page title and layout
- **Category Label Updates**: Changed "All Categories" to "All Groups" for consistency
- **Search Field Placeholder**: Updated search category field placeholder text
- **Responsive Layout**: Better responsive design in assessment form components

#### **UI/UX Polish**
- **Button Styling**: Removed borders from card styles for cleaner look
- **Category Navigation**: Improved category section organization
- **Radio Button Removal**: Streamlined acceptance flow by removing radio button from legal agreement
- **Error Messages**: Improved clarity in scoring behavior warnings

### User Experience Improvements

- **Markdown Support**: Integrated react-markdown for rendering markdown content in assistant chat
- **Question Assistant**: Enhanced question assistant chat with markdown support
- **Assessment Preview**: Better assessment preview experience with improved close functionality
- **Parent Definition Filtering**: Filters now properly exclude parent assessment definitions
- **Color Scheme Updates**: Improved color consistency in substitution modals and UI elements

---

## v2.55

### Core Features & Enhancements

#### **Multiple Select Question Type**
- **New Question Type**: Added multiple select question type with dynamic options
- **Custom Options**: "Other" input support for custom responses in multiple select questions
- **Selection Limits**: Configurable maximum selections with validation
- **Scoring Integration**: Full scoring support for multiple select answers
- **Display Component**: MultipleSelectResponseDisplay component for report rendering

#### **Email Template Enhancements**
- **Template Type Descriptions**: Added usage descriptions for email template types
- **Recipient Name Variable**: Updated descriptions and examples for recipient name variables
- **Template Organization**: Better organization of email templates for different use cases
- **Full Name Field**: Include full name in email templates for personalization

#### **Assessment Reports**
- **Multiple Response Handling**: Enhanced handling of multiple select responses in reports
- **Report Display**: Improved display of different answer types in assessment reports
- **HTML Structure**: Updated HTML structure in default section configs for proper rendering

#### **Data Quality**
- **Score Range Validation**: Added guards against invalid score ranges in editors
- **Question Validation**: Enhanced validation for multiple select questions
- **Max Selections Validation**: Improved validation requiring minimum of 2 selections

### User Experience Improvements

- **PDF Report UX**: Optimized PDF URL handling for better viewing experience
- **Form Layout**: Simplified address fields layout in Additional Information page
- **Assessment Preview**: Refined assessment preview components for improved clarity
- **Search UI**: Fixed initial search text state with improved icon color handling

---

## v2.54

### Core Features & Enhancements

#### **Intake Form V2 System**
- **Complete Rewrite**: New Intake Form V2 system with modular architecture
- **Additional Information Page**: New page for collecting extended company details
- **Multi-Step Form**: Structured multi-page intake forms with improved navigation
- **Form Configuration**: Customizable required fields and auto-requirement based on state
- **Assessment Naming Templates**: Customizable assessment naming with template variables and preview

#### **Intake Form Management**
- **Picker Modal**: New modal for selecting assessments in intake forms with search functionality
- **Paste JSON Modal**: Ability to import assessments by pasting JSON data
- **Form Sharing**: Enhanced sharing with new tab option for easy distribution
- **Category Auto-Population**: Automatic category population in intake forms

#### **Assessment Definitions**
- **QuestionCategoryListView**: New API endpoint for retrieving question categories by definition
- **Metadata & Icons**: Assessment definitions now include icon and icon_color information
- **Definition Tracking**: Assessment definition tracking to prevent re-fetch loops
- **Loading Conditions**: Improved loading state management for dashboard configuration

#### **Default Legal Agreements**
- **Legal Agreement Retrieval**: Default legal agreement text retrieval and integration
- **Legal Agreement Page**: New dedicated legal agreement page with customizable content

#### **Scoring Configuration**
- **Preset Configurations**: Enhanced preset configurations with metadata
- **Dynamic Score Ranges**: Dynamic score ranges for preset question types
- **Default Thresholds**: Automatic default scoring thresholds for 3-section assessments
- **Positional Defaults**: 3-section shorthand with positional defaults

#### **Intake Form Configuration**
- **Version Management**: Version field added to intake form configuration
- **Settings API**: Enhanced IntakeFormSettingsAPIView for single active configuration
- **Show Additional Info**: Field to toggle additional information collection
- **Expiry Date Support**: Expiry date placeholder for email templates and assessments

#### **Validation & Error Handling**
- **Custom Score Range Validation**: Enhanced validation in scoring section feedback editor
- **Error Handling**: Improved error handling in form submission with better messages
- **Modal Updates**: Better error message display in modals

#### **Icon & Image Management**
- **Icon Picker Enhancements**: hideValueText prop for icon picker button customization
- **Image Styling**: Improved image styling in intake forms for better responsiveness
- **Default Icon Styles**: Icon style option selection in icon picker

### User Experience Improvements

- **Address Fields**: Simplified address field layouts
- **Card Styling**: Removed borders from card styles for cleaner interface
- **Sidebar Integration**: Updated sidebar labels and behavior on mobile
- **Grid Layout**: Improved grid layouts in various list components
- **Maximum Width**: Adjusted max width in form components for better readability

---

## v2.53

### Core Features & Enhancements

#### **Ecosystem Map Feature**
- **Interactive Ecosystem Map**: New interactive map visualization showing ecosystem data
- **Account Mapping**: Display geocoded accounts on the map with filtering capabilities
- **Map Filters**: Comprehensive filtering system for ecosystem data
- **Legislator Integration**: Map display of legislative representatives by district
- **Zoom Management**: Smart zoom behavior based on selected accounts and filters
- **URL State Sync**: Map view state (center, zoom) synchronized with URL parameters

#### **Legislator Lookup & Display**
- **Legislator Discovery**: New functionality to find legislative representatives by location
- **Legislator Cards**: Enhanced legislator display cards with images and contact information
- **Legislator Drawer**: Dedicated drawer for detailed legislator information
- **Image Loading**: Loading skeletons for legislator images with proper handling

#### **Geocoding & Address Management**
- **Geocoding Functionality**: Address geocoding with Mapbox API integration
- **Country Code Resolution**: Automatic country code resolution in geocoding process
- **Geocoding Failure Tracking**: Track and identify accounts with geocoding failures
- **Geocoding-Only Filter**: Filter accounts to show only successfully geocoded addresses
- **Not Located Indicator**: Visual indicator for geocoding failures
- **Website Link Formatting**: Improved website link display (domain only)

#### **NAICS Explorer**
- **NAICS Industry Code**: Display NAICS industry codes in establishment details
- **NAICS Hierarchy Search**: Enhanced search for NAICS codes in hierarchy
- **Industry Code Section**: New section label for NAICS industry code in detail views
- **Cross-Reference Search**: Improved cross-reference search functionality
- **Flexible Filtering**: Enhanced account filtering by NAICS codes

#### **Data Visualization**
- **Slider Controls**: Updated EcosystemMapFilters with consistent slider labels
- **Shared Data Sliders**: Improved visibility logic and tooltip messaging
- **Zoom Constants**: Optimized zoom constant values for better map behavior
- **Center State Management**: Simplified map center state management with triggers

### User Experience Improvements

- **Flag Rendering**: Refactored flag rendering to use FlagRow component for consistency
- **Filter Panel**: Filter panel and drawer states now manage based on URL parameters
- **Map Interactions**: Improved map tile rendering and zoom handling
- **Tooltip Messaging**: Better tooltip messaging for shared data sliders
- **Animation Timing**: Updated animation duration for smoother transitions

---

## v2.52

### Core Features & Enhancements

#### **Geocoding System**
- **Address Geocoding**: New geocoding functionality for accounts using Mapbox API
- **Geocoding Service**: Comprehensive address-to-coordinates conversion
- **Address Normalization**: Enhanced address normalization for consistency
- **Location-Based Features**: Foundation for location-based account discovery and mapping

#### **Account Mapping & Discovery**
- **Account Map View**: New view showing all geocoded accounts on a map
- **Account Detail View**: Comprehensive detail view with complete account information
- **Company Logo Display**: Company logos now displayed in account views
- **Account Filtering**: Filter options for ecosystem map and account discovery
- **Filter Options View**: New endpoint returning available filter options and assessment definitions

#### **Assessment Features**
- **Public Preview Endpoint**: New public preview endpoint for YAML assessments
- **Assessment Scoring**: Improved scoring calculation with GAS_GAUGE support
- **Chart Type Scoring**: Updated average score calculation based on chart type

#### **Data Enhancement**
- **Ranking & Scoring**: Enhanced RankingHighestScoringAccountsView with score range computation
- **Assessment Metadata**: More comprehensive assessment definition information in API

#### **Performance**
- **Database Indexes**: Added database indexes to Account and related models for performance
- **Query Optimization**: Improved query efficiency in ecosystem and account views

### User Experience Improvements

- **Logo Display**: Company logos integrated into account information displays
- **Map-Based Discovery**: Location-based account discovery interface
- **Improved Filtering**: Better filtering options for account and ecosystem data
- **Error Messages**: Improved geocoding success and error messages
- **Data Organization**: Better organization of account detail information

---

## v2.51

### Core Features & Enhancements

#### **Supplier Web Reports**
- **Web Report Assignment**: Assign web reports to specific accounts
- **Per-Account Reporting**: Detailed report entries per assessment and configuration
- **Web Report Filters**: Filter assessments by definitions in web report views
- **Report Customization**: Ability to customize and manage web reports per account

#### **NAICS Explorer**
- **NAICS Accounts View**: New view to retrieve accounts by NAICS code
- **Industry Code Display**: Display NAICS industry codes and titles with account information
- **Explorer Navigation**: New endpoints for exploring accounts within industry codes

#### **AI & LLM Enhancements**
- **Async LLM Generation**: Asynchronous LLM generation with Celery task support
- **Status Endpoint**: New status endpoint for tracking LLM generation progress
- **AI Smart Solutions Refinement**: Improved error handling and validation in LLM prompts
- **AI Validation**: Enhanced category validation and error handling in LLM processes
- **Hallucination Mitigation**: Improved AI assistant accuracy and hallucination reduction

#### **Score Calculation**
- **Score Range Validation**: Custom score range validation for preset questions
- **Assessment Version**: Support for different assessment versions in scoring

#### **Logging & Performance**
- **Task Logging**: Configurable task logging to suppress verbose Celery output
- **Django Logging**: Optional Django server request logging for development

### User Experience Improvements

- **Report Access**: Easier access to per-account web reports
- **Industry Navigation**: Better navigation through NAICS industry classifications
- **AI Assistant**: Improved AI help assistant with better accuracy
- **Status Feedback**: Clear status feedback for long-running AI operations

---

## v2.50

### Core Features & Enhancements

#### **Basic Account Management**
- **Account CRUD**: Basic create, read, update operations for accounts
- **Account Settings**: Account configuration and customization
- **Company Information**: Core company details and metadata

#### **Assessment Framework**
- **Assessment Creation**: Basic assessment creation and management
- **Assessment Submission**: Response submission and tracking
- **Response Recording**: Capture and store assessment responses

#### **Email & Notifications**
- **Email Notifications**: Automated email notification system
- **Evaluation Invitations**: Email-based evaluation invitations
- **Password Recovery**: Password reset and recovery via email
- **Email Templates**: Customizable email template system

#### **User Management**
- **User Roles**: Basic role-based access control
- **Recipient Tracking**: Track evaluation recipients and responses
- **Last Evaluation Date**: Record date of most recent evaluation

#### **Branding & Customization**
- **Branding Configuration**: Basic branding and color customization
- **Custom Styling**: Configurable visual styling for accounts

---

**Last Updated**: June 2026  
**Purpose**: Internal guide for updating external user-facing documentation  
**Scope**: Features and user-visible improvements only
