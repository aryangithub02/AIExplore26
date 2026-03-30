import json
import csv

verified_phones_raw = """
95453 00989
8600487598
7263842962
8237833808
7387394801
8010945450
7768820280
8767859749
9359211306
9322893263
8087789959
9860767429
9307113617
9322767525
8080595054
8605468557
9529721212
8329423722
9096560097
9322154832
"""

phones = [p.replace(" ", "").strip() for p in verified_phones_raw.strip().split("\n") if p.strip()]

def get_possible_corruptions(ph):
    res = set()
    res.add(ph)
    res.add("91" + ph)
    
    # 9.1...E+11 form -> 91 + digits + zeroes
    # e.g. 9195453000000 -> here we look at prefix
    return res

with open("participants_master.json", "r", encoding="utf-8") as f:
    teams = json.load(f)

matched_phones = set()
matched_teams = set()

for team in teams:
    for m in team.get("members", []):
        curr = m.get("phone", "")
        
        # Determine if 'curr' matches any valid phone
        for ph in phones:
            # Check exact matches
            if curr == ph or curr == "91" + ph:
                m["phone"] = ph
                team["status"] = "Verified"
                matched_phones.add(ph)
                matched_teams.add(team["id"])
                break
                
            # Check prefix matches for corrupted numbers
            if curr.endswith("0000") or curr.endswith("00000"):
                # E.g. 9195453000000 or 9545300000
                core = curr.rstrip("0")
                if len(core) >= 4:
                    if ph.startswith(core) or ("91"+ph).startswith(core):
                        m["phone"] = ph
                        team["status"] = "Verified"
                        matched_phones.add(ph)
                        matched_teams.add(team["id"])
                        break

unmatched = set(phones) - matched_phones
print(f"Matched {len(matched_phones)} phone numbers and marked {len(matched_teams)} teams as Verified.")
print(f"Unmatched: {unmatched}")

# Save JSON
with open("participants_master.json", "w", encoding="utf-8") as f:
    json.dump(teams, f, indent=4)

# CSV writing (copied from server.py to avoid dependencies)
def save_csv(teams):
    headers = [
        "Team ID", "Team Name", "Candidate's Name", "Candidate's Email", 
        "Candidate's Mobile", "Candidate's Location", "User Type", "Domain", 
        "Course", "Course Specialization", "Course Type", "Course Duration (years)", 
        "Year of Graduation", "Candidate's Organisation", "Differently Abled", 
        "Status", "Candidate's Report", "Report Link", "Round 1 Score"
    ]
    
    rows = []
    for t in teams:
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
                "Round 1 Score": t.get('score', 0)
            })
            
    try:
        with open('Hackathon participants final list.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)
        print("[*] Successfully synchronized Hackathon participants final list.csv")
    except Exception as e:
        print(f"[!] CSV Sync Error: {e}")

save_csv(teams)
