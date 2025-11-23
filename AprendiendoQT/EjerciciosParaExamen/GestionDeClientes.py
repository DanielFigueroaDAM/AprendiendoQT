import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


class GestionClientes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.clientes = [
            {"id": 1, "nombre": "Juan", "apellidos": "García Pérez", "direccion": "Calle Mayor 1", "ciudad": "Madrid",
             "provincia": "Madrid"},
            {"id": 2, "nombre": "María", "apellidos": "López Ruiz", "direccion": "Av. Libertad 23",
             "ciudad": "Barcelona", "provincia": "Barcelona"}
        ]
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión de Clientes")
        self.setGeometry(100, 100, 500, 400)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # ComboBox para seleccionar cliente
        self.combo_clientes = QComboBox()
        self.actualizar_combo_clientes()
        self.combo_clientes.currentIndexChanged.connect(self.cargar_datos_cliente)
        layout.addWidget(QLabel("Seleccionar Cliente:"))
        layout.addWidget(self.combo_clientes)

        # Formulario de datos
        form_layout = QFormLayout()
        self.txt_id = QLineEdit()
        self.txt_nombre = QLineEdit()
        self.txt_apellidos = QLineEdit()
        self.txt_direccion = QLineEdit()
        self.txt_ciudad = QLineEdit()
        self.txt_provincia = QLineEdit()

        form_layout.addRow("Número Cliente:", self.txt_id)
        form_layout.addRow("Nombre:", self.txt_nombre)
        form_layout.addRow("Apellidos:", self.txt_apellidos)
        form_layout.addRow("Dirección:", self.txt_direccion)
        form_layout.addRow("Ciudad:", self.txt_ciudad)
        form_layout.addRow("Provincia:", self.txt_provincia)

        layout.addLayout(form_layout)

        # Botones
        btn_layout = QHBoxLayout()
        self.btn_engadir = QPushButton("Engadir")
        self.btn_editar = QPushButton("Editar")
        self.btn_borrar = QPushButton("Borrar")
        self.btn_cancelar = QPushButton("Cancelar")
        self.btn_aceptar = QPushButton("Aceptar")

        self.btn_engadir.clicked.connect(self.modo_engadir)
        self.btn_editar.clicked.connect(self.editar_cliente)
        self.btn_borrar.clicked.connect(self.borrar_cliente)
        self.btn_cancelar.clicked.connect(self.cancelar)
        self.btn_aceptar.clicked.connect(self.aceptar)

        btn_layout.addWidget(self.btn_engadir)
        btn_layout.addWidget(self.btn_editar)
        btn_layout.addWidget(self.btn_borrar)
        btn_layout.addWidget(self.btn_cancelar)
        btn_layout.addWidget(self.btn_aceptar)

        layout.addLayout(btn_layout)
        central_widget.setLayout(layout)

    def actualizar_combo_clientes(self):
        self.combo_clientes.clear()
        self.combo_clientes.addItem("-- Seleccionar Cliente --", None)
        for cliente in self.clientes:
            self.combo_clientes.addItem(f"{cliente['nombre']} {cliente['apellidos']}", cliente['id'])

    def cargar_datos_cliente(self):
        cliente_id = self.combo_clientes.currentData()
        if cliente_id:
            cliente = next((c for c in self.clientes if c['id'] == cliente_id), None)
            if cliente:
                self.txt_id.setText(str(cliente['id']))
                self.txt_nombre.setText(cliente['nombre'])
                self.txt_apellidos.setText(cliente['apellidos'])
                self.txt_direccion.setText(cliente['direccion'])
                self.txt_ciudad.setText(cliente['ciudad'])
                self.txt_provincia.setText(cliente['provincia'])

    def modo_engadir(self):
        self.limpiar_campos()
        self.txt_id.setText(str(max([c['id'] for c in self.clientes], default=0) + 1))

    def editar_cliente(self):
        # Implementar edición
        pass

    def borrar_cliente(self):
        cliente_id = self.combo_clientes.currentData()
        if cliente_id:
            reply = QMessageBox.question(self, 'Confirmar', '¿Borrar este cliente?')
            if reply == QMessageBox.StandardButton.Yes:
                self.clientes = [c for c in self.clientes if c['id'] != cliente_id]
                self.actualizar_combo_clientes()
                self.limpiar_campos()

    def cancelar(self):
        self.limpiar_campos()
        self.combo_clientes.setCurrentIndex(0)

    def aceptar(self):
        # Implementar guardado
        pass

    def limpiar_campos(self):
        self.txt_id.clear()
        self.txt_nombre.clear()
        self.txt_apellidos.clear()
        self.txt_direccion.clear()
        self.txt_ciudad.clear()
        self.txt_provincia.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = GestionClientes()
    ventana.show()
    sys.exit(app.exec())