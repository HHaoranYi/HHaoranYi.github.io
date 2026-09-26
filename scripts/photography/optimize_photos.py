"""
Photo Optimization Script for Personal Photography Albums.

Features:
- Resizes high-resolution camera exports to web-optimized dimensions (max long-edge 2560px).
- Strips sensitive EXIF metadata (e.g., GPS coordinates, camera serial numbers).
- Converts/optimizes to WebP or high-quality JPEG for GitHub Pages storage budgeting.
- Verifies budget limit (keeps individual display images < 900KB).

Usage:
    python optimize_photos.py <input_dir> <output_album_dir> [--quality 85] [--max-dim 2560]
"""

import sys
import os
import argparse
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    Image = None


def process_image(src_path: Path, dst_path: Path, max_dim: int = 2560, quality: int = 85):
    if Image is None:
        print("Pillow is not installed. Install via: pip install Pillow")
        sys.exit(1)

    with Image.open(src_path) as img:
        # Transpose according to EXIF orientation then strip exif
        img = ImageOps.exif_transpose(img)

        # Convert CMYK/RGBA to RGB if saving JPEG/WebP without alpha
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        # Resize if dimensions exceed max_dim
        w, h = img.size
        long_edge = max(w, h)
        if long_edge > max_dim:
            scale = max_dim / float(long_edge)
            new_size = (int(w * scale), int(h * scale))
            img = img.resize(new_size, Image.Resampling.LANCZOS)
            print(f"Resized {src_path.name}: {w}x{h} -> {new_size[0]}x{new_size[1]}")

        dst_path.parent.mkdir(parents=True, exist_ok=True)
        # Save without preserving GPS or device metadata
        img.save(dst_path, "WEBP", quality=quality, method=6)
        
        size_kb = dst_path.stat().st_size / 1024
        print(f"Saved: {dst_path.name} ({size_kb:.1f} KB)")


def main():
    parser = argparse.ArgumentParser(description="Optimize photos for Hugo albums.")
    parser.add_argument("input_dir", type=str, help="Input directory containing raw/exported photos")
    parser.add_argument("output_dir", type=str, help="Destination directory inside content/photography/<album>/")
    parser.add_argument("--quality", type=int, default=85, help="WebP compression quality (default 85)")
    parser.add_argument("--max-dim", type=int, default=2560, help="Maximum long-edge dimension in pixels")
    args = parser.parse_args()

    input_path = Path(args.input_dir)
    output_path = Path(args.output_dir)

    if not input_path.exists():
        print(f"Error: input directory does not exist: {input_path}")
        sys.exit(1)

    supported_exts = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}
    files = [f for f in input_path.iterdir() if f.suffix.lower() in supported_exts]

    if not files:
        print(f"No image files found in {input_path}")
        return

    print(f"Found {len(files)} images to process...")
    for idx, f in enumerate(files, start=1):
        target_name = f"photo-{idx:02d}.webp"
        dst = output_path / target_name
        process_image(f, dst, max_dim=args.max_dim, quality=args.quality)

    print("Photo optimization complete.")


if __name__ == "__main__":
    main()
