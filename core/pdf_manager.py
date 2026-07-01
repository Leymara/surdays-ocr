from pathlib import Path
import fitz
from PySide6.QtGui import QPixmap, QImage


class PDFManager:

    def obtener_info(self, ruta_pdf):

        ruta = Path(ruta_pdf)

        documento = fitz.open(ruta_pdf)

        return {
            "nombre": ruta.name,
            "ruta": str(ruta),
            "paginas": documento.page_count,
            "tamano_mb": round(ruta.stat().st_size / (1024 * 1024), 2),
        }

    def obtener_primera_pagina(self, ruta_pdf):

        documento = fitz.open(ruta_pdf)

        pagina = documento.load_page(0)

        pix = pagina.get_pixmap(matrix=fitz.Matrix(2, 2))

        imagen = QImage(
            pix.samples,
            pix.width,
            pix.height,
            pix.stride,
            QImage.Format.Format_RGB888,
        )

        return QPixmap.fromImage(imagen.copy())
