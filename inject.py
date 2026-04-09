import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

with open('ps_html.txt', 'r', encoding='utf-8') as f:
    ps_html = f.read()

pattern = r'<!-- PDF Embed Container -->.*?</div>(?=\s*</div>\s*</div>\s*</section>)'
match = re.search(pattern, text, flags=re.DOTALL)
if match:
    new_text = text[:match.start()] + ps_html + text[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Success: Replaced PDF Embed Container with Problem Statements Grid.")
else:
    print("Error: Could not find the pattern in index.html")
