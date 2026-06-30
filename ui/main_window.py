from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QPushButton,
    QLabel,
    QFileDialog,
)

from core.pdf_manager import PDFManager


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.pdf = PDFManager()

        self.setWindowTitle("SURDAYS OCR")
        self.resize(1200, 700)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        # ===== Menú lateral =====
        menu = QListWidget()
        menu.addItems([
            "📄 OCR PDF",
            "📊 Excel",
            "📁 CSV Gesfincas",
            "⚙ Configuración"
        ])
        menu.setMaximumWidth(220)

        # ===== Zona principal =====
        derecha = QVBoxLayout()

        titulo = QLabel("SURDAYS OCR")
        titulo.setStyleSheet("font-size:24px;font-weight:bold;")

        self.boton_pdf = QPushButton("Seleccionar PDF")
        self.boton_pdf.clicked.connect(self.abrir_pdf)

        self.info = QLabel(
            "Seleccione un PDF para comenzar."
        )

        derecha.addWidget(titulo)
        derecha.addWidget(self.boton_pdf)
        derecha.addWidget(self.info)
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

        datos = self.pdf.obtener_info(archivo)

        self.info.setText(
            f"""
Archivo:
{datos["nombre"]}

Páginas:
{datos["paginas"]}

Tamaño:
{datos["tamano_mb"]} MB

Estado:
✅ PDF cargado correctamente
"""
        )
