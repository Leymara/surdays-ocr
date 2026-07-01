import io

import fitz
import pytesseract
from PIL import Image

from core.parser import Parser

# Ruta de Tesseract
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Archivos de programa\Tesseract-OCR\tesseract.exe"
)


class OCRManager:

    def __init__(self):
        self.parser = Parser()

    def procesar_pdf(self, ruta_pdf):

        documento = fitz.open(ruta_pdf)

        pagina = documento.load_page(0)

        pix = pagina.get_pixmap(matrix=fitz.Matrix(4, 4))

        imagen = Image.open(io.BytesIO(pix.tobytes("png")))

        texto = pytesseract.image_to_string(
            imagen,
            lang="eng"
        )

        documento.close()

        return self.parser.analizar(texto)
