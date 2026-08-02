"""OpenCV post-processing for Fable-generated animal illustrations.

Reads raw square PNGs from assets/render/raw/, and for each:
  crop to content -> normalize onto a square canvas -> draw a frame -> optimize.
Writes the result to assets/images/<animal>.png (committed, served statically).

Usage:  python assets/render/process.py
See assets/render/prompt.md for the full pipeline + Fable prompt.
"""
from __future__ import annotations

import pathlib

import cv2
import numpy as np

# --- config -----------------------------------------------------------------
HERE = pathlib.Path(__file__).resolve().parent
RAW_DIR = HERE / "raw"
OUT_DIR = HERE.parent / "images"

TARGET_SIZE = 512          # final square edge, px
CONTENT_MARGIN = 0.06      # blank margin kept around the animal, fraction of edge
FRAME_THICKNESS = 6        # border width, px
FRAME_BGR = (247, 195, 79)  # site accent #4fc3f7, in OpenCV BGR order
BG_WHITE = (255, 255, 255)
BG_THRESHOLD = 245         # a pixel with every channel >= this counts as background


def to_bgr_on_white(img: np.ndarray) -> np.ndarray:
    """Flatten any BGR/BGRA/gray image onto a solid white background as BGR."""
    if img.ndim == 2:
        return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    if img.shape[2] == 4:
        bgr = img[:, :, :3].astype(np.float32)
        alpha = (img[:, :, 3:4].astype(np.float32)) / 255.0
        white = np.full_like(bgr, 255.0)
        blended = bgr * alpha + white * (1.0 - alpha)
        return blended.round().astype(np.uint8)
    return img


def crop_to_content(img: np.ndarray, threshold: int = BG_THRESHOLD) -> np.ndarray:
    """Trim the white background to the tight bounding box of the subject."""
    fg = np.any(img < threshold, axis=2)  # True where a pixel is non-white
    rows = np.any(fg, axis=1)
    cols = np.any(fg, axis=0)
    if not rows.any() or not cols.any():
        return img  # entirely blank; nothing to crop
    y0, y1 = np.where(rows)[0][[0, -1]]
    x0, x1 = np.where(cols)[0][[0, -1]]
    return img[y0:y1 + 1, x0:x1 + 1]


def fit_square(img: np.ndarray, size: int, margin: float = CONTENT_MARGIN) -> np.ndarray:
    """Center img on a white square canvas of `size`, keeping a blank margin."""
    inner = max(1, int(round(size * (1.0 - 2.0 * margin))))
    h, w = img.shape[:2]
    scale = inner / max(h, w)
    new_w, new_h = max(1, round(w * scale)), max(1, round(h * scale))
    interp = cv2.INTER_AREA if scale < 1 else cv2.INTER_CUBIC
    resized = cv2.resize(img, (new_w, new_h), interpolation=interp)

    canvas = np.full((size, size, 3), BG_WHITE, dtype=np.uint8)
    y = (size - new_h) // 2
    x = (size - new_w) // 2
    canvas[y:y + new_h, x:x + new_w] = resized
    return canvas


def add_frame(img: np.ndarray, thickness: int = FRAME_THICKNESS,
              color: tuple[int, int, int] = FRAME_BGR) -> np.ndarray:
    """Draw an inset border in the site accent color."""
    out = img.copy()
    h, w = out.shape[:2]
    cv2.rectangle(out, (0, 0), (w - 1, h - 1), color, thickness)
    return out


def process_image(src: np.ndarray, size: int = TARGET_SIZE) -> np.ndarray:
    """Full pipeline on a single decoded image."""
    bgr = to_bgr_on_white(src)
    cropped = crop_to_content(bgr)
    squared = fit_square(cropped, size)
    return add_frame(squared)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    raws = sorted(RAW_DIR.glob("*.png"))
    if not raws:
        print(f"no raw images in {RAW_DIR}")
        return
    for path in raws:
        img = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
        if img is None:
            print(f"skip (unreadable): {path.name}")
            continue
        out = process_image(img)
        dst = OUT_DIR / path.name
        cv2.imwrite(str(dst), out, [cv2.IMWRITE_PNG_COMPRESSION, 9])
        print(f"{path.name}: {img.shape[1]}x{img.shape[0]} -> {out.shape[1]}x{out.shape[0]}")


if __name__ == "__main__":
    main()
