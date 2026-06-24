# xiaohongshu-minimal-cover

Generate Swiss International style carousel images for Xiaohongshu (小红书). Clean, minimal, data-driven — no emojis, no rounded corners, no gradients.

A Claude Code skill optimized for tech, AI tools, policy analysis, and product launch content.

## Quick Start

1. Install into `.claude/skills/xiaohongshu-minimal-cover/`
2. Tell Claude: "帮我用 xiaohongshu-minimal-cover 做一组小红书配图"
3. Claude will ask for content, pick an accent, plan pages, and render PNGs

## Visual Style

**Swiss International** — engineered, quantified, decisive.

- Inter/Helvetica vibe (uses system fonts — works offline)
- Strict left-aligned grid + hairline rules
- Single accent color (6 palettes available)
- Card-fill matrices, KPI towers, h-bar charts, numbered statements

### Accent Palettes

| Palette | Color | Vibe |
|---------|-------|------|
| `slate` | `#2c898a` teal | Developer tools, tech products |
| `crimson` | `#c0392b` red | Policy, warnings, bold claims |
| `ikb` | `#002FA7` blue | AI, general tech |
| `lemon-green` | `#C5E803` green | Health, ecology, emerging tech |
| `safety-orange` | `#FF6B35` orange | Industrial, risk alerts |
| `wisteria` | `#7d5ba6` purple | Creative, art, wellness |

## File Structure

```
xiaohongshu-minimal-cover/
  SKILL.md                        ← Skill definition & workflow
  README.md                       ← This file
  assets/
    template-swiss.html           ← Seed HTML template (copy & fill)
  references/
    layout-recipes.md             ← 10+ layout patterns
```

## Examples

Built with this skill:

- **MiMo Code launch** (7 pages, slate accent) — AI coding tool product launch
- **Capafy marketplace** (4 pages, slate accent) — AI infrastructure industry analysis
- **AI labeling policy** (3 pages, crimson accent) — government regulation explainer
- **Win11 Intelligent Terminal** (3 pages, slate accent) — tech product feature showcase

## Requirements

- Claude Code (any version)
- Playwright (for PNG rendering)
- No external fonts needed (uses Microsoft YaHei / PingFang SC)

## Design Principles

1. **Expression first** — each page answers one question in one glance
2. **Data over decoration** — numbers, labels, grids; never blobs or emojis
3. **The larger, the lighter** — display titles at weight 200-300
4. **One accent per deck** — never mix colors
5. **System fonts only** — renders reliably on Windows without Google Fonts

## License

MIT
