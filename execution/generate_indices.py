import os

docs_dir = 'docs/Book_Summaries'
categories = {
    'COMM': 'Communication',
    'DIGI': 'Digital Parenting',
    'FMLY': 'Family & Relationships',
    'FOUND': 'Foundational Skills',
    'GLOB': 'Global Perspectives',
    'GNDR': 'Gender & Identity',
    'LIFE': 'Life Skills',
    'MENT': 'Mental Health',
    'SPEC': 'Special Needs',
    'TEEN': 'Teen Parenting',
    'MISC': 'Miscellaneous'
}

for cat_code, cat_name in categories.items():
    cat_dir = os.path.join(docs_dir, cat_code)
    if not os.path.exists(cat_dir):
        continue
        
    index_path = os.path.join(cat_dir, 'index.md')
    
    # Get all markdown files in the directory except index.md
    files = [f for f in os.listdir(cat_dir) if f.endswith('.md') and f != 'index.md']
    files.sort()
    
    content = f"# {cat_name} ({cat_code})\n\n"
    content += f"Browse our collection of curated summaries focused on **{cat_name.lower()}**.\n\n"
    content += "### Summaries in this Category\n\n"
    
    for f in files:
        # Extract title (remove prefix and extension)
        title = f.replace(f"{cat_code}-", "").replace(".md", "")
        # Handle the "NNN - Title" format
        if " - " in title:
            title = title.split(" - ", 1)[1]
            
        content += f"*   [{title}]({f})\n"
        
    with open(index_path, 'w') as out:
        out.write(content)

print("Category indices generated successfully.")
