import os
import json
import re
from pathlib import Path

# Configuration
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "Book_Summaries"
OUTPUT_DIR = BASE_DIR / "execution" / "json_output"

# Files to process (COMM-001 through COMM-010)
FILES_TO_PROCESS = [
    "COMM-001 - How to Talk So Teens Will Listen and Listen So Teens Will Talk by Adele Faber and Elaine Mazlish.md",
    "COMM-002 - How to Talk So Kids Will Listen and Listen So Kids Will Talk by Adele Faber and Elaine Mazlish.md",
    "COMM-003 - Siblings Without Rivalry by Adele Faber and Elaine Mazlish.md",
    "COMM-004 - How to Talk When Kids Won't Listen by Joanna Faber, Julie King.md",
    "COMM-005 - How to Talk When Kids Won't Listen by Joanna Faber and Julie King.md",
    "COMM-006 - How to Talk to Your Kids About Really Important Things by Charles Schaefer and Theresa Foy DiGeronimo.md",
    "COMM-007 - How to Listen So Your Kids Will Talk by Becky Harling.md",
    "COMM-008 - Talk to Me Like I'm Someone You Love by Nancy Dreyfus.md",
    "COMM-009 - Many Ways to Say I Love You by Fred Rogers.md",
    "COMM-010 - How to Stop Losing Your Sht with Your Kids by Carla Naumburg.md"
]

def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown"""
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if match:
        frontmatter = {}
        for line in match.group(1).split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip().lower()
                value = value.strip().strip('"').strip("'")
                frontmatter[key] = value
        return frontmatter
    return {}

def extract_sections(content):
    """Extract main sections from markdown"""
    # Remove frontmatter
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

    sections = {
        'executive_summary': '',
        'nuanced_topics': [],
        'checklist': [],
        'processes': []
    }

    # Extract Executive Summary
    exec_match = re.search(r'## Executive Summary\n(.*?)##', content, re.DOTALL)
    if exec_match:
        sections['executive_summary'] = exec_match.group(1).strip()

    # Extract Nuanced Main Topics
    topics_match = re.search(r'## Nuanced Main Topics\n(.*?)# Section 2:', content, re.DOTALL)
    if topics_match:
        topic_blocks = re.findall(r'### (.*?)\n(.*?)(?=###|(?=# Section 2:))', topics_match.group(1), re.DOTALL)
        for title, text in topic_blocks:
            sections['nuanced_topics'].append({
                'heading': title.strip(),
                'text': text.strip()
            })

    # Extract Checklist items
    checklist_match = re.search(r'## The Checklist\n(.*?)##', content, re.DOTALL)
    if checklist_match:
        items = re.findall(r'- \[ \] \*\*(.*?)\*\*: (.*?)$', checklist_match.group(1), re.MULTILINE)
        sections['checklist'] = [{'title': t, 'description': d} for t, d in items]

    # Extract Processes
    process_matches = re.finditer(r'### Process \d+: (.*?)\n\*\*Purpose\*\*: (.*?)\n\*\*Steps?\*\*:\n(.*?)(?=### Process|$)', content, re.DOTALL)
    for match in process_matches:
        title = match.group(1).strip()
        context = match.group(2).strip()
        steps_text = match.group(3).strip()

        # Extract steps
        steps = []
        step_matches = re.findall(r'\d+\. \*\*(.*?)\*\*:?(.*?)$', steps_text, re.MULTILINE)
        for bold_title, description in step_matches:
            steps.append({
                'bold_title': bold_title.strip(),
                'description': description.strip()
            })

        sections['processes'].append({
            'title': title,
            'context': context,
            'steps': steps
        })

    return sections

def calculate_read_time(content):
    """Calculate read time (1 min per 200 words)"""
    word_count = len(content.split())
    minutes = max(1, round(word_count / 200))
    return f"{minutes} min read"

def convert_markdown_to_json(markdown_content, filename):
    """Convert markdown content to structured JSON"""

    # Parse frontmatter
    frontmatter = parse_frontmatter(markdown_content)

    # Extract sections
    sections = extract_sections(markdown_content)

    # Get metadata
    title = frontmatter.get('title', 'Untitled')
    authors_str = frontmatter.get('author', 'Unknown')
    authors = [a.strip() for a in authors_str.replace('&', 'and').split('and')] if authors_str else ['ParentWise Summary']
    tags = frontmatter.get('tags', '').strip('[]').replace('"', '').replace("'", '').split(', ') if frontmatter.get('tags') else []

    # Build analysis array from nuanced topics
    analysis = []
    for i, topic in enumerate(sections['nuanced_topics'][:6], 1):  # Limit to 6
        analysis.append({
            "heading": f"{i}. {topic['heading']}",
            "intro_text": topic['text'][:300] + "..." if len(topic['text']) > 300 else topic['text'],
            "insight_card": {
                "title": "Key Insight",
                "icon": "fa-solid fa-lightbulb",
                "text": topic['text'][:200] + "..." if len(topic['text']) > 200 else topic['text']
            }
        })

    # Build actions array from processes
    actions = []
    for process in sections['processes']:
        actions.append({
            "title": process['title'],
            "context": process['context'],
            "steps": process['steps']
        })

    # Build JSON structure
    json_data = {
        "meta": {
            "title": title,
            "subtitle": f"A practical guide to {tags[0] if tags else 'parenting'}",
            "authors": authors,
            "tags": tags
        },
        "hero": {
            "badge": f"{frontmatter.get('category_code', 'COMM')} Core Read",
            "insights_count": len(analysis),
            "actions_count": len(actions),
            "read_time": calculate_read_time(markdown_content)
        },
        "why_matters": {
            "icon": "fa-solid fa-heart",
            "text": sections['executive_summary'][:500] if sections['executive_summary'] else "A comprehensive guide for parents."
        },
        "tabs": {
            "analysis": analysis,
            "actions": actions
        }
    }

    return json_data

def main():
    """Process all COMM files"""
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

    print(f"Processing {len(FILES_TO_PROCESS)} files...")
    print("=" * 50)

    for index, filename in enumerate(FILES_TO_PROCESS):
        try:
            print(f"[{index+1}/{len(FILES_TO_PROCESS)}] Processing {filename}...")

            # Read markdown content
            input_path = INPUT_DIR / filename
            if not input_path.exists():
                print(f"  ⚠ File not found: {input_path}")
                continue

            with open(input_path, 'r', encoding='utf-8') as f:
                markdown_content = f.read()

            # Convert to JSON
            json_data = convert_markdown_to_json(markdown_content, filename)

            # Save JSON output
            output_filename = filename.replace('.md', '.json')
            output_path = OUTPUT_DIR / output_filename

            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=2, ensure_ascii=False)

            print(f"  ✓ Saved to {output_path}")

        except Exception as e:
            print(f"  ✗ Failed: {str(e)}")
            import traceback
            traceback.print_exc()
            continue

    print("=" * 50)
    print("Conversion complete!")

if __name__ == "__main__":
    main()
