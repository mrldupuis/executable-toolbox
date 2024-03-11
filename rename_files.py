import os

old_text = input("Enter old text to replace: ")
new_text = input("Enter new text: ")

def rename_files(old_text, new_text):
    """
    Renames all files in the current working directory by replacing occurrences
    of old_text with new_text in their filenames.
    
    Parameters:
    old_text (str): The text to be replaced in the filenames.
    new_text (str): The text to replace old_text with in the filenames.
    """
    # Get a list of files and directories in the current working directory
    for item in os.listdir():
        # Check if the item is a file and if old_text is in its name
        if os.path.isfile(item) and old_text in item:
            # Construct the new filename by replacing old_text with new_text
            new_filename = item.replace(old_text, new_text)
            # Rename the file
            os.rename(item, new_filename)
            print(f"Renamed '{item}' to '{new_filename}'")

rename_files(old_text, new_text)

