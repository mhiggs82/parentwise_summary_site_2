# Design System: ParentWise Docusaurus Library

**Project ID:** 1526671829661591026  
**Based on:** ParentWise Design Style Guide v1.1

---

## 1. Visual Theme & Atmosphere

**Sophisticated Dark Sanctuary with Warm Light Mode Alternative**

The design embodies a dual-theme approach optimized for different usage contexts:

**Dark Mode (Primary):**
- Deep, immersive navy-black backgrounds create a sanctuary-like environment
- Luminous purple accents provide warmth and brand recognition
- High contrast ensures comfortable reading during evening research
- Subtle glow effects on key interactive elements

**Light Mode (Complementary):**
- Warm off-white canvas feels welcoming without clinical sterility
- Deeper purple maintains brand consistency with better contrast
- Soft shadows create gentle hierarchy
- Ideal for daytime browsing

**Mood:** Focused, Empathetic, Expert-backed, Calm

---

## 2. Color Palette & Roles

### Brand Colors
- **Primary Purple** (#7c5bff) - CTAs, active states, brand moments, links
- **Primary Purple Glow** (rgba(124, 91, 255, 0.5)) - Hover effects, emphasis
- **Primary Purple Dark** (#5d3fd9) - Pressed states, darker accents

### Background Hierarchy
- **Primary Background** (#0f1116) - Page canvas, main background
- **Secondary Background** (#1a1d2e) - Cards, content containers, elevated surfaces
- **Tertiary Background** (#252836) - Highest elevation, code blocks, modals

### Semantic Colors
- **Success Teal** (#00d9b8) - "What Went Well" indicators, positive feedback
- **Warning Orange** (#ff9f43) - "Needs Attention" indicators, alerts
- **Info Blue** (#6c78ff) - Informational elements, tips
- **Insight Green** (#00e5a0) - New insights, key takeaways, lightbulb moments

### Text Hierarchy
- **Primary Text** (#ffffff) - Headlines, emphasis, important content
- **Secondary Text** (#b4b9c8) - Body text, descriptions, paragraphs
- **Tertiary Text** (#6b7280) - Metadata, labels, subtle information

### Borders & Dividers
- **Subtle Border** (#2d3142) - Card borders, dividers
- **Focus Border** (#7c5bff) - Focus rings, active states

---

## 3. Typography Rules

### Font Family
System font stack: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif

### Type Scale
- **Display (36px)** - Page hero titles, major headings
- **Heading 1 (30px)** - Book titles, section headers
- **Heading 2 (24px)** - Subsection headers
- **Heading 3 (20px)** - Card titles, minor headers
- **Body (16px)** - Main content, optimal for reading
- **Small (14px)** - Metadata, labels, secondary info
- **Tiny (12px)** - Badges, tiny labels

### Font Weights
- **Normal (400)** - Body text
- **Medium (500)** - Emphasized text, labels
- **Semibold (600)** - Subheadings, buttons
- **Bold (700)** - Main headings

### Line Heights
- **Tight (1.25)** - Headlines only
- **Normal (1.5)** - Short paragraphs
- **Relaxed (1.75)** - Long-form summaries (optimal for reading)

---

## 4. Component Stylings

### Buttons
- **Shape:** Subtly rounded corners (12px border-radius)
- **Primary:** Purple background (#7c5bff), white text, medium shadow
- **Hover:** Darker purple (#5d3fd9), subtle lift (translateY -2px), enhanced shadow
- **Size:** 40px height, 24px horizontal padding
- **Font:** Semibold (600), 16px

### Cards/Containers
- **Background:** Secondary background (#1a1d2e)
- **Corners:** Generously rounded (16px border-radius)
- **Border:** 1px solid subtle border (#2d3142)
- **Shadow:** Medium diffused shadow (0 4px 6px rgba(0,0,0,0.4))
- **Hover:** Purple border, enhanced shadow, subtle lift
- **Padding:** 24px internal spacing

### Navigation
- **Top Bar:** Glass morphism effect (backdrop blur), sticky positioning
- **Sidebar:** 280px width, secondary background, subtle right border
- **Active Link:** Purple background, white text, medium font weight
- **Hover:** Tertiary background, primary text color, slight right shift (2px)

### Badges/Tags
- **Category Badge:** Purple glow background, purple text, uppercase, small size
- **Shape:** Pill-shaped (fully rounded)
- **Padding:** 8px horizontal, 4px vertical
- **Font:** Semibold, 12px, uppercase, letter-spaced

### Insight Cards (Callouts)
- **Background:** Gradient from purple to green tint (very subtle)
- **Left Border:** 3px solid insight green (#00e5a0)
- **Icon:** Lightbulb in insight green, 24px
- **Padding:** 20px
- **Corners:** Moderately rounded (12px)

### Action Checklists
- **Background:** Tertiary background (#252836)
- **Checkbox:** 20px square, subtle border, rounded corners (8px)
- **Checked State:** Success teal background and border
- **Item Hover:** Secondary background

---

## 5. Layout Principles

### Spacing Strategy
- **Generous whitespace** - Ample breathing room between sections
- **Consistent rhythm** - 8px base unit (multiples: 8, 16, 24, 32, 48, 64)
- **Content max-width** - 65 characters for optimal reading
- **Sidebar width** - 280px for navigation

### Grid Alignment
- **Homepage:** 3-column category grid on desktop
- **Category Pages:** 2-column book card grid
- **Book Pages:** Single column with table of contents sidebar
- **Responsive:** Mobile-first, stack columns on small screens

### Elevation Layers
1. **Base** - Page background
2. **Raised** - Cards and containers
3. **Floating** - Modals and dropdowns
4. **Sticky** - Navigation bars

### Depth & Shadows
- **Flat elements** - No shadow (backgrounds, text)
- **Whisper-soft shadows** - Cards at rest (subtle, diffused)
- **Enhanced shadows** - Hover states (more pronounced)
- **Glow effects** - Brand purple elements (luminous, 40-80px blur)

---

## 6. Design System Notes for Stitch Generation

**When generating screens, always include:**

1. **Color Palette:** Use exact hex codes listed above
2. **Typography:** System font stack, specified sizes and weights
3. **Spacing:** 8px base unit, generous whitespace
4. **Components:** Follow button, card, and badge specifications
5. **Atmosphere:** Maintain dark, sophisticated, empathetic feel
6. **Brand Elements:** Include Sophia logo (purple circle with white leaf) where appropriate
7. **Shadows:** Use diffused shadows, avoid harsh drop shadows
8. **Corners:** Generously rounded (12-16px) for major elements
9. **Hover States:** Subtle lift (2px), border color change to purple, enhanced shadow
10. **Accessibility:** High contrast text (white on dark), clear focus indicators

**Key Visual Characteristics:**
- Dark navy-black canvas (#0f1116)
- Luminous purple accents (#7c5bff) with glow effects
- White primary text (#ffffff) with high contrast
- Generous rounded corners (12-16px)
- Soft, diffused shadows
- Ample whitespace and breathing room
- Professional, sophisticated, calming aesthetic

**Component Patterns:**
- Navigation: Glass morphism top bar + sidebar
- Content: Cards with subtle borders and shadows
- CTAs: Purple buttons with hover lift
- Tags: Pill-shaped badges with purple tint
- Insights: Left-bordered cards with gradient backgrounds
- Checklists: Tertiary background with teal checkmarks

---

**Usage:** Copy Section 6 into every Stitch prompt to ensure visual consistency across all generated pages.
