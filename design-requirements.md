# Hackathon Registration Website
## Design Requirements Document

---

# 1. Design Vision

The platform should reflect:

- Modern tech aesthetic
- Energetic hackathon vibe
- Clean and professional layout
- Dark-mode first design
- High readability and accessibility
- Smooth micro-interactions

Primary Audience:
- College students (18–25 years)
- Event organizers (admin users)

---

# 2. Design Principles

1. Simplicity First
   - Avoid clutter
   - Clear CTA hierarchy

2. Visual Hierarchy
   - Large bold hero headline
   - Clear section separation
   - Distinct CTA buttons

3. Consistency
   - Reusable components
   - Uniform spacing system
   - Consistent button styles

4. Accessibility
   - Minimum contrast ratio 4.5:1
   - Keyboard navigable
   - Focus states visible
   - Click/tap targets ≥ 44px

---

# 3. Theme & Branding

## 3.1 Color Palette

Primary Background: #0F172A  
Card Background: #1E293B  
Primary Accent: #3B82F6  
Secondary Accent: #8B5CF6  
Success: #10B981  
Error: #EF4444  
Warning: #F59E0B  
Text Primary: #F8FAFC  
Text Secondary: #CBD5E1  

---

## 3.2 Typography

Font Family:
- Poppins or Inter (Google Fonts)

Font Scale:
- Hero Title: 56–64px (Bold)
- Section Headings: 32–36px (Semi-Bold)
- Subheadings: 22–24px
- Body Text: 16–18px
- Small Text: 14px

Line Height:
- Headings: 1.2
- Body: 1.6

---

# 4. Layout System

Grid System:
- 12-column desktop layout
- 8-column tablet layout
- 4-column mobile layout

Max Width:
- 1200px container
- Center aligned

Spacing System:
Use 8px spacing scale:
- 8px
- 16px
- 24px
- 32px
- 48px
- 64px

---

# 5. Component Design Specifications

## 5.1 Buttons

Primary Button:
- Background: #3B82F6
- Text: White
- Padding: 12px 24px
- Border-radius: 8px
- Hover: Slight glow + translateY(-2px)

Secondary Button:
- Border: 1px solid #3B82F6
- Transparent background

Disabled Button:
- Opacity 50%
- Cursor not-allowed

---

## 5.2 Cards

- Background: #1E293B
- Border radius: 12px
- Padding: 24px
- Shadow: Soft drop shadow
- Hover: Slight lift effect

---

## 5.3 Input Fields

- Background: #0F172A
- Border: 1px solid #334155
- Focus:
  - Border: #3B82F6
  - Glow shadow
- Error:
  - Border: #EF4444
  - Error message below field

---

## 5.4 Modals

- Centered
- Backdrop blur
- Smooth fade + scale animation
- Close button (top-right)

---

## 5.5 Toast Notifications

Position:
- Top-right (desktop)
- Bottom (mobile)

Types:
- Success
- Error
- Info

Duration:
- 3–5 seconds

---

# 6. Page-Level UI Requirements

## 6.1 Landing Page

Sections:
- Sticky Navbar
- Hero
- Prizes
- Schedule
- FAQ
- Footer

Hero Requirements:
- Full viewport height
- Gradient animated background
- Countdown timer
- Primary CTA

Schedule:
- Vertical timeline design
- Expandable entries (optional)

FAQ:
- Accordion style
- Smooth open/close animation

---

## 6.2 Authentication UI

- Centered card layout
- Minimal distractions
- Clear error messages
- Loading spinner on submit

---

## 6.3 Dashboard UI

Layout:
- Sidebar (fixed left)
- Main content (right)

Sidebar:
- Icons + labels
- Active state highlight

Dashboard Cards:
- Registration Status badge
- Team Info
- Payment Status

---

## 6.4 Registration Form

- Multi-step layout
- Progress bar at top
- Validation before next step
- Success confirmation screen

---

## 6.5 Admin Panel

- Data table layout
- Search functionality
- Filter dropdown
- Approve/Reject buttons
- Export CSV button

---

# 7. Animations & Micro-interactions

- Button hover glow
- Smooth scroll
- Accordion animation
- Card hover lift
- Animated success checkmark
- Loading spinner
- Countdown live update

---

# 8. Responsive Requirements

Mobile:
- Hamburger navigation
- Single-column layout
- Sticky bottom CTA
- Larger touch targets

Tablet:
- Adjusted grid (8 columns)
- Sidebar collapsible

Desktop:
- 12-column layout
- Fixed sidebar

---

# 9. Performance Requirements

- Page load < 3 seconds
- Optimized images
- Minimal JS blocking
- Lazy loading where applicable

---

# 10. Security (Frontend-Level)

- Sanitize form inputs
- Prevent duplicate team names
- Validate email format
- Validate required fields

---

END OF DESIGN REQUIREMENTS