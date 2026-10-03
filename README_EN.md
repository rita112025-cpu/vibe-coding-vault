# Vibe Coding Vault

> 30 free, open-source dev & design resources, collected into one ink-wash scroll. Bilingual (ZH/EN), searchable, with a light/dark theme toggle.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Resources: 30](https://img.shields.io/badge/Resources-30-blue)
![Static Site](https://img.shields.io/badge/Static-No%20Backend-green)

**中文:** [README.md](README.md)

## What is this

When you are building a site, a demo, or vibe coding with an AI, it is hard to remember where the good components, effects and inspiration live. This project turns a widely shared "30 free resources" list into a small searchable library with preview images.

It is a **fully static** site: one `index.html`, one JSON file and some preview images. No backend, no framework runtime, and it deploys to GitHub Pages as-is.

## Features

- **Ink-wash paper UI**: cream paper, vermilion accents, a vertical scroll-style rail with a progress line, and categories laid out as numbered chapters.
- **Light / dark theme**: toggle at the bottom of the rail. Your choice is remembered; the first visit follows the system setting.
- **Preview images**: each resource has a preview (the site's public social image), lightly tinted like paper and restored to full colour on hover.
- **Instant search and category filter** across names, descriptions and categories.
- **Three display languages**: Chinese, bilingual, English (cycle with one button).
- **Responsive**: on narrow screens the rail becomes a top bar.
- **Accessible**: keyboard friendly, visible focus ring, honours `prefers-reduced-motion`.

## Project structure

```
.
├── index.html              # built output (data inlined, opens by double-click)
├── src/template.html       # page source (HTML + CSS + JS)
├── data/resources.json     # the 30 resources (single source of truth)
├── assets/previews/        # preview images (webp, 800px wide)
├── build.py                # inlines the JSON into the template -> index.html
├── README.md
├── README_EN.md
└── LICENSE
```

## Data format

`data/resources.json` is an array of objects:

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

When `image` is `null`, the page generates an ink-landscape placeholder.

## Adding or editing resources

1. Add or edit an entry in `data/resources.json`.
2. Put the preview into `assets/previews/` and set `image` (800px wide, ~1.9:1 webp recommended).
3. Rebuild:

```bash
python build.py
```

4. Open `index.html` to check.

> There are five fixed categories (the `CH` array in `src/template.html`). Edit that array to add a new one.

## Deploy to GitHub Pages

1. Push to GitHub.
2. In **Settings → Pages**, choose the `main` branch, root `/`.
3. Your site will be at `https://<user>.github.io/vibe-coding-vault/`.

## Resources

### Core Components (8)

The skeleton of a site: React / Tailwind component libraries and UI kits.

| # | Name | Description |
|---|---|---|
| 1 | [Scrolltide](https://scrolltide.co) | Ultimate vibe coding vault with 600+ 3D, animation, storytelling templates |
| 2 | [Aceternity UI](https://ui.aceternity.com) | 200+ crazy animated React/Tailwind components for showcase hero sections |
| 3 | [Magic UI](https://magicui.design) | Ready-to-insert animated React components for high-conversion marketing sites |
| 4 | [Motion Primitives](https://motion-primitives.com) | Reusable React components for advanced UI interactions |
| 12 | [shadcn/ui](https://ui.shadcn.com) | Gold standard copy-paste React/Tailwind framework |
| 13 | [Uiverse](https://uiverse.io) | Thousands open source UI elements |
| 14 | [UIAble](https://uiable.com) | Open source React library extending shadcn ecosystem |
| 15 | [mapcn](https://mapcn.dev) | Copy-paste map components for React |

### Animation & Effects (8)

Motion and effects: animation libraries, micro-interactions, CSS tricks.

| # | Name | Description |
|---|---|---|
| 5 | [OpenMotion](https://openmotion.design) | Build and edit product demos & animations using AI |
| 6 | [Kinetics](https://kinetics.colorion.co) | 150+ animation effects with React code and ready prompts |
| 23 | [Liquid Glass](https://glass.samasante.com) | Dynamic glass refraction effects React components |
| 24 | [MicroKit UI](https://microkit.co) | Top micro-interactions for buttons and inputs |
| 25 | [CSS Text Effects](https://text-effects.colorion.co) | Copyable animated text effects |
| 26 | [Circle Loaders](https://circleloaders.dominikakiss.com) | 24 modern SVG circular loaders |
| 27 | [Gradient Buttons](https://gradientbuttons.colorion.co) | One-click copyable CSS gradient buttons |
| 30 | [Anime.js](https://animejs.com) | Lightweight JS library for complex DOM animation |

### Vibe Coding AI (5)

Working with AI: prompts, design specs and style references.

| # | Name | Description |
|---|---|---|
| 7 | [21st.dev](https://21st.dev) | Vibe coding NPM packages, huge component registry via MCP |
| 8 | [DESIGNmd](https://designmd.ai) | Hundreds of design systems converted to markdown for AI agent |
| 9 | [VibePrompt](https://vibeprompts.dev) | Ready visual prompts for dashboard, landing, complex UI |
| 10 | [Refero Styles](https://styles.refero.design) | 2000+ real product styles with layout |
| 11 | [Kage](https://kage.design) | Real UI inspiration directly mapped to prompts |

### Inspiration Galleries (7)

Look before you build: design examples for every kind of web section.

| # | Name | Description |
|---|---|---|
| 16 | [Component Gallery](https://component.gallery) | 2600+ examples showing how top design systems handle same element |
| 17 | [Minimal Gallery](https://minimal.gallery) | Curated high-end modern websites for inspiration |
| 18 | [AppShot Gallery](https://appshot.gallery) | Real app screenshots for mobile UI inspiration |
| 19 | [Navbar Gallery](https://navbar.gallery) | Hundreds of high-end navbars |
| 20 | [Footer Design](https://footer.design) | Gallery dedicated to well-built footers |
| 21 | [CTA Gallery](https://cta.gallery) | Conversion optimized forms, popups, buttons |
| 22 | [404s](https://404s.design) | Creative 404 pages collection |

### Illustrations & 3D (2)

Finishing touches: illustrations, icons and 3D assets.

| # | Name | Description |
|---|---|---|
| 28 | [Kitbitz](https://kitbitz.art) | 2000+ free hand-drawn illustrations |
| 29 | [3Dicons](https://3dicons.co) | Open source 3D icons for spatial UI |

## About the preview images

Previews are each site's public social-share (Open Graph) image; copyright belongs to the respective authors and they are shown here only as previews. Motion Primitives publishes a broken share image (it points to localhost), so its preview is a screenshot of the homepage; Circle Loaders no longer resolves, so it uses a placeholder. If you have any concern, open an issue and it will be removed right away.

## License

Code and curation are released under the [MIT License](LICENSE). Each listed resource follows its own license; check the official site.

## Credits

The original list came from @Himanshu on X / Threads. This repo re-organises it as open source with a redesigned interface.
