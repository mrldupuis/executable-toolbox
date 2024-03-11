import os

old_text = input("Enter old text to replace: ")
new_text = input("Enter new text: ")

def rename_files_recursive(old_text, new_text):
    """
    Recursively renames files in all subdirectories of the cwd by replacing
    occurrences of old_text with new_text in their filenames.
    
    Parameters:
    old_text (str): The text to be replaced in the filenames.
    new_text (str): The text to replace old_text with in the filenames.
    """
    for dirpath, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            if old_text in filename:
                full_path = os.path.join(dirpath, filename)
                new_filename = filename.replace(old_text, new_text)
                new_full_path = os.path.join(dirpath, new_filename)
                os.rename(full_path, new_full_path)
                print(f"Renamed '{full_path}' to '{new_full_path}'")

rename_files_recursive(old_text, new_text)

