#This file is for generating the _sidebar.MD
import os

# Get the current directory
current_dir = os.getcwd()

# List all files in the current directory
files = os.listdir(current_dir)

# Filter out only the markdown files
md_files = [file for file in files if file.endswith('.md')]

# Write the names of the markdown files
with open('_sidebar.md', 'w') as sidebar_file:
    sidebar_file.write("- [Home Page](/)\n")
    for md_file in md_files:
        if md_file != "readme.md" and md_file != '_sidebar.md':
            sidebar_file.write("- [" + md_file.replace('-', ' ').replace('.md', '') + "](/" + md_file +")\n")
