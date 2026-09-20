# 30 Best Free Dev & Design Resources - Vibe Coding Vault

> 終極氛圍編程寶庫 | 30 個免費開源的開發與設計資源，中英對照，可一鍵部署到 GitHub Pages

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Resources: 30](https://img.shields.io/badge/Resources-30-blue)
![Free: 100%](https://img.shields.io/badge/Free-100%25-green)

這個專案源自一張爆紅的資源清單截圖，我把它整理成 **可搜尋、可點擊、中英對照** 的 Notion 風格儀表板，並打包成可直接上傳到 GitHub 的結構。

**線上預覽:** 啟用 GitHub Pages 後，`index.html` 就是你的網站。

## ✨ 特色
- Notion 風格 UI，乾淨極簡
- 5 大分類 + 即時搜尋
- 中文 / 中英對照切換
- 全部 30 個資源皆可點擊，`target="_blank"`
- 純靜態，無需後端，GitHub Pages 一鍵部署

## 📂 專案結構
```
.
├── index.html          # Notion 風格互動儀表板 (GitHub Pages 入口)
├── data/
│   └── resources.json  # 30 筆資源的結構化資料
├── README.md           # 中文說明 (本檔)
├── README_EN.md        # English version
├── LICENSE             # MIT
└── .gitignore
```

## 🚀 快速上傳到 GitHub
```bash
# 1. 建立新 repo (在 GitHub 網頁先建一個空 repo)
git init
git add .
git commit -m "feat: add 30 free dev & design resources vault"
git branch -M main
git remote add origin https://github.com/<你的帳號>/vibe-coding-vault.git
git push -u origin main

# 2. 開啟 GitHub Pages
# 到 GitHub repo > Settings > Pages > Source 選 main branch / root
# 網址就會是 https://<你的帳號>.github.io/vibe-coding-vault/
```

## 📚 資源清單

### Core Components 核心元件 (8)
| # | 名稱 | 網址 | 中文說明 |
|---|---|---|---|
| 1 | Scrolltide | https://scrolltide.co | 終極氛圍編程寶庫，600+ 模板 |
| 2 | Aceternity UI | https://ui.aceternity.com | 超炫動畫 React 元件 |
| 3 | Magic UI | https://magicui.design | 高轉換率行銷動畫元件 |
| 12 | shadcn/ui | https://ui.shadcn.com | 黃金標準框架 |
| 13 | Uiverse | https://uiverse.io | 數千開源 UI 元素 |
| 14 | UIAble | https://uiable.com | 擴展 shadcn 的 React 庫 |
| 15 | mapcn | https://mapcn.dev | React 地圖元件 |
| 4 | Motion Primitives | https://motion-primitives.com | 進階 UI 互動元件 |

### Animation & Effects 動畫特效 (8)
| # | 名稱 | 網址 | 中文說明 |
|---|---|---|---|
| 5 | OpenMotion | https://openmotion.design | AI 產品演示動畫 |
| 6 | Kinetics | https://kinetics.colorion.co | 150+ 動畫效果 |
| 23 | Liquid Glass | https://glass.samasante.com | 玻璃折射效果 |
| 24 | MicroKit UI | https://microkit.co | 微互動 |
| 25 | CSS Text Effects | https://text-effects.colorion.co | 動畫文字 |
| 26 | Circle Loaders | https://circleloaders.dominikakiss.com | 圓形載入器 |
| 27 | Gradient Buttons | https://gradientbuttons.colorion.co | 漸層按鈕 |
| 30 | Anime.js | https://animejs.com | 輕量動畫庫 |

### Vibe Coding AI (5)
| # | 名稱 | 網址 |
|---|---|---|
| 7 | 21st.dev | https://21st.dev |
| 8 | DESIGNmd | https://designmd.ai |
| 9 | VibePrompt | https://vibeprompts.dev |
| 10 | Refero Styles | https://styles.refero.design |
| 11 | Kage | https://kage.design |

### Inspiration Galleries 靈感圖庫 (7)
Component Gallery, Minimal Gallery, AppShot Gallery, Navbar Gallery, Footer Design, CTA Gallery, 404s

### Illustrations & 3D 插圖 (2)
Kitbitz (kitbitz.art), 3Dicons (3dicons.co)

完整 30 筆請看 `data/resources.json` 或直接開 `index.html`

## 📝 License
MIT - 可商用，可自由分享

## 🙏 Credit
原始清單來自 X / Threads 上 @Himanshu 的整理，重新整理為開源格式。
