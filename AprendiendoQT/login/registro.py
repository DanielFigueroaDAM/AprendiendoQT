
from PyQt6.QtWidgets import (QLineEdit, QMessageBox, QDialog, QLabel, QPushButton, QLineEdit, QMessageBox, QLabel)

from PyQt6.QtGui import QFont

class RegistrarUsuarioView(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.generar_formulario()

    def generar_formulario(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("Registration Window")

        user_label = QLabel(self)
        user_label.setText("Usuario: ")
        user_label.setFont(QFont('Arial',10))
        user_label.move(20,44)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(90,40)

        password_1_label = QLabel(self)
        password_1_label.setText("Password: ")
        password_1_label.setFont(QFont('Arial',10))
        password_1_label.move(20,74)

        self.password_1_input = QLineEdit(self)
        self.password_1_input.resize(250,24)
        self.password_1_input.move(90,70)

        self.password_1_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        password_2_label = QLabel(self)
        password_2_label.setText("Password: ")
        password_2_label.setFont(QFont('Arial',10))
        password_2_label.move(20,104)

        self.password_2_input = QLineEdit(self)
        self.password_2_input.resize(250,24)
        self.password_2_input.move(90,100)

        self.password_2_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        create_button = QPushButton(self)
        create_button.setText("Crear")
        create_button.resize(150,32)
        create_button.move(20,170)
        create_button.clicked.connect(self.crear_usuario)

        cancel_button = QPushButton(self)
        cancel_button.setText("Cancelar")
        cancel_button.resize(150,32)
        cancel_button.move(170,170)
        cancel_button.clicked.connect(self.cancelar_creacion)

    def cancelar_creacion(self):
        self.close()

    def crear_usuario(self):
        user_path = "usuarios.txt"
        usuario = self.user_input.text()
        password_1 = self.password_1_input.text()
        password_2 = self.password_2_input.text()

        if password_1 == "" or password_2 == "" or usuario == "":
            QMessageBox.warning(
                self,
                "Error",
                "Ningun campo puede estar vacio",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close
            )
        elif password_1 != password_2:
            QMessageBox.warning(
                self,
                "Error",
                "Las conraseñas no coinciden",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)
        else:
            try :
                with open(user_path, "a+") as f:
                    f.write(f"{usuario},{password_1}\n")
                QMessageBox.information(self, "Creacion exitosa",
                                        "El usuario ha sido creado exitosamente",
                                        QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok)
                self.close()
            except FileNotFoundError as e:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"La base de datos de usuarios no se ha encontrado.{e}",
                    QMessageBox.StandardButton.Close,
                    QMessageBox.StandardButton.Close
                )


