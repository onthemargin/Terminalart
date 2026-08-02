# Animal illustrations — generation + render pipeline

The gallery shows each animal's **ASCII art** side-by-side with a rendered
**illustration**. The illustrations are pre-rendered once and committed as static
PNGs under `assets/images/`; nothing runs at request time. This document lets
anyone reproduce them.

## Pipeline

```
Fable (draws SVG)   →  assets/render/svg/<animal>.svg   (committed, human-readable source)
        │ render_svg.py (headless Chromium)
        ▼
raw bitmap          →  assets/render/raw/<animal>.png   (1024x1024, white bg)
        │ process.py (OpenCV)
        ▼
final illustration  →  assets/images/<animal>.png       (normalized + framed, committed, served)
```

> **Why SVG, not a raster image model?** The intent was to have Fable *draw* each
> animal. On this box the Vertex AI image endpoints are unavailable to the deploy
> service account (403 on `aiplatform.endpoints.predict`), so Fable instead
> hand-authors a vector **SVG** for each animal, which Chromium rasterizes. This
> is actually better for reproduction: the "source" is committed, human-readable,
> deterministic, and needs no cloud API or keys — just a browser.

## Step 1 — Fable draws each animal as SVG

Model: `claude-fable-5`. One SVG per animal. Prompt template (swap `<ANIMAL>`):

> Create a hand-authored SVG illustration of a single cute cartoon **<ANIMAL>**,
> front-facing, centered, as a friendly kid-friendly mascot.
>
> Style requirements:
> - viewBox 0 0 1024 1024, square
> - Simple, clean cartoon/sticker style with bold DARK outlines and flat fill colors
> - Solid pure-white background rect (#FFFFFF) covering the whole canvas, no scenery,
>   no text, no ground shadow
> - The whole animal fully visible with comfortable margin (~70-80% of the canvas)
> - Cheerful, adorable, appealing to young children
>
> Verify by rendering to PNG with headless Chromium and inspecting; iterate until cute.

Animals (must match the registry keys in `main.js` / `generators/`):
`dog, cat, bird, fish, butterfly, rabbit, snake, frog, owl`

Output: `assets/render/svg/<animal>.svg`

## Step 2 — Rasterize the SVGs

```
python assets/render/render_svg.py     # svg/*.svg -> raw/*.png (1024², white bg)
```

Uses headless Chromium (already on the box); no extra Python deps.

## Step 3 — Finish with OpenCV

```
pip install -r assets/render/requirements-render.txt   # opencv + numpy
python assets/render/process.py                        # raw/*.png -> assets/images/*.png
```

`process.py` (OpenCV 4.x), for each raw image:
1. **Crop** — trim the white background to the animal's bounding box.
2. **Normalize** — center on a square white canvas, resize to 512×512.
3. **Frame** — draw a border in the site accent color (#4fc3f7) to match the terminal look.
4. **Convert/optimize** — write an optimized PNG to `assets/images/<animal>.png`.

Steps 2–3 are idempotent: re-running rebuilds `raw/` and `assets/images/` from the SVGs.
```
python assets/render/render_svg.py && python assets/render/process.py
```
