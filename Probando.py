import sys
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QHBoxLayout, QTextEdit, QPushButton,
                             QListView, QLabel, QGroupBox)


class VentanaConListas(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.show()

    def inicializarUI(self):
        self.setWindowTitle("Lista con Model-View")
        self.setGeometry(100, 100, 500, 400)

        # Inicializar componentes
        self.crear_area_entrada()
        self.crear_lista()
        self.crear_controles_avanzados()

        # Layout principal
        layout_principal = QVBoxLayout()

        # Grupo para área de entrada
        grupo_entrada = QGroupBox("Añadir Elementos a la Lista")
        grupo_entrada.setLayout(self.cajaHorizontal)
        layout_principal.addWidget(grupo_entrada)

        # Grupo para lista
        grupo_lista = QGroupBox("Lista de Elementos")
        layout_lista = QVBoxLayout()
        layout_lista.addWidget(self.lista1)
        grupo_lista.setLayout(layout_lista)
        layout_principal.addWidget(grupo_lista)

        # Controles avanzados
        layout_principal.addWidget(self.grupo_controles)

        self.setLayout(layout_principal)

    def crear_area_entrada(self):
        """Crea el área para añadir nuevos elementos"""
        self.label = QTextEdit()
        self.label.setMaximumHeight(60)  # Limitar altura
        self.label.setPlaceholderText("Escribe el texto del nuevo elemento...")

        self.botonAñadir = QPushButton("Añadir")
        self.botonBorrar = QPushButton("Borrar Último")
        self.botonLimpiar = QPushButton("Limpiar Todo")

        self.cajaHorizontal = QHBoxLayout()
        self.cajaHorizontal.addWidget(self.label)
        self.cajaHorizontal.addWidget(self.botonAñadir)
        self.cajaHorizontal.addWidget(self.botonBorrar)
        self.cajaHorizontal.addWidget(self.botonLimpiar)

        # Conectar señales
        self.botonAñadir.clicked.connect(self.anadirElemento)
        self.botonBorrar.clicked.connect(self.borrarUltimoElemento)
        self.botonLimpiar.clicked.connect(self.limpiarLista)

    def crear_lista(self):
        """Inicializa el modelo y la vista de lista"""
        # Crear el modelo
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Elementos de la Lista"])  # Encabezado

        # Crear la vista
        self.lista1 = QListView()
        self.lista1.setModel(self.model)  # Conectar modelo con vista

        # Añadir algunos elementos de ejemplo
        elementos_ejemplo = ["Elemento de ejemplo 1", "Elemento de ejemplo 2"]
        for elemento in elementos_ejemplo:
            item = QStandardItem(elemento)
            self.model.appendRow(item)

    def crear_controles_avanzados(self):
        """Crea controles adicionales para gestionar la lista"""
        self.grupo_controles = QGroupBox("Controles de la Lista")
        layout_controles = QHBoxLayout()

        # Botones adicionales
        self.botonBorrarSeleccionado = QPushButton("Borrar Seleccionado")
        self.botonEditar = QPushButton("Editar Seleccionado")
        self.botonContar = QPushButton("Contar Elementos")

        # Etiqueta para información
        self.etiqueta_info = QLabel("Elementos: 2")

        layout_controles.addWidget(self.botonBorrarSeleccionado)
        layout_controles.addWidget(self.botonEditar)
        layout_controles.addWidget(self.botonContar)
        layout_controles.addWidget(self.etiqueta_info)

        self.grupo_controles.setLayout(layout_controles)

        # Conectar señales
        self.botonBorrarSeleccionado.clicked.connect(self.borrarSeleccionado)
        self.botonEditar.clicked.connect(self.editarSeleccionado)
        self.botonContar.clicked.connect(self.actualizarContador)

        # Conectar señal de selección cambiada
        self.lista1.selectionModel().selectionChanged.connect(self.seleccionCambiada)

    def anadirElemento(self):
        """Añade un nuevo elemento a la lista"""
        text = self.label.toPlainText().strip()
        if not text:
            return

        # Crear y configurar el item
        item = QStandardItem(text)
        item.setToolTip(f"Elemento añadido: {text}")

        # Añadir al modelo
        self.model.appendRow(item)

        # Limpiar el área de texto
        self.label.clear()

        # Actualizar contador
        self.actualizarContador()

        # Seleccionar el nuevo elemento
        index = self.model.index(self.model.rowCount() - 1, 0)
        self.lista1.setCurrentIndex(index)

    def borrarUltimoElemento(self):
        """Elimina el último elemento de la lista"""
        if self.model.rowCount() > 0:
            self.model.removeRow(self.model.rowCount() - 1)
            self.actualizarContador()

    def borrarSeleccionado(self):
        """Elimina el elemento seleccionado"""
        index = self.lista1.currentIndex()
        if index.isValid():
            self.model.removeRow(index.row())
            self.actualizarContador()

    def editarSeleccionado(self):
        """Permite editar el elemento seleccionado"""
        index = self.lista1.currentIndex()
        if index.isValid():
            # Activar edición en la vista
            self.lista1.edit(index)

    def limpiarLista(self):
        """Elimina todos los elementos de la lista"""
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["Elementos de la Lista"])
        self.actualizarContador()

    def seleccionCambiada(self):
        """Maneja el cambio de selección en la lista"""
        index = self.lista1.currentIndex()
        if index.isValid():
            elemento = self.model.itemFromIndex(index).text()
            self.etiqueta_info.setText(f"Seleccionado: {elemento}")

    def actualizarContador(self):
        """Actualiza el contador de elementos"""
        count = self.model.rowCount()
        self.etiqueta_info.setText(f"Elementos: {count}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaConListas()
    sys.exit(app.exec())