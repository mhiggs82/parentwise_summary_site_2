# ParentWise Stitch Build Loop

This directory contains the Stitch build loop setup for generating the ParentWise Docusaurus library UI.

## 🎯 Project Overview

- **Stitch Project ID:** 1526671829661591026
- **Project Name:** ParentWise Docusaurus Library
- **Purpose:** Generate sophisticated, accessible UI layouts for the documentation site

## 📁 File Structure

```
website/
├── stitch.json           # Stitch project ID (persist this!)
├── SITE.md               # Site vision, sitemap, roadmap
├── DESIGN.md             # Design system for Stitch prompts
├── DESIGN_PLAN.md        # Full design specification
├── next-prompt.md        # Current build task (the baton)
├── queue/                # Staging area for Stitch output
│   ├── {page}.html       # Generated HTML
│   └── {page}.png        # Screenshots
└── README_STITCH.md      # This file
```

## 🚀 Quick Start

### Option 1: Manual Loop Execution

Run the build loop manually by asking the AI agent:

```
Please execute the Stitch build loop using the next-prompt.md file
```

The agent will:
1. Read `next-prompt.md` to get the current task
2. Generate the page using Stitch MCP
3. Save output to `queue/`
4. Update `SITE.md` sitemap
5. Write the next task to `next-prompt.md`

### Option 2: Automated Loop (Future)

Set up GitHub Actions or CI/CD to automatically trigger on `next-prompt.md` changes.

## 📋 Build Queue Status

### Current Task
- **Page:** Homepage
- **Status:** Ready to generate
- **Description:** Hero section with search, category grid, featured books

### Completed Pages
- None yet (first iteration)

### Roadmap
1. Homepage (current)
2. Category page template
3. Book summary template
4. Search results page
5. About page
6. Getting started guide
7. 404 error page

## 🎨 Design System

The design system is documented in `DESIGN.md` and must be included in every Stitch prompt. Key characteristics:

- **Dark Mode Primary:** Navy-black (#0f1116) with purple accents (#7c5bff)
- **Typography:** System fonts, 16px body, 1.75 line height
- **Components:** Rounded corners (12-16px), soft shadows, generous spacing
- **Atmosphere:** Sophisticated, empathetic, calming

## 🔄 Build Loop Workflow

### Step 1: Read the Baton
```bash
cat next-prompt.md
```

### Step 2: Generate with Stitch
The AI agent uses Stitch MCP tools:
- `mcp_stitch_generate_screen_from_text` - Generate the page
- `mcp_stitch_get_screen` - Retrieve HTML and screenshot

### Step 3: Review Output
```bash
ls -la queue/
open queue/homepage.png  # View screenshot
```

### Step 4: Integrate (Manual)
```bash
# Move to Docusaurus when ready
cp queue/homepage.html src/pages/index.html
```

### Step 5: Continue Loop
The agent automatically updates `next-prompt.md` with the next task.

## 📊 Progress Tracking

Track progress in `SITE.md`:
- **Section 4 (Sitemap):** Check off completed pages
- **Section 5 (Roadmap):** Remove completed tasks
- **Section 6 (Creative Freedom):** Add new ideas

## 🛠️ Troubleshooting

### Stitch Generation Fails
- Verify the design system block is included in the prompt
- Check that `stitch.json` has the correct project ID
- Ensure the prompt is clear and detailed

### Inconsistent Styles
- Make sure `DESIGN.md` is copied correctly into prompts
- Verify color hex codes match the design system
- Check that component specifications are followed

### Loop Stalls
- Ensure `next-prompt.md` has valid YAML frontmatter
- Verify the `page` field is set correctly
- Check that the prompt includes design system section

## 📚 Resources

- **Full Design Plan:** `DESIGN_PLAN.md`
- **Site Vision:** `SITE.md`
- **Design System:** `DESIGN.md`
- **Stitch Loop Skill:** `../Skills/stitch-loop/SKILL.md`

## 🎯 Next Steps

1. **Generate Homepage:** Run the build loop to create the first page
2. **Review Output:** Check `queue/homepage.html` and `queue/homepage.png`
3. **Iterate:** Continue the loop for category pages and book templates
4. **Integrate:** Move generated HTML into Docusaurus structure
5. **Customize:** Adapt generated code to work with React components

---

**Created:** February 5, 2026  
**Last Updated:** February 5, 2026  
**Status:** Ready for first iteration
