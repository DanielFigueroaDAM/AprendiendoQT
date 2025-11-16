import sys

from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QListView


class VentanaListas(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.cajaHorizontal = QHBoxLayout()

        self.modelo = QStandardItemModel()

        self.hoja1= QStandardItem("Hoja 1")
        self.hoja2= QStandardItem("Hoja 2")
        self.hoja3= QStandardItem("Hoja 3")
        self.hoja4= QStandardItem("Hoja 4")
        self.hoja5= QStandardItem("Hoja 5")

        self.modelo.appendRow(self.hoja1)
        self.modelo.appendRow(self.hoja2)
        self.modelo.appendRow(self.hoja3)
        self.modelo.appendRow(self.hoja4)
        self.modelo.appendRow(self.hoja5)

        self.botonesDelMedio()
        self.lista1()
        self.lista2()

        self.botonMostrar.clicked.connect(self.mostrar)
        self.botonOcultar.clicked.connect(self.ocultar)



        self.cajaHorizontal.addWidget(self.listaVisibles)
        self.cajaHorizontal.addLayout(self.cajaVertical)
        self.cajaHorizontal.addWidget(self.listaOcultas)

        self.setLayout(self.cajaHorizontal)


        self.show()


    def botonesDelMedio(self):
        self.botonOcultar =QPushButton("Ocultar>>")
        self.botonMostrar = QPushButton("<<Mostrar")
        self.cajaVertical = QVBoxLayout()
        self.cajaVertical.addWidget(self.botonOcultar)
        self.cajaVertical.addWidget(self.botonMostrar)

    def lista1(self):
        self.listaVisibles = QListView()
        self.listaVisibles.setModel(self.modelo)

    def lista2(self):
        self.listaOcultas = QListView()
        self.modeloOcultas = QStandardItemModel()
        self.listaOcultas.setModel(self.modeloOcultas)

    def mostrar(self):
        self.mover(self.modeloOcultas, self.modelo, self.listaOcultas)

    def ocultar(self):
        self.mover(self.modelo, self.modeloOcultas, self.listaVisibles)

    def mover(self, origen_modelo, destino_modelo, lista_view):
        indexes = lista_view.selectionModel().selectedIndexes()
        if not indexes:
            return

        rows = sorted({i.row() for i in indexes}, reverse=True)
        for row in rows:
            destino_modelo.appendRow(origen_modelo.takeRow(row))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaListas()
    sys.exit(app.exec())