"""
18 — Text to video (text → video).

Same idea as 17_hf_image_demo.py but outputs a short MP4.
Much heavier — GPU strongly recommended.

Requirements:
  pip install -r 18_hf_requirements.txt

Usage:
  python 18_hf_video_demo.py "a bird flying over the ocean"
  python 18_hf_video_demo.py

First run downloads model weights (several GB).
"""

import sys
from pathlib import Path

OUTPUT = Path(__file__).resolve().parent / "generated_video.mp4"
DEFAULT_PROMPT = "a cat eating rets from a plan has rats as fruits."
MODEL_ID = "cerspense/zeroscope_v2_576w"


def main() -> None:
    prompt = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PROMPT
    print(f"Prompt: {prompt}")
    print(f"Model:  {MODEL_ID}")
    print("Loading pipeline (first run downloads weights)...\n")

    try:
        import torch
        from diffusers import DiffusionPipeline
        from diffusers.utils import export_to_video
    except ImportError:
        print("Install deps first:")
        print("  pip install -r 18_hf_requirements.txt")
        sys.exit(1)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32
    print(f"Device: {device}")
    if device == "cpu":
        print("Warning: text-to-video on CPU is very slow and needs lots of RAM.\n")
    else:
        print()

    pipe = DiffusionPipeline.from_pretrained(MODEL_ID, torch_dtype=dtype)

    # enable_model_cpu_offload() is for GPU VRAM saving and requires `accelerate`.
    # On plain CPU, just load everything on CPU with .to("cpu").
    if device == "cuda":
        pipe = pipe.to(device)
    else:
        pipe = pipe.to("cpu")

    steps = 25 if device == "cuda" else 8
    height = 320 if device == "cuda" else 256
    width = 576 if device == "cuda" else 384
    print(f"Generating video ({steps} steps, {width}x{height})...")

    result = pipe(
        prompt,
        num_inference_steps=25,
        height=height,
        width=width,
    )
    frames = result.frames[0]

    export_to_video(frames, str(OUTPUT), fps=8)
    print(f"Saved: {OUTPUT}")
    print(f"Frames: {len(frames)}")


if __name__ == "__main__":
    main()
