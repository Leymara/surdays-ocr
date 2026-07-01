from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QPushButton,
    QLabel,
    QFileDialog,
    QMessageBox,
)

from PySide6.QtCore import Qt

from core.pdf_manager import PDFManager
from core.ocr_manager import OCRManager


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.pdf = PDFManager()
        self.ocr = OCRManager()

        self.ruta_pdf = None

        self.setWindowTitle("SURDAYS OCR")
        self.resize(1300, 750)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        # ==========================
        # Menú lateral
        # ==========================

        menu = QListWidget()

        menu.addItems([
            "📄 OCR PDF",
            "📊 Excel",
            "📁 CSV Gesfincas",
            "⚙ Configuración"
        ])

        menu.setMaximumWidth(220)

        # ==========================
        # Zona principal
        # ==========================

        derecha = QVBoxLayout()

        titulo = QLabel("SURDAYS OCR")
        titulo.setStyleSheet("font-size:24px;font-weight:bold;")

        self.boton_pdf = QPushButton("Seleccionar PDF")
        self.boton_pdf.clicked.connect(self.abrir_pdf)

        self.boton_ocr = QPushButton("Procesar OCR")
        self.boton_ocr.clicked.connect(self.procesar_ocr)

        self.info = QLabel("Seleccione un PDF para comenzar.")

        self.preview = QLabel()
        self.preview.setAlignment(Qt.AlignCenter)
        self.preview.setMinimumSize(500, 650)

        derecha.addWidget(titulo)
        derecha.addWidget(self.boton_pdf)
        derecha.addWidget(self.boton_ocr)
        derecha.addWidget(self.info)
        derecha.addWidget(self.preview)
        derecha.addStretch()

        layout.addWidget(menu)
        layout.addLayout(derecha)

    def abrir_pdf(self):

        archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar PDF",
            "",
            "PDF (*.pdf)"
        )

        if not archivo:
            return

        self.ruta_pdf = archivo

        datos = self.pdf.obtener_info(archivo)

        self.info.setText(
            f"""Archivo:
{datos['nombre']}

Páginas:
{datos['paginas']}

Tamaño:
{datos['tamano_mb']} MB

Estado:
✅ PDF cargado correctamente
"""
        )

        imagen = self.pdf.obtener_primera_pagina(archivo)

        self.preview.setPixmap(
            imagen.scaled(
                450,
                600,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

    def procesar_ocr(self):

        if self.ruta_pdf is None:

            QMessageBox.warning(
                self,
                "Aviso",
                "Primero seleccione un PDF."
            )

            return

        texto = self.ocr.leer_primera_pagina(self.ruta_pdf)

        QMessageBox.information(
            self,
            "Resultado OCR",
            texto[:3500]
        )
