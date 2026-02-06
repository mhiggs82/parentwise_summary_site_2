# JSON Quality Standard for Parenting Book Summaries

## Overview
This document defines the quality standards for generating JSON book summaries used by the ParentWise platform. All generated JSON files must adhere to these standards to pass Quality Control (QC).

## Structural Standards

### 1. "Why It Matters" (Executive Summary)
- **Model**: Must follow the [Thesis] -> [Unique Contribution] -> [Target Outcome] flow.
- **Length**: Exactly 3 to 4 sentences. No more, no less.

### 2. Analysis & Insights (The Learning Tab)
- **Insight Cards**: The `text` within an insight card must be a standalone nugget of wisdom.
- **Terminology**: Preserve the author's specific terminology and logic.

### 3. Actionable Frameworks (The Doing Tab)
- **Quantity**: Provide a range of **3 to 5** action frameworks per book.
- **Steps per Framework**: Each framework must contain a range of **3 to 7** actionable steps.
- **Bold Titles**: 
  - Use high-energy imperative phrases.
  - NEVER use a single word (e.g., ❌ NO: "PAUSE"; ✅ YES: "PAUSE and breathe").
- **Descriptions**: Must be full, clear descriptive sentences explaining HOW and WHY.
- **Success Checks**: The final step of a process should include a **Success Check** or **Warning** caveat.

### 4. Metadata & Hero
- **Badge**: Must be `[CATEGORY] Core Read`.
- **Hero counts**: `insights_count` and `actions_count` must exactly match the number of items in the tabs.

## Technical Constraints
- **JSON Format**: Return valid JSON only.
- **Escaping**: Ensure backslashes and quotes are properly escaped to prevent MDX build errors.
