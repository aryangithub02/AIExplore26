import fitz
import re

doc = fitz.open('c:/Users/lenovo/Downloads/AIExplore26-main/AIExplore26-main/AI Explore.pdf')
ps_list = []

for i, page in enumerate(doc):
    text = page.get_text()
    if 'PS-ID: AX-' in text:
        ps_id_match = re.search(r'PS-ID:\s*(AX-\d+)', text)
        title_match = re.search(r'TITLE:\s*(.*?)(?:\nPROBLEM STATEMENT|$)', text, re.DOTALL)
        prob_match = re.search(r'PROBLEM STATEMENT\s*(.*?)(?:\nEXPECTED SOLUTION|$)', text, re.DOTALL)
        sol_match = re.search(r'EXPECTED SOLUTION\s*(.*?)(?:\nPresented By:|Terminal ID:|$)', text, re.DOTALL)
        
        ps_id = ps_id_match.group(1).strip() if ps_id_match else f"AX-{i}"
        title = title_match.group(1).strip().replace('\n', ' ') if title_match else "Unknown Title"
        prob = prob_match.group(1).strip().replace('\n', ' ') if prob_match else ""
        sol = sol_match.group(1).strip() if sol_match else ""
        
        title = title.replace("Next Slide", "").strip()
        ps_list.append((ps_id, title, prob, sol))

html = ["<style>",
".ps-hero-card { margin-bottom: 40px; padding: 40px; border-radius: 24px; background: rgba(28, 28, 28, 0.4); border: 1px solid rgba(255, 255, 255, 0.05); position: relative; overflow: hidden; backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); transition: transform 0.4s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.4s; }",
".ps-hero-card:hover { transform: translateY(-8px); box-shadow: 0 30px 60px rgba(0, 0, 0, 0.5); border-color: rgba(59, 130, 246, 0.3); background: rgba(35, 35, 35, 0.6); }",
".ps-hero-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, transparent, var(--blue), var(--pink), transparent); opacity: 0; transition: opacity 0.4s; }",
".ps-hero-card:hover::before { opacity: 1; }",
".ps-bg-text { position: absolute; top: -30px; right: 20px; font-family: var(--display); font-size: 180px; font-weight: 900; color: rgba(255, 255, 255, 0.02); pointer-events: none; user-select: none; z-index: 0; line-height: 1; transition: color 0.4s; }",
".ps-hero-card:hover .ps-bg-text { color: rgba(59, 130, 246, 0.04); }",
".ps-content { position: relative; z-index: 1; }",
".ps-header { display: flex; align-items: flex-start; flex-direction: column; margin-bottom: 32px; gap: 16px; }",
".ps-title { font-family: var(--display); font-size: clamp(28px, 4vw, 36px); font-weight: 800; line-height: 1.25; color: var(--text); }",
".ps-body { display: grid; grid-template-columns: 1fr; gap: 32px; }",
"@media (min-width: 1024px) { .ps-body { grid-template-columns: 1fr 1fr; gap: 48px; } }",
".ps-block { background: rgba(0, 0, 0, 0.25); padding: 32px; border-radius: 16px; border-left: 3px solid transparent; box-shadow: inset 0 0 20px rgba(0,0,0,0.2); }",
".ps-block-prob { border-left-color: var(--blue); }",
".ps-block-sol { border-left-color: var(--green); }",
".ps-block-title { font-size: 14px; text-transform: uppercase; letter-spacing: 2px; font-weight: 800; margin-bottom: 16px; display: flex; align-items: center; gap: 10px; }",
".ps-block-title-prob { color: var(--blue); }",
".ps-block-title-sol { color: var(--green); }",
".ps-text { font-size: 16px; color: var(--text2); line-height: 1.8; }",
".ps-meta-tags { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 24px; }",
".ps-meta-tag { font-family: var(--mono); font-size: 12px; color: var(--text3); background: rgba(255, 255, 255, 0.03); padding: 6px 12px; border-radius: 6px; border: 1px solid rgba(255, 255, 255, 0.05); }",
".ps-meta-tag:hover { color: var(--blue); border-color: var(--blue); }",
"@media (max-width: 768px) { .ps-hero-card { padding: 24px; } .ps-block { padding: 20px; } .ps-bg-text { font-size: 100px; right: 0px; top: 0px;} }",
"</style>",
"<div class=\"ps-list\" style=\"width: 100%; max-width: 1200px; margin-top: 60px;\">"]

for ps_id, title, prob, sol in ps_list:
    sol_str = ""
    if sol:
        points = [p.strip() for p in sol.split('•') if p.strip()]
        if len(points) == 1:
            points = [p.strip() for p in sol.split('\n') if p.strip()]
        
        if len(points) > 1:
            sol_str = "<ul style='padding-left: 20px; margin: 0; display: flex; flex-direction: column; gap: 12px;'>"
            for p in points:
                if 'Terminal ID' in p or 'Next Slide' in p: continue
                sol_str += f"<li style='margin-bottom: 4px;'>{p}</li>"
            sol_str += "</ul>"
        else:
            sol_str = f"<p style='margin: 0;'>{sol}</p>"

    prob_str = prob
    if "Next Slide" in prob_str: prob_str = prob_str.replace("Next Slide", "")

    card = f'''
          <!-- {ps_id} Full View -->
          <div class="ps-hero-card">
            <div class="ps-bg-text">{ps_id.replace("AX-", "")}</div>
            <div class="ps-content">
              <div class="ps-header">
                <div>
                  <span class="badge badge-info" style="font-family: var(--mono); background: rgba(59, 130, 246, 0.1); color: var(--blue); padding: 8px 18px; border-radius: 30px; font-size: 15px; font-weight: 700; letter-spacing: 1px; display: inline-block; border: 1px solid rgba(59,130,246,0.3); box-shadow: 0 0 20px rgba(59,130,246,0.2);">PS-ID: {ps_id}</span>
                </div>
                <h3 class="ps-title">{title}</h3>
              </div>
              
              <div class="ps-body">
                <!-- Problem Half -->
                <div class="ps-block ps-block-prob">
                  <div class="ps-block-title ps-block-title-prob">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
                    The Challenge
                  </div>
                  <div class="ps-text">{prob_str}</div>
                  
                  <div class="ps-meta-tags">
                    <span class="ps-meta-tag">TRACK-{ps_id.replace("AX-", "")}</span>
                    <span class="ps-meta-tag">INNOVATION</span>
                    <span class="ps-meta-tag">AIXPLORE</span>
                  </div>
                </div>

                <!-- Solution Half -->
                <div class="ps-block ps-block-sol">
                  <div class="ps-block-title ps-block-title-sol">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                    Expected Deliverables
                  </div>
                  <div class="ps-text">{sol_str}</div>
                </div>
              </div>
            </div>
          </div>'''
    html.append(card)

html.append("</div>")

with open("ps_html_v2.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(html))
print(f"Generated {len(ps_list)} lengthy problem statements.")
