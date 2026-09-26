# AGENTS.md — PaperMod Operating & Development Guidelines

This document guides AI coding assistants, automated workflows, and contributors in maintaining, editing, and publishing content on this website.

---

## 1. Purpose

A quiet academic personal website that gradually becomes an editorial technical blog and photography journal as the visitor explores it.

- **Primary Persona**: Haoran Yi, PhD Researcher in Integrated Circuits and Systems at Linköping University, Sweden.
- **Visual Direction Inspiration**: [https://insel-sagt.com/](https://insel-sagt.com/) — Simplicity, editorial rhythm, whitespace, typography-first, natural integration of text and photography, low visual noise.

---

## 2. Content Hierarchy & Navigation

Top Navigation (Strictly 4 links + Logo + Theme Toggle):
```text
Haoran Yi                         Research   Writing   Photography   CV   ◐
```

Content Architecture:
```text
content/
├── research/index.md           -> /research/
├── writing/                    -> /writing/
│   ├── _index.md
│   ├── <slug>/index.md         (categories: ["Technical"] or ["Journal"])
├── projects/                   -> /projects/
│   ├── _index.md
│   ├── <slug>/index.md         (technical case study format)
├── photography/                -> /photography/
│   ├── _index.md
│   └── <album-slug>/index.md   (editorial image journal)
└── cv/index.md                 -> /cv/
```

---

## 3. Design Principles (Strict Constraints)

- **Editorial Rather Than Dashboard**: Avoid SaaS landing layouts, dashboard cards, floating containers, and busy UI widgets.
- **Typography-First**:
  - Sans-serif stack for navigation, UI, and headings.
  - Serif typography for long-form article reading (font-size 17–18px, line-height ~1.7).
  - Maximum 2 font families across the site.
- **Strictly Prohibited**:
  - NO gradients.
  - NO glassmorphism.
  - NO floating pill buttons or drop shadows.
  - NO large rounded cards (border-radius strictly `0–4px`).
  - NO skill progress bars or animated stats counters.
  - NO oversized hero banners.
  - NO decorative SVG illustrations.
- **Palette**:
  - Light mode: Warm off-white (`#faf9f7`), near black text (`#222222`), neutral gray secondary (`#666666`), subtle borders (`#e6e3df`), restrained dark blue accent (`#1b4965`).
  - Dark mode: Near black (`#161616`), soft off-white text (`#e0e0e0`), neutral gray (`#8c8c8c`), subtle borders (`#2a2a2a`).
- **Width System**:
  - General container: `1080px`
  - Long-form article text: `720px`
  - Research / Project case studies: `820px`
  - Photography: `1180px`

---

## 4. Publishing Rules & Integrity

Never:
1. Invent paper metadata, DOIs, venues, or co-authors.
2. Fabricate research silicon measurements, tapeout results, or foundry process nodes.
3. Publish confidential, pre-filing, or unverified project details without authorization.
4. Expose private contact details, GPS EXIF coordinates, or camera serial numbers.
5. Alter factual academic or educational history without verified documentation.

---

## 5. Development & Deployment

- **Upstream Theme**: Hugo PaperMod at `themes/PaperMod` (keep unmodified; customize via `assets/css/extended/` and `layouts/`).
- **Local Dev Server**:
  ```powershell
  hugo server -D
  ```
- **Production Build**:
  ```powershell
  hugo --minify
  ```
- **GitHub Actions Deployment**:
  Pushes to `main` branch automatically build and publish to GitHub Pages using Hugo Extended v0.146.0 with `submodules: recursive`.
