#!/usr/bin/env python3
"""Process FOUND-006 through FOUND-016 markdown files to JSON with semantic extraction."""

import json
import re
import os
from pathlib import Path

# Base directories
BOOK_SUMMARIES_DIR = Path("/Users/mhiggs/Documents/GitHub/ParentWise Summary Site 2/Book_Summaries")
JSON_OUTPUT_DIR = Path("/Users/mhiggs/Documents/GitHub/ParentWise Summary Site 2/execution/json_output")
MDX_OUTPUT_DIR = Path("/Users/mhiggs/Documents/GitHub/ParentWise Summary Site 2/execution/mdx_output")
WEBSITE_DOCS_DIR = Path("/Users/mhiggs/Documents/GitHub/ParentWise Summary Site 2/website/docs/foundational")
WEBSITE_DATA_DIR = Path("/Users/mhiggs/Documents/GitHub/ParentWise Summary Site 2/website/static/data/books")

# Ensure output directories exist
JSON_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
MDX_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
WEBSITE_DOCS_DIR.mkdir(parents=True, exist_ok=True)
WEBSITE_DATA_DIR.mkdir(parents=True, exist_ok=True)

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
            metadata[key.strip()] = value.strip().strip('"\'')
    return metadata

def extract_analysis_topics(content):
    """Extract analysis topics from Section 1."""
    section1_match = re.search(r'# Section 1: Analysis & Insights\n(.*?)(?=\n# Section 2:|$)', content, re.DOTALL)
    if not section1_match:
        return []

    section1 = section1_match.group(1)

    # Find all h3 headers (### ) for main topics
    topics = []
    h3_pattern = r'### (\d+\. [^\n]+)\n\n(.*?)(?=\n### \d+\. |$)'
    matches = re.finditer(h3_pattern, section1, re.DOTALL)

    for match in matches:
        heading = match.group(1).strip()
        content_block = match.group(2).strip()

        # Split into first paragraph (intro) and insight card text
        paragraphs = content_block.split('\n\n')
        intro_text = paragraphs[0] if paragraphs else ""
        insight_text = paragraphs[1] if len(paragraphs) > 1 else intro_text

        topics.append({
            "heading": heading,
            "intro_text": intro_text[:300],  # Limit to first 300 chars
            "insight_card": insight_text[:250]  # Limit to first 250 chars
        })

    return topics

def extract_action_frameworks(content):
    """Extract action frameworks from Section 2."""
    section2_match = re.search(r'# Section 2: Actionable Framework\n(.*?)(?=\n# |$)', content, re.DOTALL)
    if not section2_match:
        return []

    section2 = section2_match.group(1)

    # Find all Process sections (Process 1, Process 2, etc.)
    actions = []
    process_pattern = r'### Process (\d+): ([^\n]+)\n\n\*\*Purpose\*\*: ([^\n]+)\n\n\*\*Steps\*\*:\n(.*?)(?=\n### Process \d+:|$)'
    matches = re.finditer(process_pattern, section2, re.DOTALL)

    for match in matches:
        title = match.group(2).strip()
        context = match.group(3).strip()
        steps_text = match.group(4).strip()

        # Parse steps (numbered list)
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
            # Fallback: just get numbered items
            simple_steps = re.findall(r'\d+\. ([^\n]+)', steps_text)
            steps = [{"label": f"Step {i+1}", "description": s.strip()} for i, s in enumerate(simple_steps)]

        actions.append({
            "title": title,
            "context": context,
            "steps": steps
        })

    return actions

def create_json_structure(filename, metadata, analysis_topics, action_frameworks):
    """Create the JSON structure for the book."""
    # Extract just the filename without path
    file_base = filename.replace('.md', '')

    # Determine read time (estimate based on content length)
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

    # Read the file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract components
    metadata = extract_metadata(content)
    analysis_topics = extract_analysis_topics(content)
    action_frameworks = extract_action_frameworks(content)

    if not metadata or not analysis_topics or not action_frameworks:
        print(f"⚠️  Warning: Could not extract all components from {filename}")
        if not metadata:
            print(f"   Missing metadata")
        if not analysis_topics:
            print(f"   Missing analysis topics (found {len(analysis_topics)})")
        if not action_frameworks:
            print(f"   Missing action frameworks (found {len(action_frameworks)})")

    # Create JSON structure
    json_data = create_json_structure(filename, metadata, analysis_topics, action_frameworks)

    # Save JSON
    json_filename = filename.replace('.md', '.json')
    json_filepath = JSON_OUTPUT_DIR / json_filename
    with open(json_filepath, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)

    print(f"✅ JSON created: {json_filename}")
    print(f"   - {len(analysis_topics)} analysis topics")
    print(f"   - {len(action_frameworks)} action frameworks")

    return True

# Process FOUND-006 through FOUND-016
files_to_process = [
    "FOUND-006 - Peaceful Parent Happy Kids by Laura Markham.md",
    "FOUND-007 - Peaceful Parent Happy Siblings by Laura Markham.md",
    "FOUND-008 - Hold On to Your Kids by Gordon Neufeld and Gabor Mate.md",
    "FOUND-009 - How to Raise Kids Who Aren't Assholes by Melinda Wenner Moyer.md",
    "FOUND-010 - Brain-Body Parenting by Mona Delahooke.md",
    "FOUND-011 - Simplicity Parenting by Kim John Payne and Lisa M. Ross.md",
    "FOUND-012 - The Soul of Discipline by Kim John Payne.md",
    "FOUND-013 - Raising Happiness by Christine Carter.md",
    "FOUND-014 - Raising Human Beings by Ross Greene.md",
    "FOUND-015 - The Explosive Child by Ross Greene.md",
    "FOUND-016 - Playful Parenting by Lawrence Cohen.md",
]

print("=" * 60)
print("PROCESSING FOUND-006 through FOUND-016")
print("=" * 60)

success_count = 0
for filename in files_to_process:
    if process_file(filename):
        success_count += 1
    print()

print("=" * 60)
print(f"✅ Successfully processed {success_count}/{len(files_to_process)} files")
print("=" * 60)
