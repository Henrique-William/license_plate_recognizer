from text_utils import clean_plate_text

def run_easyocr(image, reader):

    result = reader.readtext(image, detail=0)
    text = " ".join(result)

    return clean_plate_text(text)