#!/usr/bin/env python3
"""Fix the JSON files for FOUND-006 through FOUND-016 by properly parsing YAML."""

import json
import re
import yaml
from pathlib import Path

BOOK_SUMMARIES_DIR = Path("/Users/mhiggs/Documents/GitHub/ParentWise Summary Site 2/Book_Summaries")
JSON_OUTPUT_DIR = Path("/Users/mhiggs/Documents/GitHub/ParentWise Summary Site 2/execution/json_output")

def extract_metadata_proper(content):
    """Extract YAML frontmatter properly using yaml parser."""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}

    frontmatter = match.group(1)
    try:
        metadata = yaml.safe_load(frontmatter)
        return metadata if metadata else {}
    except:
        return {}

def extract_analysis_topics(content):
    """Extract analysis topics."""
    section1_match = re.search(r'# Section 1: Analysis & Insights\n(.*?)(?=\n# Section 2:|$)', content, re.DOTALL)
    if not section1_match:
        return []

    section1 = section1_match.group(1)
    topics = []

    # Pattern 1: ### N. Topic Name
    h3_pattern = r'### (\d+\. [^\n]+)\n\n(.*?)(?=\n### \d+\. |$)'
    matches = list(re.finditer(h3_pattern, section1, re.DOTALL))

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

    # Pattern 2: #### Topic N: Title
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
    """Extract action frameworks."""
    section2_match = re.search(r'# Section 2: Actionable Framework\n(.*?)(?=\n# |$)', content, re.DOTALL)
    if not section2_match:
        return []

    section2 = section2_match.group(1)
    actions = []

    # Pattern 1: ### Process N: Title
    process_pattern = r'### Process (\d+): ([^\n]+)\n\n\*\*Purpose\*\*: ([^\n]+)\n\n\*\*Steps\*\*:\n(.*?)(?=\n### Process \d+:|$)'
    matches = list(re.finditer(process_pattern, section2, re.DOTALL))

    for match in matches:
        title = match.group(2).strip()
        context = match.group(3).strip()
        steps_text = match.group(4).strip()

        steps = []
        step_pattern = r'\d+\. \*\*([^*]+)\*\* (.+?)(?=\n\d+\. |$)'
        step_matches = re.finditer(step_pattern, steps_text, re.DOTALL)

        for step_match in step_matches:
            step_label = step_match.group(1).strip()
            step_desc = step_match.group(2).strip().replace('\n', ' ')
            steps.append({"label": step_label, "description": step_desc})

        if steps:
            actions.append({"title": title, "context": context, "steps": steps})

    # Pattern 2: #### Step N: Title
    if not actions:
        step_pattern = r'#### (Step \d+: [^\n]+)\n\n(.*?)(?=\n#### Step \d+:|$)'
        matches = list(re.finditer(step_pattern, section2, re.DOTALL))

        for match in matches:
            heading = match.group(1).strip()
            content_block = match.group(2).strip()

            title = heading.replace('Step ', '').split(': ', 1)
            title = title[1] if len(title) > 1 else heading

            steps = []
            item_pattern = r'\d+\. ([^\n]+)'
            items = re.findall(item_pattern, content_block)

            for i, item in enumerate(items):
                steps.append({"label": f"Step {i+1}", "description": item.strip()})

            if steps:
                actions.append({"title": title, "context": "", "steps": steps})

    # Pattern 3: Daily/Weekly/Monthly Practices
    if not actions:
        practice_pattern = r'### ([A-Za-z]+ (?:Practices|Steps))\n(.*?)(?=\n### |$)'
        matches = list(re.finditer(practice_pattern, section2, re.DOTALL))

        for i, match in enumerate(matches[:5]):
            practice_type = match.group(1).strip()
            content_block = match.group(2).strip()

            items = re.findall(r'\- \[ \] ([^\n]+)', content_block)

            if items:
                steps = [{"label": f"Step {j+1}", "description": item.strip()} for j, item in enumerate(items[:5])]
                actions.append({
                    "title": practice_type,
                    "context": f"Implement these {practice_type.lower()}",
                    "steps": steps
                })

    return actions

def create_json_structure(filename, metadata, analysis_topics, action_frameworks):
    """Create the JSON structure."""
    file_base = filename.replace('.md', '')
    read_time = f"{max(5, len(analysis_topics) + len(action_frameworks))} min read"

    # Ensure tags is a list
    tags = metadata.get('tags', [])
    if isinstance(tags, str):
        tags = [tags]
    if not tags:
        tags = []

    # Ensure authors is a list
    author = metadata.get('author', '')
    if isinstance(author, list):
        authors = author
    elif author:
        authors = [author]
    else:
        authors = []

    # Ensure key_principles exists and is a list
    key_principles = metadata.get('key_principles', [])
    if isinstance(key_principles, str):
        key_principles = [key_principles]
    if not key_principles:
        key_principles = ['Practical parenting wisdom']

    return {
        "meta": {
            "title": metadata.get('title', file_base),
            "subtitle": metadata.get('subtitle', ''),
            "authors": authors,  # MUST be an array
            "tags": tags,  # Ensure this is a list
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
            "text": key_principles[0] if key_principles else 'Practical parenting wisdom'
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
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    metadata = extract_metadata_proper(content)
    analysis_topics = extract_analysis_topics(content)
    action_frameworks = extract_action_frameworks(content)

    json_data = create_json_structure(filename, metadata, analysis_topics, action_frameworks)

    json_filename = filename.replace('.md', '.json')
    json_filepath = JSON_OUTPUT_DIR / json_filename
    with open(json_filepath, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)

    return len(analysis_topics), len(action_frameworks)

# Files to fix
files = [
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

print("=" * 70)
print("FIXING JSON FILES FOR FOUND-006 through FOUND-016")
print("=" * 70)

for filename in files:
    result = process_file(filename)
    if result:
        analysis_count, action_count = result
        num = filename.split('-')[0]
        print(f"✅ {filename}: Fixed")

print("=" * 70)
print("✅ All JSON files fixed and regenerated")
print("=" * 70)
