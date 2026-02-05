# ParentWise Design Style Guide

## Design Philosophy

**Voice**: Empathetic, focused, expert-backed
**Aesthetic**: Sophisticated dark interface with purposeful use of luminous accents
**Tone**: Professional yet warm, calm and reassuring for parents navigating challenging moments

---

## 1. Foundation

### Color Palette

#### Primary Colors
```css
--primary-purple: #7c5bff;        /* Brand primary, CTAs, active states */
--primary-purple-glow: #7c5bff80; /* Glow/blur effects */
--primary-purple-dark: #5d3fd9;   /* Hover states */
```

#### Background & Surface
```css
--bg-primary: #0f1116;            /* Main background */
--bg-secondary: #1a1d2e;          /* Card backgrounds */
--bg-tertiary: #252836;           /* Elevated surfaces */
```

#### Semantic Colors
```css
--success: #00d9b8;               /* "What Went Well" indicators */
--success-bg: #00d9b814;          /* Success background tint */

--warning: #ff9f43;               /* "Needs Attention" indicators */
--warning-bg: #ff9f4314;          /* Warning background tint */

--info: #6c78ff;                  /* Informational elements */
--insight: #00e5a0;               /* New insights */
```

#### Text Colors
```css
--text-primary: #ffffff;          /* Headlines, primary content */
--text-secondary: #b4b9c8;        /* Body text, descriptions */
--text-tertiary: #6b7280;         /* Subtle text, metadata */
--text-disabled: #4b5563;         /* Disabled states */
```

#### Borders & Dividers
```css
--border-subtle: #2d3142;         /* Card borders */
--border-focus: #7c5bff;          /* Focus rings */
--divider: #1e2130;               /* Section dividers */
```

### Light Mode Color Palette

ParentWise's light mode maintains the calm, sophisticated atmosphere through warm neutrals and softer contrasts - designed for daytime use without sacrificing the empathetic, focused experience.

#### Primary Colors (Light Mode)
```css
--primary-purple-light: #6b4ce6;      /* Slightly deeper for contrast */
--primary-purple-glow-light: #7c5bff30; /* Softer glow for light backgrounds */
--primary-purple-dark-light: #5939c9; /* Hover states */
```

#### Background & Surface (Light Mode)
```css
--bg-primary-light: #faf9f7;          /* Warm off-white main background */
--bg-secondary-light: #ffffff;        /* Pure white for cards */
--bg-tertiary-light: #f5f3f0;         /* Elevated surfaces, subtle warmth */
--bg-accent-light: #f8f5ff;           /* Purple-tinted backgrounds */
```

#### Semantic Colors (Light Mode)
```css
--success-light: #00a896;             /* Deeper teal for readability */
--success-bg-light: #e6f7f5;          /* Soft teal background */

--warning-light: #f27b3d;             /* Deeper orange for contrast */
--warning-bg-light: #fff4ed;          /* Soft peach background */

--info-light: #5563e8;                /* Deeper blue for readability */
--insight-light: #00c48c;             /* Deeper green for insights */
```

#### Text Colors (Light Mode)
```css
--text-primary-light: #1a1d2e;        /* Near-black for headlines */
--text-secondary-light: #4a5568;      /* Warm gray for body text */
--text-tertiary-light: #718096;       /* Lighter gray for metadata */
--text-disabled-light: #a0aec0;       /* Disabled states */
```

#### Borders & Dividers (Light Mode)
```css
--border-subtle-light: #e8e5e0;       /* Warm gray borders */
--border-focus-light: #6b4ce6;        /* Purple focus rings */
--divider-light: #f0ede8;             /* Subtle section dividers */
```

### Theme Comparison Quick Reference

| Element | Dark Mode | Light Mode | Purpose |
|---------|-----------|------------|---------|
| **Primary Background** | `#0f1116` Deep navy-black | `#faf9f7` Warm off-white | Main canvas |
| **Card Background** | `#1a1d2e` Elevated navy | `#ffffff` Pure white | Content containers |
| **Primary Text** | `#ffffff` White | `#1a1d2e` Near-black | Headlines, emphasis |
| **Secondary Text** | `#b4b9c8` Light gray | `#4a5568` Warm gray | Body copy |
| **Brand Purple** | `#7c5bff` Bright purple | `#6b4ce6` Deeper purple | CTAs, accents |
| **Success Color** | `#00d9b8` Bright teal | `#00a896` Deep teal | Positive feedback |
| **Warning Color** | `#ff9f43` Bright orange | `#f27b3d` Deep orange | Needs attention |
| **Shadow Intensity** | High opacity (0.3-0.5) | Low opacity (0.06-0.12) | Depth perception |
| **Glow Effect** | Prominent (`rgba(124, 91, 255, 0.5)`) | Subtle (`rgba(107, 76, 230, 0.15)`) | Brand accent |
| **Border Weight** | Subtle, blends in | More defined | Structure |

**Design Philosophy by Theme:**

**Dark Mode (Night):**
- Deep, immersive backgrounds create sanctuary
- High contrast for eye comfort in low light
- Luminous accents feel warm and inviting
- Shadows create dramatic depth
- Ideal for: Late evening check-ins, bedtime routine discussions, late-night stress moments

**Light Mode (Day):**
- Warm neutrals feel welcoming, not clinical
- Softer contrasts reduce visual fatigue
- Purple accents feel professional yet approachable
- Subtle shadows maintain hierarchy
- Ideal for: Morning routine planning, midday problem-solving, school pickup conversations



### Typography

#### Font Stack
```css
--font-primary: -apple-system, BlinkMacSystemFont, "SF Pro Display", 
                "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--font-mono: "SF Mono", Monaco, "Cascadia Code", "Roboto Mono", 
             Consolas, monospace;
```

#### Type Scale
```css
--text-xs: 0.75rem;    /* 12px - metadata, labels */
--text-sm: 0.875rem;   /* 14px - body small, secondary text */
--text-base: 1rem;     /* 16px - body text */
--text-lg: 1.125rem;   /* 18px - card titles */
--text-xl: 1.25rem;    /* 20px - section headers */
--text-2xl: 1.5rem;    /* 24px - page titles */
--text-3xl: 1.875rem;  /* 30px - hero text */
--text-4xl: 2.25rem;   /* 36px - display text */
```

#### Font Weights
```css
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
```

#### Line Heights
```css
--leading-tight: 1.25;   /* Headlines */
--leading-normal: 1.5;   /* Body text */
--leading-relaxed: 1.75; /* Long-form content */
```

### Spacing System

```css
--space-1: 0.25rem;   /* 4px */
--space-2: 0.5rem;    /* 8px */
--space-3: 0.75rem;   /* 12px */
--space-4: 1rem;      /* 16px */
--space-5: 1.25rem;   /* 20px */
--space-6: 1.5rem;    /* 24px */
--space-8: 2rem;      /* 32px */
--space-10: 2.5rem;   /* 40px */
--space-12: 3rem;     /* 48px */
--space-16: 4rem;     /* 64px */
--space-20: 5rem;     /* 80px */
```

### Border Radius

```css
--radius-sm: 8px;     /* Small elements, chips */
--radius-md: 12px;    /* Buttons, inputs */
--radius-lg: 16px;    /* Cards */
--radius-xl: 24px;    /* Large cards, modals */
--radius-full: 9999px; /* Circular elements, badges */
```

### Shadows & Effects

#### Dark Mode Shadows
```css
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.3);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.4),
             0 2px 4px -1px rgba(0, 0, 0, 0.3);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.5),
             0 4px 6px -2px rgba(0, 0, 0, 0.3);
--shadow-glow: 0 0 40px rgba(124, 91, 255, 0.5),
               0 0 80px rgba(124, 91, 255, 0.3);
```

#### Light Mode Shadows
```css
--shadow-sm-light: 0 1px 2px 0 rgba(0, 0, 0, 0.06);
--shadow-md-light: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
                   0 2px 4px -1px rgba(0, 0, 0, 0.06);
--shadow-lg-light: 0 10px 15px -3px rgba(0, 0, 0, 0.12),
                   0 4px 6px -2px rgba(0, 0, 0, 0.08);
--shadow-glow-light: 0 0 30px rgba(107, 76, 230, 0.15),
                     0 0 60px rgba(107, 76, 230, 0.08);
```

### Transitions

```css
--transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
--transition-base: 250ms cubic-bezier(0.4, 0, 0.2, 1);
--transition-slow: 350ms cubic-bezier(0.4, 0, 0.2, 1);
--transition-bounce: 500ms cubic-bezier(0.68, -0.55, 0.265, 1.55);
```

---

## 2. Components

### Logo Icon

**The Sophia Icon**
- Three-petal leaf design in white
- Contained in circular purple background
- Glow effect for emphasis moments
- Size variants: 40px (small), 80px (medium), 120px (large)

```css
.logo-icon {
  background: var(--primary-purple);
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--shadow-glow);
}

.logo-icon--large {
  width: 120px;
  height: 120px;
}
```

### Buttons

#### Primary Button (CTA)
```css
.button-primary {
  background: var(--primary-purple);
  color: var(--text-primary);
  padding: var(--space-4) var(--space-6);
  border-radius: var(--radius-md);
  font-weight: var(--font-semibold);
  font-size: var(--text-base);
  transition: all var(--transition-base);
  border: none;
  cursor: pointer;
}

.button-primary:hover {
  background: var(--primary-purple-dark);
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}

.button-primary:active {
  transform: translateY(0);
}
```

#### Icon in Button
- Microphone icon for voice features
- Left-aligned with 8px spacing
- 20px icon size

### Cards

#### Standard Card
```css
.card {
  background: var(--bg-secondary);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  border: 1px solid var(--border-subtle);
  transition: all var(--transition-base);
}

.card:hover {
  border-color: var(--primary-purple);
  box-shadow: var(--shadow-md);
}
```

#### Feature Card (Large)
```css
.card-feature {
  background: var(--bg-secondary);
  border-radius: var(--radius-xl);
  padding: var(--space-10);
  text-align: center;
  min-height: 400px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
```

#### Session Card
- Contains session metadata (date, title)
- Divided sections: "What Went Well" and "Needs Attention"
- Color-coded indicators
- Action plan preview with checkboxes

```css
.session-card-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-4);
}

.session-card-positive {
  background: var(--success-bg);
  border-left: 3px solid var(--success);
}

.session-card-warning {
  background: var(--warning-bg);
  border-left: 3px solid var(--warning);
}
```

### Navigation

#### Top Navigation
```css
.nav {
  display: flex;
  gap: var(--space-8);
  padding: var(--space-6) 0;
  border-bottom: 1px solid var(--border-subtle);
}

.nav-item {
  color: var(--text-secondary);
  font-size: var(--text-base);
  font-weight: var(--font-medium);
  padding: var(--space-3) var(--space-4);
  border-bottom: 2px solid transparent;
  transition: all var(--transition-fast);
}

.nav-item--active {
  color: var(--text-primary);
  border-bottom-color: var(--primary-purple);
}

.nav-item:hover {
  color: var(--text-primary);
}
```

### Status Indicators

#### Icon Badges
```css
.status-badge {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-sm);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
}

.status-badge--success {
  background: var(--success-bg);
  color: var(--success);
}

.status-badge--warning {
  background: var(--warning-bg);
  color: var(--warning);
}

.status-badge--info {
  background: rgba(108, 120, 255, 0.1);
  color: var(--info);
}
```

### Form Elements

#### Checkbox
```css
.checkbox {
  width: 20px;
  height: 20px;
  border: 2px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  background: transparent;
  transition: all var(--transition-fast);
}

.checkbox:checked {
  background: var(--primary-purple);
  border-color: var(--primary-purple);
}
```

### Typography Components

#### Page Header
```css
.page-header {
  font-size: var(--text-2xl);
  font-weight: var(--font-bold);
  color: var(--text-primary);
  margin-bottom: var(--space-2);
}
```

#### Section Label
```css
.section-label {
  font-size: var(--text-xs);
  font-weight: var(--font-semibold);
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
```

#### Metadata Text
```css
.metadata {
  font-size: var(--text-sm);
  color: var(--text-tertiary);
  display: flex;
  align-items: center;
  gap: var(--space-2);
}
```

---

## 3. Layout Patterns

### Centered Hero Layout
**Usage**: Onboarding, conversation start screens

```css
.hero-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--space-8);
  text-align: center;
}
```

### Dashboard Grid
**Usage**: Main dashboard view

```css
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: var(--space-6);
  padding: var(--space-6);
}
```

### Two-Column Split
**Usage**: Session details with analysis sections

```css
.split-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-4);
}

@media (max-width: 768px) {
  .split-layout {
    grid-template-columns: 1fr;
  }
}
```

---

## 4. Interaction Patterns

### Hover States
- Subtle elevation (translateY -1px to -2px)
- Border color change to primary purple
- Enhanced shadow
- Transition duration: 250ms

### Focus States
- 2px solid focus ring in primary purple
- 4px offset from element
- High contrast for accessibility

### Loading States
- Pulsing opacity animation on cards
- Spinning indicator for async operations
- Skeleton screens for content placeholders

### Empty States
- Centered icon and text
- Secondary text color
- Encouraging messaging
- Clear call-to-action

---

## 5. Iconography

### Icon System
- **Style**: Rounded line icons
- **Stroke width**: 2px
- **Size variants**: 16px, 20px, 24px, 32px
- **Color**: Inherits from parent or uses semantic colors

### Common Icons
- Microphone (voice input)
- Thumbs up (positive feedback)
- Wrench/Tool (needs attention)
- Lightbulb (insights)
- Clock/History (sessions)
- Arrow right (navigation, "view more")
- Checkbox (tasks, actions)

---

## 6. Animation Guidelines

### Page Transitions
```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-in {
  animation: fadeInUp 500ms ease-out forwards;
}
```

### Staggered Reveals
- First element: 0ms delay
- Subsequent elements: +100ms per element
- Maximum stagger: 400ms

### Micro-interactions
- Button press: scale(0.98) for 150ms
- Hover lift: translateY(-2px)
- Success checkmark: scale bounce from 0 to 1
- Loading pulse: opacity 1 → 0.5 → 1 (2s infinite)

---

## 7. Accessibility

### Contrast Ratios
- Primary text on dark background: 16:1 (AAA)
- Secondary text on dark background: 7:1 (AA)
- Interactive elements: 4.5:1 minimum (AA)

### Focus Management
- Visible focus indicators on all interactive elements
- Logical tab order
- Skip navigation links where appropriate

### ARIA Labels
- All icons require aria-labels
- Status messages use aria-live regions
- Form inputs have associated labels

### Keyboard Navigation
- Enter/Space activates buttons
- Arrow keys navigate lists
- Escape closes modals/overlays

---

## 8. Responsive Breakpoints

```css
--breakpoint-sm: 640px;   /* Mobile landscape */
--breakpoint-md: 768px;   /* Tablet */
--breakpoint-lg: 1024px;  /* Desktop */
--breakpoint-xl: 1280px;  /* Large desktop */
```

### Mobile-First Approach
- Base styles for mobile (320px+)
- Progressive enhancement for larger screens
- Touch-friendly targets (minimum 44x44px)
- Simplified layouts on small screens

---

## 9. Content Guidelines

### Voice & Tone
- **Empathetic**: Acknowledge parent struggles
- **Focused**: Clear, actionable guidance
- **Expert-backed**: Reference research where appropriate
- **Non-judgmental**: Avoid prescriptive language

### Microcopy Examples
- "Tell me about a moment that happened with you and Leo."
- "Your parenting journey continues."
- "What Went Well" / "Needs Attention"
- "Start New Conversation"
- "Full Analysis"

### Empty State Messages
- Friendly and encouraging
- Brief explanation of why it's empty
- Clear next action

---

## 10. Brand Elements

### Tagline
"FOCUSED • EMPATHETIC • EXPERT-BACKED"
- All caps
- Letter-spaced
- Separated by bullet points (•)
- Positioned at bottom of hero screens

### Name Treatment
- "ParentWise" - single word, CamelCase
- "Sophia" - AI assistant name, always personified
- "Leo" - example child name in demos

---

## 11. Do's and Don'ts

### ✅ Do
- Use ample white space for breathing room
- Maintain high contrast for readability in both themes
- Apply glow effects sparingly on brand purple
- Center important CTAs and hero elements
- Group related information in cards
- Use semantic colors consistently across themes
- **Light mode**: Use warm neutrals (cream/beige tints) instead of pure gray
- **Dark mode**: Leverage deep, rich backgrounds for depth
- Ensure smooth transitions when switching themes (300ms)
- Test both themes in different lighting conditions

### ❌ Don't
- Use bright, saturated backgrounds in either theme
- Overcrowd the interface with multiple CTAs
- Mix metaphors in iconography
- Use more than 3 colors in a single component
- Apply glow effects to multiple elements simultaneously
- **Light mode**: Use pure white (#ffffff) as primary background (use #faf9f7)
- **Light mode**: Use pure black (#000000) for text (use #1a1d2e)
- **Dark mode**: Use pure white text everywhere (use #ffffff sparingly)
- Create jarring transitions between themes
- Assume light mode is just "inverted dark mode" - each needs careful consideration

---

## 12. Implementation Notes

### CSS Architecture
Recommend CSS-in-JS or CSS modules with design tokens:

```javascript
// Example with CSS variables
const theme = {
  colors: {
    primary: 'var(--primary-purple)',
    background: {
      primary: 'var(--bg-primary)',
      secondary: 'var(--bg-secondary)',
    },
    // ...
  },
  spacing: (multiplier) => `calc(${multiplier} * var(--space-4))`,
};
```

### Performance Considerations
- Use CSS transforms for animations (GPU-accelerated)
- Lazy load images and heavy components
- Minimize shadow complexity on mobile
- Use will-change sparingly

### Theme Implementation

ParentWise uses a dual-theme system optimized for different usage contexts:

**Dark Mode (Default)**: Primary theme for evening/night use when parents are dealing with stressful situations. The dark interface creates a calm, focused environment that won't strain eyes or disturb sleeping household members.

**Light Mode**: Complementary theme for daytime use, maintaining the same sophisticated, empathetic tone through warm neutrals and softer contrasts. Designed to feel welcoming and professional during busy morning or afternoon parenting moments.

#### Theme Switching Strategy

```css
/* Root level theme variables */
:root[data-theme="dark"] {
  --bg-primary: #0f1116;
  --bg-secondary: #1a1d2e;
  --text-primary: #ffffff;
  --text-secondary: #b4b9c8;
  --primary-purple: #7c5bff;
  --shadow: var(--shadow-md);
  /* ... other dark mode variables */
}

:root[data-theme="light"] {
  --bg-primary: #faf9f7;
  --bg-secondary: #ffffff;
  --text-primary: #1a1d2e;
  --text-secondary: #4a5568;
  --primary-purple: #6b4ce6;
  --shadow: var(--shadow-md-light);
  /* ... other light mode variables */
}

/* Auto theme based on system preference */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme]) {
    /* Apply dark mode variables */
  }
}

@media (prefers-color-scheme: light) {
  :root:not([data-theme]) {
    /* Apply light mode variables */
  }
}
```

#### Theme Toggle Component

Users should be able to manually override system preferences:
- Toggle location: Settings panel or user profile menu
- States: Auto (system), Light, Dark
- Icon: Sun (light), Moon (dark), System (auto)
- Transition: 300ms ease for smooth theme changes

---

## 13. Theme-Specific Component Adaptations

### Buttons in Light Mode

```css
.button-primary[data-theme="light"] {
  background: var(--primary-purple-light);
  color: #ffffff;
  box-shadow: 0 2px 4px rgba(107, 76, 230, 0.2);
}

.button-primary[data-theme="light"]:hover {
  background: var(--primary-purple-dark-light);
  box-shadow: 0 4px 8px rgba(107, 76, 230, 0.25);
}

/* Secondary button in light mode */
.button-secondary[data-theme="light"] {
  background: transparent;
  border: 2px solid var(--border-subtle-light);
  color: var(--text-primary-light);
}

.button-secondary[data-theme="light"]:hover {
  border-color: var(--primary-purple-light);
  color: var(--primary-purple-light);
  background: var(--bg-accent-light);
}
```

### Cards in Light Mode

```css
.card[data-theme="light"] {
  background: var(--bg-secondary-light);
  border: 1px solid var(--border-subtle-light);
  box-shadow: var(--shadow-sm-light);
}

.card[data-theme="light"]:hover {
  border-color: var(--primary-purple-light);
  box-shadow: var(--shadow-md-light);
}

/* Session card sections in light mode */
.session-card-positive[data-theme="light"] {
  background: var(--success-bg-light);
  border-left: 3px solid var(--success-light);
}

.session-card-warning[data-theme="light"] {
  background: var(--warning-bg-light);
  border-left: 3px solid var(--warning-light);
}
```

### Logo Icon in Light Mode

```css
.logo-icon[data-theme="light"] {
  background: linear-gradient(135deg, #6b4ce6 0%, #8b6ff0 100%);
  box-shadow: var(--shadow-glow-light);
}

/* Sophia icon maintains white fill in both themes */
.logo-icon svg {
  fill: #ffffff;
}
```

### Navigation in Light Mode

```css
.nav[data-theme="light"] {
  border-bottom: 1px solid var(--border-subtle-light);
}

.nav-item[data-theme="light"] {
  color: var(--text-secondary-light);
}

.nav-item--active[data-theme="light"] {
  color: var(--text-primary-light);
  border-bottom-color: var(--primary-purple-light);
}
```

### Status Badges in Light Mode

```css
.status-badge--success[data-theme="light"] {
  background: var(--success-bg-light);
  color: var(--success-light);
  border: 1px solid rgba(0, 168, 150, 0.2);
}

.status-badge--warning[data-theme="light"] {
  background: var(--warning-bg-light);
  color: var(--warning-light);
  border: 1px solid rgba(242, 123, 61, 0.2);
}

.status-badge--info[data-theme="light"] {
  background: #f0f2ff;
  color: var(--info-light);
  border: 1px solid rgba(85, 99, 232, 0.2);
}
```

### Typography Contrast Adjustments

In light mode, certain text treatments require adjustment for optimal readability:

```css
/* Subtle text needs more contrast in light mode */
.metadata[data-theme="light"] {
  color: var(--text-tertiary-light);
}

.section-label[data-theme="light"] {
  color: var(--text-secondary-light);
  opacity: 0.8;
}

/* Disabled states */
.button:disabled[data-theme="light"] {
  background: #e8e5e0;
  color: var(--text-disabled-light);
  cursor: not-allowed;
}
```

### Form Elements in Light Mode

```css
.checkbox[data-theme="light"] {
  border: 2px solid var(--border-subtle-light);
  background: var(--bg-secondary-light);
}

.checkbox:checked[data-theme="light"] {
  background: var(--primary-purple-light);
  border-color: var(--primary-purple-light);
}

.checkbox:focus[data-theme="light"] {
  outline: 2px solid var(--border-focus-light);
  outline-offset: 2px;
}
```

### Hero Section in Light Mode

The centered hero maintains its calming presence in light mode:

```css
.hero-layout[data-theme="light"] {
  background: radial-gradient(
    circle at center,
    var(--bg-accent-light) 0%,
    var(--bg-primary-light) 100%
  );
}

/* Tagline treatment */
.hero-tagline[data-theme="light"] {
  color: var(--text-tertiary-light);
  letter-spacing: 0.1em;
}
```

### Accessibility in Light Mode

Ensure contrast ratios meet WCAG standards:

```css
/* Primary text on light backgrounds: 12:1 (AAA) */
--text-primary-light: #1a1d2e;

/* Secondary text on light backgrounds: 7:1 (AA) */
--text-secondary-light: #4a5568;

/* Purple on white backgrounds: 4.8:1 (AA Large) */
--primary-purple-light: #6b4ce6;
```

### Theme Transition Animation

```css
* {
  transition: background-color 300ms ease,
              border-color 300ms ease,
              color 300ms ease;
}

/* Prevent layout shift during theme change */
@media (prefers-reduced-motion: reduce) {
  * {
    transition: none;
  }
}
```

---

## Version History
- v1.1 - Added light mode variant with warm, sophisticated palette for daytime use
- v1.0 - Initial style guide based on onboarding and dashboard screens
