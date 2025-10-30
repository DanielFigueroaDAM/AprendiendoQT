import sys


from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget)


class VentanaCajas(QMainWindow):
    def __init__(self):
        super().__init__()

        #creamos la caja de
