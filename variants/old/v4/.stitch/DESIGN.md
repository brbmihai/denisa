# Design System: Denisa Dragomir — Running Coach (Trail & Mountain)

**Project ID:** `TBD` — create a Stitch project and replace with the numeric ID from Google Stitch (`projects/{id}`).

This document was synthesized to match the local reference screen `.stitch/designs/home.html` (warm palette, trail running, mountain atmosphere). Use it as the single source of truth for Stitch prompts and the stitch-loop baton.

---

## 1. Visual Theme & Atmosphere

**Warm trail at golden hour.** The interface should feel like early morning or late afternoon on a mountain path: soft light, breathable whitespace, earthy warmth, and quiet confidence. Density is **medium**: generous hero, clear typographic hierarchy, and editorial-style sections—not a dashboard, not a neon sports app.

**Keywords for Stitch:** warm, organic, trail running, mountain silhouette, golden hour, soft gradients, matte surfaces, approachable elite, Romanian coaching brand.

**Philosophy:** Athletic credibility without cold tech minimalism; nature-forward imagery; human-centered copy blocks.

---

## 2. Color Palette & Roles

| Role | Descriptive name | Hex | Usage |
|------|------------------|-----|--------|
| Page backdrop | **Alpine Cream** | `#FAF4EC` | Main background, large quiet areas |
| Primary surface | **Paper Mist** | `#FFFFFF` | Cards, nav bar, modals |
| Primary text | **Pine Ink** | `#1E2A24` | Headlines, body |
| Secondary text | **Slate Trail** | `#5C6B63` | Subheads, captions, meta |
| Primary action | **Terracotta Run** | `#C45C3E` | Primary buttons, key links, small accents |
| Action hover / depth | **Burnt Clay** | `#A34A32` | Button hover, pressed states |
| Accent / highlights | **Summit Amber** | `#D9A441` | Badges, icons, subtle dividers, “elite” highlights |
| Deep accent | **Evergreen Ridge** | `#2F4D3F` | Footer, dark bands, secondary buttons (outline on cream) |
| Atmospheric gradient | **Dawn Horizon** | linear from `#E8C9A8` (12% opacity wash) to transparent | Hero overlays only—keep subtle |

**Functional rules**

- **Terracotta Run** is reserved for one primary CTA per viewport when possible.  
- **Evergreen Ridge** grounds the layout (footer, sticky nav on scroll optional variant).  
- Avoid pure black; use **Pine Ink** for maximum contrast.

---

## 3. Typography Rules

- **Display / H1–H2:** A high-contrast serif with personality — e.g. **Fraunces** (Google Fonts), weight 600–700, slightly tight tracking for headlines; line-height ~1.1–1.2.  
- **UI & body:** **DM Sans** or **Source Sans 3**, weight 400–600; body size 16–18px desktop, 15–16px mobile; line-height 1.55–1.65.  
- **Labels / nav:** Uppercase optional only for tiny labels (10–11px, letter-spacing +0.06em); default nav is sentence case in Romanian.  
- **Numbers** (paces, distances): use tabular lining figures where available; same family as body.

---

## 4. Component Stylings

- **Buttons (primary):** Pill-shaped or generously rounded (`border-radius` ~999px or 14px). Filled **Terracotta Run**, text **Paper Mist**, no harsh inner shadow. Hover: **Burnt Clay**, slight translateY(-1px) optional.  
- **Buttons (secondary):** Outline 1.5px **Evergreen Ridge** on cream/white; hover fill **Evergreen Ridge** with white label.  
- **Cards:** **Paper Mist** on **Alpine Cream**, corner radius 16–20px, **whisper-soft** shadow: `0 8px 30px rgba(30, 42, 36, 0.06)`. Optional 1px border `rgba(47, 77, 63, 0.08)`.  
- **Nav:** Mobile-first: full-height **drawer from the right**; **drawer title bar** uses the same frosted surface as **`.site-header`** (cream on inner pages, lighter frost on hero). **Hamburger** is lines-only (no tile/border). From **900px** up, horizontal links in the header; drawer hidden.  
- **Hero:** Full-width atmospheric layer (mountain + trail imagery or abstract gradient mesh); headline left or center; subcopy max-width ~36rem.  
- **Forms:** Rounded inputs (12px), border `rgba(92, 107, 99, 0.35)`, focus ring **Summit Amber** at 2px offset.

---

## 5. Layout Principles

- **Mobile-first:** Base layout and typography target phones; from **900px** widen grids (strip 3 columns, plan grid multi-column), increase section padding, and switch nav to horizontal bar.  
- **Vertical rhythm:** section padding 72–96px desktop, 48–64px mobile; consistent 8px grid.  
- **Imagery:** prefer trail, ridge lines, single runner silhouette, soft mist; avoid stocky “corporate wellness” poses.  
- **Motion (if any):** slow parallax or opacity fades only; respect `prefers-reduced-motion`.

---

## 6. Design System Notes for Stitch Generation

Paste this block into Stitch `generate_screen_from_text` prompts and into `.stitch/next-prompt.md` batons.

```markdown
**DESIGN SYSTEM (REQUIRED):**
- Platform: Web, desktop-first (scale down to mobile).
- Atmosphere: Warm trail running coach site; golden-hour mountains; organic, editorial, approachable elite.
- Palette: Alpine Cream (#FAF4EC) background; Pine Ink (#1E2A24) text; Terracotta Run (#C45C3E) primary actions; Evergreen Ridge (#2F4D3F) footer/deep UI; Summit Amber (#D9A441) accents; Paper Mist (#FFFFFF) cards.
- Typography: Fraunces (600–700) for H1–H2; DM Sans (400–600) for body and UI.
- Styles: Generous radius (16–20px cards, pill primary buttons); whisper-soft shadows; subtle hero gradient wash; no neon, no glass-heavy chrome aesthetic.
- Imagery: mountain horizon, trail path, single runner, soft mist or dawn light.

**PAGE STRUCTURE:**
1. Header: logo wordmark, primary nav (Acasă, Despre mine, Planuri, Blog, Contact), CTA button “Scrie-mi”.
2. Hero: full-bleed warm mountain/trail mood; H1 + short subhead + 2 CTAs (Planuri / Despre mine).
3. Proof strip: 3 metrics or trust chips (ani de alergare, tipuri de planuri, experiență competițională).
4. Services teaser: 2–3 cards (Plan personalizat, Planuri online, evenimente).
5. Testimonial snippet + link to full page.
6. Footer: evergreen background, links, social icons, copyright.
```
