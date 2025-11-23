import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QDate


class GestionPedidos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pedidos = []
        self.clientes = ["Cliente A", "Cliente B", "Cliente C"]
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión de Pedidos")
        self.setGeometry(100, 100, 700, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Selección de cliente
        cliente_layout = QHBoxLayout()
        cliente_layout.addWidget(QLabel("Cliente:"))
        self.combo_clientes = QComboBox()
        self.combo_clientes.addItems(self.clientes)
        cliente_layout.addWidget(self.combo_clientes)
        layout.addLayout(cliente_layout)

        # Detalles del pedido
        form_layout = QFormLayout()
        self.txt_num_pedido = QLineEdit()
        self.txt_fecha = QDateEdit()
        self.txt_fecha.setDate(QDate.currentDate())
        self.txt_producto = QLineEdit()
        self.txt_cantidad = QSpinBox()
        self.txt_cantidad.setMaximum(100)

        form_layout.addRow("Número Pedido:", self.txt_num_pedido)
        form_layout.addRow("Fecha:", self.txt_fecha)
        form_layout.addRow("Producto:", self.txt_producto)
        form_layout.addRow("Cantidad:", self.txt_cantidad)

        layout.addLayout(form_layout)

        # Lista de productos del pedido
        self.lista_productos = QListWidget()
        layout.addWidget(QLabel("Productos del Pedido:"))
        layout.addWidget(self.lista_productos)

        # Botones
        btn_layout = QHBoxLayout()
        btn_agregar = QPushButton("Agregar Producto")
        btn_nuevo = QPushButton("Nuevo Pedido")
        btn_guardar = QPushButton("Guardar Pedido")
        btn_cancelar = QPushButton("Cancelar")

        btn_agregar.clicked.connect(self.agregar_producto_pedido)
        btn_nuevo.clicked.connect(self.nuevo_pedido)
        btn_guardar.clicked.connect(self.guardar_pedido)
        btn_cancelar.clicked.connect(self.cancelar_pedido)

        btn_layout.addWidget(btn_agregar)
        btn_layout.addWidget(btn_nuevo)
        btn_layout.addWidget(btn_guardar)
        btn_layout.addWidget(btn_cancelar)

        layout.addLayout(btn_layout)
        central_widget.setLayout(layout)

    def agregar_producto_pedido(self):
        producto = self.txt_producto.text()
        cantidad = self.txt_cantidad.text()
        if producto and cantidad:
            self.lista_productos.addItem(f"{producto} - {cantidad} unidades")
            self.txt_producto.clear()
            self.txt_cantidad.setValue(0)

    def nuevo_pedido(self):
        self.lista_productos.clear()
        self.txt_num_pedido.clear()
        self.txt_producto.clear()
        self.txt_cantidad.setValue(0)

    def guardar_pedido(self):
        # Implementar guardar pedido
        QMessageBox.information(self, "Éxito", "Pedido guardado correctamente")

    def cancelar_pedido(self):
        self.nuevo_pedido()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = GestionPedidos()
    ventana.show()
    sys.exit(app.exec())