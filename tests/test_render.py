"""Tests for the OpenCV illustration pipeline (assets/render/process.py)."""

import importlib.util
import pathlib

import cv2
import numpy as np
import pytest

# Load the module by path (assets/ is not a package).
_SPEC_PATH = pathlib.Path(__file__).resolve().parent.parent / "assets" / "render" / "process.py"
_spec = importlib.util.spec_from_file_location("render_process", _SPEC_PATH)
process = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(process)


def _white(h, w):
    return np.full((h, w, 3), 255, dtype=np.uint8)


def test_crop_to_content_trims_white_border():
    img = _white(100, 100)
    img[40:60, 30:70] = (0, 0, 0)  # a black block in the middle
    cropped = process.crop_to_content(img)
    assert cropped.shape[:2] == (20, 40)


def test_crop_to_content_handles_blank_image():
    img = _white(50, 50)
    assert process.crop_to_content(img).shape[:2] == (50, 50)


def test_to_bgr_on_white_flattens_alpha():
    rgba = np.zeros((10, 10, 4), dtype=np.uint8)  # fully transparent
    out = process.to_bgr_on_white(rgba)
    assert out.shape == (10, 10, 3)
    assert (out == 255).all()  # transparent -> white


def test_fit_square_produces_target_size():
    img = _white(40, 80)
    img[:, :] = (10, 20, 30)
    out = process.fit_square(img, 256)
    assert out.shape == (256, 256, 3)


def test_process_image_size_and_frame():
    src = _white(300, 300)
    src[100:200, 100:200] = (0, 0, 0)
    out = process.process_image(src, size=256)
    assert out.shape == (256, 256, 3)
    # top-left corner pixel should be the accent frame color, not white
    assert tuple(int(c) for c in out[0, 0]) == process.FRAME_BGR
