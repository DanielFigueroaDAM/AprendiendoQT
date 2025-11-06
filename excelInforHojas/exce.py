import sys


from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget,
                             QGridLayout, QListView, QListWidget)


class PanelExcelINFO(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ExceleINFO - Hojas")
        self.setFixedSize(800, 600)

        # --- Layout principal ---
        myGrid = QGridLayout()

        # --- Labels superiores ---
        lblVisible = QLabel("Hojas Visibles")
        lblOcultas = QLabel("Hojas Ocultas")

        myGrid.addWidget(lblVisible, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        myGrid.addWidget(lblOcultas, 0, 2, alignment=Qt.AlignmentFlag.AlignCenter)

        # --- Listas ---
        cuadroListaIzquierda = QListWidget()
        cuadroListaDerecha = QListWidget()
        myGrid.addWidget(cuadroListaIzquierda, 1, 0)
        myGrid.addWidget(cuadroListaDerecha, 1, 2)

        cuadroListaIzquierda.addItems(["Hoja1", "Hoja2", "Hoja3", "Hoja4", "Hoja5"])
        cuadroListaDerecha.addItems(["Hoja6", "Hoja7", "Hoja8"])



        # --- Botones centrales ---
        self.botonOcultar = QPushButton("Ocultar →")
        self.botonMostrar = QPushButton("← Mostrar")
        self.botonOcultar.clicked.connect(self.on_botonOcultar_clicked)
        self.botonMostrar.clicked.connect(self.on_botonMostrar_clicked)



        # Layout vertical para centrar ambos botones
        botonesLayout = QVBoxLayout()
        botonesLayout.addWidget(self.botonMostrar)
        botonesLayout.addWidget(self.botonOcultar)
        botonesLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # --- Ajustes de padding y espacio ---
        botonesLayout.setContentsMargins(20, 0, 20, 40)  # (izquierda, arriba, derecha, abajo)
        botonesLayout.setSpacing(25)  # espacio entre los botones


        # Widget contenedor para los botones
        botonesWidget = QWidget()
        botonesWidget.setLayout(botonesLayout)

        # Añadimos ese contenedor al grid en la columna central
        myGrid.addWidget(botonesWidget, 1, 1, alignment=Qt.AlignmentFlag.AlignTop)


        # --- Botón Cerrar (abajo derecha) ---
        self.botonCerrar = QPushButton("Cerrar")
        self.botonCerrar.clicked.connect(self.cerrar)
        myGrid.addWidget(self.botonCerrar, 2, 2, alignment=Qt.AlignmentFlag.AlignRight)

        # --- Ajuste de proporciones ---
        myGrid.setColumnStretch(0, 4)
        myGrid.setColumnStretch(1, 1)
        myGrid.setColumnStretch(2, 4)
        myGrid.setRowStretch(1, 10)

        # --- Contenedor central ---
        container = QWidget()
        container.setLayout(myGrid)
        self.setCentralWidget(container)

    def on_botonOcultar_clicked(self):
        pass
    def on_botonMostrar_clicked(self):
        pass
    def cerrar(self):
        self.close()






if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = PanelExcelINFO()
    ventana.show()
    aplicacion.exec()



