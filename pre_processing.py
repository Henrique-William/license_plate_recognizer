import cv2

# PRÉ-PROCESSAMENTO
def preprocess_for_ocr(image):

    h, w = image.shape[:2]
    scale = 300 / h

    image = cv2.resize(image,(int(w * scale), 300), interpolation=cv2.INTER_CUBIC
    )

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Usando gaussian blur para suavizar as bordas
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    # Melhorando o contraste com o CLAHE. Sem isso, as fotos com placa na sombra ou com o farol estourado não passavam na binarização.
    clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(8, 8))

    gray = clahe.apply(gray)

    # treshold para corte da imagem
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

    # Suaviza pequenas falhas das letras
    binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=1)

    # remove ruídos pequenos
    binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)

    return binary

def detect_plate(image, detector):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    plates = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=3, minSize=(50, 15))

    if len(plates) == 0:
        return None

    plates = sorted(plates, key=lambda p: p[2] * p[3], reverse=True)

    return plates[0]