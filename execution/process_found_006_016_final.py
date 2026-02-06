#!/usr/bin/env python3
"""Process FOUND-006 through FOUND-016 with comprehensive pattern matching."""

import json
import re
from pathlib import Path

BOOK_SUMMARIES_DIR = Path("/Users/mhiggs/Documents/GitHub/ParentWise Summary Site 2/Book_Summaries")
JSON_OUTPUT_DIR = Path("/Users/mhiggs/Documents/GitHub/ParentWise Summary Site 2/execution/json_output")
JSON_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def extract_metadata(content):
    """Extract YAML frontmatter."""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}

    frontmatter = match.group(1)
    metadata = {}
    for line in frontmatter.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip().strip('"\'[]')
    return metadata

def extract_executive_summary(content):
    """Extract the Executive Summary section for why_matters."""
    summary_match = re.search(r'## Executive Summary\n\n(.*?)(?=\n## |\n---)', content, re.DOTALL)
    if not summary_match:
        return None

    summary_text = summary_match.group(1).strip()

    # Pattern 1: **Thesis**: format
    thesis_match = re.search(r'\*\*Thesis\*\*:\s*(.+?)(?=\n\n|\*\*)', summary_text, re.DOTALL)
    unique_match = re.search(r'\*\*Unique Contribution\*\*:\s*(.+?)(?=\n\n|\*\*)', summary_text, re.DOTALL)
    target_match = re.search(r'\*\*Target Outcome\*\*:\s*(.+?)(?=\n\n|$)', summary_text, re.DOTALL)

    # Pattern 2: ### Thesis format (for alternate markdown structure)
    if not thesis_match:
        thesis_match = re.search(r'### Thesis\n+(.+?)(?=\n### |\n##|$)', summary_text, re.DOTALL)
    if not unique_match:
        unique_match = re.search(r'### Unique Contribution\n+(.+?)(?=\n### |\n##|$)', summary_text, re.DOTALL)
    if not target_match:
        target_match = re.search(r'### Target Outcome\n+(.+?)(?=\n### |\n##|$)', summary_text, re.DOTALL)

    thesis = thesis_match.group(1).strip() if thesis_match else ""
    unique = unique_match.group(1).strip() if unique_match else ""
    target = target_match.group(1).strip() if target_match else ""

    # Combine into a comprehensive summary (thesis is most important)
    if thesis:
        parts = [thesis]
        if unique:
            parts.append(unique)
        if target:
            parts.append(target)
        return " ".join(parts)

    return None

def extract_analysis_topics(content):
    """Extract analysis topics—handles both ### and #### headers."""
    section1_match = re.search(r'# Section 1: Analysis & Insights\n(.*?)(?=\n# Section 2:|$)', content, re.DOTALL)
    if not section1_match:
        return []

    section1 = section1_match.group(1)
    topics = []

    # Pattern 1: ### N. Topic Name (3 hash marks)
    h3_pattern = r'### (\d+\. [^\n]+)\n\n(.*?)(?=\n### \d+\. |$)'
    matches = list(re.finditer(h3_pattern, section1, re.DOTALL))

    if matches:
        for match in matches:
            heading = match.group(1).strip()
            content_block = match.group(2).strip()
            paragraphs = content_block.split('\n\n')
            intro_text = paragraphs[0] if paragraphs else ""
            insight_text = paragraphs[1] if len(paragraphs) > 1 else intro_text

            topics.append({
                "heading": heading,
                "intro_text": intro_text[:300],
                "insight_card": insight_text[:250]
            })

    # Pattern 2: #### Topic N: Topic Name (4 hash marks)
    if not topics:
        h4_pattern = r'#### (Topic \d+: [^\n]+)\n\n(.*?)(?=\n#### Topic \d+:|$)'
        matches = list(re.finditer(h4_pattern, section1, re.DOTALL))

        for match in matches:
            heading = match.group(1).strip()
            content_block = match.group(2).strip()
            paragraphs = content_block.split('\n\n')
            intro_text = paragraphs[0] if paragraphs else ""
            insight_text = paragraphs[1] if len(paragraphs) > 1 else intro_text

            topics.append({
                "heading": heading,
                "intro_text": intro_text[:300],
                "insight_card": insight_text[:250]
            })

    return topics

def extract_action_frameworks(content):
    """Extract action frameworks with comprehensive pattern matching."""
    section2_match = re.search(r'# Section 2: Actionable Framework\n(.*?)(?=\n# |$)', content, re.DOTALL)
    if not section2_match:
        return []

    section2 = section2_match.group(1)
    actions = []

    # Pattern 1: ### Process N: Title with **Purpose** and **Steps**
    process_pattern = r'### Process (\d+): ([^\n]+)\n\n\*\*Purpose\*\*: ([^\n]+)\n\n\*\*Steps\*\*:\n(.*?)(?=\n### Process \d+:|$)'
    matches = list(re.finditer(process_pattern, section2, re.DOTALL))

    for match in matches:
        title = match.group(2).strip()
        context = match.group(3).strip()
        steps_text = match.group(4).strip()

        # Parse steps (numbered list with ** ** formatting)
        steps = []
        step_pattern = r'\d+\. \*\*([^*]+)\*\* (.+?)(?=\n\d+\. |$)'
        step_matches = re.finditer(step_pattern, steps_text, re.DOTALL)

        for step_match in step_matches:
            step_label = step_match.group(1).strip()
            step_desc = step_match.group(2).strip().replace('\n', ' ')
            steps.append({
                "label": step_label,
                "description": step_desc
            })

        if steps:
            actions.append({
                "title": title,
                "context": context,
                "steps": steps
            })

    # Pattern 2: #### Step N: Title (4 hash marks)
    if not actions:
        step_pattern = r'#### (Step \d+: [^\n]+)\n\n(.*?)(?=\n#### Step \d+:|$)'
        matches = list(re.finditer(step_pattern, section2, re.DOTALL))

        for match in matches:
            heading = match.group(1).strip()
            content_block = match.group(2).strip()

            # Extract title from heading
            title = heading.replace('Step ', '').split(': ', 1)
            title = title[1] if len(title) > 1 else heading

            # Extract numbered steps from content
            steps = []
            item_pattern = r'\d+\. ([^\n]+)'
            items = re.findall(item_pattern, content_block)

            for i, item in enumerate(items):
                steps.append({
                    "label": f"Step {i+1}",
                    "description": item.strip()
                })

            if steps:
                actions.append({
                    "title": title,
                    "context": "",
                    "steps": steps
                })

    # Pattern 3: ### Daily Practices and similar checklist patterns
    if not actions:
        daily_pattern = r'#### (Daily|Weekly|Monthly|Implementation) Practices[^\n]*\n(.*?)(?=\n#### |$)'
        matches = list(re.finditer(daily_pattern, section2, re.DOTALL))

        for match in matches:
            practice_type = match.group(1).strip()
            content_block = match.group(2).strip()

            # Extract checklist items
            items = re.findall(r'\- \[ \] ([^\n]+)', content_block)

            if items:
                actions.append({
                    "title": f"{practice_type} Practices",
                    "context": f"Implement these {practice_type.lower()} practices consistently",
                    "steps": [{"label": f"Practice {i+1}", "description": item.strip()} for i, item in enumerate(items[:5])]
                })

    return actions

def create_json_structure(filename, metadata, analysis_topics, action_frameworks, why_matters_text=None):
    """Create the JSON structure for the book."""
    file_base = filename.replace('.md', '')
    read_time = f"{max(5, len(analysis_topics) + len(action_frameworks))} min read"

    # Ensure authors is always an array
    authors = metadata.get('author', '')
    if isinstance(authors, str):
        authors = [authors] if authors else []
    elif not isinstance(authors, list):
        authors = []

    # Use extracted executive summary if available, otherwise fall back to first principle
    if not why_matters_text:
        key_principles = metadata.get('key_principles', [])
        if isinstance(key_principles, list):
            why_matters_text = key_principles[0] if key_principles else 'Practical parenting wisdom'
        else:
            why_matters_text = key_principles if key_principles else 'Practical parenting wisdom'

    return {
        "meta": {
            "title": metadata.get('title', file_base),
            "subtitle": metadata.get('subtitle', ''),
            "authors": authors,
            "tags": metadata.get('tags', []),
            "category_code": metadata.get('category_code', 'FOUND')
        },
        "hero": {
            "badge": metadata.get('category_code', 'FOUND'),
            "insights_count": len(analysis_topics),
            "actions_count": len(action_frameworks),
            "read_time": read_time
        },
        "why_matters": {
            "icon": "lightbulb",
            "text": why_matters_text
        },
        "tabs": {
            "analysis": analysis_topics,
            "actions": action_frameworks
        }
    }

def process_file(filename):
    """Process a single markdown file."""
    filepath = BOOK_SUMMARIES_DIR / filename

    if not filepath.exists():
        print(f"❌ File not found: {filename}")
        return False

    print(f"📖 Processing: {filename}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    metadata = extract_metadata(content)
    analysis_topics = extract_analysis_topics(content)
    action_frameworks = extract_action_frameworks(content)
    why_matters_text = extract_executive_summary(content)

    if not metadata or not analysis_topics:
        print(f"⚠️  Warning: Missing components")
        if not metadata:
            print(f"   - Metadata")
        if not analysis_topics:
            print(f"   - Analysis topics (found {len(analysis_topics)})")

    json_data = create_json_structure(filename, metadata, analysis_topics, action_frameworks, why_matters_text)

    json_filename = filename.replace('.md', '.json')
    json_filepath = JSON_OUTPUT_DIR / json_filename
    with open(json_filepath, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)

    print(f"✅ JSON created: {json_filename}")
    print(f"   - {len(analysis_topics)} analysis topics")
    print(f"   - {len(action_frameworks)} action frameworks")

    return True

# Files to reprocess
files_to_process = [
    "FOUND-006 - Peaceful Parent Happy Kids by Laura Markham.md",
    "FOUND-007 - Peaceful Parent Happy Siblings by Laura Markham.md",
    "FOUND-008 - Hold On to Your Kids by Gordon Neufeld and Gabor Mate.md",
    "FOUND-009 - How to Raise Kids Who Aren't Assholes by Melinda Wenner Moyer.md",
    "FOUND-010 - Brain-Body Parenting by Mona Delahooke.md"
]

print("=" * 60)
print("REPROCESSING FOUND-006 through FOUND-010 (Quality Fix)")
print("=" * 60)

success_count = 0
for filename in files_to_process:
    if process_file(filename):
        success_count += 1
    print()

print("=" * 60)
print(f"✅ Successfully reprocessed {success_count}/{len(files_to_process)} files")
print("=" * 60)
