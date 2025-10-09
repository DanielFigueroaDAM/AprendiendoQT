import sys


from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout)

class NosaPrimeiraFiestra(QMainWindow):
    def __init__(self):
        super().__init__()

        #Vamos a cambiar propiedades
        self.setWindowTitle("un titulo")
        self.setFixedSize(800,600) #hace mas grande la ventana al iniiciarse
        self.setMinimumSize(500,300)
        self.txtSaudo = QLineEdit()
        self.show()
        self.lblEtiqueta = QLabel("Ola a todos")
        fonte = self.lblEtiqueta.font()
        fonte.setPointSize(30)
        self.lblEtiqueta.setFont(fonte)
        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter| Qt.AlignmentFlag.AlignVCenter)





if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = NosaPrimeiraFiestra()
    aplicacion.exec()

