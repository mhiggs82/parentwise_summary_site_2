import json
import os
from pathlib import Path

# Configuration
BASE_DIR = Path(__file__).resolve().parent.parent
JSON_OUTPUT_DIR = BASE_DIR / "execution" / "json_output"
STATIC_DATA_DIR = BASE_DIR / "website" / "static" / "data" / "books"

def standardize_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"Skipping invalid JSON: {file_path}")
            return False

    changed = False

    # 1. Standardize meta.tags (Crucial: Fix the stringified array issue)
    if 'meta' in data and 'tags' in data['meta']:
        tags = data['meta']['tags']
        if isinstance(tags, str):
            # Handle the specific "Tag1\", \"Tag2" format
            # First, normalize by removing escaped quotes if they are literally in the string
            cleaned_tags = tags.replace('\\"', '"').replace('"', '')
            # Split by comma and strip whitespace
            tag_list = [t.strip() for t in cleaned_tags.split(',')]
            # Filter out empty strings
            tag_list = [t for t in tag_list if t]
            data['meta']['tags'] = tag_list
            changed = True
            print(f"  Fixed tags for {file_path.name}")

    # 2. Standardize insight_card
    if 'tabs' in data and 'analysis' in data['tabs']:
        for item in data['tabs']['analysis']:
            if 'insight_card' in item:
                if isinstance(item['insight_card'], str):
                    # Handle "---" or empty strings by creating a placeholder or preserving
                    text = item['insight_card'] if item['insight_card'] != "---" else "Key insight pending."
                    item['insight_card'] = {
                        "title": "Key Insight",
                        "icon": "fa-solid fa-lightbulb",
                        "text": text
                    }
                    changed = True
                elif isinstance(item['insight_card'], dict):
                    if 'title' not in item['insight_card'] or not item['insight_card']['title']:
                        item['insight_card']['title'] = "Key Insight"
                        changed = True
                    if 'icon' not in item['insight_card'] or not item['insight_card']['icon']:
                        item['insight_card']['icon'] = "fa-solid fa-lightbulb"
                        changed = True
                    # Ensure icon has fa-prefix
                    icon = item['insight_card'].get('icon', '')
                    if icon and not icon.startswith('fa-'):
                        item['insight_card']['icon'] = f"fa-solid fa-{icon}"
                        changed = True

    # 3. Standardize steps (label -> bold_title)
    if 'tabs' in data and 'actions' in data['tabs']:
        for section in data['tabs']['actions']:
            if 'steps' in section:
                for step in section['steps']:
                    if 'label' in step and 'bold_title' not in step:
                        step['bold_title'] = step.pop('label')
                        changed = True
                    # Ensure bold_title exists
                    if 'bold_title' not in step:
                        step['bold_title'] = "ACTION"
                        changed = True

    # 4. Standardize hero icon in why_matters
    if 'why_matters' in data and isinstance(data['why_matters'], dict):
        icon = data['why_matters'].get('icon', '')
        if icon and not icon.startswith('fa-'):
            mapping = {
                "lightbulb": "fa-solid fa-lightbulb",
                "heart": "fa-solid fa-heart",
                "brain": "fa-solid fa-brain",
                "compass": "fa-solid fa-compass"
            }
            data['why_matters']['icon'] = mapping.get(icon.lower(), "fa-solid fa-circle-info")
            changed = True

    # 5. Standardize hero badge
    if 'hero' in data and 'badge' in data['hero']:
        badge = data['hero']['badge']
        if badge in ["FOUND", "COMM", "SPEC", "MENT", "TEEN", "PRNT"]:
             data['hero']['badge'] = f"{badge} Core Read"
             changed = True

    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    return False

def main():
    print("🧹 Standardizing JSON data formats...")
    
    targets = list(JSON_OUTPUT_DIR.glob("*.json")) + list(STATIC_DATA_DIR.glob("*.json"))
    updated_count = 0
    
    for target in targets:
        if standardize_file(target):
            updated_count += 1
            print(f"✅ Updated: {target.name}")

    print(f"\nDone! Standardized {updated_count} files.")

if __name__ == "__main__":
    main()
