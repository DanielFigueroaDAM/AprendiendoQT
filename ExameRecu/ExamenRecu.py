import sys
from PyQt6.QtWidgets import *



class Exame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()


    def initUI(self):
        self.pestañas()
        #primera linea
        self.zonaActivada = QLabel("Zoa activada")
        self.casillaZoaActivada = QCheckBox()
        #segunda linea
        self.horaComezo = QLabel("Hora de comezo de rego")
        self.inputHora = QLineEdit()
        #Tercera linea
        self.duracionRego = QLabel("Duración rego")
        self.duracionCircul = QDial()
        # Lateral
        self.radioButon1 = QRadioButton("Diario")
        self.radioButon2 = QRadioButton("Semanal")
        self.checkCaja1 = QCheckBox("Antiaxiada")
        self.checkCaja2 = QCheckBox("Chuvia")
        self.cajaVertical = QVBoxLayout()
        self.cajaVertical.addWidget(self.radioButon1)
        self.cajaVertical.addWidget(self.radioButon2)
        self.cajaVertical.addWidget(self.checkCaja1)
        self.cajaVertical.addWidget(self.checkCaja2)
        self.grupoOpcions = QGroupBox("Opcións")
        self.grupoOpcions.setLayout(self.cajaVertical)
        #Base
        self.checkLunes = QCheckBox("Luns")
        self.checkMartes = QCheckBox("Martes")
        self.checkMiercoles = QCheckBox("Mércores")
        self.checkJueves = QCheckBox("Xoves")
        self.checkVenres = QCheckBox("Venres")
        self.checkSabado = QCheckBox("Sábado")
        self.checkDomingo = QCheckBox("Domingo")
        self.grupoSemana = QGroupBox("Días")
        self.cajaHorizontal = QHBoxLayout()
        self.cajaHorizontal.addWidget(self.checkLunes)
        self.cajaHorizontal.addWidget(self.checkMartes)
        self.cajaHorizontal.addWidget(self.checkMiercoles)
        self.cajaHorizontal.addWidget(self.checkJueves)
        self.cajaHorizontal.addWidget(self.checkVenres)
        self.cajaHorizontal.addWidget(self.checkSabado)
        self.cajaHorizontal.addWidget(self.checkDomingo)
        self.grupoSemana.setLayout(self.cajaHorizontal)
        #Boton de Aceptar
        self.botonAceptar = QPushButton("Aceptar")

        self.maia = QGridLayout()

        self.maia.addWidget(self.zonaActivada, 0,0)
        self.maia.addWidget(self.casillaZoaActivada, 0,1)
        self.maia.addWidget(self.horaComezo, 1,0)
        self.maia.addWidget(self.inputHora, 1,1, 1, 3)
        self.maia.addWidget(self.duracionRego,2,0)
        self.maia.addWidget(self.duracionCircul,2,2)
        self.maia.addWidget(self.grupoOpcions,0,4,3,1)


        self.horizontal = QHBoxLayout()
        self.horizontal.addLayout(self.maia)
        self.vertical = QVBoxLayout()
        self.vertical.addLayout(self.horizontal)
        self.vertical.addWidget(self.grupoSemana)
        self.botonH = QHBoxLayout()
        self.botonH.addWidget(self.botonAceptar)
        self.botonH.setContentsMargins(460, 0, 0, 0)
        self.vertical.addLayout(self.botonH)

        #Todo para inicializar
        self.tab1.setLayout(self.vertical)
        self.verticalPrueba = QHBoxLayout()
        self.verticalPrueba.addWidget(self.pestaña)
        container = QWidget()
        container.setLayout(self.verticalPrueba)

        # Establece el contenedor como el widget central de la ventana
        self.setCentralWidget(container)


        self.casillaZoaActivada.toggled.connect(self.botonZoa)
        self.radioButon1.toggled.connect(self.selectBotonDiario)
        self.radioButon2.toggled.connect(self.selectBotonSemanal)
        self.botonAceptar.clicked.connect(self.anadirDatos)

    def botonZoa(self):
        if self.casillaZoaActivada.isChecked():
            self.grupoOpcions.setEnabled(False)
            self.grupoSemana.setEnabled(False)
            self.duracionCircul.setEnabled(False)
            self.botonAceptar.setEnabled(False)
            self.inputHora.setEnabled(False)
        else:
            self.grupoOpcions.setEnabled(True)
            self.grupoSemana.setEnabled(True)
            self.duracionCircul.setEnabled(True)
            self.botonAceptar.setEnabled(True)
            self.inputHora.setEnabled(True)
    def selectBotonDiario(self):
        if not self.checkLunes.isChecked():
            self.checkLunes.checkState()
        if not self.checkMartes.isChecked():
            self.checkMartes.click()
        if not self.checkMiercoles.isChecked():
            self.checkMiercoles.click()
        if not self.checkJueves.isChecked():
            self.checkJueves.click()
        if not self.checkVenres.isChecked():
            self.checkVenres.click()
        if not self.checkSabado.isChecked():
            self.checkSabado.click()
        if not self.checkDomingo.isChecked():
            self.checkDomingo.click()

    def selectBotonSemanal(self):
        if self.radioButon2.isChecked():
            self.grupoSemana.setEnabled(False)
        else:
            self.grupoSemana.setEnabled(True)

    def anadirDatos(self):
        textoHora = self.inputHora.text()
        texto2 = ""
        if self.radioButon1.isChecked():
            texto2 = "Diario"
        elif self.radioButon2.isChecked():
            texto2 = "Semanal"
        self.cajaTexto.setText(textoHora+" "+texto2)



    def pestañas(self):
        self.pestaña = QTabWidget()
        self.tab1 = QWidget()
        self.pestaña.addTab(self.tab1, "Configuracion Zoa 1")
        self.tab2 = QWidget()
        self.pestaña.addTab(self.tab2, "Configuracion Zoa 2")
        self.tab3 = QWidget()
        self.pestaña.addTab(self.tab3, "Consola")
        self.cajaTexto = QTextEdit()
        caja = QHBoxLayout()
        caja.addWidget(self.cajaTexto)
        self.tab3.setLayout(caja)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Exame()
    sys.exit(app.exec())