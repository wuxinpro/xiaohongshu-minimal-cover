---
name: xiaohongshu-minimal-cover
description: Generate Swiss International style Xiaohongshu carousel images (3:4). Clean, data-driven, minimal design with Slate/Crimson/IKB accent palettes. Use when the user asks for 小红书配图, 小红书图文, Rednote images, social cards, or carousel covers.
---

# Xiaohongshu Minimal Cover Skill

Generate polished Xiaohongshu carousel image sets (3:4, 1080×1440) in Swiss International style.

Clean typography, strict grids, single accent color, no decoration. Perfect for tech, AI tools, policy analysis, product launches, and data-driven content.

## What It Produces

- Xiaohongshu carousel sets (5-9 pages, 3:4 cover + content pages)
- Single-page social cards
- Text-only layouts (works great without images — Swiss excels at data + text)

Do NOT use for:
- Full slide decks or PPT websites
- WeChat cover pairs (this skill focuses on 3:4 Xiaohongshu only)
- Heavy photo showcase posts (the style is minimal, not lifestyle)

## Core Principle

Expression first. Each page must answer in one glance:
- What should the viewer understand?
- What evidence supports it?
- Which words must be large, which become captions?

## Style Identity

**Swiss International** — engineered, quantified, decisive.

- Inter/Helvetica feel (uses Microsoft YaHei on Windows — always available)
- Strict left-aligned grid, hairline rules
- One high-saturation accent per deck
- Card-fill matrices, KPI towers, h-bar charts, numbered statements
- No emoji, no rounded corners, no gradients, no box-shadows

### Accent Palettes

| Accent | Color | Best for |
|--------|-------|----------|
| **slate** (default) | `#2c898a` teal | Developer tools, B2B, infrastructure |
| **crimson** | `#c0392b` red | Policy, warnings, urgent claims |
| **ikb** | `#002FA7` blue | AI, technology, general purpose |
| **lemon-green** | `#C5E803` green | Ecology, health, emerging tech |
| **safety-orange** | `#FF6B35` orange | Industrial, risk, decision points |
| **wisteria** | `#7d5ba6` purple | Creative, art, wellness |

One accent per deck. Never mix.

## Workflow

### 1. Intake

Gather only what changes the output:
- Source text, title, or article
- Topic category (tech, policy, product, lifestyle, etc.)
- Supplied screenshots/photos (if any)

If user has no images, ask once:
> 这篇需要配图吗？三种走法：
> A. 你传截图/照片（推荐）
> B. 我去网上找
> C. 纯文字排版（Swiss 风格完全撑得住）

### 2. Extract Story

Turn source into page plan:
- Page 1 = cover hook
- Pages 2-N = one idea each
- 5-9 pages for most posts
- Keep nuance in post body; images carry hooks, comparisons, data, takeaways

### 3. Pick Accent

Match accent to content tone:
- AI/tech product → slate or ikb
- Policy/warning → crimson
- Health/eco → lemon-green
- Review/critique → slate or crimson

### 4. Plan Pages

```text
Page 01 / cover / hook / layout intent
Page 02 / point / key copy / layout intent
...
```

Choose from layout recipes in `references/layout-recipes.md`. Avoid repeating the same layout.

### 5. Build From Seed Template

Copy `assets/template-swiss.html` → `index.html`.
Set accent on `<html>`: `<html data-accent="slate">`.

Replace `<!-- POSTERS_HERE -->` with one `<section class="poster xhs">` per page.

### 6. Render

Use Playwright with a local HTTP server (Google Fonts won't load via `file://`).
- 1080×1440px per poster
- Wait 1.5-2s for system fonts
- Save to `output/`

### 7. Deliver

Show images inline, summarize what was built. Ask: "你自己先看还是我先核查一遍？"

## Non-Negotiables

- No emoji — use typed labels and numbers
- No `border-radius`, `box-shadow`, `linear-gradient` on card elements
- "The larger, the lighter" — display titles use weight 200-300
- Minimum readable size: body 26px, meta 20px
- One accent color per deck — never mix
- Text must not overflow or touch edges
- 3:4 cards must fill ≥75% canvas height
- Use `.h-xl` / `.h-statement` / `.lead` / `.body` / `.t-cat` / `.t-meta` classes — never inline font-size+weight on titles
