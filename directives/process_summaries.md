# Summary Processing Directive

## Overview
This directive governs the standardization and processing of parenting book summaries. The goal is to ensure high-quality, structured Markdown files with YAML frontmatter, analysis, and actionable frameworks.

## Workflow

### 1. File Selection
- Select the next book from the `Book_Summaries/` directory based on alphabetical order or specific category codes (e.g., FOUND, SPEC, TEEN).

### 2. Standardization Format
Each processed file must contain:
- **YAML Frontmatter**: Title, Author, Category Code, Tags, Key Principles, and `agentic_search_ready: true`.
- **Section 1: Analysis & Insights**: Executive Summary, Chapter Breakdown, and Nuanced Main Topics.
- **Section 2: Actionable Framework**: Daily Practices, Connection Building, Boundary Setting, and Implementation Processes.

### 3. Execution
- Use `execution/standardize_summary.py` (when created) to automate the formatting where possible.
- Manually review for quality and insight density.

## Edge Cases
- **Low Quality Input**: If the source material is sparse, use the LLM to research and augment the summary while maintaining the standard format.
- **Duplicated Titles**: Check `Book_Summaries/` for similar titles and consolidate if necessary.

## Learnings
- Focus on "Good Inside" methodology for FOUND category.
- Ensure "Two Things Are True" framework is highlighted in connection-based summaries.
