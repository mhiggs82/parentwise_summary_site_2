import json
import os
import re
from pathlib import Path

# Configuration
BASE_DIR = Path(__file__).resolve().parent.parent
JSON_DIR = BASE_DIR / "website" / "static" / "data" / "books"
OUTPUT_DIR = BASE_DIR / "execution" / "json_output"

def migrate_pitfalls(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"Skipping {json_path.name} - Invalid JSON")
            return False

    if 'tabs' not in data or 'actions' not in data.get('tabs', {}):
        return False

    actions = data['tabs']['actions']
    if not actions:
        return False

    last_action = actions[-1]
    steps = last_action.get('steps', [])
    if not steps:
        return False

    last_step = steps[-1]
    desc = last_step.get('description', '')

    if '## Common Pitfalls' in desc:
        print(f"Migrating pitfalls for {json_path.name}...")
        
        # Split into main description and pitfalls section
        parts = desc.split('## Common Pitfalls')
        new_desc = parts[0].strip()
        pitfalls_raw = parts[1].strip()

        # Clean up description (remove trailing --- if present)
        new_desc = re.sub(r'---.*$', '', new_desc, flags=re.DOTALL).strip()
        last_step['description'] = new_desc

        # Extract pitfalls
        # Format: ⚠️ **Pitfall X**: Title - **Solution**: Text
        # or ⚠️ **Pitfall X**: Title - Text
        pitfall_items = []
        
        # Split by the warning emoji or "Pitfall X"
        raw_items = re.split(r'⚠️\s*\*\*Pitfall\s+\d+\*\*:\s*', pitfalls_raw)
        for item in raw_items:
            item = item.strip()
            if not item:
                continue
            
            # Remove trailing "--- Immediate Next Step..." if it leaked in
            item = re.split(r'---\s*\*\*Immediate Next Step\*\*', item, flags=re.IGNORECASE)[0].strip()
            
            # Try to split by " - **Solution**: " or " - "
            if ' - **Solution**: ' in item:
                title, text = item.split(' - **Solution**: ', 1)
            elif ' - ' in item:
                title, text = item.split(' - ', 1)
            else:
                title = "Common Pitfall"
                text = item
            
            # Cleanup Markdown bolding in title
            title = title.replace('**', '').strip()
            text = text.strip()

            pitfall_items.append({
                "title": title,
                "icon": "fa-solid fa-triangle-exclamation",
                "text": text
            })

        if pitfall_items:
            data['tabs']['pitfalls'] = pitfall_items
            
            # Save to website static folder
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            # Also save to execution/json_output for backup
            output_path = OUTPUT_DIR / json_path.name
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            return True

    return False

def main():
    JSON_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    count = 0
    for json_file in JSON_DIR.glob("*.json"):
        if migrate_pitfalls(json_file):
            count += 1

    print(f"Successfully migrated {count} files.")

if __name__ == "__main__":
    main()
