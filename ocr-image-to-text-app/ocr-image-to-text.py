from pathlib import Path
import pytesseract
from PIL import Image, UnidentifiedImageError


def extract_text_from_image(image_path: str | Path) -> str:
    """Extracts and returns text from a given image file."""
    path = Path(image_path)

    if not path.is_file():
        raise FileNotFoundError(f"Image not found at: {path}")

    try:
        with Image.open(path) as img:
            gray_img = img.convert("L")
            return pytesseract.image_to_string(gray_img).strip()

    except UnidentifiedImageError:
        raise ValueError(f"The file at '{path}' is not a valid or supported image.")


if __name__ == "__main__":
    try:
        extracted_text = extract_text_from_image("image.jpg")
        print(extracted_text)
    except Exception as e:
        print(f"Error: {e}")
