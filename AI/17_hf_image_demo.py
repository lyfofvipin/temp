"""
16 (optional) — Hugging Face image generation.

NOT the same as 12_hg_model_bot.py (which is text-generation only).

Requirements (uncomment in 16_langchain_requirements.txt):
  pip install torch diffusers accelerate transformers

Usage:
  python 16_hf_image_demo.py "a cat astronaut on the moon"
  python 16_hf_image_demo.py   # default prompt

CPU works but is VERY slow. GPU strongly recommended.
"""

import sys
from pathlib import Path

OUTPUT = Path(__file__).resolve().parent / "generated_image.png"
DEFAULT_PROMPT = "a watercolor painting of mountains at sunset"
MODEL_ID = "stabilityai/sd-turbo"  # smaller / faster than full SD


def main() -> None:
    prompt = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PROMPT
    print(f"Prompt: {prompt}")
    print(f"Model:  {MODEL_ID}")
    print("Loading pipeline (first run downloads weights)...\n")

    try:
        import torch
        from diffusers import AutoPipelineForText2Image
    except ImportError:
        print("Install image deps first:")
        print("  pip install torch diffusers accelerate transformers")
        sys.exit(1)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32
    print(f"Device: {device} (CPU image gen can take many minutes)\n")

    pipe = AutoPipelineForText2Image.from_pretrained(
        MODEL_ID,
        torch_dtype=dtype,
        variant="fp16" if device == "cuda" else None,
    )
    pipe = pipe.to(device)

    image = pipe(prompt, num_inference_steps=4 if device == "cuda" else 2).images[0]
    image.save(OUTPUT)
    print(f"Saved: {OUTPUT}")


if __name__ == "__main__":
    main()
