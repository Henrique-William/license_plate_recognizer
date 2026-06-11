import cv2
import os
import easyocr

from models.tesseract_run import run_tesseract
from pre_processing import detect_plate, preprocess_for_ocr
from models.easyocr_run import run_easyocr

if __name__ == "__main__":
    dataset_path = "placas_exercicio"
    output_path = "resultados"

    roi_path = os.path.join(output_path, "placas_extraidas")
    detected_path = os.path.join(output_path, "imagens_detectadas")
    processed_path = os.path.join(output_path, "placas_processadas")

    os.makedirs(output_path, exist_ok=True)
    os.makedirs(roi_path, exist_ok=True)
    os.makedirs(detected_path, exist_ok=True)
    os.makedirs(processed_path, exist_ok=True)

    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")

    # Reader em inglês foi o melhor resultado obtido. O modelo em português estava "alucinando" nos números
    reader = easyocr.Reader(["en"], gpu=False)

    tesseract_file = open(os.path.join(output_path, "tesseract_results.txt"), "w", encoding="utf-8")
    easyocr_file = open(os.path.join(output_path, "easyocr_results.txt"), "w", encoding="utf-8")

    for image_name in os.listdir(dataset_path):

        image_path = os.path.join(dataset_path, image_name)
        image = cv2.imread(image_path)

        if image is None:
            continue

        base_name = os.path.splitext(image_name)[0]
        plate = detect_plate(image, detector)

        if plate is None:
            tesseract_file.write(f"{image_name} -> PLACA_NAO_DETECTADA\n")
            easyocr_file.write(f"{image_name} -> PLACA_NAO_DETECTADA\n")

            continue

        # Extraindo ROI da placa
        x, y, w, h = plate

        plate_roi = image[y:y + h, x:x + w]

        roi_h, roi_w = plate_roi.shape[:2]

        # Cortando as bordas da placa
        top = int(roi_h * 0.18)
        bottom = int(roi_h * 0.08)

        left = int(roi_w * 0.05)
        right = int(roi_w * 0.05)

        plate_roi = plate_roi[
            top:roi_h - bottom,
            left:roi_w - right
        ]

        h_roi = plate_roi.shape[0]

        plate_roi = plate_roi[
            int(h_roi * 0.12):,
            :
        ]

        cv2.imwrite(os.path.join(roi_path, f"{base_name}_roi.png"), plate_roi)

        # Chamada da função de pré-processamento
        processed_plate = preprocess_for_ocr(plate_roi)

        cv2.imwrite(os.path.join(processed_path, f"{base_name}_processed.png"), processed_plate)

        # OCR TESSERACT
        text_tesseract = run_tesseract(processed_plate)

        tesseract_file.write(f"{image_name} -> {text_tesseract}\n")

        # OCR EASYOCR
        text_easyocr = run_easyocr(processed_plate, reader)

        easyocr_file.write(f"{image_name} -> {text_easyocr}\n")

        detected = image.copy()

        cv2.rectangle(detected, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imwrite(os.path.join(detected_path, f"{base_name}_detected.png"), detected)

        print(f"{image_name} | " f"Tesseract={text_tesseract} | " f"EasyOCR={text_easyocr}")

    tesseract_file.close()
    easyocr_file.close()

    print("\nProcessamento finalizado.")