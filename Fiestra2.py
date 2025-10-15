from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget)

class NosaPrimeiraFiestra2(QMainWindow):
    def __init__(self, outraFiestra=None):
        super().__init__()
        self.outraFiestra = outraFiestra

        # Configuración de la ventana
        self.setWindowTitle("un titulo")
        self.setFixedSize(800, 600)
        self.setMinimumSize(500, 300)

        # Widgets
        self.txtSaudo = QLineEdit()
        self.lblEtiqueta = QLabel("Ola a todos")

        fonte = self.lblEtiqueta.font()
        fonte.setPointSize(30)
        self.lblEtiqueta.setFont(fonte)

        # Layout
        caixaV = QVBoxLayout()
        self.lblEtiqueta.setText("boa tarde2")
        self.txtSaudo.setPlaceholderText("Introduce o teu nome")
        # CORRECCIÓN: Usar Qt.AlignmentFlag
        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        btnSaudo = QPushButton("Pulsa aquí")
        btnSaudo.clicked.connect(self.on_btnSaudo_clicked)

        btnSalida = QPushButton("Volver á outra fiestra")
        btnSalida.clicked.connect(self.cambioVentana)

        caixaV.addWidget(self.lblEtiqueta)
        caixaV.addWidget(self.txtSaudo)
        caixaV.addWidget(btnSaudo)
        caixaV.addWidget(btnSalida)

        container = QWidget()
        container.setLayout(caixaV)
        self.setCentralWidget(container)

        self.txtSaudo.returnPressed.connect(self.on_btnSaudo_clicked)

    def cambioVentana(self):
        if self.outraFiestra:
            self.hide()
            self.outraFiestra.show()

    def on_btnSaudo_clicked(self):
        nome = self.txtSaudo.text().strip()
        if len(nome) != 0:
            self.lblEtiqueta.setText("Ola " + nome + " encantado/a de coñecerte")
            self.txtSaudo.clear()
        else:
            self.lblEtiqueta.setText("Está vacio")