from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QPushButton,
    QLabel,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("SURDAYS ERP")
        self.resize(1200, 700)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        # Menú lateral
        menu = QListWidget()
        menu.addItems([
            "🏠 Dashboard",
            "📄 OCR",
            "💰 Contabilidad",
            "📊 Gesfincas",
            "👤 Propietarios",
            "⚙ Configuración"
        ])
        menu.setMaximumWidth(250)

        # Zona principal
        derecha = QVBoxLayout()

        titulo = QLabel("Bienvenido a SURDAYS ERP")
        titulo.setStyleSheet("font-size:24px;font-weight:bold;")

        boton = QPushButton("Seleccionar PDF")

        derecha.addWidget(titulo)
        derecha.addWidget(boton)
        derecha.addStretch()

        layout.addWidget(menu)
        layout.addLayout(derecha)
