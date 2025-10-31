import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QApplication,QLabel,QWidget, QLineEdit, QPushButton, QMessageBox, QCheckBox)

from registro import RegistrarUsuarioView

from main import MainWindow


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("Mi login")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.is_logged = False

        user_label = QLabel(self)
        user_label.setText("Usuario:")
        user_label.setFont(QFont('Arial',10))
        user_label.move(20,54)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(90,50)

        password_label = QLabel(self)
        password_label.setText("Password:")
        password_label.setFont(QFont('Arial', 10))
        password_label.move(20, 86)

        self.password_input = QLineEdit(self)
        self.password_input.resize(250, 34)
        self.password_input.move(90, 82)
        self.password_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        login_button = QPushButton("Login", self)
        login_button.resize(320, 24)
        login_button.move(20, 140)
        login_button.clicked.connect(self.login)

        register_button = QPushButton("Register", self)
        register_button.resize(320, 34)
        register_button.move(20, 180)
        register_button.clicked.connect(self.iniciar_register)


        self.check_view_password = QCheckBox("Mostrar password", self)
        self.check_view_password.move(90,112)
        self.check_view_password.toggled.connect(self.mostar_comtrasena) #cambiamos clicked por toggled

    def mostar_comtrasena(self, clicked):
        if clicked:
            self.password_input.setEchoMode(
                QLineEdit.EchoMode.Normal
            )
        else:
            self.password_input.setEchoMode(
                QLineEdit.EchoMode.Password
            )


    def login(self):
        users = []
        user_path = "usuarios.txt"

        try:

            with open(user_path, "r") as f:
                for line in f:
                    users.append(line.strip("\n"))
                # CÓDIGO CORREGIDO PARA EL FORMATO DE CREDENCIALES
                login_information = f"{self.user_input.text()},{self.password_input.text()}"

                if login_information in users:
                    QMessageBox.information(self, "Inicio  de sesión", "Inicio de sesión exitoso", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
                    self.is_logged = True
                    self.close()
                    self.open_main_window()
                else:
                    QMessageBox.warning(self,"Error Message", "Usuario o contraseña incorrectos", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)

        except FileNotFoundError as e:
            QMessageBox.warning(self,"Error Message", f"No se ha encontrado el archivo de usuarios{e}", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        except Exception as e:
            QMessageBox.warning(self,"Error Message", f"Ha ocurrido un error inesperado {e}", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()




    def iniciar_register(self):
        self.new_user_form = RegistrarUsuarioView()
        self.new_user_form.show()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())