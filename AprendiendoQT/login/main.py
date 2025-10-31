
from PyQt6.QtWidgets import QWidget, QLabel, QMessageBox
from PyQt6.QtGui import QPixmap




class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUi()

    def inicializarUi(self):
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("Ventana Principal")
        self.generar_contenido()
        self.show()


    def generar_contenido(self):
        image_path = "galiciaFondo.jpg"
        try:
            with open(image_path):
                image_label = QLabel(self)
                image_label.setPixmap(QPixmap(image_path))

        except FileNotFoundError as e:
            QMessageBox.warning(
                self,
                "Error",
                f"No se pudo cargar la imagen: {e}",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close
            )
        except Exception as e:
            QMessageBox.warning(
                self,
                "Error",
                f"Ocurrió un error inesperado: {e}",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close
            )

