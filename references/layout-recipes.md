# Layout Recipes — Swiss International for 3:4

Each `<section class="poster xhs">` uses one recipe. Mix recipes across pages — never repeat the same layout twice in one deck.

## S01 — Accent Cover

Best for page 1. Big title, one accent stripe, bottom metadata.

```
chrome-min (top strip)
t-cat + h-statement title
[grow spacer]
hr-accent
lead subtitle (1-2 lines)
t-meta row
```

## S02 — Two Signals / Comparison

Best for "old vs new", "voice vs keyboard", feature comparisons.

```
chrome-min
h-xl title
.two-signals grid:
  .signal-block.solid (ink bg, white text, icon + title + bullets)
  .signal-block.outlined (border, icon + title + bullets)
```

## S10 — H-Bar Chart

Best for benchmark comparisons, rankings, percentage data.

```
chrome-min
h-xl title
.h-bar-chart:
  .bar-row × N:
    .row-lbl (item name)
    .row-track > .row-fill (colored bar, width = --w%)
    .row-val (number)
t-meta footnote
```

## S11 — Stacked Ledger

Best for feature lists, capability inventories, "5 things" summaries.

```
chrome-min
h-xl title
.stacked-ledger:
  .ledger-row × N:
    .ledger-num (large thin number)
    .ledger-lbl (title + .sub description)
    .ledger-icn (Lucide icon, optional)
```

## S12 — Matrix + Hero Stat

Best for capability grids, memory systems, benefit breakdowns.

```
chrome-min
h-xl title
.matrix-fill (2×N grid):
  .matrix-cell × N:
    .cell-nb (mono label)
    .cell-title (name)
  one .is-accent cell for highlight
.hero-stat-bottom:
  left: kicker + lead
  right: num-mega
```

## Custom — Scenario Grid

Best for "4 use cases", before/after scenarios, workflow steps.

```
chrome-min
h-xl title
.scenario-grid (2×2):
  .scenario-card × 4:
    .sc-num
    .sc-title
    .sc-body
```

## Custom — Tag Grid

Best for policy labels, category lists, rules summary.

```
chrome-min
h-xl title
.tag-grid:
  .tag-item × N:
    .tag-num
    .tag-name
```

## Custom — Three Point Rows

Best for "key takeaways", numbered conclusions.

```
chrome-min
h-xl title
.point-row × 3:
  .point-num
  .point-text
card-accent (closing CTA)
```

## Custom — Info Cards

Best for "what you need to know", install instructions, summary.

```
chrome-min
h-xl title
.card-fill × N (with icon/emoji-free label + body)
.card-accent (closing statement)
t-meta tags row
```
