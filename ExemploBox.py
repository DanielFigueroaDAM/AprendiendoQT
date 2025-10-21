import sys
import ExemplosCor

from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow, QApplication, QWidget

class ExemploBox(QMainWindow):
    def __init__(self):
        #"aquaMarine","blue","green","pink","yellow","grey"
        caixaH = QHBoxLayout
        caixaV1 = QVBoxLayout
        caixaV2 = QVBoxLayout
        caixaV1.addWidget(CaixaCor.CaixaCor("blue"))
        caixaV1.addWidget(CaixaCor.CaixaCor("green"))
        caixaV1.addWidget(CaixaCor.CaixaCor("red"))

        caixaH.addLayout(CaixaCor.CaixaCor("yellow"))

        caixaV2 = QVBoxLayout()
        caixaV2.addWidget(CaixaCor.CaixaCor("pink"))
        caixaV2.addWidget(CaixaCor.CaixaCor("grey"))

        caixaH.addLayout(caixaV2)

        self.setCentralWidget(QWidget().setLayout(caixaH))

        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = ExemploBox()
    fiestra.show()
    sys.exit(aplicacion.exec())
