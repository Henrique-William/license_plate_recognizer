# Vehicle License Plate Recognizer

**[EN]** This directory contains a university project focused on detecting vehicle license plates from photos. The goal is to use and compare tools like EasyOCR and Tesseract in the recognition and extraction of text (String) from the images.

___

**[PT]** Este diretório contém um projeto universitário focado na detecção de placas de veículos a partir de fotos. O objetivo é utilizar e comparar ferramentas como EasyOCR e Tesseract no reconhecimento e na extração de texto (String) das imagens.

## Author

- [Henrique William Oliveira da Silva](https://github.com/Henrique-William) - RA: 220021662 

## Installation & Execution

This project was developed and executed using WSL (Ubuntu). Follow the steps below to set up the environment and run the project:

1. Update your packages and install Tesseract along with the Portuguese language pack:
    ```bash
    sudo apt update
    sudo apt install tesseract-ocr tesseract-ocr-por
    ```
2. Access the **.venv** environment:
    ```bash
   source .venv/bin/activate
   ```

3. Install the required Python libraries:
    ```bash
    pip install opencv-python pytesseract easyocr matplotlib 
    ```

4. Execute the main script:
        
    ```bash
    python3 main.py    
    ```