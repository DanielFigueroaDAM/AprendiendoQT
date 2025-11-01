import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QHBoxLayout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setMinimumWidth(600)
        self.setFixedHeight(80)
        self.setWindowTitle('Layout Horizontal')
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        correo_label = QLabel("Correo electrónico: ")
        correo_input = QLineEdit()
        enviar_button = QPushButton("Enviar")

        layout = QHBoxLayout()
        layout.addWidget(correo_label)
        layout.addWidget(correo_input)
        layout.addWidget(enviar_button)

        self.setLayout(layout) # Definimos nuestro layout como el layout principal de la ventana



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())