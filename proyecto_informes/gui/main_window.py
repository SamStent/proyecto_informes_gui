from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox, QTableView
)
from proyecto_informes.core.informes import leer_csv, leer_excel
from proyecto_informes.gui.table_model import DataFrameModel
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

        # Botón de exportar archivo
        self.btn_exportar = QPushButton("Exportar DataFrame")
        self.btn_exportar.clicked.connect(self.exportar_archivo)
        layout.addWidget(self.btn_exportar)

        layout.addWidget(self.btn_cargar)

        self.table = QTableView()
        layout.addWidget(self.table)

        # Contenedor central
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def cargar_archivo(self):
        ruta, _ = QFileDialog.getOpenFileName(
        self,
        "Seleccionar archivo",
        "",
        "Todos los archivos soportados (*.csv *.xlsx *.xls);;CSV (*.csv);;Excel (*.xlsx *.xls)"
        )

        if not ruta:
            return # Usuario canceló

        try:
            if ruta.endswith(".csv"):
                df = leer_csv(ruta)
            else:
                df = leer_excel(ruta)

            # Guardar el DataFrame en la instancia
            self.df = df

            # Mostrar en consola or ahora
            modelo = DataFrameModel(df)
            self.table.setModel(modelo)
            # print(df.head())

            QMessageBox.information(self, "Éxito", "Archivo cargado correctamente.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar el archivo:\n{e}")

    def exportar_archivo(self):
        if not hasattr(self, "df"):
            QMessageBox.warning(self, "Sin datos", "Primero debes cargar un archivo.")
            return

        ruta, filtro = QFileDialog.getSaveFileName(
            self,
            "Guardar archivo",
            "",
            "CSV (*.csv);;Excel (*.xlsx)"
        )

        if not ruta:
            return

        try:
            if ruta.endswith(".csv"):
                from proyecto_informes.core.informes import exportar_csv
                exportar_csv(self.df, ruta)
            else:
                from proyecto_informes.core.informes import exportar_excel
                exportar_excel(self.df, ruta)

            QMessageBox.information(self, "Éxito", "Archivo exportado correctamente.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo exportar el archivo:\n{e}")