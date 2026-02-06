import os
import json
import re
from pathlib import Path

# Configuration
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "Book_Summaries"
OUTPUT_DIR = BASE_DIR / "execution" / "json_output"

FILES_TO_PROCESS = [] # Set to empty list to automatically detect all files

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
    exec_match = re.search(r'##? (?:1\.\s+)?Executive Summary\s+(.*?)(?=\n##|\n#|$)', content, re.DOTALL)
    if exec_match:
        sections['executive_summary'] = exec_match.group(1).strip()

    # Extract Nuanced Main Topics / Insights
    # Prioritize "Nuanced Main Topics" or "Deep Insights" over "Chapter Breakdown"
    topics_match = None
    for pattern in [r'##? (?:2\.\s+)?Nuanced Main Topics', r'##? (?:2\.\s+)?Deep Insights Analysis', r'##? (?:2\.\s+)?Paradigm Shifts', r'##? (?:2\.\s+)?Chapter Breakdown', r'##? (?:2\.\s+)?Structural Overview']:
        match = re.search(pattern + r'\s+(.*?)(?=\n##(?!#)|\n# Section 2:|# PART 2:|$)', content, re.DOTALL)
        if match:
            topics_match = match
            break
    if topics_match:
        topic_text = topics_match.group(1).strip()
        # Split by ### level headings
        blocks = re.split(r'\n###?\s+', '\n' + topic_text)
        for block in blocks:
            if not block.strip(): continue
            lines = block.strip().split('\n')
            if len(lines) >= 2:
                heading = lines[0].strip()
                text = '\n'.join(lines[1:]).strip()
                if heading and text:
                    sections['nuanced_topics'].append({
                        'heading': heading,
                        'text': text
                    })

    # Extract Checklist items
    checklist_match = re.search(r'##? (?:The Checklist|Impactful Concepts)\s+(.*?)(?=\n##|\n#|$)', content, re.DOTALL)
    if checklist_match:
        # Match both checkbox style and simple bold titles
        items = re.findall(r'(?:- \[ \] \*\*|\* \*\*|\d+\. \*\*)(.*?)\*\*:?\s*(.*?)(?=\n-|\n\*|\n\d+\.|\n##|$)', checklist_match.group(1), re.MULTILINE | re.DOTALL)
        sections['checklist'] = [{'title': t.strip(), 'description': d.strip()} for t, d in items]

    # Extract Processes
    # Flexible matching for Process 1: Title, Purpose: context, Steps: list
    process_matches = re.finditer(r'##? Process \d+: (.*?)\s+(?:\*\*Purpose\*\*[:\s]+(.*?))?\s+(?:\*\*Prerequisites\*\*[:\s]+(.*?))?\s+\*\*(?:Actionable )?Steps\*\*[:\s]*\n(.*?)(?=##? Process|# Suggested Next Step|$)', content, re.DOTALL | re.IGNORECASE)
    for match in process_matches:
        title = match.group(1).strip()
        context = match.group(2).strip() if match.group(2) else ""
        steps_text = match.group(4).strip()

        # Extract steps - handle varying markers (1., -, *, ✓, 🔑, ⚠️, ↻)
        steps = []
        step_matches = re.findall(r'^\s*(?:\d+\.|\*|-|✓|🔑|⚠️|↻)\s*\*\*(.*?)\*\*(?:[:\s-]*(.*?))?$', steps_text, re.MULTILINE)
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
    
    # Smart category extraction: Frontmatter > Filename Prefix > Default 'COMM'
    category_code = frontmatter.get('category_code')
    if not category_code:
        # Try to extract from filename (e.g., "COMM-001 - Title.md" -> "COMM")
        prefix_match = re.search(r'([A-Z]{3,4})-\d+', filename)
        if prefix_match:
            category_code = prefix_match.group(1)
        else:
            category_code = 'COMM'
    
    # Clean category code
    category_code = category_code.strip().upper()
    print(f"    -> Category: {category_code}")

    # Build analysis array from nuanced topics
    analysis = []
    for i, topic in enumerate(sections['nuanced_topics'], 1):  # Process ALL topics
        analysis.append({
            "heading": f"{i}. {topic['heading']}",
            "intro_text": topic['text'],
            "insight_card": {
                "title": "Key Insight",
                "icon": "fa-solid fa-lightbulb",
                "text": topic['text']
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
            "tags": tags,
            "category_code": category_code
        },
        "hero": {
            "badge": f"{category_code} Core Read",
            "insights_count": len(analysis),
            "actions_count": len(actions),
            "read_time": calculate_read_time(markdown_content)
        },
        "why_matters": {
            "icon": "fa-solid fa-heart",
            "text": sections['executive_summary'] if sections['executive_summary'] else "A comprehensive guide for parents."
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

    print(f"Detecting files in {INPUT_DIR}...")

    if FILES_TO_PROCESS:
        markdown_files = []
        for prefix in FILES_TO_PROCESS:
            matches = list(INPUT_DIR.glob(f"{prefix}*.md"))
            markdown_files.extend(matches)
    else:
        # Get all .md files, excluding readme or templates if they existed
        markdown_files = sorted([f for f in INPUT_DIR.glob("*.md") if not f.name.startswith('_')])

    print(f"Processing {len(markdown_files)} files...")
    print("=" * 50)

    for index, input_path in enumerate(markdown_files):
        try:
            filename = input_path.name
            print(f"[{index+1}/{len(markdown_files)}] Processing {filename}...")

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
