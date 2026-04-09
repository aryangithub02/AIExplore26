with open('tracks.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("href='index.html#prizes')", "href='index.html#prizes'")
text = text.replace("href='index.html#schedule')", "href='index.html#schedule'")
text = text.replace("href='index.html#parallel-events')", "href='index.html#parallel-events'")
text = text.replace("href='index.html#venue')", "href='index.html#venue'")
text = text.replace("href='index.html#sponsors')", "href='index.html#sponsors'")
text = text.replace("href='index.html#management')", "href='index.html#management'")
text = text.replace("href='index.html#faq')", "href='index.html#faq'")

with open('tracks.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Fixed nav links in tracks.html")
