import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class GestionProductos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.productos = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión de Productos")
        self.setGeometry(100, 100, 600, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Formulario
        form_layout = QFormLayout()
        self.txt_codigo = QLineEdit()
        self.txt_nombre = QLineEdit()
        self.txt_precio = QDoubleSpinBox()
        self.txt_precio.setMaximum(10000)
        self.txt_stock = QSpinBox()
        self.txt_stock.setMaximum(1000)

        form_layout.addRow("Código:", self.txt_codigo)
        form_layout.addRow("Nombre:", self.txt_nombre)
        form_layout.addRow("Precio:", self.txt_precio)
        form_layout.addRow("Stock:", self.txt_stock)

        layout.addLayout(form_layout)

        # Tabla de productos
        self.tabla_productos = QTableWidget()
        self.tabla_productos.setColumnCount(4)
        self.tabla_productos.setHorizontalHeaderLabels(["Código", "Nombre", "Precio", "Stock"])
        self.tabla_productos.cellClicked.connect(self.seleccionar_producto)
        layout.addWidget(self.tabla_productos)

        # Botones
        btn_layout = QHBoxLayout()
        btn_agregar = QPushButton("Agregar")
        btn_editar = QPushButton("Editar")
        btn_eliminar = QPushButton("Eliminar")
        btn_limpiar = QPushButton("Limpiar")

        btn_agregar.clicked.connect(self.agregar_producto)
        btn_editar.clicked.connect(self.editar_producto)
        btn_eliminar.clicked.connect(self.eliminar_producto)
        btn_limpiar.clicked.connect(self.limpiar_formulario)

        btn_layout.addWidget(btn_agregar)
        btn_layout.addWidget(btn_editar)
        btn_layout.addWidget(btn_eliminar)
        btn_layout.addWidget(btn_limpiar)

        layout.addLayout(btn_layout)
        central_widget.setLayout(layout)

    def agregar_producto(self):
        # Implementar agregar producto
        pass

    def editar_producto(self):
        # Implementar editar producto
        pass

    def eliminar_producto(self):
        # Implementar eliminar producto
        pass

    def seleccionar_producto(self, row, column):
        # Implementar selección desde tabla
        pass

    def limpiar_formulario(self):
        self.txt_codigo.clear()
        self.txt_nombre.clear()
        self.txt_precio.setValue(0)
        self.txt_stock.setValue(0)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = GestionProductos()
    ventana.show()
    sys.exit(app.exec())