# Author: Stefania Verduga
# Module: Web Services and Applications
# 

import requests
from github import Github
from config import config as cfg

def replace_text_in_file(repo_name, file_path, old_text, new_text):
    # Authenticate with GitHub
    apikey = cfg["githubkey"]
    g = Github(apikey)
    
    # Get the repository
    repo = g.get_repo("StefaniaVerduga/WSAA-coursework")
    
    # Get the file content
    file_content = repo.get_contents(file_path)
    file_content_decoded = file_content.decoded_content.decode("utf-8")
    
    # Replace text
    new_content = file_content_decoded.replace(old_text, new_text)
    
    # Commit changes
    repo.update_file(file_path, "Updated text", new_content, file_content.sha)
    
    print(f"Text replaced successfully in file: {file_path}")

# Define your GitHub repository name and file path
repo_name = "WSAA-coursework"
file_path = "assignments/text-assignment4.txt"

# Text to replace
old_text = "Andrew"
new_text = "Stefania"

# Replace text and commit changes
replace_text_in_file(repo_name, file_path, old_text, new_text)
