import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt



class AgendaContactos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.contactos = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Agenda de Contactos")
        self.setGeometry(100, 100, 500, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Búsqueda
        buscar_layout = QHBoxLayout()
        self.txt_buscar = QLineEdit()
        self.txt_buscar.setPlaceholderText("Buscar contacto...")
        self.txt_buscar.textChanged.connect(self.buscar_contacto)
        buscar_layout.addWidget(QLabel("Buscar:"))
        buscar_layout.addWidget(self.txt_buscar)
        layout.addLayout(buscar_layout)

        # Lista de contactos
        self.lista_contactos = QListWidget()
        self.lista_contactos.itemClicked.connect(self.mostrar_contacto)
        layout.addWidget(self.lista_contactos)

        # Formulario de contacto
        form_layout = QFormLayout()
        self.txt_nombre = QLineEdit()
        self.txt_telefono = QLineEdit()
        self.txt_email = QLineEdit()
        self.txt_direccion = QTextEdit()
        self.txt_direccion.setMaximumHeight(60)

        form_layout.addRow("Nombre:", self.txt_nombre)
        form_layout.addRow("Teléfono:", self.txt_telefono)
        form_layout.addRow("Email:", self.txt_email)
        form_layout.addRow("Dirección:", self.txt_direccion)

        layout.addLayout(form_layout)

        # Botones
        btn_layout = QHBoxLayout()
        btn_agregar = QPushButton("Agregar")
        btn_editar = QPushButton("Editar")
        btn_eliminar = QPushButton("Eliminar")
        btn_limpiar = QPushButton("Limpiar")

        btn_agregar.clicked.connect(self.agregar_contacto)
        btn_editar.clicked.connect(self.editar_contacto)
        btn_eliminar.clicked.connect(self.eliminar_contacto)
        btn_limpiar.clicked.connect(self.limpiar_formulario)

        btn_layout.addWidget(btn_agregar)
        btn_layout.addWidget(btn_editar)
        btn_layout.addWidget(btn_eliminar)
        btn_layout.addWidget(btn_limpiar)

        layout.addLayout(btn_layout)
        central_widget.setLayout(layout)

    def buscar_contacto(self):
        texto = self.txt_buscar.text().lower()
        self.lista_contactos.clear()
        for contacto in self.contactos:
            if texto in contacto['nombre'].lower():
                self.lista_contactos.addItem(contacto['nombre'])

    def agregar_contacto(self):
        nombre = self.txt_nombre.text()
        if nombre:
            self.contactos.append({
                'nombre': nombre,
                'telefono': self.txt_telefono.text(),
                'email': self.txt_email.text(),
                'direccion': self.txt_direccion.toPlainText()
            })
            self.actualizar_lista()
            self.limpiar_formulario()

    def mostrar_contacto(self, item):
        # Implementar mostrar contacto seleccionado
        pass

    def editar_contacto(self):
        # Implementar edición
        pass

    def eliminar_contacto(self):
        current_item = self.lista_contactos.currentItem()
        if current_item:
            reply = QMessageBox.question(self, 'Confirmar', '¿Eliminar este contacto?')
            if reply == QMessageBox.StandardButton.Yes:
                # Implementar eliminación
                pass

    def actualizar_lista(self):
        self.lista_contactos.clear()
        for contacto in self.contactos:
            self.lista_contactos.addItem(contacto['nombre'])

    def limpiar_formulario(self):
        self.txt_nombre.clear()
        self.txt_telefono.clear()
        self.txt_email.clear()
        self.txt_direccion.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = AgendaContactos()
    ventana.show()
    sys.exit(app.exec())