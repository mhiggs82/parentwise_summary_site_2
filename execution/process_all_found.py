#!/usr/bin/env python3
"""Process all FOUND files with comprehensive pattern matching."""

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

def extract_analysis_topics(content):
    """Extract analysis topics—handles ### and #### headers."""
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
    """Extract action frameworks with multiple pattern matching."""
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

    # Pattern 3: ### Daily/Weekly/Monthly Practices checklist pattern
    if not actions:
        practice_pattern = r'### ([A-Za-z]+ (?:Practices|Steps))\n(.*?)(?=\n### |$)'
        matches = list(re.finditer(practice_pattern, section2, re.DOTALL))

        for i, match in enumerate(matches[:5]):  # Limit to 5 practice groups
            practice_type = match.group(1).strip()
            content_block = match.group(2).strip()

            # Extract checklist items
            items = re.findall(r'\- \[ \] ([^\n]+)', content_block)

            if items:
                # Take first 5 items as representative steps
                steps = [{"label": f"Step {j+1}", "description": item.strip()} for j, item in enumerate(items[:5])]
                actions.append({
                    "title": practice_type,
                    "context": f"Implement these {practice_type.lower()}",
                    "steps": steps
                })

    # Pattern 4: Look for standalone implementation sections with numeric lists
    if not actions:
        impl_pattern = r'### ([^\n]+)\n(.*?)(?=\n### |$)'
        matches = list(re.finditer(impl_pattern, section2, re.DOTALL))

        for match in matches:
            title = match.group(1).strip()
            content_block = match.group(2).strip()

            # Check if this section has numbered items
            items = re.findall(r'\d+\. ([^\n]+)', content_block)

            if items and len(items) >= 3:
                steps = [{"label": f"Step {i+1}", "description": item.strip()} for i, item in enumerate(items[:5])]
                actions.append({
                    "title": title,
                    "context": "",
                    "steps": steps
                })

    return actions

def create_json_structure(filename, metadata, analysis_topics, action_frameworks):
    """Create the JSON structure."""
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
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    metadata = extract_metadata(content)
    analysis_topics = extract_analysis_topics(content)
    action_frameworks = extract_action_frameworks(content)

    json_data = create_json_structure(filename, metadata, analysis_topics, action_frameworks)

    json_filename = filename.replace('.md', '.json')
    json_filepath = JSON_OUTPUT_DIR / json_filename
    with open(json_filepath, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)

    return len(analysis_topics), len(action_frameworks)

# Process all FOUND-006 through FOUND-016
files = [f"FOUND-{i:03d} - {name}.md" for i, name in [
    (6, "Peaceful Parent Happy Kids by Laura Markham"),
    (7, "Peaceful Parent Happy Siblings by Laura Markham"),
    (8, "Hold On to Your Kids by Gordon Neufeld and Gabor Mate"),
    (9, "How to Raise Kids Who Aren't Assholes by Melinda Wenner Moyer"),
    (10, "Brain-Body Parenting by Mona Delahooke"),
    (11, "Simplicity Parenting by Kim John Payne and Lisa M. Ross"),
    (12, "The Soul of Discipline by Kim John Payne"),
    (13, "Raising Happiness by Christine Carter"),
    (14, "Raising Human Beings by Ross Greene"),
    (15, "The Explosive Child by Ross Greene"),
    (16, "Playful Parenting by Lawrence Cohen"),
]]

print("=" * 70)
print("PROCESSING FOUND-006 through FOUND-016")
print("=" * 70)

total_analysis = 0
total_actions = 0

for filename in files:
    result = process_file(filename)
    if result:
        analysis_count, action_count = result
        total_analysis += analysis_count
        total_actions += action_count
        num = filename.split('-')[0]
        print(f"✅ {filename}: {analysis_count} topics, {action_count} actions")

print("=" * 70)
print(f"📊 TOTALS: {total_analysis} analysis topics, {total_actions} action frameworks")
print("=" * 70)
