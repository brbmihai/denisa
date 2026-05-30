---
name: Nordic Peak Design System
colors:
  surface: '#fff8f5'
  surface-dim: '#ebd6c7'
  surface-bright: '#fff8f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fff1e8'
  surface-container: '#ffeadb'
  surface-container-high: '#fae4d4'
  surface-container-highest: '#f4dfcf'
  on-surface: '#241910'
  on-surface-variant: '#424844'
  inverse-surface: '#3a2e24'
  inverse-on-surface: '#ffeee1'
  outline: '#727974'
  outline-variant: '#c2c8c2'
  surface-tint: '#486556'
  primary: '#0a271b'
  on-primary: '#ffffff'
  primary-container: '#213d30'
  on-primary-container: '#89a897'
  inverse-primary: '#aecebc'
  secondary: '#9a4600'
  on-secondary: '#ffffff'
  secondary-container: '#fd8a3e'
  on-secondary-container: '#672c00'
  tertiary: '#23221c'
  on-tertiary: '#ffffff'
  tertiary-container: '#393730'
  on-tertiary-container: '#a4a097'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#caead7'
  primary-fixed-dim: '#aecebc'
  on-primary-fixed: '#032015'
  on-primary-fixed-variant: '#304d3f'
  secondary-fixed: '#ffdbc9'
  secondary-fixed-dim: '#ffb68c'
  on-secondary-fixed: '#321200'
  on-secondary-fixed-variant: '#753400'
  tertiary-fixed: '#e7e2d8'
  tertiary-fixed-dim: '#cac6bd'
  on-tertiary-fixed: '#1d1c16'
  on-tertiary-fixed-variant: '#494740'
  background: '#fff8f5'
  on-background: '#241910'
  surface-variant: '#f4dfcf'
typography:
  h1:
    fontFamily: Hanken Grotesk
    fontSize: 64px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Hanken Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style

This design system is built for an audience that values endurance, the serenity of nature, and premium athletic guidance. It bridges the gap between rugged outdoor performance and elegant Scandinavian minimalism. The visual language focuses on the "Golden Hour"—that specific moment in trail running where the light is warm, the shadows are soft, and the connection to the landscape is at its peak.

The style is a blend of **Minimalism** and **Tactile Modernism**. It prioritizes high-quality white space and refined typography while introducing organic, mountain-inspired curves. The emotional goal is to evoke a sense of calm confidence, professional expertise, and the quiet beauty of alpine trails. Imagery should lean into emotional storytelling, using natural light and high-grain textures to avoid a "sterile" corporate look.

## Colors

The palette is rooted in the natural landscape of a forest at sunset. 
- **Forest Green (#213D30):** The primary anchor, representing stability, growth, and the alpine environment.
- **Golden Hour (#E3762B):** Used sparingly for primary actions, mimicking the warm glow of the sun against the peaks.
- **Alabaster (#F5F0E6):** A warm earthy neutral used for backgrounds to create a soft, paper-like feel that is easier on the eyes than pure white.
- **Obsidian (#1C1209):** A deep, warm near-black for high-contrast typography and structural elements.

Gradients should be used subtly to simulate natural light fall-off. Backgrounds often utilize the **Sunlight Gradient** to create a sense of depth and warmth across large sections.

## Typography

The typography strategy balances authority with approachability. 
- **Headings:** We use **Hanken Grotesk** for its sharp, modern precision. The heavy weights (Bold/ExtraBold) are used for high-impact emotional statements and section titles, providing a "strong" athletic foundation.
- **Body Text:** **Manrope** is selected for its exceptional legibility and refined geometric structure. It ensures that training advice and storytelling remain accessible even on smaller mobile screens during a run.
- **Labels:** Uppercase Hanken Grotesk with generous letter spacing is used for overlines and categories to create a sense of premium editorial design.

## Layout & Spacing

The layout philosophy follows a **Fixed-Fluid Hybrid** model. Content is contained within a 1280px max-width container on desktop, utilizing a 12-column grid. However, background elements and "mountain path" curves are allowed to bleed off-canvas to suggest the infinite nature of the outdoors.

Spacing is generous, favoring `lg` (48px) and `xl` (80px) gaps between major sections to prevent the UI from feeling cluttered. We aim for an "Open Air" feel where every element has room to breathe, mirroring the expansive scale of trail running.

## Elevation & Depth

Depth is achieved through **Tonal Layering** and **Ambient Shadows** rather than harsh outlines. 
- **Surfaces:** Cards and containers use a slightly lighter tint of the background or a pure white surface with a very soft, diffused shadow (15% opacity of the #1C1209 neutral) to appear as if they are floating gently above the ground.
- **Glassmorphism:** For navigation bars and mobile overlays, a subtle backdrop blur (12px) with a semi-transparent Alabaster (#F5F0E6) fill is used to maintain a sense of place within the landscape.
- **Atmospheric Depth:** Section dividers often use a "mist" effect—a soft gradient transition between dark forest green and the warm neutral beige to separate content without hard lines.

## Shapes

The shape language is organic and soft. 
- **Corners:** We use a **Rounded (Level 2)** approach. Standard components have a 0.5rem radius, while larger cards use 1rem. This softens the technical nature of the training data and makes the UI feel more "human."
- **Organic Curves:** A signature element of this design system is the "Path Curve." Section dividers should occasionally use the abstract, flowing mountain silhouette from the logo as a mask or SVG divider. These curves should always flow from left to right, mimicking the progression of a runner along a trail.
- **Icons:** Use thin-stroke, rounded-end icons to match the refined Scandinavian aesthetic.

## Components

- **Primary Buttons:** High-contrast Golden Hour (#E3762B) backgrounds with Obsidian (#1C1209) text. These should have a subtle "glow" hover effect that mimics a sunbeam.
- **Secondary Buttons:** Forest Green (#213D30) outlines with a transparent core, using the "soft" roundedness for a premium feel.
- **Cards:** Use Alabaster (#F5F0E6) surfaces. For "Success Stories," cards should incorporate a full-bleed background image with a gradient overlay that ensures typography remains legible in the "Golden Hour" style.
- **Progress Trackers:** For running plans, use a custom "Path" style line (derived from the logo's trail) rather than a straight linear bar. This reinforces the "journey" aspect of the academy.
- **Input Fields:** Minimalist design with only a bottom border in Forest Green, which transforms into a 2px Golden Hour line upon focus.
- **Chips/Badges:** Small, pill-shaped elements using low-opacity Forest Green backgrounds and bold Hanken Grotesk text. Use these for difficulty levels (e.g., "Beginner," "Alpine Expert").