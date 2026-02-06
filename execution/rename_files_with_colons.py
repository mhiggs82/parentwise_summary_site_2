import os
import shutil

def rename_files_with_colons(directory):
    """
    Renames files in the given directory (and subdirectories) that contain colons.
    Replaces ': ' with ' - ' and ':' with '-'.
    """
    print(f"Scanning {directory} for files with colons...")
    count = 0
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if ':' in filename:
                old_path = os.path.join(root, filename)
                
                # Replace ': ' with ' - ' first to handle subtitles nicely
                new_filename = filename.replace(': ', ' - ')
                # Replace any remaining ':' with '-'
                new_filename = new_filename.replace(':', '-')
                
                new_path = os.path.join(root, new_filename)
                
                # Rename the file
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {filename} -> {new_filename}")
                    count += 1
                except Exception as e:
                    print(f"Error renaming {filename}: {e}")
    
    print(f"Renaming complete. {count} files renamed.")

if __name__ == "__main__":
    # Define directories to scan
    base_dir = os.getcwd()
    json_dir = os.path.join(base_dir, "website/static/data/books")
    docs_dir = os.path.join(base_dir, "website/docs") # Also check generated docs just in case, though we will regenerate them.

    if os.path.exists(json_dir):
        rename_files_with_colons(json_dir)
    else:
        print(f"Directory not found: {json_dir}")

    # We don't strictly need to rename docs recursively if we are going to regenerate them, 
    # but it cleans up any manual artifacts or things tracked in git.
    if os.path.exists(docs_dir):
        rename_files_with_colons(docs_dir)
