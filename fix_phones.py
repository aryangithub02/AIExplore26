import csv, json, re

SCI_RE = re.compile(r'^\d+\.\d+[Ee][+\-]?\d+$')

# ── 1. Build phone lookup from CSV ──────────────────────────────────────────
phone_by_name  = {}
phone_by_email = {}

with open('Hackathon participants final list.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        name  = row["Candidate's Name"].strip().lower()
        email = row["Candidate's Email"].strip().lower()
        phone = row["Candidate's Mobile"].strip()

        # Phone in CSV might also be sci-notation — convert it
        if SCI_RE.match(phone):
            try:
                phone = str(int(float(phone)))
            except Exception:
                pass

        if name  and phone: phone_by_name[name]   = phone
        if email and phone: phone_by_email[email]  = phone

print(f"[*] Loaded {len(phone_by_name)} name lookups from CSV")

# ── 2. Load JSON ─────────────────────────────────────────────────────────────
with open('participants_master.json', encoding='utf-8') as f:
    teams = json.load(f)

# ── 3. Fix phones ─────────────────────────────────────────────────────────────
def fix(phone, name, email):
    raw = str(phone).strip()
    if not SCI_RE.match(raw):
        return raw   # already a plain number

    # Try CSV lookup (name → phone)
    found = phone_by_name.get(name.strip().lower())
    if found:
        return found

    # Try CSV lookup (email → phone)
    found = phone_by_email.get(email.strip().lower())
    if found:
        return found

    # Last resort: convert sci-notation mathematically
    try:
        n = str(int(float(raw)))
        # Drop leading country code '91' for 12-digit numbers
        if len(n) == 12 and n.startswith('91'):
            n = n[2:]
        return n
    except Exception:
        return raw   # give up, keep original

total_fixed = 0
for team in teams:
    for m in team.get('members', []):
        original  = m.get('phone', '')
        corrected = fix(original, m.get('name', ''), m.get('email', ''))
        if corrected != original:
            print(f"  FIXED [{team['name']}] {m['name']}: {original!r} → {corrected!r}")
            m['phone'] = corrected
            total_fixed += 1

# ── 4. Save JSON ──────────────────────────────────────────────────────────────
with open('participants_master.json', 'w', encoding='utf-8') as f:
    json.dump(teams, f, indent=4, ensure_ascii=False)

print(f"\n[✓] Fixed {total_fixed} phone numbers → participants_master.json saved")
