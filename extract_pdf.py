import fitz  # PyMuPDF
doc = fitz.open('c:/Users/lenovo/Downloads/AIExplore26-main/AIExplore26-main/AI Explore.pdf')
for i, page in enumerate(doc):
    print(f"--- PAGE {i+1} ---")
    print(page.get_text())
