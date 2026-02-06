import os
import json
from pathlib import Path
from converter import convert_markdown_to_json

# Configuration
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "Book_Summaries"
OUTPUT_DIR = BASE_DIR / "execution" / "json_output"

def process_files(filenames):
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    
    for filename in filenames:
        print(f"Processing {filename}...")
        input_path = INPUT_DIR / filename
        if not input_path.exists():
            print(f"Error: {filename} not found.")
            continue
            
        with open(input_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
            
        try:
            json_data = convert_markdown_to_json(markdown_content, filename)
            
            output_filename = filename.replace('.md', '.json')
            output_path = OUTPUT_DIR / output_filename
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=2, ensure_ascii=False)
            
            print(f"✓ Saved to {output_path}")
        except Exception as e:
            print(f"✗ Failed to process {filename}: {str(e)}")

if __name__ == "__main__":
    files_to_process = [
        "GNDR-002 - Strong and Smart by David Scott Thomas.md",
        "GNDR-003 - Better Dads Stronger Sons by Rick I Johnson.md",
        "GNDR-004 - Strong Fathers Strong Daughters by Meg Meeker.md"
    ]
    process_files(files_to_process)
