import os
import subprocess

def run_git_cmd(args):
    try:
        subprocess.run(["git"] + args, check=True)
        print(f"Git command success: {' '.join(args)}")
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {' '.join(args)} -> {e}")

def cleanup_files(directory):
    """
    Scans directory. 
    If file has colon:
      Construct new name (hyphenated).
      If new name exists: git rm old_name (Duplicate)
      If new name doesn't exist: git mv old_name new_name (Rename)
    """
    print(f"Scanning {directory}...")
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if ':' in filename:
                old_path = os.path.join(root, filename)
                
                # Logic to determine new filename (same as before)
                new_filename = filename.replace(': ', ' - ').replace(':', '-')
                new_path = os.path.join(root, new_filename)
                
                if os.path.exists(new_path):
                    print(f"Duplicate found. Removing: {filename}")
                    run_git_cmd(["rm", old_path])
                else:
                    print(f"Renaming: {filename} -> {new_filename}")
                    run_git_cmd(["mv", old_path, new_path])

if __name__ == "__main__":
    base_dir = os.getcwd()
    
    # Directories to clean
    dirs_to_clean = [
        os.path.join(base_dir, "website/static/data/books"),
        os.path.join(base_dir, "website/docs"),
        os.path.join(base_dir, "Book_Summaries")
    ]

    for d in dirs_to_clean:
        if os.path.exists(d):
            cleanup_files(d)
        else:
            print(f"Directory skipped (not found): {d}")
