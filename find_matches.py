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

# Load the original CSV which has the raw corrupted strings
csv_data = []
with open('Hackathon participants final list.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    csv_data = list(reader)

mapping = {}

for ph in phones:
    best_match = None
    best_len = 0
    # Try to match against the CSV mobile column
    for row in csv_data:
        raw_csv_mobile = row["Candidate's Mobile"].strip()
        name = row["Candidate's Name"].strip()
        team_name = row["Team Name"].strip()
        
        # Determine the digits shown in CSV
        # If it's scientific like "9.186E+11", we can extract "86"
        # Let's just remove non-digits
        digits = "".join(c for c in raw_csv_mobile if c.isdigit())
        
        # Just manually slice and check
        if ph in raw_csv_mobile or raw_csv_mobile in ph:
            best_match = (row, raw_csv_mobile)
            best_len = len(raw_csv_mobile)
            break
            
        if "E+" in raw_csv_mobile or "e+" in raw_csv_mobile:
            # E.g. "9.19545E+11"
            # It starts with 9.1 usually. The real digits are after 9.1
            # E.g. raw = "9.19545E+11", after "9.1" it is "9545"
            prefix = raw_csv_mobile.split("E")[0].split("e")[0].replace("9.1", "").replace(".", "")
            if len(prefix) >= 3 and ph.startswith(prefix):
                if len(prefix) > best_len:
                    best_match = (row, raw_csv_mobile)
                    best_len = len(prefix)

    mapping[ph] = best_match

print("MATCHES:")
for ph, match in mapping.items():
    if match:
        row, raw_val = match
        print(f"{ph} => TEAM: {row['Team Name']}, NAME: {row['Candidate\\'s Name']}, RAW: {raw_val}")
    else:
        print(f"{ph} => NO MATCH")
