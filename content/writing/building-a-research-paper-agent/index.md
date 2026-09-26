---
title: "Building a Research Paper Agent: LLMs, Codex, and Zotero Workflows"
summary: "An engineering exploration of building an autonomous research literature agent for continuous paper ingestion, citation analysis, and circuit benchmark extraction."
date: 2026-09-26
slug: "building-a-research-paper-agent"
categories:
  - Technical
tags:
  - Research Tools
  - AI Agents
  - Workflow
aliases:
  - /blog/building-a-research-paper-agent/
---

## Overview

Staying abreast of literature in integrated circuits, neuromorphic hardware, and AI accelerators is an increasingly challenging task. As preprint volumes surge, manual literature tracking and manual parameter extraction quickly become throughput bottlenecks.

To address this, I built an experimental local agentic workflow that interfaces directly with local Zotero libraries, ArXiv APIs, and LLM reasoning models.

## Architecture

The system consists of three modular components:

1. **Ingestion & Metadata Parsing**: Monitors RSS feeds and query triggers across IEEE Xplore and ArXiv. Automatically extracts paper text, authors, abstracts, and circuit benchmark tables.
2. **Schema-Constrained Extraction**: Utilizes structured prompting to extract key quantitative metrics: CMOS technology node (nm), supply voltage (V), energy efficiency (TOPS/W or pJ/SOP), area (mm²), and key circuit topology.
3. **Graph Synthesis & Note Generation**: Synthesizes comparative tradeoff notes directly into markdown format, generating backlinked notes for my personal knowledge repository.

## Takeaways

- Automated ingestion reduces initial literature triage time by over 70%.
- Strict JSON schema validation is essential when extracting hardware performance figures to prevent model hallucination.
