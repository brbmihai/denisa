# Hero section design language

**Source:** `component-test/5_hero_section.png` (DENISA outdoor apparel hero)

## Color palette

| Token | Hex | Usage |
|-------|-----|--------|
| Coal | `#0D0D0B` | Left panel background |
| White (warm) | `#FAF9F6` | Headlines, body on dark |
| Inverse muted | `rgba(255,255,255,0.75)` | Eyebrow, paperclip |
| Burnt orange | `#D86A2B` | Button hover, outline CTA |
| Hero line gold | `#B87942` | Title underline, button underline (default ornaments) |
| Clay | `#A08B45` | Alternate accent |

## Typography

| Role | Family | Size (mobile → desktop) | Weight | Transform |
|------|--------|-------------------------|--------|-----------|
| Eyebrow | Inter | 0.75rem → 0.8125rem | 500 | uppercase, 0.12em tracking |
| Title | Cormorant Garamond | 2.5rem → 4.5rem | 400 | sentence case |
| Subtitle body | Inter | 0.875rem → 1rem | 400 | none |
| Button label | Inter | 0.875rem | 600 | uppercase, 0.08em tracking |
| Hand-script | Caveat | 1.375rem → 1.625rem | 400 | none, slight rotation |

## Components

| # | Name | Class | File |
|---|------|-------|------|
| 1 | Eyebrow | `.hero-eyebrow` | `eyebrow.html` |
| 2 | Title + underline | `.hero-title-block` · `.hero-title` · `.hero-title-underline` | `title.html` |
| 2b | Title underline only | `.hero-title-underline` | `title-underline.html` |
| 3 | Subtitle element | `.hero-subtitle-element` | `subtitle-element.html` |
| 4 | Button (ghost outline) | `.hero-btn.hero-btn--outline` | `button.html` |
| 5 | Button + underline | `.hero-btn-text` · `.hero-button-underline` | `button-with-subtitle-element.html` |
| 5b | Button underline only | `.hero-button-underline` | `button-underline.html` |
| 6 | Hand-script + clip | `.hero-hand-script` | `hand-script-with-subtitle-element.html` |

Shared styles: `hero-components.css`  
Ornaments: `hero-ornaments.svg` · `hero-gold-underline.svg` · Path data: `hero-line-paths.json`

### Gold cubic underline (default)

| Piece | Class | Size | viewBox |
|-------|-------|------|---------|
| Title ribbon | `.hero-title-underline` | `min(20rem, 100%)` × `1.125rem` | `0 0 320 18` |
| Button ribbon | `.hero-button-underline` | `6.75rem` × `0.95rem` | `0 0 320 18` |

Same cubic path; gradient `hero-gold-underline-fade` fades `#B87942` from 0% → 70% → transparent at 100% (`userSpaceOnUse`, x2=320).

### Line variants (`line-variants.html`)

| ID | Profile | Use when |
|----|---------|----------|
| **v1** | Flat, no bend | Minimal / strict grid |
| **v2** | Whisper arch (0.2px) | Flattest match with hint of hand-drawn |
| **v3** | Reference (0.28px arch) | **Default** — closest to `5_hero_section.png` |
| **v4** | Soft S-curve | Slightly more organic underline |
| **v5** | Late fade (75%) | Longer full-weight segment before taper |
| **v6** | Gold cubic | User-supplied cubic path; `#B87942`; viewBox `0 0 420 28`; fade from 70% |

**Taper rule (all variants):** uniform ~1.3px stroke from the left; from **70%** of length, stroke narrows to a point and opacity fades via `linearGradient`.

## Subtitle element anatomy

1. **Ornament line** — thin burnt-orange ribbon with **very subtle arch**; **constant width 0–70%**, then **width + opacity fade** to a soft point (`hero-subtitle-element__line`). Five variants in `line-variants.html`; default **v3 Reference**.
2. **Body** — 2–3 lines of supporting copy (`hero-subtitle-element__text`)

## Button patterns

- **Outline CTA:** transparent fill, 1px warm-white border, inverts on hover (white fill, coal text).
- **Text CTA:** no box; gold cubic underline (`.hero-button-underline`) beneath label.

## Hand-script block

- **Subtitle element:** paperclip icon (line art, muted white, ~−12° rotation)
- **Quote:** Caveat, burnt orange, max-width ~22rem, slight counter-rotation

## Accessibility

- Ornament SVGs marked `aria-hidden="true"`
- Hand-script wrapped in `<figure>` / `<blockquote>`
- Focus rings use `--focus-ring-color` (burnt orange, 3px)

## Integration

```html
<link rel="stylesheet" href="../v3-design-extract-typography/denisa-dragomir-variables.css">
<link rel="stylesheet" href="../v3-design-extract-typography/denisa-dragomir-typography.css">
<link rel="stylesheet" href="hero-components.css">
```

Preview: open `component-test/index.html` in a browser (local server recommended).

## WCAG notes (static review)

| Check | Status |
|-------|--------|
| Eyebrow contrast on coal | ~4.8:1 — pass (large text AA) |
| Title / body on coal | >7:1 — pass |
| Burnt orange script on coal | ~4.2:1 — borderline for small script; acceptable for decorative quote |
| Focus indicators | Visible on interactive elements |
