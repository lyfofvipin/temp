"""
18 — Read text from images (image → text).

Two modes:
  caption — describe what is in the image (image-to-text)
  ocr     — read written text from the image (TrOCR)

Same pattern as 17_hf_image_demo.py, opposite direction.

Requirements:
  pip install -r 18_hf_requirements.txt

Usage:
  python 18_hf_image_to_text_demo.py caption photo.jpg
  python 18_hf_image_to_text_demo.py ocr screenshot.png
  python 18_hf_image_to_text_demo.py ocr          # built-in sample with text
"""

import sys
from pathlib import Path

CAPTION_MODEL = "Salesforce/blip-image-captioning-base"
OCR_MODEL = "microsoft/trocr-base-printed"
SAMPLE_IMAGE = Path(__file__).resolve().parent / "sample_ocr_image.png"


def make_sample_image() -> Path:
    """Create a simple image with text for OCR demo."""
    from PIL import Image, ImageDraw

    img = Image.new("RGB", (420, 120), color="white")
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, 410, 110], outline="black", width=2)
    draw.text((30, 45), "Hello from XYZ ORG — Invoice #1234", fill="black")
    img.save(SAMPLE_IMAGE)
    return SAMPLE_IMAGE


def run_caption(image_path: Path) -> None:
    from transformers import pipeline

    print(f"Mode:   caption (what is in the image?)")
    print(f"Model:  {CAPTION_MODEL}")
    print(f"Image:  {image_path}\n")

    captioner = pipeline("image-to-text", model=CAPTION_MODEL)
    result = captioner(str(image_path))
    text = result[0]["generated_text"] if result else "(no output)"
    print(f"Caption:\n{text}")


def run_ocr(image_path: Path) -> None:
    from transformers import pipeline

    print(f"Mode:   ocr (read exact text)")
    print(f"Model:  {OCR_MODEL}")
    print(f"Image:  {image_path}\n")

    reader = pipeline("image-to-text", model=OCR_MODEL)
    result = reader(str(image_path))
    text = result[0]["generated_text"] if result else "(no output)"
    print(f"Read text:\n{text}")


def main() -> None:
    try:
        from PIL import Image  # noqa: F401
        from transformers import pipeline  # noqa: F401
    except ImportError:
        print("Install deps first:")
        print("  pip install -r 18_hf_requirements.txt")
        sys.exit(1)

    mode = (sys.argv[1] if len(sys.argv) > 1 else "ocr").lower()

    if len(sys.argv) > 2:
        image_path = Path(sys.argv[2])
        if not image_path.exists():
            print(f"File not found: {image_path}")
            sys.exit(1)
    else:
        if mode == "ocr":
            image_path = make_sample_image()
            print(f"Created sample image: {image_path}\n")
        else:
            print("Usage: python 18_hf_image_to_text_demo.py caption path/to/image.jpg")
            sys.exit(1)

    if mode == "caption":
        run_caption(image_path)
    elif mode == "ocr":
        run_ocr(image_path)
    else:
        print("Usage: python 18_hf_image_to_text_demo.py [caption|ocr] [image_path]")
        sys.exit(1)


if __name__ == "__main__":
    main()
