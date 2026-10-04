"""由 data/resources.json 與 src/template.html 產生 index.html（資料內嵌，可直接雙擊開啟），
並同步重產 README.md / README_EN.md 中 <!-- RESOURCES:START --> ... <!-- RESOURCES:END --> 之間的資源表與徽章筆數。
用法：python build.py
"""
import json
import re

# 分類順序與說明（新增分類時，請同步修改 src/template.html 內的 CH 陣列）
CATEGORIES = [
    ("Core Components", "核心元件", "搭站的骨架：React / Tailwind 元件庫與介面套件。",
     "The skeleton of a site: React / Tailwind component libraries and UI kits."),
    ("Animation & Effects", "動畫特效", "讓畫面有動勢：動畫庫、特效與微互動。",
     "Motion and effects: animation libraries, micro-interactions, CSS tricks."),
    ("Vibe Coding AI", "氛圍編程 AI", "與 AI 協作：提示詞、設計規範與風格參考。",
     "Working with AI: prompts, design specs and style references."),
    ("Inspiration Galleries", "靈感圖庫", "動手前先看：各類型網頁區塊的設計範例。",
     "Look before you build: design examples for every kind of web section."),
    ("Illustrations & 3D", "插圖與立體", "點睛素材：插圖、圖示與 3D icon。",
     "Finishing touches: illustrations, icons and 3D assets."),
]
TAG_ZH = {"Open Source": "開源", "Free": "免費", "Freemium": "部分免費"}

with open('data/resources.json', encoding='utf8') as f:
    data = json.load(f)


def table(cat, lang):
    head = "| # | 名稱 | 授權 | 說明 |\n|---|---|---|---|\n" if lang == "zh" else \
        "| # | Name | Licence | Description |\n|---|---|---|---|\n"
    rows = ""
    for x in data:
        if x['category'] != cat:
            continue
        tag = x.get('tag')
        tag = (TAG_ZH.get(tag, tag) if lang == "zh" else tag) if tag else ""
        rows += "| %d | [%s](%s) | %s | %s |\n" % (x['id'], x['name'], x['url'], tag, x[lang])
    return head + rows


def section(lang):
    out = ""
    for key, zh_name, blurb_zh, blurb_en in CATEGORIES:
        n = sum(1 for x in data if x['category'] == key)
        if lang == "zh":
            out += "\n### %s · %s（%d）\n\n%s\n\n%s" % (zh_name, key, n, blurb_zh, table(key, lang))
        else:
            out += "\n### %s (%d)\n\n%s\n\n%s" % (key, n, blurb_en, table(key, lang))
    return out


for readme, lang in (('README.md', 'zh'), ('README_EN.md', 'en')):
    with open(readme, encoding='utf8') as f:
        text = f.read()
    text = re.sub(r'<!-- RESOURCES:START -->.*?<!-- RESOURCES:END -->',
                  lambda m: '<!-- RESOURCES:START -->' + section(lang) + '<!-- RESOURCES:END -->',
                  text, flags=re.S)
    text = re.sub(r'Resources-\d+-blue', 'Resources-%d-blue' % len(data), text)
    text = re.sub(r'!\[Resources: \d+\]', '![Resources: %d]' % len(data), text)
    with open(readme, 'w', encoding='utf8', newline='\n') as f:
        f.write(text)

payload = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
with open('src/template.html', encoding='utf8') as f:
    html = f.read().replace('__DATA__', payload)
with open('index.html', 'w', encoding='utf8') as f:
    f.write(html)
print('built:', len(data), 'resources')
