"""由 data/resources.json 與 src/template.html 產生 index.html（資料內嵌，可直接雙擊開啟）。
用法：python build.py
"""
import json

with open('data/resources.json', encoding='utf8') as f:
    data = json.load(f)
payload = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
with open('src/template.html', encoding='utf8') as f:
    html = f.read().replace('__DATA__', payload)
with open('index.html', 'w', encoding='utf8') as f:
    f.write(html)
print('index.html built:', len(data), 'resources')
