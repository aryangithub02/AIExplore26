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

with open('Hackathon participants final list.csv', newline='', encoding='utf-8') as f:
    csv_data = list(csv.DictReader(f))

# Find the best match for each phone in the CSV based on prefix
matched_teams_set = set() # Store team names that matched

for ph in phones:
    best_match = None
    best_len = 0
    # Try all rows to find the one where the phone prefix matches
    for row in csv_data:
        raw_csv_mobile = row["Candidate's Mobile"].strip()
        
        # If it's a direct substring match
        if ph in raw_csv_mobile or raw_csv_mobile in ph:
            best_match = row
            best_len = 10
            break
            
        # If the number in CSV is scientific like 9.186E+11, the core digits are "86"
        if "E+" in raw_csv_mobile or "e+" in raw_csv_mobile:
            prefix = raw_csv_mobile.split("E")[0].split("e")[0].replace("9.1", "").replace(".", "")
            if len(prefix) >= 3 and ph.startswith(prefix):
                if len(prefix) > best_len:
                    best_match = row
                    best_len = len(prefix)
                    
    if best_match:
        matched_teams_set.add(best_match["Team Name"])

# Now update JSON using the exact matched team names
with open("participants_master.json", "r", encoding="utf-8") as f:
    teams = json.load(f)

for t in teams:
    if t["name"] in matched_teams_set:
        t["status"] = "Verified"

with open("participants_master.json", "w", encoding="utf-8") as f:
    json.dump(teams, f, indent=4)

print(f"Updated {len(matched_teams_set)} teams to Verified status.")
