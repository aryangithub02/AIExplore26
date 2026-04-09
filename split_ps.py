import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Grab everything Before the landing page wrapper to use for tracks.html head and nav
# <div id="landing-view"> is around the start of the landing page.
head_match = re.search(r'^(.*?)<!-- ===================== LANDING PAGE ===================== -->', text, flags=re.DOTALL)
head_nav_code = head_match.group(1)

# In head_nav_code, I need to patch the links
# Mobile links
head_nav_code = head_nav_code.replace("smoothScrollTo('#problem-statements')", "window.location.href='tracks.html'")
head_nav_code = head_nav_code.replace("<span class=\"nav-link\" onclick=\"window.location.href='tracks.html'\">PS</span>", "<a class=\"nav-link\" href=\"tracks.html\">PS</a>")
# Navbar links
head_nav_code = head_nav_code.replace("onclick=\"\n          window.location.href='tracks.html';\n          toggleMobileMenu();\n        \"", 'onclick="window.location.href=\'tracks.html\'"')

# Let's fix the links so they point to index.html#id if we are not on index.html
tracks_head_nav_code = head_nav_code.replace("smoothScrollTo('#", "window.location.href='index.html#")

# 2. Extract Problem Statements Section
ps_pattern = r'(<!-- PROBLEM STATEMENTS -->\s*<section class="section" id="problem-statements">.*?</section>)'
ps_match = re.search(ps_pattern, text, flags=re.DOTALL)
ps_code = ps_match.group(1) if ps_match else ""

# 3. Extract Footer
footer_pattern = r'(<!-- ===================== FOOTER ===================== -->.*</html>)'
foot_match = re.search(footer_pattern, text, flags=re.DOTALL)
footer_code = foot_match.group(1) if foot_match else "</body></html>"

# Assemble tracks.html
tracks_html = tracks_head_nav_code + '\n<div style="padding-top: 100px;"></div>\n' + ps_code + '\n' + footer_code

with open('tracks.html', 'w', encoding='utf-8') as f:
    f.write(tracks_html)

# 4. Modify index.html
# Create the sleek teaser block
teaser_block = """<!-- PROBLEM STATEMENTS TEASER -->
    <section class="section" id="problem-statements">
      <div class="glow-blob glow-blob-purple" style="top: 10%; right: -50px;"></div>
      <div class="container">
        <div class="section-header">
          <div class="section-tag">// Themes & Tracks</div>
          <h2 class="section-title">Problem Statements</h2>
          <p class="section-desc">
            Explore 15 distinct real-world challenges waiting to be solved. View the full list or download the official PDF.
          </p>
        </div>
        
        <div style="display: flex; flex-direction: column; align-items: center; gap: 30px;">
          <!-- Action Buttons -->
          <div style="display: flex; gap: 16px; flex-wrap: wrap; justify-content: center;">
            <a href="tracks.html" class="btn btn-primary" style="padding: 14px 28px; font-size: 16px; text-decoration: none; display: inline-flex; align-items: center; justify-content: center;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right: 8px;">
                <circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line>
              </svg>
              View All 15 Tracks Detailed
            </a>
            <a href="AI Explore.pdf" target="_blank" class="btn btn-secondary" style="padding: 14px 28px; font-size: 16px; text-decoration: none;">
              Download Rulebook PDF
            </a>
          </div>
        </div>
      </div>
    </section>
"""

# Replace in index.html
new_index = text[:ps_match.start()] + teaser_block + text[ps_match.end():]
# Fix navigation in index.html too so it navigates to tracks.html
new_index = new_index.replace("smoothScrollTo('#problem-statements')", "window.location.href='tracks.html'")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_index)

print("Created tracks.html and updated index.html with teaser.")
