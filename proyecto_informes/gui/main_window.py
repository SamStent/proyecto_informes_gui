from PySide6.QtWidgets import QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de prueba")
        self.setCentralWidget(QLabel("Hola, PySide está funcionando"))