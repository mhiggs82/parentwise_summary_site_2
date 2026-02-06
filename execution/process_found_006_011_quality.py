#!/usr/bin/env python3
"""High-quality extraction for FOUND-006 through FOUND-011."""

import json
import re
import yaml
from pathlib import Path

BOOK_SUMMARIES_DIR = Path("/Users/mhiggs/Documents/GitHub/ParentWise Summary Site 2/Book_Summaries")
JSON_OUTPUT_DIR = Path("/Users/mhiggs/Documents/GitHub/ParentWise Summary Site 2/execution/json_output")

def extract_metadata(content):
    """Extract YAML frontmatter."""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1))
    except:
        return {}

def extract_analysis_topics(content):
    """Extract the 5 main topics from Nuanced Main Topics section."""
    # Find the Nuanced Main Topics section
    match = re.search(r'## Nuanced Main Topics\n(.*?)(?=\n---|\n# Section 2:|$)', content, re.DOTALL)
    if not match:
        return []

    section = match.group(1)
    topics = []

    # Extract ### N. Topic Name sections
    pattern = r'### (\d+\. [^\n]+)\n\n(.*?)(?=\n### \d+\. |$)'

    for match in re.finditer(pattern, section, re.DOTALL):
        heading = match.group(1).strip()
        content_block = match.group(2).strip()

        # First paragraph is the intro
        paragraphs = content_block.split('\n\n')
        intro_text = paragraphs[0] if paragraphs else ""

        # Find the next paragraph for insight_card
        insight_text = ""
        for para in paragraphs[1:]:
            if para.strip() and not para.startswith('**'):
                insight_text = para
                break
        if not insight_text:
            insight_text = intro_text

        topics.append({
            "heading": heading,
            "intro_text": intro_text[:400],  # Slightly longer for quality
            "insight_card": insight_text[:300]
        })

    return topics

def extract_action_frameworks(content):
    """Extract Process 1-5 from Implementation Steps section."""
    # Find Section 2: Actionable Framework
    match = re.search(r'# Section 2: Actionable Framework\n(.*?)(?=\n# |$)', content, re.DOTALL)
    if not match:
        return []

    section = match.group(1)
    actions = []

    # Extract ### Process N: Title sections
    pattern = r'### Process (\d+): ([^\n]+)\n\n\*\*Purpose\*\*: ([^\n]+)\n\n\*\*Steps\*\*:\n(.*?)(?=\n### Process \d+:|$)'

    for match in re.finditer(pattern, section, re.DOTALL):
        title = match.group(2).strip()
        context = match.group(3).strip()
        steps_text = match.group(4).strip()

        # Extract numbered steps with ** ** formatting
        steps = []
        step_pattern = r'\d+\. \*\*([^*]+)\*\* ([^\n]+(?:\n(?!\d+\. \*\*).*)*)'

        for step_match in re.finditer(step_pattern, steps_text):
            label = step_match.group(1).strip()
            description = step_match.group(2).strip().replace('\n', ' ')
            steps.append({
                "label": label,
                "description": description[:200]
            })

        if steps:
            actions.append({
                "title": title,
                "context": context,
                "steps": steps
            })

    return actions

def create_json(filename, metadata, analysis_topics, action_frameworks):
    """Create properly structured JSON."""
    # Ensure arrays
    tags = metadata.get('tags', [])
    if not isinstance(tags, list):
        tags = [tags] if tags else []

    author = metadata.get('author', '')
    authors = [author] if author else []

    key_principles = metadata.get('key_principles', [])
    if not isinstance(key_principles, list):
        key_principles = [key_principles] if key_principles else []

    return {
        "meta": {
            "title": metadata.get('title', ''),
            "subtitle": metadata.get('subtitle', ''),
            "authors": authors,
            "tags": tags,
            "category_code": metadata.get('category_code', 'FOUND')
        },
        "hero": {
            "badge": metadata.get('category_code', 'FOUND'),
            "insights_count": len(analysis_topics),
            "actions_count": len(action_frameworks),
            "read_time": f"{max(6, len(analysis_topics) + len(action_frameworks))} min read"
        },
        "why_matters": {
            "icon": "lightbulb",
            "text": key_principles[0] if key_principles else "Practical parenting wisdom"
        },
        "tabs": {
            "analysis": analysis_topics,
            "actions": action_frameworks
        }
    }

def process_file(filename):
    """Process a single file."""
    filepath = BOOK_SUMMARIES_DIR / filename
    if not filepath.exists():
        return None

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    metadata = extract_metadata(content)
    analysis_topics = extract_analysis_topics(content)
    action_frameworks = extract_action_frameworks(content)

    json_data = create_json(filename, metadata, analysis_topics, action_frameworks)

    json_filepath = JSON_OUTPUT_DIR / filename.replace('.md', '.json')
    with open(json_filepath, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)

    return len(analysis_topics), len(action_frameworks)

# Process FOUND-006 through FOUND-011
files = [
    "FOUND-006 - Peaceful Parent Happy Kids by Laura Markham.md",
    "FOUND-007 - Peaceful Parent Happy Siblings by Laura Markham.md",
    "FOUND-008 - Hold On to Your Kids by Gordon Neufeld and Gabor Mate.md",
    "FOUND-009 - How to Raise Kids Who Aren't Assholes by Melinda Wenner Moyer.md",
    "FOUND-010 - Brain-Body Parenting by Mona Delahooke.md",
    "FOUND-011 - Simplicity Parenting by Kim John Payne and Lisa M. Ross.md",
]

print("=" * 80)
print("QUALITY EXTRACTION: FOUND-006 through FOUND-011")
print("=" * 80)

for filename in files:
    result = process_file(filename)
    if result:
        topics, actions = result
        print(f"✅ {filename}")
        print(f"   Topics: {topics}, Actions: {actions}")
    else:
        print(f"❌ {filename} - Failed")

print("=" * 80)
print("✅ Done - Ready for MDX conversion")
print("=" * 80)
