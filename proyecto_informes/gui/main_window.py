from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
)
from proyecto_informes.core.informes import leer_csv, leer_excel
import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Proyecto Informes")

        # Layout principal
        layout = QVBoxLayout()

        # Botón para cargar archivo
        self.btn_cargar = QPushButton("Cargar archivo CSV/Excel")
        self.btn_cargar.clicked.connect(self.cargar_archivo)

        layout.addWidget(self.btn_cargar)

        # Contenedor central
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def cargar_archivo(self):
        ruta, _ = QFileDialog.getOpenFileName(
        self,
        "Seleccionar archivo",
        "",
        "Archivos CSV;;Archivos Excel (*.xlsx *.xls)"
        )

        if not ruta:
            return # Usuario canceló

        try:
            if ruta.endswith(".csv"):
                df = leer_csv(ruta)
            else:
                df = leer_excel(ruta)

            # Mostrar en consola or ahora
            print(df.head())

            QMessageBox.information(self, "Éxito", "Archivo cargado correctamente.")

        except Execption as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar el archivo:\n{e}")