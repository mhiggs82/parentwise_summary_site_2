import os
import json
import re
import math
from pathlib import Path
from dotenv import load_dotenv
import litellm
from execution.quality_standards import QUALITY_MANIFESTO

# Load environment variables
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# Configuration
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "Book_Summaries"
OUTPUT_DIR = BASE_DIR / "execution" / "json_output"
MODEL = os.environ.get("LLM_MODEL", "anthropic/claude-3-5-sonnet-20240620")

# System prompt for high-fidelity AI extraction
SYSTEM_PROMPT = f"""You are a book summary analyzer. Your task is to extract structured data from the provided markdown book summary.

{QUALITY_MANIFESTO}

PRIME DIRECTIVE: 
Adhere strictly to the semantic meaning and nuance of the source text. Do NOT over-summarize or omit details that contribute to the author's specific perspective. Your goal is faithful restructuring, not transformation.

EXTRACTION RULES:
1. ANALYSIS & INSIGHTS:
   - Extract ALL distinct analysis points.
   - For each point, preserve the core arguments, evidence, or logic presented.
   - Use the original tone and terminology where appropriate.
2. ACTIONABLE STEPS:
   - Extract every strategy, process, or action plan.
   - Ensure steps are clear and maintain the original sequence and caveats.
3. WHY IT MATTERS (EXECUTIVE SUMMARY):
   - Capture the central Thesis, Unique Contribution, and Target Outcome.
   - Maintain the "voice" of the summary while ensuring it's compelling for a card view.
   - Use bolding for emphasis on key philosophical or tactical shifts.

JSON SCHEMA:
{
  "meta": {
    "title": "Full book title",
    "subtitle": "A catchy, high-impact subtitle reflecting the book's core value",
    "authors": ["Author Name"],
    "tags": ["Tag1", "Tag2"],
    "category_code": "COMM"
  },
  "hero": {
    "badge": "COMM Core Read",
    "insights_count": <int>,
    "actions_count": <int>,
    "read_time": "X min read"
  },
  "why_matters": {
    "icon": "fa-solid fa-heart",
    "text": "The semantic heart of the guide."
  },
  "tabs": {
    "analysis": [
      {
        "heading": "1. Topic Title",
        "intro_text": "Detailed semantic extraction of the topic",
        "insight_card": {
          "title": "Key Insight",
          "icon": "fa-solid fa-lightbulb",
          "text": "The core takeaway, preserved in its original nuance"
        }
      }
    ],
    "actions": [
      {
        "title": "Action Strategy Title",
        "context": "When and why to use this, per the text",
        "steps": [
          {
            "bold_title": "Step Name",
            "description": "Semantic detail of the step"
          }
        ]
      }
    ]
  }
}

Return ONLY valid JSON."""

def calculate_read_time(content):
    """Calculate accurate read time (1 min per 200 words)"""
    word_count = len(content.split())
    minutes = max(1, math.ceil(word_count / 200))
    return f"{minutes} min read"

def convert_markdown_to_json(markdown_content, filename):
    """Convert markdown content to structured JSON using AI"""
    try:
        read_time_str = calculate_read_time(markdown_content)
        
        response = litellm.completion(
            model=MODEL,
            max_tokens=4096,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": markdown_content}
            ]
        )

        response_text = response.choices[0].message.content
        if response_text.strip().startswith("```"):
            lines = response_text.strip().split("\n")
            response_text = "\n".join(lines[1:-1])
            if response_text.startswith("json"):
                response_text = response_text[4:].strip()

        json_data = json.loads(response_text)

        # Post-processing overrides for consistency
        json_data.setdefault("hero", {})["read_time"] = read_time_str
        
        # Smart category correction
        meta = json_data.setdefault("meta", {})
        current_cat = meta.get("category_code", "COMM")
        
        prefix_match = re.search(r'([A-Z]{3,4})-\d+', filename)
        if prefix_match:
            new_cat = prefix_match.group(1).upper()
            meta["category_code"] = new_cat
            json_data["hero"]["badge"] = f"{new_cat} Core Read"

        return json_data

    except Exception as e:
        print(f"  ✗ AI Error for {filename}: {str(e)}")
        raise

# Set to specific prefixes to process (e.g., ["FOUND"]) or empty [] for all
FILES_TO_PROCESS = ["FOUND"]

def main():
    """Process files using AI conversion"""
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

    print("🌟 ParentWise Quality Standards Loaded:")
    print(QUALITY_MANIFESTO)
    print("=" * 60)

    print(f"Detecting files in {INPUT_DIR}...")
    
    if FILES_TO_PROCESS:
        markdown_files = []
        for prefix in FILES_TO_PROCESS:
            matches = list(INPUT_DIR.glob(f"{prefix}*.md"))
            markdown_files.extend(matches)
        # Ensure unique and sorted
        markdown_files = sorted(list(set(markdown_files)))
    else:
        markdown_files = sorted([f for f in INPUT_DIR.glob("*.md") if not f.name.startswith('_')])

    print(f"Processing {len(markdown_files)} files with full AI Semantic Extraction...")
    print("=" * 50)

    for index, input_path in enumerate(markdown_files):
        try:
            filename = input_path.name
            print(f"[{index+1}/{len(markdown_files)}] Semantic Processing: {filename}...")

            with open(input_path, 'r', encoding='utf-8') as f:
                markdown_content = f.read()

            # AI Conversion
            json_data = convert_markdown_to_json(markdown_content, filename)

            # Save JSON
            output_filename = filename.replace('.md', '.json')
            output_path = OUTPUT_DIR / output_filename

            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=2, ensure_ascii=False)

            print(f"  ✓ Semantic JSON saved to {output_path}")

        except Exception as e:
            print(f"  ✗ Failed: {str(e)}")
            continue

    print("=" * 50)
    print("Full AI Migration complete!")

if __name__ == "__main__":
    main()
