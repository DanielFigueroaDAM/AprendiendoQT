import sys


from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget)

class NosaPrimeiraFiestra(QMainWindow):
    def __init__(self):
        super().__init__()

        #Vamos a cambiar propiedades
        self.setWindowTitle("un titulo")
        self.setFixedSize(800,600) #hace mas grande la ventana al iniiciarse
        self.setMinimumSize(500,300)
        self.txtSaudo = QLineEdit()

        self.lblEtiqueta = QLabel("Ola a todos")
        fonte = self.lblEtiqueta.font()
        fonte.setPointSize(30)
        self.lblEtiqueta.setFont(fonte)
        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter| Qt.AlignmentFlag.AlignVCenter)

        caixaV = QVBoxLayout()
        self.lblEtiqueta.setText("boa tarde")

        self.txtSaudo = QLineEdit()

        self.txtSaudo.placeholderText()

        btnSaudo = QPushButton("pulsa aqui")
        btnSaudo.clicked.connect(self.on_btnSaudo_clicked)

        caixaV.addWidget(self.lblEtiqueta)
        caixaV.addWidget(self.txtSaudo)
        caixaV.addWidget(btnSaudo)

        container = QWidget()

        container.setLayout(caixaV)

        self.setCentralWidget(container)

        self.txtSaudo.returnPressed.connect(self.on_btnSaudo_clicked)

        self.show()

    def on_btnSaudo_clicked(self):
        nome = self.txtSaudo.text()
        nome = nome.strip()
        if len(nome) != 0:
            self.lblEtiqueta.setText("Ola "+ nome + " encantado/a de coñecerte")
            self.txtSaudo.clear()
        else:
            self.lblEtiqueta.setText("Está vacio")








if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = NosaPrimeiraFiestra()
    aplicacion.exec()



