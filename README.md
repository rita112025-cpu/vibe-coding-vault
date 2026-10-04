# 氛圍寶庫 · Vibe Coding Vault

> 精選免費、開源與可免費試用的開發與設計資源，收進一卷宣紙水墨風的網頁裡。中英對照、可搜尋、可切換亮色／暗色。

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Resources: 48](https://img.shields.io/badge/Resources-48-blue)
![Static Site](https://img.shields.io/badge/Static-No%20Backend-green)

**English:** [README_EN.md](README_EN.md)

## 這是什麼

做網站、做 Demo、做 Vibe Coding 的時候，常常不知道去哪裡找元件、動效和靈感。這個專案把網路上流傳的一份「30 個免費資源」清單（並持續擴充），整理成一個可以搜尋、可以點擊、附預覽圖的小型資源館。

整個網站是**純靜態**的：一個 `index.html`、一份 JSON 資料、一些預覽圖，沒有後端、沒有框架依賴，丟到 GitHub Pages 就能運作。

## 特色

- **宣紙水墨介面**：米色紙張底、朱紅點綴、直排卷軸導覽與隨捲動延伸的進度線，分類以「壹、貳、參…」章節呈現。
- **亮色 / 暗色切換**：左側卷軸底部按鈕切換；記住你的選擇，第一次進站則跟隨系統設定。
- **預覽圖**：每個資源附網站預覽圖與授權標籤（開源 / 免費 / 部分免費）（取自各站公開的社群分享圖），預設帶一點紙色調，滑過才還原。
- **即時搜尋與分類篩選**：名稱、中英文說明、分類都能搜。
- **三種語言顯示**：中文 → 中英對照 → English 循環切換。
- **響應式**：手機寬度下，左側卷軸自動變成頂部橫列導覽。
- **無障礙**：鍵盤可操作、可見的焦點框、支援 `prefers-reduced-motion`。

## 專案結構

```
.
├── index.html              # 建置產物（資料已內嵌，可直接雙擊開啟）
├── src/template.html       # 頁面原始碼（HTML + CSS + JS）
├── data/resources.json     # 資源資料（唯一資料來源）
├── assets/previews/        # 預覽圖（webp，寬 800px）
├── build.py                # 把 JSON 內嵌進模板，產生 index.html
├── README.md
├── README_EN.md
└── LICENSE
```

## 資料格式

`data/resources.json` 是一個陣列，每筆資源如下：

```json
{
  "id": 1,
  "name": "Scrolltide",
  "url": "https://scrolltide.co",
  "category": "Core Components",
  "zh": "終極氛圍編程寶庫，600+ 3D、動畫、波動敘事網頁模板",
  "en": "Ultimate vibe coding vault with 600+ 3D, animation, storytelling templates",
  "image": "assets/previews/01.webp"
}
```

`image` 為 `null` 時，頁面會自動生成一張水墨山景當占位圖。

## 如何修改與新增資源

1. 在 `data/resources.json` 新增或修改一筆資料。
2. 預覽圖放進 `assets/previews/`，並填入 `image` 路徑（建議 800px 寬、約 1.9:1 的 webp）。
3. 執行建置：

```bash
python build.py
```

4. 開啟 `index.html` 確認結果。

> 分類目前固定為 5 類（見 `src/template.html` 內的 `CH` 陣列）。要新增分類，請同步修改該陣列。

## 部署到 GitHub Pages

1. 把專案推上 GitHub。
2. 到 repo 的 **Settings → Pages**，Source 選 `main` 分支、根目錄 `/`。
3. 網址會是 `https://<你的帳號>.github.io/vibe-coding-vault/`。

## 資源清單
<!-- RESOURCES:START -->
### 核心元件 · Core Components（13）

搭站的骨架：React / Tailwind 元件庫與介面套件。

| # | 名稱 | 授權 | 說明 |
|---|---|---|---|
| 1 | [Scrolltide](https://scrolltide.co) |  | 終極氛圍編程寶庫，600+ 3D、動畫、波動敘事網頁模板 |
| 2 | [Aceternity UI](https://ui.aceternity.com) |  | 200+ 超炫動畫 React/Tailwind 元件，專做 Hero 區 |
| 3 | [Magic UI](https://magicui.design) |  | 高轉換率行銷網站動畫 React 元件 |
| 4 | [Motion Primitives](https://motion-primitives.com) |  | 可重用進階 UI 互動 React 元件 |
| 12 | [shadcn/ui](https://ui.shadcn.com) |  | 黃金標準，複製貼上的 React/Tailwind 框架 |
| 13 | [Uiverse](https://uiverse.io) |  | 數千開源 UI 元素，支援 HTML/CSS/Tailwind/React |
| 14 | [UIAble](https://uiable.com) |  | 擴展 shadcn 生態的開源 React 庫 |
| 15 | [mapcn](https://mapcn.dev) |  | React 地圖元件，標記、路線、彈窗 |
| 31 | [DaisyUI](https://daisyui.com) | 開源 | Tailwind CSS 元件庫，語意化 class 與內建主題，少寫 class 也能快速搭 UI |
| 32 | [Tremor](https://www.tremor.so) | 開源 | 開源、無障礙的 React 元件，以 Tailwind 打造圖表與儀表板 |
| 33 | [DevSnips](https://devsnips.site) | 開源 | 開源 UI 註冊庫，提供 React / Tailwind / Vanilla 的元件、區塊與完整模板 |
| 34 | [Park UI](https://park-ui.com) | 開源 | 以 Ark UI 與 Panda CSS 打造的精緻元件，支援多種前端框架 |
| 35 | [Origin UI](https://originui.com) | 開源 | 現已更名為 coss ui：基於 Base UI 的現代元件庫，收錄 500+ 個元件範例 |

### 動畫特效 · Animation & Effects（13）

讓畫面有動勢：動畫庫、特效與微互動。

| # | 名稱 | 授權 | 說明 |
|---|---|---|---|
| 5 | [OpenMotion](https://openmotion.design) |  | 用 AI 建立產品演示與動畫 |
| 6 | [Kinetics](https://kinetics.colorion.co) |  | 150+ 動畫效果，附 React 程式碼與提示 |
| 23 | [Liquid Glass](https://glass.samasante.com) |  | 動態玻璃折射效果 React 元件 |
| 24 | [MicroKit UI](https://microkit.co) |  | 按鈕與輸入框的頂級微互動 |
| 25 | [CSS Text Effects](https://text-effects.colorion.co) |  | 可直接複製的動畫文字特效 |
| 26 | [Circle Loaders](https://circleloaders.dominikakissi.com) |  | 24 個現代 SVG 圓形載入器 |
| 27 | [Gradient Buttons](https://gradientbuttons.colorion.co) |  | 一鍵複製的 CSS 漸層按鈕 |
| 30 | [Anime.js](https://animejs.com) |  | 輕量級 JS 函式庫，處理複雜 DOM 動畫 |
| 36 | [Motion](https://motion.dev) | 開源 | 原 Framer Motion，適用 React、JavaScript 與 Vue 的高效能動畫庫 |
| 37 | [GSAP](https://gsap.com) | 免費 | 專業級的強大 JavaScript 動畫庫，萬物皆可動畫，由 Webflow 支持 |
| 38 | [Lenis](https://lenis.darkroom.engineering) | 開源 | 輕量、高效能且兼顧無障礙的平滑捲動函式庫 |
| 39 | [AutoAnimate](https://auto-animate.formkit.com) | 開源 | 零設定、即插即用，自動為網頁元素加上平滑過場動畫 |
| 40 | [LottieFiles](https://lottiefiles.com) | 部分免費 | Lottie 動畫平台，提供大量可直接使用的動畫與編輯工具 |

### 氛圍編程 AI · Vibe Coding AI（9）

與 AI 協作：提示詞、設計規範與風格參考。

| # | 名稱 | 授權 | 說明 |
|---|---|---|---|
| 7 | [21st.dev](https://21st.dev) |  | 氛圍編碼 NPM 套件與 MCP 元件登錄庫 |
| 8 | [DESIGNmd](https://designmd.ai) |  | 數百個設計系統轉成 Markdown 供 AI 讀取 |
| 9 | [VibePrompt](https://vibeprompts.dev) |  | 儀表板、登陸頁、複雜 UI 的視覺提示 |
| 10 | [Refero Styles](https://styles.refero.design) |  | 2000+ 真實產品樣式與排版 |
| 11 | [Kage](https://kage.design) |  | 真實 UI 靈感直接對應到 Prompt |
| 41 | [v0.dev](https://v0.dev) | 部分免費 | Vercel 的 AI 助手：用對話設計、迭代並擴展全端網頁應用 |
| 42 | [Kombai Gallery](https://kombai.com/gallery) | 免費 | 持續增長的網頁與行動 UI 設計庫，挑一個用 Kombai 重混或直接帶回專案 |
| 43 | [Google Stitch](https://stitch.withgoogle.com) | 免費 | Google 的 AI 介面設計工具，快速生成行動與網頁 UI |
| 44 | [Relume](https://www.relume.io) | 部分免費 | 以逾 200 萬個網站採用的人工設計元件系統為基礎，可在 Relume 發布或匯出 |

### 靈感圖庫 · Inspiration Galleries（9）

動手前先看：各類型網頁區塊的設計範例。

| # | 名稱 | 授權 | 說明 |
|---|---|---|---|
| 16 | [Component Gallery](https://component.gallery) |  | 2600+ 範例，看頂尖設計系統如何處理同一元件 |
| 17 | [Minimal Gallery](https://minimal.gallery) |  | 精選高端現代網站，給編碼代理靈感 |
| 18 | [AppShot Gallery](https://appshot.gallery) |  | 真實 App 截圖，行動 UI 靈感 |
| 19 | [Navbar Gallery](https://navbar.gallery) |  | 數百個高端導航列範例 |
| 20 | [Footer Design](https://footer.design) |  | 專做漂亮 Footer 的圖庫 |
| 21 | [CTA Gallery](https://cta.gallery) |  | 轉換率最佳化的表單、彈窗、按鈕 |
| 22 | [404s](https://404s.design) |  | 創意 404 頁面合集 |
| 45 | [Mobbin](https://mobbin.com) | 部分免費 | 40 萬+ 可搜尋的行動與網頁 App 截圖庫，省下 UI/UX 研究時間 |
| 46 | [Landingfolio](https://www.landingfolio.com) | 免費 | 精選 Landing Page 設計、模板與元件的靈感庫 |

### 插圖與立體 · Illustrations & 3D（4）

點睛素材：插圖、圖示與 3D icon。

| # | 名稱 | 授權 | 說明 |
|---|---|---|---|
| 28 | [Kitbitz](https://kitbitz.art) |  | 2000+ 免費手繪插圖 |
| 29 | [3Dicons](https://3dicons.co) |  | 開源 3D 圖示，適合空間 UI |
| 47 | [unDraw](https://undraw.co) | 免費 | 開源免費插圖庫，可自訂主色，適用網站與產品 |
| 48 | [Storyset](https://storyset.com) | 部分免費 | 可客製、可動畫化的免費插圖，適合 Landing Page、App 與簡報 |
<!-- RESOURCES:END -->

## 關於預覽圖

預覽圖為各網站公開的社群分享圖（Open Graph image），版權屬於各站原作者，此處僅作為資源的預覽用途。其中 Motion Primitives 的分享圖設定錯誤（指向 localhost），改用本機瀏覽器截取首頁；LottieFiles 受 Cloudflare 機器人驗證保護，抓不到預覽圖，暫用占位圖。如有任何疑慮，歡迎開 issue，會立即移除。

## 授權

程式碼與整理內容以 [MIT License](LICENSE) 釋出。清單中各資源的授權請以其官方網站為準。

## 致謝

原始清單來自 X / Threads 上 @Himanshu 的整理，這裡重新整理成開源格式並重新設計介面。
