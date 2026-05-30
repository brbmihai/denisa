# Denisa Dragomir — Design Language

> Extracted from mockup: `test-ai-gen-web/2__4screens.png`  
> Brand: trail running coach & community · rugged, organic, scrapbook aesthetic

## Overview

Professional mountain trail-running site blending full-bleed photography, torn-paper textures, Polaroid frames, hand-drawn trail lines, and editorial serif typography. Dark forest sections alternate with warm paper-toned content blocks. Burnt orange is the sole vibrant accent for CTAs and links.

**Pages analyzed:** Home, About, Coaching, Community (+ embedded style guide)

---

## Color Palette

| Token | Hex | Usage |
|-------|-----|--------|
| Coal | `#0D0D0B` | Deepest backgrounds, hero overlays |
| Basalt | `#1F211A` | Dark UI, nav on scroll, stat boxes |
| Forest Night | `#2E3427` | Section backgrounds, cards on dark |
| Stone | `#D9E2D5` | Light section fills, torn-paper base |
| Sand | `#D5C7B5` | Warm paper, secondary light BG |
| Clay | `#A08B45` | Muted gold accents, tags |
| Burnt Orange | `#D86A2B` | Primary buttons, links, highlights |
| Alpine Moss | `#6B705F` | Secondary text, icons on light |
| Glacier Fog | `#DDE2E3` | Cool neutrals, borders, subtle BG |

### Semantic mapping

- **Background (dark):** Coal → Basalt → Forest Night
- **Background (light):** Stone, Sand, Glacier Fog
- **Text on dark:** warm white `#FAF9F6`, Stone at 80% for secondary
- **Text on light:** Coal, Basalt for headings; Alpine Moss for body secondary
- **Accent / CTA:** Burnt Orange
- **Borders:** Alpine Moss at 30–40% opacity, or 1px `#0D0D0B` on secondary buttons

---

## Typography (mobile-first)

**Approach:** All type tokens default to **mobile** sizes in `:root`. Values step up at **tablet (768px)** and **desktop (1024px)**. Wide desktop (1280px) only scales hero further.

**CSS files:** `denisa-dragomir-variables.css` (tokens) · `denisa-dragomir-typography.css` (utility classes)

### Font families

| Role | Family | Fallback |
|------|--------|----------|
| Display / headings | **Cormorant Garamond** | Georgia, serif |
| Body / UI | **Inter** | system-ui, sans-serif |
| Handwritten | **Caveat** | cursive |

```html
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@400;500&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

### Breakpoints

| Device | Min-width | CSS variable |
|--------|-----------|--------------|
| **Mobile** (default) | 0 | — |
| **Tablet** | 768px (`48rem`) | `--bp-tablet` |
| **Desktop** | 1024px (`64rem`) | `--bp-desktop` |
| **Wide** | 1280px (`80rem`) | `--bp-wide` |

### Responsive type scale

| Token | Mobile | Tablet | Desktop | Font | Use |
|-------|--------|--------|---------|------|-----|
| `display-hero` | 2.5rem | 3.5rem | 4.5rem (6rem wide) | Cormorant | Hero headline |
| `display-xl` | 2rem | 2.75rem | 3.5rem | Cormorant | Page titles |
| `display-lg` | 1.75rem | 2.25rem | 3rem | Cormorant | Section heroes |
| `display-md` | 1.5rem | 1.875rem | 2.25rem | Cormorant | Program names (50K) |
| `heading-xl` | 1.375rem | 1.625rem | 2rem | Cormorant | Major sections |
| `heading-lg` | 1.25rem | 1.375rem | 1.75rem | Cormorant | Card titles |
| `heading-md` | 1.125rem | 1.25rem | 1.5rem | Cormorant | Subsections |
| `heading-sm` | 1rem | 1rem | 1.25rem | Cormorant | Accordion, small titles |
| `body-xl` | 1.0625rem | 1.125rem | 1.125rem | Inter | Intro copy |
| `body-lg` | 1rem | 1.0625rem | 1.0625rem | Inter | Lead paragraphs |
| `body` | 1rem | 1rem | 1rem | Inter | Default body (16px) |
| `body-sm` | 0.875rem | 0.875rem | 0.875rem | Inter | Bios, meta (14px min) |
| `label` | 0.75rem | 0.75rem | 0.8125rem | Inter 600 | Tags, uppercase |
| `overline` | 0.75rem | 0.75rem | 0.8125rem | Inter 600 | Section labels |
| `caption` | 0.75rem | 0.75rem | 0.75rem | Inter | Fine print |
| `nav` | 0.75rem | 0.8125rem | 0.8125rem | Inter 500 | Nav links |
| `button` | 0.875rem | 0.875rem | 0.875rem | Inter 600 | Button labels |
| `polaroid-caption` | 1.15rem | 1.2rem | 1.25rem | Cormorant | Polaroid serif caption |
| `quote` | 1.25rem | 1.5rem | 1.75rem | Cormorant italic | Pull quotes |
| `handwritten` | 1.375rem | 1.375rem | 1.625rem | Caveat | Polaroid captions |
| `stat-num` | 1.75rem | 2.25rem | 2.5rem | Cormorant | Stat numbers |
| `stat-label` | 0.75rem | 0.75rem | 0.8125rem | Inter | Stat captions |
| `logo` | 0.75rem | 0.75rem | 0.8125rem | Inter 600 | Stacked wordmark |
| `form-title` | 1.5rem | 1.75rem | 2rem | Cormorant | Form headings |
| `form-label` | 0.875rem | 0.875rem | 0.875rem | Inter 600 | Field labels |
| `form-input` | 1rem | 1rem | 1rem | Inter | Inputs |
| `form-hint` | 0.75rem | 0.75rem | 0.75rem | Inter | Helper text |
| `form-error` | 0.75rem | 0.75rem | 0.75rem | Inter 500 | Errors |

### Utility classes

Apply responsive type with classes: `.text-display-hero`, `.text-heading-lg`, `.text-body`, `.text-polaroid-caption`, `.text-nav`, `.text-form-label`, etc. See `denisa-dragomir-typography.css`. Tailwind: import `denisa-dragomir-variables.css` and use `text-body`, `text-display-hero`, etc. (sizes bind to CSS variables).

### Typography rules

- Mobile: shorter line lengths; hero may wrap to 2–3 lines; nav collapses to hamburger
- Tablet: two-column forms; nav still compact until desktop
- Desktop: full horizontal nav; display sizes reach editorial scale
- Nav: Inter, uppercase, `letter-spacing: 0.08em`
- Prose containers: `.prose` max-width grows 36rem → 42rem

---

## Spacing System (mobile-first)

| Token | Mobile | Tablet | Desktop |
|-------|--------|--------|---------|
| `section-y` | 3rem | 4.5rem | 6rem (7.5rem wide) |
| `section-x` | 1.25rem | 2rem | 2.5rem |
| `gutter` | 1rem | 1.5rem | 2rem |
| `header-height` | 3.5rem | 4rem | 4.5rem |

Base unit: **4px**. Stack scale: 1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24.

---

## Layout & Grid

- **Mobile:** single column; full-width CTAs; stacked cards (2-col only for small program grid)
- **Tablet:** 2-column grids; inline newsletter; form row pairs
- **Desktop:** 3–4 column grids; horizontal nav; max content width 75rem

Patterns: 12-column desktop grid · organic About collage · full-bleed heroes · community node map

---

## Border Radius

| Token | Value | Use |
|-------|-------|-----|
| `none` | 0 | Photos edge-to-edge |
| `sm` | 4px | Tags, stat boxes |
| `md` | 8px | Cards (subtle) |
| `full` | 9999px | Avatar circles, pills |

Polaroids and torn paper use **mask images**, not border-radius.

---

## Shadows

Minimal elevation; depth from photography and texture.

| Token | Value |
|-------|-------|
| `shadow-polaroid` | `0 4px 24px rgba(13, 13, 11, 0.15)` |
| `shadow-card` | `0 8px 32px rgba(13, 13, 11, 0.25)` on dark sections |
| `shadow-nav` | `0 1px 0 rgba(255,255,255,0.08)` when scrolled on dark |

---

## Components

**CSS file:** `denisa-dragomir-components.css` · **Preview:** `denisa-dragomir-preview.html#components`

| Component | Class prefix | Mobile behavior |
|-----------|--------------|-----------------|
| Container | `.ds-container` | Horizontal padding from `--space-section-x` |
| Section | `.ds-section` | Vertical rhythm from `--space-section-y` |
| Grid 2/3/4 | `.ds-grid-*` | 1 col → 2 col (tablet) → 3–4 col (desktop) |
| Header | `.ds-header` | Sticky; hamburger `.ds-nav-toggle`; nav hidden until desktop |
| Logo | `.ds-logo` | Stacked wordmark + mountain mark |
| Button primary | `.ds-btn--primary` | Full-width option: `.ds-btn--block` |
| Button secondary | `.ds-btn--secondary` | `.on-dark` variant for dark sections |
| Button ghost / icon | `.ds-btn--ghost`, `.ds-btn--icon` | — |
| Text link | `.ds-link` | Arrow suffix |
| Tag / badge | `.ds-tag`, `.ds-badge` | Outline and dark variants |
| Stat | `.ds-stat` | Editorial top rule; `.on-dark` for dark surfaces |
| Card / program card | `.ds-card`, `.ds-card--program` | Image overlay gradient |
| Avatar / member | `.ds-avatar`, `.ds-member` | Size scales 3.5rem → 5.5rem |
| Polaroid | `figure.polaroid` | Tape pseudo-elements, 4:5 img (grayscale), serif caption + `.script`; variant `.polaroid--warm`. Legacy: `.ds-polaroid` |
| Timeline | `.ds-timeline` | Left border + orange dots |
| Alert | `.ds-alert--info/success/warning/error` | Full border + tinted fill |
| Breadcrumb | `.ds-breadcrumb` | Wrap on mobile |
| Tabs | `.ds-tabs` | Horizontal scroll tab list on mobile |
| Accordion | `.ds-accordion` | Full-width triggers |
| CTA band | `.ds-cta-band` | Centered stack |
| Quote block | `.ds-quote-block` | Sand background |
| Footer | `.ds-footer` | 1 → 2 → 4 columns |
| Search | `.ds-search` | Full-width input |
| Tooltip | `.ds-tooltip-wrap` | Hover/focus reveal |
| Modal | `.ds-modal-backdrop` | Bottom sheet mobile; centered tablet+ |
| Divider | `.ds-divider`, `.ds-divider--dashed` | — |

### Decorative (non-component CSS)

- Elevation line on hero · world map dots · dashed member network paths · torn paper masks · topo background

---

## Forms

**CSS file:** `denisa-dragomir-forms.css` · **Preview:** `denisa-dragomir-preview.html#forms`

### Form layouts

| Pattern | Classes | Responsive |
|---------|---------|------------|
| Stacked (default) | `.ds-form` | Single column all breakpoints |
| Two-column row | `.ds-form-row--2` | Stacked mobile; side-by-side tablet+ |
| Inline actions | `.ds-form-actions--inline` | Stacked mobile; row desktop |
| Newsletter | `.ds-newsletter` | Stacked mobile; input + button row tablet+ |
| On dark hero | `.ds-form--on-dark` | Light text; translucent inputs |
| Compact login | `.ds-form-compact` | Reduced field gaps |

### Field types

| Control | Class | Notes |
|---------|-------|-------|
| Text / email / tel | `.ds-input` | Min-height 48px mobile; focus orange ring |
| Textarea | `.ds-textarea` | Min 7rem height |
| Select | `.ds-select` | Custom chevron |
| Checkbox | `.ds-check` | Accent Burnt Orange |
| Radio group | `.ds-radio-group` | Inline option on tablet+ |
| Toggle | `.ds-toggle` | Switch for booleans |
| File upload | `.ds-file` | Dashed drop zone |
| Input + icon | `.ds-input-group` | Left icon padding |

### States

- **Hint:** `.ds-field__hint`
- **Error:** `.ds-field.is-error` + `.ds-field__error` + red border
- **Required:** `.required` on label (orange asterisk)
- **Disabled:** native `disabled` on controls + `.ds-btn:disabled`

### Form templates (in preview)

1. **Join the Club** — name, email, experience select, checkbox, full-width CTA  
2. **Coaching application** — radio program, textarea, toggle, inline actions  
3. **Camp waitlist (dark)** — email + phone on Forest Night  
4. **Newsletter** — inline email + subscribe  
5. **Error state demo** — invalid email  
6. **File upload + compact login** — avatar upload, remember me

---

## Textures & Graphics

| Asset type | Description |
|------------|-------------|
| Torn paper | Cream `#D5C7B5` / Stone edges, PNG mask between sections |
| Lined / graph paper | Subtle background for journal-style blocks |
| Topo map | Dark green repeating pattern for map sections |
| Hand-drawn mountains | Line art, 1–2px stroke, white or Coal |
| Polaroid frames | White border, soft shadow, slight rotation (-2° to 4°) |

**Handwritten quote reference:** *"The mountains are not a place, they are a teacher."*

---

## Icons

Thin line icons, 1.5–2px stroke, rounded caps:

- Weather: sun, cloud
- Trail: mountain, path, arrow
- UI: heart, bell, gear, calendar, location pin

Color: inherit or Alpine Moss on light; white/Stone on dark.

---

## Motion (inferred)

- Hero: subtle Ken Burns on background image (optional)
- Scroll: header gains solid Basalt background
- Paper sections: fade-up on enter viewport
- Trail line: stroke-dashoffset draw animation on community page
- Hover: buttons darken Burnt Orange ~8%; cards scale image 1.03

**Duration:** 200–400ms ease-out for UI; 800–1200ms for decorative draws.

---

## Accessibility

| Check | Notes |
|-------|-------|
| Orange on white | Burnt Orange `#D86A2B` on white ≈ 4.5:1 — verify large text only; use Coal for small body links if needed |
| White on Burnt Orange | Primary button passes AA for normal text |
| White on Forest Night | Strong contrast for headings |
| Stone on Coal | Good for secondary text |
| Focus | 2px Burnt Orange outline offset 2px |
| Images | Meaningful alt for runners, maps decorative with `aria-hidden` |
| **Estimated WCAG score** | **~88/100** (pending live audit; contrast on Clay/Sand pairs should be validated) |

---

## Page Patterns

1. **Home:** Hero → beliefs (paper) → community map (dark) → join CTA
2. **About:** Title + timeline + collage → drives me (dark) → life balance triptych
3. **Coaching:** Ultra stats hero → 3 challenge cards → beginner benefits → 4-up program grid
4. **Community:** Hero → member constellation → closing quote on paper

---

## Implementation files

| File | Purpose |
|------|---------|
| `denisa-dragomir-variables.css` | Tokens (mobile-first + tablet/desktop overrides) |
| `denisa-dragomir-typography.css` | Type utility classes |
| `denisa-dragomir-components.css` | UI components |
| `denisa-dragomir-forms.css` | Form patterns |
| `denisa-dragomir-preview.html` | Live reference (resize to test breakpoints) |

Import order: `variables` → `typography` → `components` → `forms`

## Source

Extracted manually from design mockup `2__4screens.png` — not a live URL crawl.
