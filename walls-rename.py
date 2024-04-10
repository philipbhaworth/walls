#!/usr/bin/env python3

import os

# Sets the directory_path to the current directory where the script is located
directory_path = os.path.dirname(os.path.realpath(__file__))

# List of files and directories to ignore
ignore_list = ['.git', '.gitignore', 'README.md', 'walls-rename.py']

def rename_files_in_directory(directory_path):
    # Iterate over each item in the directory
    for item_name in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item_name)
        # Check and skip the items in the ignore list
        if item_name in ignore_list:
            continue  # Skip the current iteration and proceed with the next item
        
        # Also check and skip specific folders like "system" and "scripts"
        if os.path.isdir(item_path) and item_name not in ["system", "scripts"]:
            # List files and sort them to maintain a sequential order
            files = sorted(os.listdir(item_path), key=lambda x: x.lower())
            current_count = 1  # Initialize counter for each folder
            
            for file_name in files:
                file_path = os.path.join(item_path, file_name)
                # Check if it's a file to avoid renaming subdirectories and if it's not in the ignore list
                if os.path.isfile(file_path) and file_name not in ignore_list:
                    # Extract file extension
                    file_extension = os.path.splitext(file_name)[1]
                    # New file name: folder name + counter + file extension
                    new_file_name = f"{item_name}-{current_count}{file_extension}"
                    new_file_path = os.path.join(item_path, new_file_name)
                    # Rename the file
                    os.rename(file_path, new_file_path)
                    current_count += 1  # Increment counter after each file is renamed

# Execute the function
rename_files_in_directory(directory_path)
