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
        
        # fix title
        title = title.replace("Next Slide", "").strip()
        
        ps_list.append((ps_id, title, prob, sol))

html = ["<style>",
".ps-card:hover { transform: translateY(-5px); border-color: var(--blue); box-shadow: 0 10px 30px rgba(0,0,0,0.4); }",
".ps-card p { display: block; }",
"</style>",
"<div class=\"ps-grid\" style=\"display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; width: 100%; max-width: 1200px; margin-top: 40px;\">"]

for ps_id, title, prob, sol in ps_list:
    # convert newlines in sol to proper li/br or text
    sol_str = ""
    if sol:
        # If it looks like bullet points, make them bullet points. In our previous extract it had newlines for bullet points
        points = [p.strip() for p in sol.split('•') if p.strip()]
        if len(points) == 1:
            points = [p.strip() for p in sol.split('\n') if p.strip()]
        
        if len(points) > 1:
            sol_str = "<ul style='padding-left: 20px; margin: 0;'>"
            for p in points:
                if 'Terminal ID' in p or 'Next Slide' in p: continue
                sol_str += f"<li style='margin-bottom: 6px;'>{p}</li>"
            sol_str += "</ul>"
        else:
            sol_str = sol

    prob_str = prob
    if "Next Slide" in prob_str: prob_str = prob_str.replace("Next Slide", "")

    card = f'''
          <!-- {ps_id} Card -->
          <div class="ps-card" style="background: rgba(28, 28, 28, 0.6); border: 1px solid var(--border); border-radius: 16px; padding: 24px; transition: all 0.3s; position: relative; overflow: hidden; backdrop-filter: blur(10px);">
            <div style="position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: linear-gradient(to bottom, var(--blue), var(--pink));"></div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px;">
              <span class="badge badge-info" style="font-family: var(--mono); background: rgba(59, 130, 246, 0.15); color: var(--blue); padding: 4px 10px; border-radius: 20px; font-size: 13px; font-weight: 600;">{ps_id}</span>
            </div>
            <h3 style="font-family: var(--display); font-size: 20px; font-weight: 700; margin-bottom: 16px; color: var(--text); line-height: 1.3;">{title}</h3>
            
            <div class="ps-section" style="margin-bottom: 16px;">
              <div style="font-size: 12px; color: var(--blue); text-transform: uppercase; letter-spacing: 1px; font-weight: 700; margin-bottom: 8px; display: flex; align-items: center; gap: 6px;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
                Problem Statement
              </div>
              <p style="font-size: 14px; color: var(--text2); line-height: 1.6; margin: 0;">{prob_str}</p>
            </div>

            <div class="ps-section">
              <div style="font-size: 12px; color: var(--green); text-transform: uppercase; letter-spacing: 1px; font-weight: 700; margin-bottom: 8px; display: flex; align-items: center; gap: 6px;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                Expected Solution
              </div>
              <div style="font-size: 14px; color: var(--text3); line-height: 1.6;">{sol_str}</div>
            </div>
          </div>'''
    html.append(card)

html.append("</div>")

with open("ps_html.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(html))
print(f"Generated {len(ps_list)} problem statements.")
