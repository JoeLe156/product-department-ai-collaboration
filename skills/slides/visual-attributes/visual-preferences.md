# Visual Preferences — PM + AI Deck

Style name: Vivid Gradient Minimal (inspired by your screenshot)

- Purpose: Modern, energetic slides with readable contrast over vivid gradients; minimal chrome; on-slide citations supported.
- Usage: Works with Reveal.js previews and can be translated to PowerPoint/Google Slides.

## Color System
- Primary gradient
  - `--vp-accent-1` Hot Pink: `#FF3D81`
  - `--vp-accent-2` Neon Orange: `#FF6A00`
  - `--vp-accent-3` Coral Red: `#FF2D55`
  - `--vp-accent-4` Sun Yellow: `#FFD166`
  - `--vp-accent-5` Electric Magenta: `#D900FF`
- Neutrals
  - `--vp-text` Ink: `#0C0D0F`
  - `--vp-text-muted` Slate: `#60636B`
  - `--vp-surface` White: `#FFFFFF`
  - `--vp-gridline` `#EAECEF`
- Status (optional)
  - Success `#22C55E`, Warning `#F59E0B`, Danger `#EF4444`

Gradient background
- Default: linear 135° from Hot Pink → Neon Orange → Sun Yellow.
- Add soft radial bubbles (pink/orange with 15–25% opacity) for depth.

## Typography
- Titles: Poppins, 700–800; fallback: Segoe UI, Arial, sans-serif.
- Body: Inter, 400–600; fallback: Segoe UI, Arial, sans-serif.
- Sizes (16:9, 1280×720 target)
  - H1 64–72px; H2 44–56px; H3 32–36px; body 24–28px; footnotes 16–18px.
- Tracking: titles +1 to +3; all-caps allowed for short section dividers.

## Layout & Spacing
- Grid: 12-column, 64px outer margin, 24px gutters.
- Spacing scale: 8, 12, 16, 24, 32, 48, 64.
- Safe area for citations: bottom-left 104px × full width; footers at 12–16px.

## Components
- Title slide
  - Full-bleed gradient; white H1; subtle text-shadow for contrast.
  - Optional translucent pill (white @ 8–12% alpha) for subtitle.
- Section divider
  - Left-aligned large H2; thin white hairline; small kicker above.
- Content slide
  - Left text, right chart/graphic; keep max 5 bullets.
  - Use white “card” (8–12% opacity) if readability over gradient is low.
- KPI slide
  - One large number (H1) with small label; minimal supporting text.
- Checklist/process
  - 3–5 steps with numbered pills (accent gradient fill, white text).
- Closing/thank-you
  - Return to full-bleed gradient; center aligned.

## Charts (static styling)
- Palette: bars/lines use `#FF5252`, `#FF6A00`, `#FFD166`, `#D900FF`.
- Gridlines light (`#EAECEF`); axes dark ink; labels medium.
- Bar radius 6–8px; line 3px; point 6px.
- Avoid 3D; keep 0–1 animation for web preview only.

## Imagery & Shapes
- Abstract radial bubbles: pink/orange circles with soft blur.
- Rounded rectangles for callouts (8–12px radius) with glass effect (white 10% alpha + backdrop blur if supported).

## Illustrations
- Purpose: clarify concepts and reduce text density; use sparingly (≤1 per slide).
- Style: abstract, geometric, or light isometric scenes; avoid heavy realism. Prefer vector/SVG when possible.
- Color: apply duotone/tint to match accents; keep contrast with background. Avoid mixing more than 3 accent hues per illustration.
- Placement: right column on content slides; full‑bleed on dividers; keep within safe area. Pair with a short caption if needed.
- Reuse: create a small set of reusable motifs (agent orchestration, roadmap, research synthesis, prototype‑first, evaluation) and repeat across the deck.
- Accessibility: ensure legible edges over gradients (add subtle card/backdrop).
- Licensing: use original, brand‑owned, or permissively licensed art (unDraw, OpenMoji, Iconoir). Track licenses in appendix.
- File guidance: SVG preferred; PNG @2x fallback; keep under 300KB per slide.

Illustration usage (examples)
- Strategy: a simple node‑graph motif tinted with accent gradient.
- Launch/GTM: timeline or checklist motif with numbered pills.
- Research: layered documents with magnifier motif; RoR shelf icon.
- Artifacts: wireframe/prototype blocks; code/design dual icons.
- Insights: sparkline + spotlight motif; callout card with delta arrows.

## Accessibility
- Check contrast: white text on gradient ≥ 4.5:1; add text-shadow.
- Provide dark text on white cards when gradient is intense.
- Font sizing min body 24px for projector readability.

## Citations
- On-slide footer (10–12pt) left-aligned; use bracketed keys [1][2]; full entries in appendix.

## File Map (this repo)
- `theme.css` — Reveal.js theme overrides (tokens and layout).
- `preview.html` — demo of the theme.
- `tokens.json` — color and type tokens (portable to PPT/Slides).

---

## Tokens (quick copy)
```
{
  "colors": {
    "accent1": "#FF3D81",
    "accent2": "#FF6A00",
    "accent3": "#FF2D55",
    "accent4": "#FFD166",
    "accent5": "#D900FF",
    "text": "#0C0D0F",
    "textMuted": "#60636B",
    "surface": "#FFFFFF",
    "gridline": "#EAECEF"
  },
  "fonts": {
    "title": "Poppins",
    "body": "Inter"
  },
  "sizes": {
    "h1": 68,
    "h2": 52,
    "h3": 34,
    "body": 26,
    "foot": 16
  }
}
```
