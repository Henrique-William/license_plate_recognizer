import pytesseract

from text_utils import clean_plate_text

def run_tesseract(image):
    config = (
        "--oem 3 "
        "--psm 7 "
        "-c tessedit_char_whitelist="
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    )

    text = pytesseract.image_to_string(image, config=config)

    return clean_plate_text(text)