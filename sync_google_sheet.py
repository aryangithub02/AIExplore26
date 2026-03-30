import json
import csv
import urllib.request
import io
import re

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

# Extract exactly the last 10 digits as the core phone number
def get_clean_phone(p):
    nums = re.sub(r'\D', '', p)
    return nums[-10:] if len(nums) >= 10 else nums

phones = {get_clean_phone(p) for p in verified_phones_raw.strip().split("\n") if p.strip()}

url = 'https://docs.google.com/spreadsheets/d/1Ia9yYL4e-IlfU3H4N-SdyqCA0bDpZ35lO_JC_UE4aXk/export?format=csv'

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    csv_bytes = response.read()

csv_text = csv_bytes.decode('utf-8')
reader = csv.DictReader(io.StringIO(csv_text))
sheet_rows = list(reader)

email_phone_map = {}
for r in sheet_rows:
    email = r.get("Candidate's Email", "").strip().lower()
    phone = r.get("Candidate's Mobile", "").strip()
    if email and phone:
        email_phone_map[email] = get_clean_phone(phone)

with open('participants_master.json', 'r', encoding='utf-8') as f:
    teams = json.load(f)

verified_count = 0

for t in teams:
    team_verified = False
    
    for m in t.get('members', []):
        email = m.get('email', '').strip().lower()
        if email in email_phone_map:
            m['phone'] = email_phone_map[email]
            
            # Check if this member's core phone is in the verified list
            # It might be that the leader in JSON is not the leader in the verified numbers list.
            if email_phone_map[email] in phones:
                team_verified = True
    
    if team_verified:
        t['status'] = 'Verified'
        verified_count += 1
    else:
        t['status'] = 'In-progress'  # Reset just in case to undo previous errors

with open('participants_master.json', 'w', encoding='utf-8') as f:
    json.dump(teams, f, indent=4)

print(f"Marked {verified_count} teams as Verified using robust matched numbers.")

import update_csv  # To generate the newest CSV with the 'Verified or not' column
