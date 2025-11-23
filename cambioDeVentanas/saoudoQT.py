import sys


from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget)

from Fiestra2 import NosaPrimeiraFiestra2


# Importación de clases necesarias de PyQt6 (no están incluidas aquí,
# pero se asume que se importan al principio del programa)
# from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
# from PyQt6.QtCore import Qt


class NosaPrimeiraFiestra(QMainWindow):
    def __init__(self):
        super().__init__()  # Inicializa la clase base QMainWindow

        outraFiestra = None

        # =========================================================
        # CONFIGURACIÓN DE LA VENTANA PRINCIPAL
        # =========================================================
        self.setWindowTitle("un titulo")       # Establece el título de la ventana
        self.setFixedSize(800, 600)            # Tamaño fijo al iniciarse
        self.setMinimumSize(500, 300)          # Tamaño mínimo permitido

        # =========================================================
        # CREACIÓN Y CONFIGURACIÓN DE WIDGETS
        # =========================================================
        self.txtSaudo = QLineEdit()            # Campo de texto para introducir el nombre
        self.lblEtiqueta = QLabel("Ola a todos")  # Etiqueta inicial con texto por defecto

        # Configuración de la fuente del texto de la etiqueta
        fonte = self.lblEtiqueta.font()
        fonte.setPointSize(30)                 # Aumenta el tamaño de la letra
        self.lblEtiqueta.setFont(fonte)

        # Centra el texto de la etiqueta tanto horizontal como verticalmente
        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        # =========================================================
        # DISEÑO (LAYOUT) DE LA INTERFAZ
        # =========================================================
        caixaV = QVBoxLayout()  # Crea un layout vertical para organizar los widgets

        # Cambia el texto de la etiqueta
        self.lblEtiqueta.setText("boa tarde")

        # Configura el campo de texto con un texto de ayuda
        self.txtSaudo = QLineEdit()
        self.txtSaudo.setPlaceholderText("Introduce o teu nome")

        # Botón para saludar
        btnSaudo = QPushButton("pulsa aqui")
        btnSaudo.clicked.connect(self.on_btnSaudo_clicked)  # Conecta el clic con una función

        # Botón para abrir otra ventana
        btnFiestra = QPushButton("Outra Fiestra")
        btnFiestra.clicked.connect(self.cambioVentana)
        

        # Añade los widgets al layout vertical
        caixaV.addWidget(self.lblEtiqueta)
        caixaV.addWidget(self.txtSaudo)
        caixaV.addWidget(btnSaudo)
        caixaV.addWidget(btnFiestra)

        # Crea un contenedor para aplicar el layout a la ventana
        container = QWidget()
        container.setLayout(caixaV)

        # Establece el contenedor como el widget central de la ventana
        self.setCentralWidget(container)

        # =========================================================
        # CONEXIÓN DE SEÑALES ADICIONALES
        # =========================================================
        # Permite que al pulsar ENTER en el campo de texto se ejecute la misma acción que el botón
        self.txtSaudo.returnPressed.connect(self.on_btnSaudo_clicked)

        # Muestra la ventana en pantalla
        self.show()

    # =========================================================
    # MÉTOD0 VACÍO PARA FUTURA IMPLEMENTACIÓN
    # =========================================================
    def cambioVentana(self):
        # Aquí se podría abrir otra ventana o cambiar de vista
        self.outraFiestra.show()
        self.hide()



    # =========================================================
    # FUNCIÓN QUE SE EJECUTA AL PULSAR EL BOTÓN "pulsa aqui"
    # =========================================================
    def on_btnSaudo_clicked(self):
        nome = self.txtSaudo.text()   # Obtiene el texto introducido por el usuario
        nome = nome.strip()           # Elimina espacios en blanco al inicio y al final

        # Si el campo no está vacío, muestra un saludo personalizado
        if len(nome) != 0:
            self.lblEtiqueta.setText("Ola " + nome + " encantado/a de coñecerte")
            self.txtSaudo.clear()  # Limpia el campo de texto
        else:
            # Si está vacío, muestra un mensaje de aviso
            self.lblEtiqueta.setText("Está vacio")



if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra1 = NosaPrimeiraFiestra()
    fiestra2 = NosaPrimeiraFiestra2(fiestra1)
    fiestra1.outraFiestra = fiestra2
    
    aplicacion.exec()



