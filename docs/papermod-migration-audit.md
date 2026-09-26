# PaperMod Redesign & Migration Audit

**Date**: 2026-09-26  
**Branch**: `redesign-papermod`  
**Site**: [https://hhaoranyi.github.io/](https://hhaoranyi.github.io/)  

---

## 1. Technical Baseline & Environment

- **Static Site Generator**: Hugo Extended v0.124.1 (matching GitHub Actions workflow `peaceiris/actions-hugo@v3` with `WC_HUGO_VERSION: '0.124.1'`).
- **Target Theme**: [Hugo PaperMod](https://github.com/adityatelange/hugo-PaperMod) added via Git submodule at `themes/PaperMod`.
- **Hosting & CI/CD**: GitHub Pages triggered via `.github/workflows/publish.yaml` on push to `main`.
- **Workflow Update Needed**: Enable `submodules: true` or `submodules: recursive` in `actions/checkout@v4` step.

---

## 2. Dependencies & Files to Purge (HugoBlox Decommissioning)

The following files belong strictly to HugoBlox / Academic theme and will be safely decommissioned:

1. `config/_default/*` (`hugo.yaml`, `languages.yaml`, `menus.yaml`, `module.yaml`, `params.yaml`) → Replaced by unified root `hugo.yaml`.
2. `go.mod` (HugoBlox builder module declarations) → Purged (PaperMod is loaded as a theme, removing Go module lock issues).
3. `academic.Rproj`, `netlify.toml` → Purged.
4. `content/authors/admin/` (HugoBlox specific author system) → Author details consolidated into site config `params.author` and homepage layout; `avatar.jpg` preserved in `static/images/avatar.jpg`.
5. `data/page_sharer.toml`, `data/fonts`, `data/themes` → Purged.
6. Old HugoBlox layout overrides in `layouts/partials/components/footers/minimal.html`.
7. `content/slides/example/` and `assets/media/albums/demo/` (theme demo artifacts).

---

## 3. Content Retention & Structural Mapping

| Content Element | Current Location | Target Location in PaperMod | Retention & Strategy |
|---|---|---|---|
| **Author Portrait** | `content/authors/admin/avatar.jpg` | `static/images/avatar.jpg` | Retain real photo for editorial homepage hero (subtle 130px frame). |
| **CV PDF** | `static/uploads/resume.pdf` | `static/uploads/resume.pdf` | Retain original URL path for zero broken external links. |
| **CV Page** | `content/cv/_index.md` | `content/cv/index.md` | Retain and adapt into compact academic CV with subtle download link. |
| **Research Overview** | `content/research/_index.md` | `content/research/index.md` | Retain vision & 4 focus areas; enhance with editorial layout. |
| **ARM AI Acceleration** | `content/project/example/index.md` | `content/projects/arm-ai-acceleration/index.md` | Retain and structure as primary technical case study; alias `/project/example/`. |
| **Candidate Projects** | `content/project/<wta, cim, etc.>` | `content/projects/<slug>/index.md` | Retain structured case study drafts (`draft: true`). |
| **Technical Writing** | `content/blog/analog-cim-tradeoffs/` | `content/writing/analog-cim-tradeoffs/index.md` | Retain as Technical note (`categories: ["Technical"]`). |
| **Journal Writing** | `content/blog/phd-workflow-reflections/` | `content/writing/phd-workflow-reflections/index.md` | Retain as Journal note (`categories: ["Journal"]`). |
| **Photography** | `content/photography/` | `content/photography/` | Retain album system, editorial image flow, and clean lightbox. |
| **URL Aliases** | `/post/*`, `/blog/*`, `/project/*` | Configured via Hugo aliases | Preserve backward compatibility for all previously shared URLs. |

---

## 4. Proposed File Changes & Architecture

```text
hhaoranyi.github.io/
├── .gitmodules                         # PaperMod submodule declaration
├── hugo.yaml                           # Unified PaperMod configuration (clean, minimalist)
├── themes/PaperMod/                    # Upstream submodule (unmodified)
├── .github/workflows/publish.yaml      # Updated with submodules: true
│
├── content/
│   ├── _index.md                       # Homepage configuration
│   ├── research/
│   │   └── index.md                    # Research overview, areas, publications
│   ├── projects/
│   │   ├── _index.md                   # Selected work index
│   │   ├── arm-ai-acceleration/index.md
│   │   ├── wta-selector/index.md       (draft)
│   │   ├── hybrid-attention-cim/index.md (draft)
│   │   └── neuromorphic-processor/index.md (draft)
│   ├── writing/
│   │   ├── _index.md                   # Editorial chronological list
│   │   ├── analog-cim-tradeoffs/index.md
│   │   └── phd-workflow-reflections/index.md
│   ├── photography/
│   │   ├── _index.md                   # Large photo journal landing
│   │   └── nordic-light/index.md       # Multi-image editorial layout
│   └── cv/
│       └── index.md                    # Academic CV with PDF download
│
├── layouts/
│   ├── index.html                      # Custom editorial homepage (Hero, Themes, Selected Work, Writing, Photography)
│   ├── _default/
│   │   └── baseof.html                 # Standard typography wrapper
│   ├── partials/
│   │   ├── header.html                 # Minimalist header: Haoran Yi | Research Writing Photography CV ◐
│   │   └── footer.html                 # Minimalist 1-line footer: © Haoran Yi · GitHub · Scholar · LinkedIn · Email
│   ├── projects/
│   │   └── single.html                 # Case study format (Overview, Architecture, Contributions, Results)
│   ├── writing/
│   │   ├── list.html                   # Editorial text list grouped by year
│   │   └── single.html                 # 720px reading column, serif typography option, clean TOC
│   └── photography/
│       ├── list.html                   # Photography landing page
│       └── single.html                 # Photo album layout with responsive vanilla JS lightbox
│
├── assets/
│   └── css/extended/
│       └── custom.css                  # Typography, off-white palette, responsive widths, zero-card rules
│
├── static/
│   ├── images/avatar.jpg               # Professional portrait
│   └── uploads/resume.pdf              # Academic CV file
│
└── AGENTS.md                           # Updated development & design rules
```
