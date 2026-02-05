import sys
import os

def check_structure(root_path):
    required_dirs = ['directives', 'execution', '.tmp']
    required_files = ['agents.md', '.env', '.gitignore']
    
    print(f"Checking structure for: {root_path}")
    
    for d in required_dirs:
        path = os.path.join(root_path, d)
        if os.path.isdir(path):
            print(f"[OK] Directory found: {d}")
        else:
            print(f"[MISSING] Directory: {d}")
            
    for f in required_files:
        path = os.path.join(root_path, f)
        if os.path.isfile(path):
            print(f"[OK] File found: {f}")
        else:
            print(f"[MISSING] File: {f}")

if __name__ == "__main__":
    check_structure(os.getcwd())
