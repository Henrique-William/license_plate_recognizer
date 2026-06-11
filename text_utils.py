import re

def clean_plate_text(text):
    text = re.sub(r"[^A-Z0-9]", "", text.upper())
    mercosul = re.search(r"[A-Z]{3}[0-9][A-Z][0-9]{2}", text)

    if mercosul:
        return mercosul.group(0)

    return text