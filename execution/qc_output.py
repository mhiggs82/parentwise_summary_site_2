import json
import os
import re
from pathlib import Path
import yaml

# Configuration
BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "website" / "docs"
STATIC_DATA_DIR = BASE_DIR / "website" / "static" / "data" / "books"

# Regex patterns for MDX parsing
IMPORT_PATTERN = re.compile(r'import\s+bookData\s+from\s+["\'](.*?)["\'];')
TOC_PATTERN = re.compile(r'export\s+const\s+toc\s+=\s+\[(.*?)\];', re.DOTALL)
TOC_ITEM_PATTERN = re.compile(r'\{\s*value:\s*["\'](.*?)["\'],\s*id:\s*["\'](.*?)["\'],\s*level:\s*(\d+)\s*\}')

def clean_filename(name):
    """Normalize filenames for comparison (handles extension and case)."""
    return name.replace('.mdx', '').replace('.json', '').lower()

def check_json_file(json_path):
    errors = []
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        return [f"Invalid JSON: {e}"]

    # Basic structure checks
    required_top_level = ['meta', 'hero', 'why_matters', 'tabs']
    for field in required_top_level:
        if field not in data:
            errors.append(f"Missing top-level field: {field}")

    if 'meta' in data:
        for field in ['title', 'authors', 'category_code']:
            if field not in data['meta']:
                errors.append(f"Missing meta field: {field}")

    if 'tabs' in data:
        analysis = data['tabs'].get('analysis', [])
        for i, item in enumerate(analysis):
            if 'insight_card' in item:
                ic = item['insight_card']
                if not isinstance(ic, dict):
                    errors.append(f"tabs.analysis[{i}].insight_card must be an object (found {type(ic).__name__})")
                else:
                    for f in ['title', 'text']:
                        if f not in ic:
                            errors.append(f"tabs.analysis[{i}].insight_card missing field: {f}")

        actions = data['tabs'].get('actions', [])
        if len(actions) < 3 or len(actions) > 5:
            errors.append(f"Number of action frameworks must be 3-5 (found {len(actions)})")

        for i, section in enumerate(actions):
            steps = section.get('steps', [])
            if len(steps) < 3 or len(steps) > 7:
                errors.append(f"tabs.actions[{i}] ('{section.get('title', 'Unknown')}') must have 3-7 steps (found {len(steps)})")

            for j, step in enumerate(steps):
                if 'bold_title' not in step:
                    actual_keys = list(step.keys())
                    errors.append(f"tabs.actions[{i}].steps[{j}] missing 'bold_title' (found keys: {actual_keys})")
                else:
                    bt = step['bold_title']
                    if len(bt.split()) < 2:
                        errors.append(f"tabs.actions[{i}].steps[{j}].bold_title must be more than one word (found '{bt}')")
                
                if 'description' in step:
                    desc = step['description']
                    if len(desc.split()) < 5: 
                        errors.append(f"tabs.actions[{i}].steps[{j}].description is too short (found '{desc}')")

        if 'pitfalls' in data['tabs']:
            pitfalls = data['tabs']['pitfalls']
            for i, p in enumerate(pitfalls):
                for f in ['title', 'text']:
                    if f not in p:
                        errors.append(f"tabs.pitfalls[{i}] missing field: {f}")
                if 'title' in p:
                    if len(p['title'].split()) < 2:
                        errors.append(f"tabs.pitfalls[{i}].title must be more than one word (found '{p['title']}')")

    if 'hero' in data:
        analysis_count = len(data.get('tabs', {}).get('analysis', []))
        actions_count = len(data.get('tabs', {}).get('actions', []))
        
        if data['hero'].get('insights_count') != analysis_count:
            errors.append(f"Hero insights_count ({data['hero'].get('insights_count')}) does not match actual count ({analysis_count})")
        if data['hero'].get('actions_count') != actions_count:
            errors.append(f"Hero actions_count ({data['hero'].get('actions_count')}) does not match actual count ({actions_count})")

    if 'why_matters' in data:
        text = data['why_matters'].get('text', '')
        # Simple sentence splitter: look for ., !, ? followed by space or end of string
        sentences = re.split(r'[.!?](?:\s+|$)', text)
        sentences = [s for s in sentences if s.strip()]
        if len(sentences) < 3 or len(sentences) > 4:
            errors.append(f"why_matters.text must be 3-4 sentences (found {len(sentences)})")

    return errors

def check_mdx_file(mdx_path):
    errors = []
    try:
        with open(mdx_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return [f"Could not read MDX: {e}"]

    # 1. Frontmatter check
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        errors.append("Missing frontmatter")
    else:
        try:
            fm = yaml.safe_load(fm_match.group(1))
            required_fm = ['title', 'sidebar_label', 'description', 'author']
            for field in required_fm:
                if field not in fm or not str(fm[field]).strip():
                    errors.append(f"Missing or empty frontmatter field: {field}")
        except Exception as e:
            errors.append(f"Invalid YAML in frontmatter: {e}")

    # 2. Import check
    import_match = IMPORT_PATTERN.search(content)
    if not import_match:
        errors.append("Missing 'import bookData' statement")
    else:
        import_path = import_match.group(1)
        # Convert @site path to actual path
        if import_path.startswith("@site/"):
            rel_path = import_path.replace("@site/", "")
            actual_json_path = BASE_DIR / "website" / rel_path
            if not actual_json_path.exists():
                errors.append(f"JSON file does not exist at imported path: {import_path}")
            else:
                # Check if JSON matches the name of MDX roughly (sanity check)
                if clean_filename(actual_json_path.name) != clean_filename(mdx_path.name):
                    errors.append(f"MDX filename vs JSON source mismatch: {mdx_path.name} imports {actual_json_path.name}")
        else:
            errors.append(f"Import path should start with @site/: {import_path}")

    # 3. TOC check
    toc_match = TOC_PATTERN.search(content)
    if not toc_match:
        errors.append("Missing 'export const toc' block")
    else:
        toc_content = toc_match.group(1)
        items = TOC_ITEM_PATTERN.findall(toc_content)
        if not items:
            errors.append("TOC block is empty or malformed")
        else:
            values = [it[0] for it in items]
            required_start_values = ['Summary Overview', 'Why It Matters', 'Analysis & Insights']
            for val in required_start_values:
                if val not in values:
                    errors.append(f"Missing required TOC item: {val}")
            
            # Check for Common Pitfalls (if it's in the corresponding JSON)
            # This is a bit tricky as MDX doesn't know its JSON content here easily without reloading
            # But we can at least check if it's there if the JSON has it. 
            # Actually, let's just make it required if the section is present.

    # 4. Component check
    if "<BookSummary data={bookData} />" not in content:
        errors.append("Missing <BookSummary data={bookData} /> component call")

    return errors

def main():
    print("🚀 Running Quality Control on MDX and JSON outputs...")
    print("=" * 60)

    all_mdx = list(DOCS_DIR.rglob("*.mdx"))
    all_json = list(STATIC_DATA_DIR.glob("*.json"))

    print(f"Found {len(all_mdx)} MDX files and {len(all_json)} JSON files.")
    
    issues_found = 0

    for mdx_file in all_mdx:
        rel_path = mdx_file.relative_to(BASE_DIR)
        errors = check_mdx_file(mdx_file)
        if errors:
            print(f"\n❌ Issues in {rel_path}:")
            for err in errors:
                print(f"  - {err}")
            issues_found += len(errors)

    for json_file in all_json:
        rel_path = json_file.relative_to(BASE_DIR)
        errors = check_json_file(json_file)
        if errors:
            print(f"\n❌ Issues in {rel_path}:")
            for err in errors:
                print(f"  - {err}")
            issues_found += len(errors)

    print("\n" + "=" * 60)
    if issues_found == 0:
        print("✅ All checks passed! Output quality is looking good.")
    else:
        print(f"⚠️ Found {issues_found} issue(s). Please review and fix them.")

if __name__ == "__main__":
    main()
