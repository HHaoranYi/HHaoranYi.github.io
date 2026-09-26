# Agent Editing & Repository Guidelines

This document defines the operating rules, directory structure, truthfulness standards, and build/deploy procedures for automated AI agents and contributors maintaining this repository.

---

## 1. Site Goals & Target Audience

- **Primary Persona**: Academic homepage for Haoran Yi, PhD Researcher in Integrated Circuits and Systems at Linköping University.
- **Target Audience**: Researchers, collaborators, semiconductor/IC industry recruiters, and engineering peers.
- **Core Principle (Academic-First)**:
  - Homepage is strictly focused on academic identity, research directions, projects, and contact details.
  - Writing (`/blog/`) and Photography (`/photography/`) are secondary destinations placed in the footer.
  - No writing preview feeds or photo carousels on the homepage.

---

## 2. Information Architecture & Navigation

- **Header Navigation (Strictly 3 Links)**:
  - `Home` (`/`)
  - `Research` (`/research/`)
  - `CV` (`/cv/`)
- **Footer Navigation**:
  - `Writing` (`/blog/`)
  - `Photography` (`/photography/`)
- **URL Conventions**:
  - `content/blog/<slug>/index.md` -> `/blog/<slug>/`
  - `content/project/<slug>/index.md` -> `/project/<slug>/`
  - `content/publication/<slug>/index.md` -> `/publication/<slug>/`
  - `content/photography/<slug>/index.md` -> `/photography/<slug>/`
  - Retain `/cv/` and direct download at `/uploads/resume.pdf`.

---

## 3. Truthfulness & Content Integrity Rules

- **Zero Hallucination Policy**:
  - Never invent or assume paper DOIs, co-authors, publication dates, tapeout silicon measurements, or foundry process nodes.
  - If project data or paper details are incomplete, create them as draft (`draft: true`).
  - Candidate topics (e.g. WTA selector, CIM accelerators) must not be published as completed tapeouts unless verified.
  - Never publish third-party demo images as personal photography works.

---

## 4. Local Build & Verification Commands

- Ensure portable Hugo Extended and Go are available in PATH:
  ```powershell
  $env:PATH = "C:\Users\HRan\.local\go\bin;C:\Users\HRan\.local\bin;$env:PATH"
  ```
- **Local Dev Server**:
  ```powershell
  hugo server -D
  ```
- **Production Build (Drafts Excluded)**:
  ```powershell
  hugo --minify
  ```
- **Check Output**:
  - Verify `public/` generation without template errors or broken links.

---

## 5. Adding New Content

- **New Blog Post**:
  Create `content/blog/<slug>/index.md` using `archetypes/blog.md`.
  Specify `kind: "technical"` or `kind: "personal"`.
- **New Project**:
  Create `content/project/<slug>/index.md` using `archetypes/project.md`.
- **New Photography Album**:
  Create `content/photography/<slug>/index.md` using `archetypes/photography.md`.
  Use `scripts/photography/optimize_photos.py` to strip GPS EXIF and resize images before committing.

---

## 6. Branch & Release Workflow

- `main`: Production release branch. Automated GitHub Actions will build and deploy on push.
- `redesign-v2`: Restructuring and staging development branch.
- `legacy-v1`: Git tag preserving the pre-restructure baseline.
