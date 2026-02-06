# Install: pip install litellm python-dotenv anthropic openai google-generativeai
# Set API keys in .env file:
# ANTHROPIC_API_KEY='sk-ant-...'
# OPENAI_API_KEY='sk-...'
# GEMINI_API_KEY='...'
#
# This script converts markdown book summaries to structured JSON format using any LLM via litellm.
#
# Required library: pip install litellm python-dotenv
#
# Input: Markdown files in markdown_input/ directory
# Output: JSON files in json_output/ directory

import os
import json
import math
from pathlib import Path
from dotenv import load_dotenv
import litellm

# Load environment variables from .env
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# Configuration
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "Book_Summaries"
OUTPUT_DIR = BASE_DIR / "execution" / "json_output"

# Use litellm syntax: "anthropic/claude-3-sonnet-20240229", "openai/gpt-4", "gemini/gemini-1.5-pro"
# Defaults to Claude 3.5 Sonnet if not specified
MODEL = os.environ.get("LLM_MODEL", "anthropic/claude-3-5-sonnet-20240620")


# System prompt for AI extraction
SYSTEM_PROMPT = """You are a book summary analyzer. Extract structured data from the provided markdown book summary.

CRITICAL INSTRUCTIONS FOR COMPLETE EXTRACTION:
- Extract ALL distinct analysis points found in the text.
- Extract ALL strategies or action plans found in the content.
- Populate arrays fully with every piece of relevant content.

WHY IT MATTERS SECTION:
This is the most important part of the JSON for our library overview. It must be compelling and readable.
- Extract the core "Executive Summary".
- It should ideally cover: 1) The book's central Thesis, 2) Its Unique Contribution, and 3) The Target Outcome for the reader.
- Use bolding for key terms.
- Ensure it is 3-5 sentences or a well-structured paragraph that "sells" the value of the guide.

ICON FORMAT:
Use Font Awesome 6 Solid classes in the format: 'fa-solid fa-brain', 'fa-solid fa-layer-group', 'fa-solid fa-lightbulb', 'fa-solid fa-heart'
Common icons: fa-brain, fa-lightbulb, fa-heart, fa-layer-group, fa-compass, fa-route, fa-puzzle-piece, fa-hands-holding-child

JSON SCHEMA:
{
  "meta": {
    "title": "Full book title",
    "subtitle": "Brief subtitle describing the book's focus",
    "authors": ["Author Name"],
    "tags": ["Tag1", "Tag2"],
    "category_code": "COMM"
  },
  "hero": {
    "badge": "COMM Core Read",
    "insights_count": <number of analysis items>,
    "actions_count": <number of action items>,
    "read_time": "X min read"
  },
  "why_matters": {
    "icon": "fa-solid fa-heart",
    "text": "Compelling summary of WHY this book matters to a parent."
  },
  "tabs": {
    "analysis": [
      {
        "heading": "1. Main Topic Title",
        "intro_text": "Introduction paragraph explaining this analysis point",
        "insight_card": {
          "title": "Key Insight",
          "icon": "fa-solid fa-brain",
          "text": "The key insight or takeaway"
        }
      }
    ],
    "actions": [
      {
        "title": "Action Strategy Title",
        "context": "Context for when/why to use this strategy",
        "steps": [
          {
            "bold_title": "Step 1: Action",
            "description": "Detailed description of this step"
          }
        ]
      }
    ],
    "pitfalls": [
      {
        "title": "Pitfall Label",
        "icon": "fa-solid fa-triangle-exclamation",
        "text": "Detailed description of the pitfall and how to avoid it."
      }
    ]
  }
}

Extract all content accurately and completely. Return only valid JSON. Ensure 'pitfalls' is a distinct section under 'tabs' based on 'Common Pitfalls' or 'Common Obstacles' in the source text."""


def calculate_read_time(content):
    """
    Calculate accurate read time (1 min per 200 words)
    """
    word_count = len(content.split())
    minutes = math.ceil(word_count / 200)
    return f"{minutes} min read"


def convert_markdown_to_json(markdown_content, filename):
    """
    Convert markdown content to structured JSON using any LLM via litellm
    """
    try:
        # Calculate accurate read time (1 min per 200 words)
        read_time_str = calculate_read_time(markdown_content)

        # Call LLM via litellm
        response = litellm.completion(
            model=MODEL,
            max_tokens=4096,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": markdown_content}
            ]
        )

        # Extract JSON from response
        response_text = response.choices[0].message.content


        # Handle code block wrapping if present
        if response_text.strip().startswith("```"):
            # Remove code block markers
            lines = response_text.strip().split("\n")
            response_text = "\n".join(lines[1:-1])
            if response_text.startswith("json"):
                response_text = response_text[4:].strip()

        # Parse JSON
        json_data = json.loads(response_text)

        # Override any AI-generated read_time with accurate Python calculation
        json_data.setdefault("hero", {})
        json_data["hero"]["read_time"] = read_time_str

        # Smart category override if AI fails or defaults to COMM but filename suggests otherwise
        meta = json_data.setdefault("meta", {})
        current_cat = meta.get("category_code", "COMM")
        
        if current_cat == "COMM":
            prefix_match = re.search(r'^([A-Z]+)-\d+', filename)
            if prefix_match:
                new_cat = prefix_match.group(1).upper()
                meta["category_code"] = new_cat
                json_data["hero"]["badge"] = f"{new_cat} Core Read"

        return json_data

    except Exception as e:
        print(f"Error converting {filename}: {str(e)}")
        raise


def main():
    """
    Main conversion logic - process all markdown files
    """
    # Create input directory if it doesn't exist
    INPUT_DIR.mkdir(exist_ok=True, parents=True)

    # Create output directory if it doesn't exist
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

    # Get all markdown files
    all_files = sorted([f for f in os.listdir(INPUT_DIR) if f.endswith('.md')])

    # Process all markdown files
    markdown_files = all_files
    total = len(markdown_files)

    if total == 0:
        print(f"No markdown files found in {INPUT_DIR}/")
        return

    print(f"Found {total} markdown files to process")
    print("=" * 50)

    # Process each file
    for index, filename in enumerate(markdown_files):
        try:
            print(f"[{index+1}/{total}] Processing {filename}...")

            # Read markdown content
            input_path = INPUT_DIR / filename
            with open(input_path, 'r', encoding='utf-8') as f:
                markdown_content = f.read()

            # Convert to JSON
            json_data = convert_markdown_to_json(markdown_content, filename)

            # Save JSON output
            output_filename = filename.replace('.md', '.json')
            output_path = OUTPUT_DIR / output_filename

            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=2, ensure_ascii=False)

            print(f"✓ Saved to {output_path}")

        except Exception as e:
            print(f"✗ Failed to process {filename}: {str(e)}")
            continue


    print("=" * 50)
    print(f"Conversion complete! Processed {total} files.")


if __name__ == "__main__":
    main()
