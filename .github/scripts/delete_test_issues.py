#!/usr/bin/env python3
import os
from github import Github

# Initialize GitHub client
g = Github(os.environ['GITHUB_TOKEN'])
repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])

# Get all open issues with reminder labels
issues = repo.get_issues(state='open', labels=['reminder'])

# Delete each test issue
for issue in issues:
    print(f"Deleting issue: {issue.title}")
    issue.edit(state='closed')
    print(f"Closed issue: {issue.title}") 