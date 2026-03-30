import json
import csv

with open("participants_master.json", "r", encoding="utf-8") as f:
    teams = json.load(f)

headers = [
    "Team ID", "Team Name", "Candidate's Name", "Candidate's Email", 
    "Candidate's Mobile", "Candidate's Location", "User Type", "Domain", 
    "Course", "Course Specialization", "Course Type", "Course Duration (years)", 
    "Year of Graduation", "Candidate's Organisation", "Differently Abled", 
    "Status", "Candidate's Report", "Report Link", "Round 1 Score", "Verified or not"
]

rows = []
for t in teams:
    # Separate members: Leader first, then others
    sorted_members = sorted(t.get('members', []), key=lambda x: not x.get('isLeader', False))
    for m in sorted_members:
        rows.append({
            "Team ID": t.get('id', ''),
            "Team Name": t.get('name', ''),
            "Candidate's Name": m.get('name', ''),
            "Candidate's Email": m.get('email', ''),
            "Candidate's Mobile": m.get('phone', ''),
            "Candidate's Location": m.get('address', ''),
            "User Type": "Team Leader" if m.get('isLeader') else "Team Member",
            "Domain": "General",
            "Course": m.get('college', ''),
            "Course Specialization": m.get('dept', ''),
            "Course Type": "Technical",
            "Course Duration (years)": 4,
            "Year of Graduation": m.get('gradYear', ''),
            "Candidate's Organisation": m.get('college', ''),
            "Differently Abled": "No",
            "Status": t.get('status', 'In-progress'),
            "Candidate's Report": "Pending",
            "Report Link": "-",
            "Round 1 Score": t.get('score', 0),
            "Verified or not": "Yes" if t.get('status') == 'Verified' else "No"
        })
        
try:
    with open('Hackathon participants final list.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    print("Successfully generated Hackathon participants final list.csv with Verified column")
except Exception as e:
    print(f"Error: {e}")
