# ParentWise Docusaurus Site - Design Plan

**Project:** ParentWise Actionable Summary Guides  
**Platform:** Docusaurus v3 + React + TypeScript  
**Design System:** ParentWise Design Style Guide v1.1  
**Component Strategy:** shadcn/ui + Custom React Components  
**Created:** February 5, 2026

---

## 1. Executive Summary

This design plan outlines the UI/UX strategy for transforming the ParentWise Docusaurus documentation site into a sophisticated, empathetic, and highly usable resource for parents. The design will leverage the existing ParentWise brand identity while adapting it for a content-focused documentation experience.

### Design Goals
- **Empathetic Experience**: Create a calm, reassuring environment for parents seeking guidance
- **Content Clarity**: Ensure book summaries and actionable frameworks are easily scannable and digestible
- **Professional Polish**: Maintain sophisticated aesthetics that build trust and credibility
- **Accessibility First**: WCAG AAA compliance for text, AA for interactive elements
- **Performance**: Fast page loads, smooth transitions, optimized for mobile

---

## 2. Visual Theme & Atmosphere

### Overall Aesthetic
**Sophisticated Dark Sanctuary with Warm Light Mode Alternative**

The site will embody a dual-theme approach optimized for different usage contexts:

**Dark Mode (Primary)**
- Deep, immersive navy-black backgrounds (`#0f1116`) create a sanctuary-like environment
- Luminous purple accents (`#7c5bff`) provide warmth and brand recognition
- High contrast ensures comfortable reading during evening research sessions
- Subtle glow effects on key interactive elements create inviting focal points

**Light Mode (Complementary)**
- Warm off-white canvas (`#faf9f7`) feels welcoming without clinical sterility
- Deeper purple variant (`#6b4ce6`) maintains brand consistency with better contrast
- Soft shadows and subtle borders create gentle hierarchy
- Ideal for daytime browsing and printing summaries

### Mood Descriptors
- **Focused**: Clear visual hierarchy guides attention to actionable content
- **Empathetic**: Warm color palette and generous spacing reduce cognitive load
- **Expert-backed**: Sophisticated typography and professional polish build credibility
- **Calm**: Muted backgrounds and purposeful use of color create a stress-free environment

---

## 3. Color System & Semantic Roles

### Brand Colors
```css
/* Primary Brand */
--primary-purple: #7c5bff;           /* CTAs, active states, brand moments */
--primary-purple-glow: #7c5bff80;    /* Hover effects, emphasis */
--primary-purple-dark: #5d3fd9;      /* Pressed states */

/* Light Mode Variants */
--primary-purple-light: #6b4ce6;     /* Better contrast on light backgrounds */
--primary-purple-dark-light: #5939c9; /* Light mode pressed states */
```

### Background Hierarchy
```css
/* Dark Mode */
--bg-primary: #0f1116;               /* Page canvas */
--bg-secondary: #1a1d2e;             /* Cards, content containers */
--bg-tertiary: #252836;              /* Elevated surfaces, code blocks */

/* Light Mode */
--bg-primary-light: #faf9f7;         /* Warm off-white canvas */
--bg-secondary-light: #ffffff;       /* Pure white cards */
--bg-tertiary-light: #f5f3f0;        /* Subtle elevation */
--bg-accent-light: #f8f5ff;          /* Purple-tinted highlights */
```

### Semantic Colors
```css
/* Success - "What Went Well" */
--success: #00d9b8;                  /* Dark mode */
--success-light: #00a896;            /* Light mode */
--success-bg: #00d9b814;             /* Tinted backgrounds */

/* Warning - "Needs Attention" */
--warning: #ff9f43;                  /* Dark mode */
--warning-light: #f27b3d;            /* Light mode */
--warning-bg: #ff9f4314;             /* Tinted backgrounds */

/* Info - Insights & Tips */
--info: #6c78ff;                     /* Dark mode */
--info-light: #5563e8;               /* Light mode */
--insight: #00e5a0;                  /* New insights badge */
```

### Text Hierarchy
```css
/* Dark Mode */
--text-primary: #ffffff;             /* Headings, emphasis */
--text-secondary: #b4b9c8;           /* Body text */
--text-tertiary: #6b7280;            /* Metadata, labels */

/* Light Mode */
--text-primary-light: #1a1d2e;       /* Near-black headings */
--text-secondary-light: #4a5568;     /* Warm gray body */
--text-tertiary-light: #718096;      /* Subtle metadata */
```

---

## 4. Typography System

### Font Stack
```css
--font-primary: -apple-system, BlinkMacSystemFont, "SF Pro Display", 
                "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--font-mono: "SF Mono", Monaco, "Cascadia Code", "Roboto Mono", 
             Consolas, monospace;
```

### Type Scale for Documentation
```css
/* Display & Hero */
--text-4xl: 2.25rem;    /* 36px - Page hero titles */
--text-3xl: 1.875rem;   /* 30px - Book titles */
--text-2xl: 1.5rem;     /* 24px - Section headers */

/* Content Hierarchy */
--text-xl: 1.25rem;     /* 20px - H3, card titles */
--text-lg: 1.125rem;    /* 18px - H4, emphasized text */
--text-base: 1rem;      /* 16px - Body text (optimal for reading) */
--text-sm: 0.875rem;    /* 14px - Metadata, labels */
--text-xs: 0.75rem;     /* 12px - Tiny labels, badges */
```

### Reading Optimization
```css
/* Line Heights for Long-form Content */
--leading-tight: 1.25;      /* Headlines only */
--leading-normal: 1.5;      /* Short paragraphs */
--leading-relaxed: 1.75;    /* Long-form summaries (optimal) */

/* Line Length for Readability */
--content-max-width: 65ch;  /* Optimal reading width */
--sidebar-width: 280px;     /* Navigation sidebar */
```

### Font Weights
```css
--font-normal: 400;         /* Body text */
--font-medium: 500;         /* Emphasized text, labels */
--font-semibold: 600;       /* Subheadings, buttons */
--font-bold: 700;           /* Main headings */
```

---

## 5. Component Design System

### 5.1 Navigation Components

#### Top Navigation Bar
```typescript
// Sticky header with glass morphism effect
.navbar {
  background: rgba(15, 17, 22, 0.8);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-subtle);
  height: 64px;
  position: sticky;
  top: 0;
  z-index: 100;
}

.navbar-brand {
  display: flex;
  align-items: center;
  gap: 12px;
  font-weight: 600;
  color: var(--text-primary);
}

.navbar-logo {
  width: 40px;
  height: 40px;
  background: var(--primary-purple);
  border-radius: 50%;
  box-shadow: 0 0 20px rgba(124, 91, 255, 0.4);
}
```

**Features:**
- Glass morphism effect for modern aesthetic
- Sticky positioning for persistent access
- Search bar integration (Docusaurus Algolia)
- Theme toggle (Auto/Light/Dark)
- Mobile hamburger menu

#### Sidebar Navigation
```typescript
.sidebar {
  width: 280px;
  background: var(--bg-secondary);
  border-right: 1px solid var(--border-subtle);
  padding: var(--space-6);
  overflow-y: auto;
}

.sidebar-category {
  margin-bottom: var(--space-6);
}

.sidebar-category-header {
  font-size: var(--text-sm);
  font-weight: var(--font-semibold);
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: var(--space-3);
}

.sidebar-link {
  display: flex;
  align-items: center;
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius-md);
  color: var(--text-secondary);
  transition: all var(--transition-fast);
}

.sidebar-link--active {
  background: var(--primary-purple);
  color: white;
  font-weight: var(--font-medium);
}

.sidebar-link:hover {
  background: var(--bg-tertiary);
  color: var(--text-primary);
  transform: translateX(2px);
}
```

**Category Organization:**
- PARENTING (PRTG)
- COMMUNICATION (COMM)
- SPECIAL EDUCATION (SPEC)
- DISCIPLINE (DISC)
- DEVELOPMENT (DEV)
- EMOTIONAL INTELLIGENCE (EI)

### 5.2 Content Cards

#### Book Summary Card
```typescript
interface BookCardProps {
  title: string;
  author: string;
  category: string;
  targetAudience: string;
  keyInsights: number;
  actionableFrameworks: number;
  slug: string;
}

// Visual Design
.book-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  transition: all var(--transition-base);
  cursor: pointer;
}

.book-card:hover {
  border-color: var(--primary-purple);
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.book-card-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: var(--space-4);
}

.book-card-category {
  display: inline-flex;
  padding: var(--space-2) var(--space-3);
  background: var(--primary-purple-glow);
  color: var(--primary-purple);
  border-radius: var(--radius-sm);
  font-size: var(--text-xs);
  font-weight: var(--font-semibold);
  text-transform: uppercase;
}

.book-card-title {
  font-size: var(--text-xl);
  font-weight: var(--font-bold);
  color: var(--text-primary);
  margin-bottom: var(--space-2);
}

.book-card-author {
  font-size: var(--text-sm);
  color: var(--text-tertiary);
}

.book-card-stats {
  display: flex;
  gap: var(--space-4);
  margin-top: var(--space-4);
  padding-top: var(--space-4);
  border-top: 1px solid var(--border-subtle);
}

.book-card-stat {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-sm);
  color: var(--text-secondary);
}
```

#### Insight Card (Callout)
```typescript
// For highlighting key insights within summaries
.insight-card {
  background: linear-gradient(
    135deg,
    rgba(124, 91, 255, 0.1) 0%,
    rgba(0, 229, 160, 0.1) 100%
  );
  border-left: 3px solid var(--insight);
  border-radius: var(--radius-md);
  padding: var(--space-5);
  margin: var(--space-6) 0;
}

.insight-card-icon {
  width: 24px;
  height: 24px;
  color: var(--insight);
  margin-bottom: var(--space-3);
}

.insight-card-title {
  font-size: var(--text-lg);
  font-weight: var(--font-semibold);
  color: var(--text-primary);
  margin-bottom: var(--space-3);
}
```

### 5.3 Interactive Components

#### Action Framework Checklist
```typescript
// For actionable steps within summaries
.action-checklist {
  background: var(--bg-tertiary);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  margin: var(--space-6) 0;
}

.action-item {
  display: flex;
  gap: var(--space-3);
  padding: var(--space-4);
  border-radius: var(--radius-md);
  transition: background var(--transition-fast);
}

.action-item:hover {
  background: var(--bg-secondary);
}

.action-checkbox {
  width: 20px;
  height: 20px;
  border: 2px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  flex-shrink: 0;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.action-checkbox:checked {
  background: var(--success);
  border-color: var(--success);
}
```

#### Search Component
```typescript
// Enhanced Docusaurus search with custom styling
.search-bar {
  background: var(--bg-tertiary);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: var(--space-3) var(--space-4);
  transition: all var(--transition-fast);
}

.search-bar:focus-within {
  border-color: var(--primary-purple);
  box-shadow: 0 0 0 3px var(--primary-purple-glow);
}

.search-results {
  background: var(--bg-secondary);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  margin-top: var(--space-2);
  max-height: 400px;
  overflow-y: auto;
}

.search-result-item {
  padding: var(--space-4);
  border-bottom: 1px solid var(--border-subtle);
  cursor: pointer;
  transition: background var(--transition-fast);
}

.search-result-item:hover {
  background: var(--bg-tertiary);
}
```

### 5.4 shadcn/ui Integration

**Selected Components for Implementation:**

1. **Button** - Primary CTAs, navigation actions
2. **Card** - Book summaries, insight callouts
3. **Badge** - Category tags, status indicators
4. **Tabs** - Switching between "Summary" and "Actionable Framework"
5. **Accordion** - Collapsible sections in long summaries
6. **Tooltip** - Contextual help, term definitions
7. **Dialog** - Quick preview modals for books
8. **Separator** - Visual dividers between sections
9. **Skeleton** - Loading states for content
10. **Toast** - Notifications for saved items, copied text

**Installation Strategy:**
```bash
# Initialize shadcn/ui in the Docusaurus src directory
cd website
npx shadcn@latest init

# Configuration choices:
# - Style: "default" (customized with ParentWise tokens)
# - Base color: "slate" (closest to our navy palette)
# - CSS variables: true
# - Tailwind config: src/css/custom.css
# - Components path: src/components/ui

# Install core components
npx shadcn@latest add button card badge tabs accordion tooltip dialog separator skeleton toast
```

**Customization Approach:**
```typescript
// src/lib/utils.ts - Extend cn() utility
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

// src/components/ui/button.tsx - Customized variants
const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md font-semibold transition-all",
  {
    variants: {
      variant: {
        default: "bg-primary-purple text-white hover:bg-primary-purple-dark shadow-md hover:shadow-lg",
        outline: "border-2 border-border-subtle text-text-secondary hover:bg-bg-tertiary",
        ghost: "hover:bg-bg-tertiary text-text-secondary",
        link: "text-primary-purple underline-offset-4 hover:underline",
      },
      size: {
        default: "h-10 px-6 py-2",
        sm: "h-9 px-4 text-sm",
        lg: "h-12 px-8 text-lg",
        icon: "h-10 w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)
```

---

## 6. Layout Patterns

### 6.1 Homepage Layout
```
┌─────────────────────────────────────────────────┐
│ Navigation Bar (Glass morphism, sticky)         │
├─────────────────────────────────────────────────┤
│                                                 │
│         Hero Section (Centered)                 │
│   ┌───────────────────────────────────┐        │
│   │  Sophia Logo (120px, glowing)     │        │
│   │  "ParentWise Actionable Summary   │        │
│   │   Guides"                          │        │
│   │  Tagline: FOCUSED • EMPATHETIC •  │        │
│   │   EXPERT-BACKED                    │        │
│   │  [Search Bar]                      │        │
│   └───────────────────────────────────┘        │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│   Category Grid (3 columns)                    │
│   ┌──────┐  ┌──────┐  ┌──────┐               │
│   │PRTG  │  │COMM  │  │SPEC  │               │
│   │ 45   │  │ 32   │  │ 28   │               │
│   │books │  │books │  │books │               │
│   └──────┘  └──────┘  └──────┘               │
│                                                 │
├─────────────────────────────────────────────────┤
│   Featured Books (Horizontal scroll)           │
│   [Card] [Card] [Card] [Card] →               │
└─────────────────────────────────────────────────┘
```

### 6.2 Category Page Layout
```
┌─────────────────────────────────────────────────┐
│ Navigation Bar                                  │
├──────────┬──────────────────────────────────────┤
│          │  Category Header                     │
│ Sidebar  │  ┌────────────────────────────┐     │
│          │  │ PARENTING (PRTG)           │     │
│ Filters: │  │ 45 Books                   │     │
│          │  │ [Filter: All | Featured]   │     │
│ □ Ages   │  └────────────────────────────┘     │
│   0-2    │                                      │
│   3-5    │  Book Grid (2 columns)              │
│   6-12   │  ┌──────────┐  ┌──────────┐        │
│          │  │ Book Card│  │ Book Card│        │
│ □ Topics │  │          │  │          │        │
│   Sleep  │  │ Title    │  │ Title    │        │
│   Behav. │  │ Author   │  │ Author   │        │
│          │  │ Stats    │  │ Stats    │        │
│          │  └──────────┘  └──────────┘        │
└──────────┴──────────────────────────────────────┘
```

### 6.3 Book Summary Page Layout
```
┌─────────────────────────────────────────────────┐
│ Navigation Bar                                  │
├──────────┬──────────────────────────────────────┤
│          │  Book Header                         │
│ TOC      │  ┌────────────────────────────┐     │
│ (Auto)   │  │ [Category Badge]           │     │
│          │  │ Book Title                 │     │
│ • Intro  │  │ by Author Name             │     │
│ • Key    │  │ Target: Parents of 3-5yr   │     │
│   Themes │  └────────────────────────────┘     │
│ • Action │                                      │
│   Frame. │  [Tabs: Summary | Framework]        │
│          │                                      │
│          │  Content Area (max-width: 65ch)     │
│          │  ┌────────────────────────────┐     │
│          │  │ ## Analysis & Insights     │     │
│          │  │                            │     │
│          │  │ Paragraph text...          │     │
│          │  │                            │     │
│          │  │ [Insight Card]             │     │
│          │  │ ┌──────────────────┐      │     │
│          │  │ │ 💡 Key Insight   │      │     │
│          │  │ │ Content...       │      │     │
│          │  │ └──────────────────┘      │     │
│          │  │                            │     │
│          │  │ ## Actionable Framework    │     │
│          │  │                            │     │
│          │  │ [Action Checklist]         │     │
│          │  └────────────────────────────┘     │
└──────────┴──────────────────────────────────────┘
```

---

## 7. Interaction Patterns

### 7.1 Hover States
```css
/* Subtle elevation and color shift */
.interactive-element:hover {
  transform: translateY(-2px);
  border-color: var(--primary-purple);
  box-shadow: var(--shadow-md);
  transition: all var(--transition-base);
}
```

### 7.2 Focus States (Accessibility)
```css
/* High-contrast focus rings */
.interactive-element:focus-visible {
  outline: 2px solid var(--primary-purple);
  outline-offset: 4px;
  border-radius: var(--radius-md);
}
```

### 7.3 Loading States
```typescript
// Skeleton screens for content loading
import { Skeleton } from "@/components/ui/skeleton"

function BookCardSkeleton() {
  return (
    <div className="book-card">
      <Skeleton className="h-6 w-20 mb-4" /> {/* Category badge */}
      <Skeleton className="h-8 w-full mb-2" /> {/* Title */}
      <Skeleton className="h-4 w-32 mb-4" /> {/* Author */}
      <Skeleton className="h-px w-full mb-4" /> {/* Divider */}
      <div className="flex gap-4">
        <Skeleton className="h-4 w-24" /> {/* Stat 1 */}
        <Skeleton className="h-4 w-24" /> {/* Stat 2 */}
      </div>
    </div>
  )
}
```

### 7.4 Page Transitions
```css
/* Fade in up animation for page content */
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

.page-content {
  animation: fadeInUp 500ms ease-out forwards;
}

/* Staggered reveals for lists */
.book-card:nth-child(1) { animation-delay: 0ms; }
.book-card:nth-child(2) { animation-delay: 100ms; }
.book-card:nth-child(3) { animation-delay: 200ms; }
.book-card:nth-child(4) { animation-delay: 300ms; }
```

### 7.5 Micro-interactions
```css
/* Button press feedback */
.button:active {
  transform: scale(0.98);
  transition: transform var(--transition-fast);
}

/* Checkbox success animation */
@keyframes checkBounce {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.2); }
}

.checkbox:checked {
  animation: checkBounce 300ms ease-out;
}

/* Toast notification slide-in */
@keyframes slideInRight {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

.toast {
  animation: slideInRight 300ms ease-out;
}
```

---

## 8. Responsive Design Strategy

### 8.1 Breakpoints
```css
/* Mobile-first approach */
--breakpoint-sm: 640px;   /* Mobile landscape */
--breakpoint-md: 768px;   /* Tablet */
--breakpoint-lg: 1024px;  /* Desktop */
--breakpoint-xl: 1280px;  /* Large desktop */
```

### 8.2 Layout Adaptations

**Mobile (< 768px):**
- Single column layout
- Hamburger menu for navigation
- Sidebar becomes bottom sheet
- Book cards stack vertically
- Reduced padding/margins
- Touch-friendly targets (min 44x44px)

**Tablet (768px - 1024px):**
- Two-column book grid
- Collapsible sidebar
- Optimized for both portrait and landscape
- Larger touch targets maintained

**Desktop (> 1024px):**
- Three-column book grid on category pages
- Persistent sidebar navigation
- Hover states fully enabled
- Maximum content width: 1440px

### 8.3 Mobile-Specific Optimizations
```css
/* Simplified shadows on mobile */
@media (max-width: 768px) {
  .card {
    box-shadow: var(--shadow-sm);
  }
  
  .card:hover {
    box-shadow: var(--shadow-sm); /* No elevation change */
  }
}

/* Sticky mobile header */
@media (max-width: 768px) {
  .navbar {
    height: 56px; /* Reduced height */
  }
  
  .navbar-brand {
    font-size: var(--text-base);
  }
}

/* Touch-friendly spacing */
@media (max-width: 768px) {
  .sidebar-link {
    padding: var(--space-4) var(--space-5);
    min-height: 44px;
  }
}
```

---

## 9. Accessibility Implementation

### 9.1 WCAG Compliance Targets

**Text Contrast:**
- Primary text on dark: 16:1 (AAA)
- Secondary text on dark: 7:1 (AA)
- Primary text on light: 12:1 (AAA)
- Interactive elements: 4.5:1 minimum (AA)

**Focus Management:**
```typescript
// Skip navigation link
<a href="#main-content" className="skip-link">
  Skip to main content
</a>

// Keyboard navigation
useEffect(() => {
  const handleKeyDown = (e: KeyboardEvent) => {
    // Escape closes modals
    if (e.key === 'Escape') closeModal()
    
    // Arrow keys navigate lists
    if (e.key === 'ArrowDown') focusNextItem()
    if (e.key === 'ArrowUp') focusPreviousItem()
  }
  
  document.addEventListener('keydown', handleKeyDown)
  return () => document.removeEventListener('keydown', handleKeyDown)
}, [])
```

### 9.2 ARIA Implementation
```typescript
// Book card with proper ARIA
<article 
  className="book-card"
  role="article"
  aria-labelledby={`book-title-${id}`}
  aria-describedby={`book-desc-${id}`}
>
  <span 
    className="book-card-category"
    aria-label={`Category: ${category}`}
  >
    {categoryCode}
  </span>
  
  <h3 id={`book-title-${id}`} className="book-card-title">
    {title}
  </h3>
  
  <p id={`book-desc-${id}`} className="book-card-author">
    by {author}
  </p>
  
  <div className="book-card-stats" aria-label="Book statistics">
    <span aria-label={`${insightCount} key insights`}>
      💡 {insightCount}
    </span>
    <span aria-label={`${frameworkCount} actionable frameworks`}>
      ✓ {frameworkCount}
    </span>
  </div>
</article>
```

### 9.3 Screen Reader Optimizations
```typescript
// Live region for search results
<div 
  role="status" 
  aria-live="polite" 
  aria-atomic="true"
  className="sr-only"
>
  {searchResults.length} results found for "{searchQuery}"
</div>

// Icon-only buttons with labels
<button 
  aria-label="Toggle dark mode"
  className="theme-toggle"
>
  <MoonIcon aria-hidden="true" />
</button>
```

---

## 10. Performance Optimization

### 10.1 Image Strategy
```typescript
// Lazy loading for book cover images (if added)
<img 
  src={coverUrl}
  alt={`${title} book cover`}
  loading="lazy"
  decoding="async"
  width={300}
  height={450}
/>

// Use WebP with fallback
<picture>
  <source srcSet={`${coverUrl}.webp`} type="image/webp" />
  <img src={`${coverUrl}.jpg`} alt={title} />
</picture>
```

### 10.2 Code Splitting
```typescript
// Lazy load heavy components
import { lazy, Suspense } from 'react'

const BookPreviewModal = lazy(() => import('@/components/BookPreviewModal'))

function BookCard() {
  return (
    <Suspense fallback={<Skeleton />}>
      {showPreview && <BookPreviewModal />}
    </Suspense>
  )
}
```

### 10.3 CSS Optimization
```css
/* Use CSS transforms for animations (GPU-accelerated) */
.card:hover {
  transform: translateY(-2px); /* ✓ GPU */
  /* Avoid: top: -2px; ✗ CPU */
}

/* Minimize shadow complexity on mobile */
@media (max-width: 768px) {
  .card {
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Simple */
  }
}

/* Use will-change sparingly */
.button:hover {
  will-change: transform;
}

.button:not(:hover) {
  will-change: auto;
}
```

---

## 11. Theme Implementation

### 11.1 CSS Variables Setup
```css
/* src/css/custom.css */
:root {
  /* Dark mode (default) */
  --bg-primary: #0f1116;
  --bg-secondary: #1a1d2e;
  --bg-tertiary: #252836;
  
  --text-primary: #ffffff;
  --text-secondary: #b4b9c8;
  --text-tertiary: #6b7280;
  
  --primary-purple: #7c5bff;
  --primary-purple-dark: #5d3fd9;
  
  --border-subtle: #2d3142;
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.4);
}

[data-theme='light'] {
  /* Light mode overrides */
  --bg-primary: #faf9f7;
  --bg-secondary: #ffffff;
  --bg-tertiary: #f5f3f0;
  
  --text-primary: #1a1d2e;
  --text-secondary: #4a5568;
  --text-tertiary: #718096;
  
  --primary-purple: #6b4ce6;
  --primary-purple-dark: #5939c9;
  
  --border-subtle: #e8e5e0;
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

/* Smooth theme transitions */
* {
  transition: background-color 300ms ease,
              border-color 300ms ease,
              color 300ms ease;
}

/* Respect reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  * {
    transition: none !important;
  }
}
```

### 11.2 Theme Toggle Component
```typescript
// src/components/ThemeToggle.tsx
import { useEffect, useState } from 'react'
import { Moon, Sun, Monitor } from 'lucide-react'
import { Button } from '@/components/ui/button'

type Theme = 'light' | 'dark' | 'auto'

export function ThemeToggle() {
  const [theme, setTheme] = useState<Theme>('auto')
  
  useEffect(() => {
    const savedTheme = localStorage.getItem('theme') as Theme
    if (savedTheme) setTheme(savedTheme)
  }, [])
  
  useEffect(() => {
    const root = document.documentElement
    
    if (theme === 'auto') {
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
      root.setAttribute('data-theme', prefersDark ? 'dark' : 'light')
    } else {
      root.setAttribute('data-theme', theme)
    }
    
    localStorage.setItem('theme', theme)
  }, [theme])
  
  const cycleTheme = () => {
    const themes: Theme[] = ['auto', 'light', 'dark']
    const currentIndex = themes.indexOf(theme)
    const nextTheme = themes[(currentIndex + 1) % themes.length]
    setTheme(nextTheme)
  }
  
  const icons = {
    auto: <Monitor className="h-5 w-5" />,
    light: <Sun className="h-5 w-5" />,
    dark: <Moon className="h-5 w-5" />
  }
  
  return (
    <Button
      variant="ghost"
      size="icon"
      onClick={cycleTheme}
      aria-label={`Current theme: ${theme}. Click to cycle.`}
    >
      {icons[theme]}
    </Button>
  )
}
```

---

## 12. Content Strategy

### 12.1 Microcopy Guidelines

**Navigation:**
- "Browse Summaries" (not "Docs" or "Documentation")
- "Search books..." (placeholder text)
- "Filter by category" (not "Categories")

**Empty States:**
- "No books found matching your filters"
- "Try adjusting your search or browse all categories"
- [Clear Filters Button]

**Actions:**
- "Read Full Summary" (not "View" or "Open")
- "View Actionable Framework"
- "Save for Later" (bookmark feature)
- "Share This Summary"

**Metadata:**
- "Target Audience: Parents of 3-5 year olds"
- "Key Insights: 12" (not "12 insights")
- "Actionable Steps: 8"

### 12.2 Voice & Tone Examples

**Empathetic:**
- "We know parenting is hard. These summaries distill expert advice into actionable steps you can use today."

**Focused:**
- "Each summary includes: Analysis & Insights, Actionable Framework, and Real-World Applications"

**Expert-backed:**
- "All summaries are based on research-backed parenting books by leading experts in child development."

**Non-judgmental:**
- "Every family is different. Use what works for you and your child."

---

## 13. Implementation Roadmap

### Phase 1: Foundation (Week 1-2)
- [ ] Set up Docusaurus theme customization
- [ ] Implement CSS variable system
- [ ] Create base layout components (Navbar, Sidebar, Footer)
- [ ] Initialize shadcn/ui and install core components
- [ ] Implement theme toggle functionality

### Phase 2: Component Library (Week 3-4)
- [ ] Build BookCard component with all variants
- [ ] Create InsightCard callout component
- [ ] Implement ActionChecklist component
- [ ] Build search result components
- [ ] Create loading skeletons for all components

### Phase 3: Page Templates (Week 5-6)
- [ ] Homepage with hero and category grid
- [ ] Category page with filtering
- [ ] Book summary page with TOC
- [ ] 404 page with helpful navigation
- [ ] Search results page

### Phase 4: Interactions & Polish (Week 7-8)
- [ ] Implement all hover states and transitions
- [ ] Add micro-interactions (button press, checkbox bounce)
- [ ] Optimize page transitions
- [ ] Add toast notifications for user actions
- [ ] Implement bookmark/save functionality

### Phase 5: Accessibility & Testing (Week 9-10)
- [ ] Keyboard navigation testing
- [ ] Screen reader testing (NVDA, JAWS, VoiceOver)
- [ ] Color contrast verification
- [ ] Focus management audit
- [ ] ARIA attribute validation

### Phase 6: Performance & Launch (Week 11-12)
- [ ] Image optimization
- [ ] Code splitting implementation
- [ ] Lighthouse audit (target: 90+ on all metrics)
- [ ] Cross-browser testing
- [ ] Mobile device testing
- [ ] Production deployment

---

## 14. Success Metrics

### User Experience Metrics
- **Time to First Meaningful Paint**: < 1.5s
- **First Input Delay**: < 100ms
- **Cumulative Layout Shift**: < 0.1
- **Lighthouse Performance Score**: 90+
- **Lighthouse Accessibility Score**: 100

### Engagement Metrics
- **Average Session Duration**: Track improvement
- **Pages per Session**: Target 3+
- **Search Usage**: % of users using search
- **Bookmark Rate**: % of summaries saved
- **Mobile vs Desktop**: Monitor usage patterns

### Accessibility Metrics
- **Keyboard Navigation Success**: 100% of features accessible
- **Screen Reader Compatibility**: Tested with 3+ screen readers
- **Color Contrast**: 100% WCAG AA compliance (AAA for text)
- **Focus Indicators**: Visible on all interactive elements

---

## 15. Design Tokens Reference

### Quick Reference Table

| Token | Dark Mode | Light Mode | Usage |
|-------|-----------|------------|-------|
| **Primary BG** | `#0f1116` | `#faf9f7` | Page canvas |
| **Card BG** | `#1a1d2e` | `#ffffff` | Content containers |
| **Primary Text** | `#ffffff` | `#1a1d2e` | Headlines |
| **Body Text** | `#b4b9c8` | `#4a5568` | Paragraphs |
| **Brand Purple** | `#7c5bff` | `#6b4ce6` | CTAs, links |
| **Success** | `#00d9b8` | `#00a896` | Positive feedback |
| **Warning** | `#ff9f43` | `#f27b3d` | Attention needed |
| **Border** | `#2d3142` | `#e8e5e0` | Dividers, outlines |

---

## 16. Maintenance & Evolution

### Design System Updates
- **Quarterly Review**: Assess component usage and identify gaps
- **User Feedback**: Collect feedback on usability and aesthetics
- **A/B Testing**: Test variations of key components (CTAs, cards)
- **Accessibility Audits**: Annual comprehensive accessibility review

### Documentation
- **Component Storybook**: Create visual component documentation
- **Design Tokens**: Maintain up-to-date token reference
- **Usage Guidelines**: Document when to use each component
- **Code Examples**: Provide copy-paste examples for developers

---

## Appendix A: File Structure

```
website/
├── src/
│   ├── components/
│   │   ├── ui/                    # shadcn/ui components
│   │   │   ├── button.tsx
│   │   │   ├── card.tsx
│   │   │   ├── badge.tsx
│   │   │   ├── tabs.tsx
│   │   │   ├── accordion.tsx
│   │   │   └── ...
│   │   ├── BookCard.tsx           # Custom components
│   │   ├── InsightCard.tsx
│   │   ├── ActionChecklist.tsx
│   │   ├── ThemeToggle.tsx
│   │   └── CategoryGrid.tsx
│   ├── css/
│   │   ├── custom.css             # Theme variables
│   │   └── components.css         # Component styles
│   ├── lib/
│   │   └── utils.ts               # cn() utility
│   └── pages/
│       ├── index.tsx              # Homepage
│       └── ...
├── docs/                          # Book summaries (Markdown)
├── static/
│   ├── img/
│   │   └── sophia-logo.svg
│   └── fonts/
└── docusaurus.config.js
```

---

## Appendix B: Resources

### Design References
- ParentWise Design Style Guide v1.1
- shadcn/ui Documentation: https://ui.shadcn.com
- Docusaurus Theming: https://docusaurus.io/docs/styling-layout
- Radix UI Primitives: https://www.radix-ui.com

### Accessibility Resources
- WCAG 2.1 Guidelines: https://www.w3.org/WAI/WCAG21/quickref/
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- A11y Project Checklist: https://www.a11yproject.com/checklist/

### Performance Tools
- Lighthouse CI
- WebPageTest
- Chrome DevTools Performance Panel

---

**Document Version:** 1.0  
**Last Updated:** February 5, 2026  
**Next Review:** March 5, 2026
