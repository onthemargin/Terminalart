"""Rasterize hand-authored SVG sources to raw PNGs, using headless Chromium.

svg/<animal>.svg  ->  raw/<animal>.png   (1024x1024, white background)

The SVGs in assets/render/svg/ are the committed, human-readable "source" for
each illustration; this step turns them into the raw bitmaps that process.py
then crops, normalizes, and frames. Chromium is used because it needs no extra
Python/system libraries beyond the browser already present on the box.

Usage:  python assets/render/render_svg.py
See assets/render/prompt.md for the full pipeline.
"""
from __future__ import annotations

import pathlib
import shutil
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
SVG_DIR = HERE / "svg"
RAW_DIR = HERE / "raw"
SIZE = 1024

CHROMIUM = shutil.which("chromium") or shutil.which("chromium-browser") or shutil.which("google-chrome")


def render(svg_path: pathlib.Path, out_path: pathlib.Path, size: int = SIZE) -> None:
    if not CHROMIUM:
        sys.exit("no chromium/chrome found on PATH")
    subprocess.run(
        [
            CHROMIUM, "--headless=new", "--no-sandbox", "--disable-gpu",
            "--force-device-scale-factor=1", "--hide-scrollbars",
            "--default-background-color=FFFFFFFF",
            f"--window-size={size},{size}",
            f"--screenshot={out_path}",
            svg_path.as_uri(),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    svgs = sorted(SVG_DIR.glob("*.svg"))
    if not svgs:
        print(f"no svg sources in {SVG_DIR}")
        return
    for svg in svgs:
        out = RAW_DIR / (svg.stem + ".png")
        render(svg, out)
        print(f"{svg.name} -> {out.relative_to(HERE)}")


if __name__ == "__main__":
    main()
