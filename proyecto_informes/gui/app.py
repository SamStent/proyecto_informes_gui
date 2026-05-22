from PySide6.QtWidgets import QApplication
from .main_window import MainWindow
import sys

def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    run()