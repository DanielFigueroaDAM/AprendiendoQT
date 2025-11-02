import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QLabel, QLineEdit)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100,100,400,150)
        self.setWindowTitle('Layouts Anidados')
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        mensaje_principal = QLabel("Por favor ingrasa sus datos: ")

        nombre_label = QLabel("Nombre: ")
        self.nombres_input = QLineEdit()
        apellido_label = QLabel("Apellido: ")
        self.apellidos_input = QLineEdit()
        edad_label = QLabel("Edad: ")
        self.edad_input = QLineEdit()
        correo_label = QLabel("Correo: ")
        self.correo_input = QLineEdit()
        direccion_label = QLabel("Dirección: ")
        self.direccion_input = QLineEdit()
        telefono_label = QLabel("Teléfono: ")
        self.telefono_input = QLineEdit()


        # Ajustamos el ancho de las etiquetas para que queden alineadas
        nombre_label.setFixedWidth(90)
        apellido_label.setFixedWidth(90)
        edad_label.setFixedWidth(90)
        correo_label.setFixedWidth(90)
        direccion_label.setFixedWidth(90)
        telefono_label.setFixedWidth(90)

        enviar_boton = QPushButton("Enviar")

        # creamos el layout vertical principal
        vertical_layout_main = QVBoxLayout()

        # creamos los layouts horizontales
        h_layout_1 = QHBoxLayout()
        h_layout_2 = QHBoxLayout()
        h_layout_3 = QHBoxLayout()

        # agregamos los widgets a los layouts horizontales
        h_layout_1.addWidget(nombre_label)
        h_layout_1.addWidget(self.nombres_input)
        h_layout_1.addWidget(correo_label)
        h_layout_1.addWidget(self.correo_input)

        h_layout_2.addWidget(apellido_label)
        h_layout_2.addWidget(self.apellidos_input)
        h_layout_2.addWidget(direccion_label)
        h_layout_2.addWidget(self.direccion_input)

        h_layout_3.addWidget(edad_label)
        h_layout_3.addWidget(self.edad_input)
        h_layout_3.addWidget(telefono_label)
        h_layout_3.addWidget(self.telefono_input)

        # agregamos los layouts horizontales al layout vertical principal
        vertical_layout_main.addWidget(mensaje_principal)
        vertical_layout_main.addLayout(h_layout_1)
        vertical_layout_main.addLayout(h_layout_2)
        vertical_layout_main.addLayout(h_layout_3)
        vertical_layout_main.addWidget(enviar_boton)

        self.setLayout(vertical_layout_main)  # Definimos nuestro layout como el layout principal de la ventana

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())









