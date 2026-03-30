import json
with open('participants_master.json', 'r', encoding='utf-8') as f:
    teams = json.load(f)

for t in teams:
    if t.get('status') == 'Verified':
        t['status'] = 'In-progress' # Revert to proper status
        t['isVerified'] = True
    else:
        # Keep existing status (Complete/In-progress)
        if 'isVerified' not in t:
            t['isVerified'] = False # Default

with open('participants_master.json', 'w', encoding='utf-8') as f:
    json.dump(teams, f, indent=4)
print("Separated status and verified in JSON.")
