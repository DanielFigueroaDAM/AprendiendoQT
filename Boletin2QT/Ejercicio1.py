import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QRadioButton, QCheckBox, QStackedLayout, QFrame,
                             QVBoxLayout)

class VentanaCajas(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(250,250,250,250)
        self.setWindowTitle("Formulario que cambie colores")

        self.cajaVertical = QVBoxLayout()

        self.panel_negro = QFrame()
        self.panel_negro.setStyleSheet("background-color: blue;")
        self.elemento = QStackedLayout()
        self.boton1 = QPushButton()

        self.boton1.clicked.connect(self.cambiarColor)


        self.elemento.addWidget(self.panel_negro)

        self.cajaVertical.addLayout(self.elemento)

        self.cajaVertical.addWidget(self.boton1)

        self.setLayout(self.cajaVertical)

        self.show()

    def cambiarColor(self):
        self.panel_negro.setStyleSheet("background-color: yellow;")








if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaCajas()
    sys.exit(app.exec())




