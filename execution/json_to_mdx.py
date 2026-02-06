import os
import json
import re
from pathlib import Path

# Configuration
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "execution" / "json_output"
OUTPUT_DIR = BASE_DIR / "execution" / "mdx_output"

# MDX Template
TEMPLATE = """---
title: {title_formatted}
sidebar_label: {short_title}
subtitle: "{subtitle}"
author: "{author}"
hide_title: true
hide_extra_header: true
hide_table_of_contents: false
---

import BookSummary from '@site/src/components/BookSummary';
import bookData from '@site/static/data/books/{json_filename}';

export const toc = [
{toc_items}
];

<BookSummary data={{bookData}} />
"""

# Helper to slugify text for IDs (matches JS logic)
def slugify(text):
    """
    Python implementation of: text.toLowerCase().replace(/[^\\w\\s-]/g, '').replace(/[\\s_]+/g, '-').trim();
    """
    text = text.lower()
    # Remove non-word characters (except spaces and hyphens)
    text = re.sub(r'[^\w\s-]', '', text)
    # Replace spaces and underscores with hyphens
    text = re.sub(r'[\s_]+', '-', text)
    return text.strip('-')

def generate_toc_items(data):
    """
    Generate the TOC items list for the MDX export
    """
    items = [
        "  { value: 'Summary Overview', id: 'summary-overview', level: 2 },",
        "  { value: 'Why It Matters', id: 'why-it-matters', level: 2 },",
        "  { value: 'Analysis & Insights', id: 'analysis', level: 2 },"
    ]

    # Add Analysis sub-headings (H3)
    if 'tabs' in data and 'analysis' in data['tabs']:
        for item in data['tabs']['analysis']:
            heading = item.get('heading', '')
            if heading:
                slug = slugify(heading)
                # Escape single/double quotes in value if they exist for JS string safety
                val = heading.replace("'", "\\'").replace('"', '\\"')
                items.append(f"  {{ value: '{val}', id: '{slug}', level: 3 }},")

    # Add Actionable Framework (H2) and sub-items (H3)
    items.append("  { value: 'Actionable Framework', id: 'actions', level: 2 },")
    if 'tabs' in data and 'actions' in data['tabs']:
        for item in data['tabs']['actions']:
            title = item.get('title', '')
            if title:
                slug = slugify(title)
                val = title.replace("'", "\\'").replace('"', '\\"')
                items.append(f"  {{ value: '{val}', id: '{slug}', level: 3 }},")

    return "\n".join(items)

def generate_mdx(json_filepath, json_filename):
    """
    Generate MDX file from JSON data with dynamic TOC
    """
    try:
        # Load JSON data
        with open(json_filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Extract metadata
        title = data['meta']['title']
        subtitle = data['meta'].get('subtitle', '').replace('"', '\\"')
        author = data['meta'].get('authors', ['ParentWise Summary'])[0].replace('"', '\\"')

        # Create short_title by splitting on : and taking first part
        short_title = title.split(':')[0].strip()

        # Replace : with - in full title for frontmatter
        title_formatted = title.replace(':', ' -')

        # Generate TOC items
        toc_items = generate_toc_items(data)

        # Format MDX content
        mdx_content = TEMPLATE.format(
            title_formatted=title_formatted,
            short_title=short_title,
            subtitle=subtitle,
            author=author,
            json_filename=json_filename,
            toc_items=toc_items
        )

        return mdx_content

    except Exception as e:
        print(f"Error generating MDX for {json_filename}: {str(e)}")
        raise

def main():
    """
    Main generation logic - process all JSON files
    """
    # Create output directory if it doesn't exist
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

    # Get all JSON files
    if not INPUT_DIR.exists():
        print(f"Error: Input directory {INPUT_DIR} does not exist.")
        return

    all_files = sorted([f for f in os.listdir(INPUT_DIR) if f.endswith('.json')])

    # Filter for all COMM books
    json_files = [f for f in all_files if f.startswith('COMM-')]
    total = len(json_files)

    if total == 0:
        print(f"No JSON files found in {INPUT_DIR}/")
        return

    print(f"⚙️ Generating MDX for {total} files...")
    print("=" * 50)

    # Process each file
    for index, filename in enumerate(json_files):
        try:
            print(f"[{index+1}/{total}] Generating {filename}...")

            # Generate MDX content
            input_path = INPUT_DIR / filename
            mdx_content = generate_mdx(input_path, filename)

            # Save MDX output
            output_filename = filename.replace('.json', '.mdx')
            output_path = OUTPUT_DIR / output_filename

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(mdx_content)

            print(f"✓ Saved to {output_path}")

        except Exception as e:
            print(f"✗ Failed to generate MDX for {filename}: {str(e)}")
            continue

    print("=" * 50)
    print(f"Generation complete! Created {total} MDX files.")

if __name__ == "__main__":
    main()
