import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QFormLayout, QHBoxLayout, QDateEdit, QComboBox)

from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100,100,200,600)
        self.setWindowTitle("FormLayout")
        self.crearFormulario()
        self.show()

    def crearFormulario(self):
        titulo = QLabel("Solicitud de ingreso")
        titulo.setFont(QFont('Arial',18))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.nombreEdit = QLineEdit()
        self.nombreEdit.setPlaceholderText("Nombre")

        self.apellidoEdit = QLineEdit()
        self.apellidoEdit.setPlaceholderText("Apellido")

        self.genero_selection = QComboBox()
        self.genero_selection.addItems(["Masculino", "Femenino", "Otro"])

        self.fechaNacimiento = QDateEdit()
        self.fechaNacimiento.setDisplayFormat("yyyy-MM-dd")
        self.fechaNacimiento.setMaximumDate(QDate.currentDate())
        self.fechaNacimiento.setCalendarPopup(True)
        self.fechaNacimiento.setDate(QDate.currentDate())

        self.telefono = QLineEdit()
        self.telefono.setPlaceholderText("000-000-000")

        submit_button = QPushButton("Enviar")
        submit_button.clicked.connect(self.mostrar_info)


        primer_h_box = QHBoxLayout()
        primer_h_box.addWidget(self.nombreEdit)
        primer_h_box.addWidget(self.apellidoEdit)

        main_form = QFormLayout()
        main_form.addRow(titulo)
        main_form.addRow("Nombre y Apellido: ", primer_h_box)
        main_form.addRow("Género: ", self.genero_selection)
        main_form.addRow("Fecha de Nacimiento: ", self.fechaNacimiento)
        main_form.addRow("Teléfono: ", self.telefono)
        main_form.addRow(submit_button)

        self.setLayout(main_form)


    def mostrar_info(self):
        QMessageBox.information(self,
                                "Información",
                                f"Nombre: {self.nombreEdit.text()}\n"
                                f"Apellido: {self.apellidoEdit.text()}\n"
                                f"Género: {self.genero_selection.currentText()}\n"
                                f"Fecha de Nacimiento: {self.fechaNacimiento.date().toString()}\n",
                                QMessageBox.StandardButton.Ok,
                                QMessageBox.StandardButton.Ok
                             )






if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())
