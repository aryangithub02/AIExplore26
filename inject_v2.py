import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

with open('ps_html_v2.txt', 'r', encoding='utf-8') as f:
    ps_html = f.read()

# Pattern to find the current <style> .ps-card ... and the <div class="ps-grid"... up to the closing tags at the end of the section
pattern = r'<style>\s*\.ps-card:hover.*?</div>\s*</div>\s*</section>'
match = re.search(pattern, text, flags=re.DOTALL)

if match:
    # Instead of deleting from <style> to </section>, we just replace the inner part
    # Actually wait! If we do pattern down to </section>, we will delete </section>. Let's keep the end
    end_part = "\n        </div>\n      </div>\n    </section>"
    new_text = text[:match.start()] + ps_html + end_part + text[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Success: Replaced grid with detailed V2 list.")
else:
    print("Error: Could not find the pattern in index.html to replace. (Maybe missing <style> .ps-card?)")
