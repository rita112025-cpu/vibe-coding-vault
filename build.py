"""由 data/resources.json 與 src/template.html 產生 index.html（資料內嵌，可直接雙擊開啟），
並同步重產 README.md / README_EN.md 中 <!-- RESOURCES:START --> ... <!-- RESOURCES:END --> 之間的資源表與徽章筆數。
分類與授權標籤只在本檔定義，建置時注入頁面。
用法：python build.py
"""
import json
import re
import sys

# 分類（順序即頁面章節順序）
#   key：對應 resources.json 的 category
#   zh：章名　nav：左側導覽短名（兩字）　tone：徽記色 g 青 / r 朱 / i 墨
#   blurb：頁面章節題詞　readme_zh / readme_en：README 分類說明
CATEGORIES = [
    {"key": "Core Components", "zh": "核心元件", "nav": "元件", "tone": "g",
     "blurb": "骨架先立。元件庫是起手式，擇一而深用之。",
     "readme_zh": "搭站的骨架：React / Tailwind 元件庫與介面套件。",
     "readme_en": "The skeleton of a site: React / Tailwind component libraries and UI kits."},
    {"key": "Animation & Effects", "zh": "動畫特效", "nav": "動效", "tone": "r",
     "blurb": "皮肉見神。一點動勢，便有生氣。",
     "readme_zh": "讓畫面有動勢：動畫庫、特效與微互動。",
     "readme_en": "Motion and effects: animation libraries, micro-interactions, CSS tricks."},
    {"key": "Vibe Coding AI", "zh": "氛圍編程 AI", "nav": "助筆", "tone": "i",
     "blurb": "以言語作畫。提示、規範與風格，交給機器落筆。",
     "readme_zh": "與 AI 協作：提示詞、設計規範與風格參考。",
     "readme_en": "Working with AI: prompts, design specs and style references."},
    {"key": "Inspiration Galleries", "zh": "靈感圖庫", "nav": "圖庫", "tone": "g",
     "blurb": "眼要先見過。先逛一圈，再動手。",
     "readme_zh": "動手前先看：各類型網頁區塊的設計範例。",
     "readme_en": "Look before you build: design examples for every kind of web section."},
    {"key": "Illustrations & 3D", "zh": "插圖與立體", "nav": "插圖", "tone": "r",
     "blurb": "點睛之處。圖標與立體素材，補上最後一筆。",
     "readme_zh": "點睛素材：插圖、圖示與 3D icon。",
     "readme_en": "Finishing touches: illustrations, icons and 3D assets."},
]
# 授權標籤：英文鍵（resources.json 的 tag）→ 中文顯示
TAGS = {"Open Source": "開源", "Free": "免費", "Freemium": "部分免費"}

with open('data/resources.json', encoding='utf8') as f:
    data = json.load(f)

keys = {c["key"] for c in CATEGORIES}
errors = ["#%s %s：未知分類 %r" % (x['id'], x['name'], x['category']) for x in data if x['category'] not in keys]
errors += ["#%s %s：未知標籤 %r" % (x['id'], x['name'], x['tag']) for x in data if x.get('tag') and x['tag'] not in TAGS]
if errors:
    sys.exit("resources.json 有誤，請在 build.py 補上定義或修正資料：\n" + "\n".join(errors))


def table(cat, lang):
    head = "| # | 名稱 | 授權 | 說明 |\n|---|---|---|---|\n" if lang == "zh" else \
        "| # | Name | Licence | Description |\n|---|---|---|---|\n"
    rows = ""
    for x in data:
        if x['category'] != cat:
            continue
        tag = x.get('tag')
        tag = (TAGS[tag] if lang == "zh" else tag) if tag else ""
        rows += "| %d | [%s](%s) | %s | %s |\n" % (x['id'], x['name'], x['url'], tag, x[lang])
    return head + rows


def section(lang):
    out = ""
    for c in CATEGORIES:
        n = sum(1 for x in data if x['category'] == c["key"])
        if lang == "zh":
            out += "\n### %s · %s（%d）\n\n%s\n\n%s" % (c["zh"], c["key"], n, c["readme_zh"], table(c["key"], lang))
        else:
            out += "\n### %s (%d)\n\n%s\n\n%s" % (c["key"], n, c["readme_en"], table(c["key"], lang))
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


def embed(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')


config = {"categories": [{k: c[k] for k in ("key", "zh", "nav", "tone", "blurb")} for c in CATEGORIES],
          "tags": TAGS}
with open('src/template.html', encoding='utf8') as f:
    html = f.read().replace('__DATA__', embed(data)).replace('__CONFIG__', embed(config))
with open('index.html', 'w', encoding='utf8') as f:
    f.write(html)
print('built:', len(data), 'resources,', len(CATEGORIES), 'categories')
