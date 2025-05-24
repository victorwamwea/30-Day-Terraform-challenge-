# Check-in Management Guide

## Overview
This guide explains how to manage weekly check-ins and mark attendance for the 30-Day Terraform Challenge participants.

## Check-in Schedule
- Every Friday at 6:00 PM EAT
- Dates:
  - May 30, 2025
  - June 6, 2025
  - June 13, 2025
  - June 20, 2025

## How to Mark Attendance

### 1. During the Check-in Meeting
- Take note of all participants present
- Record any notable discussions or questions
- Note any exceptional contributions or help provided by participants

### 2. Creating Attendance Records
For each participant present, create an issue with:

```bash
Title format: check-in YYYY-MM-DD username
Example: check-in 2025-05-30 johndoe
```

Required elements:
- Label: `check-in`
- Title must contain:
  - The exact date in YYYY-MM-DD format
  - The participant's GitHub username
  - The words "check-in" at the start

### 3. Bulk Creation Script
For efficiency, you can use this script to create attendance issues for multiple participants:

```bash
#!/bin/bash
DATE="2025-05-30"  # Update for each check-in
PARTICIPANTS=(
  "username1"
  "username2"
  "username3"
)

for participant in "${PARTICIPANTS[@]}"; do
  gh issue create \
    --title "check-in $DATE $participant" \
    --label "check-in" \
    --body "Attended weekly check-in session on $DATE at 6:00 PM EAT"
done
```

### 4. Points System
- Each confirmed attendance: 5 points
- Points are automatically added to the participant's total
- Points are reflected in the leaderboard
- Perfect attendance (all 4 sessions): Special recognition

## Verification
- The leaderboard script automatically verifies attendance by checking:
  - Issue exists with correct format
  - Issue was created by repo owner
  - Issue has 'check-in' label
  - Date matches a scheduled check-in date

## Best Practices
1. Create attendance issues immediately after the check-in
2. Use consistent naming format
3. Don't modify issue titles after creation
4. Don't delete check-in issues
5. Verify leaderboard updates correctly

## Troubleshooting
If points aren't being awarded correctly, verify:
1. Issue title format is exact
2. Issue has 'check-in' label
3. You (repo owner) created the issue
4. Date in title matches scheduled check-in date

## Support
If you encounter any issues with the check-in system:
1. Check the GitHub Actions logs
2. Verify the issue format
3. Create a bug report if needed 