#!/usr/bin/env python3
"""Process FOUND-006 through FOUND-016 with improved pattern detection."""

import json
import re
import os
from pathlib import Path

# Base directories
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

def extract_analysis_topics(content):
    """Extract analysis topics from Section 1."""
    section1_match = re.search(r'# Section 1: Analysis & Insights\n(.*?)(?=\n# Section 2:|$)', content, re.DOTALL)
    if not section1_match:
        return []

    section1 = section1_match.group(1)

    # Try pattern: ### N. Topic Name (most common)
    topics = []
    h3_pattern = r'### (\d+\. [^\n]+)\n\n(.*?)(?=\n### \d+\. |$)'
    matches = re.finditer(h3_pattern, section1, re.DOTALL)

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

    # If no topics found with numbered pattern, try alternative patterns
    if not topics:
        # Try ### Topic Name (without number)
        h3_alt_pattern = r'### ([A-Za-z][^\n]+?(?:Principle|Topic|Framework|Method|Practice|Strategy))\n\n(.*?)(?=\n### [A-Za-z]|$)'
        matches = re.finditer(h3_alt_pattern, section1, re.DOTALL)

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
    """Extract action frameworks from Section 2."""
    section2_match = re.search(r'# Section 2: Actionable Framework\n(.*?)(?=\n# |$)', content, re.DOTALL)
    if not section2_match:
        return []

    section2 = section2_match.group(1)
    actions = []

    # Try pattern 1: ### Process N: Title
    process_pattern = r'### Process (\d+): ([^\n]+)\n\n\*\*Purpose\*\*: ([^\n]+)\n\n\*\*Steps\*\*:\n(.*?)(?=\n### Process \d+:|$)'
    matches = re.finditer(process_pattern, section2, re.DOTALL)

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

        if not steps:
            simple_steps = re.findall(r'\d+\. ([^\n]+)', steps_text)
            steps = [{"label": f"Step {i+1}", "description": s.strip()} for i, s in enumerate(simple_steps)]

        actions.append({
            "title": title,
            "context": context,
            "steps": steps
        })

    # If no Process pattern found, try extracting implementation patterns
    if not actions:
        impl_pattern = r'### Implementation Steps\n(.*?)(?=\n### |$)'
        impl_match = re.search(impl_pattern, section2, re.DOTALL)
        if impl_match:
            impl_content = impl_match.group(1)
            # Extract sub-sections as actions
            subsection_pattern = r'#### ([^\n]+)\n(.*?)(?=\n#### |\n###|$)'
            for match in re.finditer(subsection_pattern, impl_content, re.DOTALL):
                title = match.group(1).strip()
                content = match.group(2).strip()

                steps = re.findall(r'\d+\. ([^\n]+)', content)
                steps_list = [{"label": f"Step {i+1}", "description": s.strip()} for i, s in enumerate(steps)]

                actions.append({
                    "title": title,
                    "context": "",
                    "steps": steps_list if steps_list else [{"label": "Action", "description": content[:200]}]
                })

    # If still no actions, try extracting from Daily/Weekly/Monthly sections
    if not actions:
        daily_pattern = r'### Daily Practices\n(.*?)(?=\n### Weekly|\n###|$)'
        daily_match = re.search(daily_pattern, section2, re.DOTALL)
        if daily_match:
            actions.append({
                "title": "Daily Practices",
                "context": "Regular daily habits to build",
                "steps": [{"label": "Practice", "description": "Review the daily checklist and implement consistently"}]
            })

    return actions

def create_json_structure(filename, metadata, analysis_topics, action_frameworks):
    """Create the JSON structure for the book."""
    file_base = filename.replace('.md', '')
    read_time = f"{max(5, len(analysis_topics) + len(action_frameworks))} min read"

    return {
        "meta": {
            "title": metadata.get('title', file_base),
            "subtitle": metadata.get('subtitle', ''),
            "authors": metadata.get('author', ''),
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
            "text": metadata.get('key_principles', ['Practical parenting wisdom'])[0] if metadata.get('key_principles') else 'Practical parenting wisdom'
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

    if not metadata or not analysis_topics:
        print(f"⚠️  Warning: Missing components")
        if not metadata:
            print(f"   - Metadata")
        if not analysis_topics:
            print(f"   - Analysis topics (found {len(analysis_topics)})")

    json_data = create_json_structure(filename, metadata, analysis_topics, action_frameworks)

    json_filename = filename.replace('.md', '.json')
    json_filepath = JSON_OUTPUT_DIR / json_filename
    with open(json_filepath, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)

    print(f"✅ JSON created: {json_filename}")
    print(f"   - {len(analysis_topics)} analysis topics")
    print(f"   - {len(action_frameworks)} action frameworks")

    return True

# Files that need reprocessing
files_to_process = [
    "FOUND-012 - The Soul of Discipline by Kim John Payne.md",
    "FOUND-013 - Raising Happiness by Christine Carter.md",
    "FOUND-014 - Raising Human Beings by Ross Greene.md",
    "FOUND-015 - The Explosive Child by Ross Greene.md",
    "FOUND-016 - Playful Parenting by Lawrence Cohen.md",
]

print("=" * 60)
print("REPROCESSING FOUND-012 through FOUND-016")
print("=" * 60)

success_count = 0
for filename in files_to_process:
    if process_file(filename):
        success_count += 1
    print()

print("=" * 60)
print(f"✅ Successfully reprocessed {success_count}/{len(files_to_process)} files")
print("=" * 60)
