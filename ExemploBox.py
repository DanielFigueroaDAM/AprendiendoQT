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


# Layouts

# maia = QGridLayourt()
# maia.addWidget(CaixaCor.CaixaCor("red"))
# maia.addWidget(CaixaCor.CaixaCor("blue"),0,1,1,2))
# maia.addWidget(CaixaCor.CaixaCor("green"),1,0,2,1))
# maia.addWidget(CaixaCor.CaixaCor("green"),1,1,1,2))
# maia.addWidget(CaixaCor.CaixaCor("green"),2,1,1,1))
# maia.addWidget(CaixaCor.CaixaCor("yellow"),2,2,1,1))
#
#