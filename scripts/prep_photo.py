import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image
from rembg import remove


def prep_photo(input_path):
    input_path = Path(input_path)
    output_path = input_path.with_name("source-prepped.png")

    print(f"Loading: {input_path}")

    # Remove background
    image = Image.open(input_path).convert("RGBA")
    cutout = remove(image)

    # White background
    background = Image.new("RGBA", cutout.size, (255, 255, 255, 255))
    composited = Image.alpha_composite(background, cutout)

    # Convert to grayscale
    rgb = composited.convert("RGB")
    img = np.array(rgb)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Improve local contrast
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(gray)

    # Slightly soften noise
    enhanced = cv2.GaussianBlur(enhanced, (3, 3), 0)

    result = Image.fromarray(enhanced)

    result.save(output_path)

    print(f"Saved: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/prep_photo.py source-photo.png")
        sys.exit(1)

    prep_photo(sys.argv[1])
