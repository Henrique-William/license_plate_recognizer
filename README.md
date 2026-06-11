# Vehicle License Plate Recognizer
Este diretório contém um projeto universitário focado na detecção de placas de veículos a partir de fotos. O objetivo é utilizar e comparar ferramentas como EasyOCR e Tesseract no reconhecimento e na extração de texto (String) das imagens.

## Relatório de Desempenho
Foi realizada uma avaliação utilizando um dataset de 20 imagens de placas para comparar a eficácia do EasyOCR e do Tesseract. Duas métricas principais foram avaliadas:
1. **Reconhecimento da Placa:** A capacidade do motor OCR de detectar padrões de texto/placa na imagem recortada.
2. **Precisão da Leitura:** A correspondência exata do texto extraído com a placa real.

| Métrica | EasyOCR | Tesseract |
| :--- | :---: | :---: |
| **Reconhecimento da Placa** | 20/20 (100%) | 11/20 (55%) |
| **Precisão da Leitura** | 11/20 (55%) | 8/20 (40%) |

**Observação:** As imagens 5 e 10 apresentaram problemas durante a etapa de extração da ROI (Região de Interesse), o que impactou negativamente a precisão da leitura nestes casos. De forma geral, o EasyOCR demonstrou um desempenho superior tanto na detecção quanto na leitura correta dos caracteres neste projeto.

## Conclusão
Com base nos resultados experimentais, o **EasyOCR** provou ser o modelo superior para este pipeline específico de reconhecimento de placas veiculares. Enquanto alcançou uma **taxa de detecção perfeita de 100%** para localizar as regiões de texto, o **Tesseract** enfrentou dificuldades, identificando apenas **55%** das placas. Em termos de precisão na leitura dos caracteres, o EasyOCR também liderou com **55%** contra **40%** do Tesseract.

Uma conclusão crucial deste projeto é o impacto da fase de Pré-processamento e Segmentação (ROI). Os problemas encontrados nas imagens 5 e 10 demonstram que se o Haar Cascade falhar em isolar a placa perfeitamente, a precisão do OCR subsequente cai drasticamente. Como melhorias futuras, a substituição do Haar Cascade tradicional por um detetor baseado em deep learning (como o YOLO) e o ajuste fino (*fine-tuning*) dos motores de OCR especificamente para fontes do padrão Mercosul seriam os passos ideais para aproximar o sistema de um nível de produção profissional.

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