from pathlib import Path
import fitz  # PyMuPDF


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
