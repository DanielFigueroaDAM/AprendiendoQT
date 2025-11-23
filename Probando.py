import sys
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import (QApplication, QWidget, QHBoxLayout, QPushButton,
                             QVBoxLayout, QListView, QLabel, QGroupBox)


class VentanaListasAvanzada(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle("Transferencia Avanzada entre Modelos")
        self.setGeometry(100, 100, 700, 400)

        # Inicializar modelos
        self.modelo_visibles = QStandardItemModel()
        self.modelo_ocultas = QStandardItemModel()

        # Configurar datos iniciales
        self.configurar_datos_iniciales()

        # Crear interfaz
        self.crear_interfaz()

        # Conectar señales
        self.conectar_señales()

        self.show()

    def configurar_datos_iniciales(self):
        """Configura los datos iniciales en el modelo de visibles"""
        elementos = ["Hoja 1", "Hoja 2", "Hoja 3", "Hoja 4", "Hoja 5",
                     "Documento A", "Documento B", "Archivo X", "Archivo Y"]

        for elemento in elementos:
            item = QStandardItem(elemento)
            # Añadir algunas propiedades adicionales
            item.setToolTip(f"Tooltip para {elemento}")
            self.modelo_visibles.appendRow(item)

    def crear_interfaz(self):
        """Crea toda la interfaz de usuario"""
        layout_principal = QHBoxLayout()

        # Lista de elementos visibles
        grupo_visibles = self.crear_grupo_lista(
            "Elementos Visibles",
            self.modelo_visibles,
            "lista_visibles"
        )

        # Botones centrales
        grupo_botones = self.crear_grupo_botones()

        # Lista de elementos ocultos
        grupo_ocultos = self.crear_grupo_lista(
            "Elementos Ocultos",
            self.modelo_ocultas,
            "lista_ocultas"
        )

        layout_principal.addWidget(grupo_visibles)
        layout_principal.addWidget(grupo_botones)
        layout_principal.addWidget(grupo_ocultos)

        self.setLayout(layout_principal)

    def crear_grupo_lista(self, titulo, modelo, nombre_vista):
        """Crea un grupo con una lista y su información"""
        grupo = QGroupBox(titulo)
        layout = QVBoxLayout()

        # Crear la vista de lista
        lista = QListView()
        lista.setModel(modelo)
        lista.setObjectName(nombre_vista)

        # Configurar selección múltiple
        lista.setSelectionMode(QListView.SelectionMode.ExtendedSelection)

        # Etiqueta informativa
        info_label = QLabel(f"Elementos: {modelo.rowCount()}")
        info_label.setObjectName(f"info_{nombre_vista}")

        layout.addWidget(lista)
        layout.addWidget(info_label)
        grupo.setLayout(layout)

        # Guardar referencia a la lista
        setattr(self, nombre_vista, lista)
        setattr(self, f"info_{nombre_vista}", info_label)

        return grupo

    def crear_grupo_botones(self):
        """Crea el grupo de botones centrales"""
        grupo = QGroupBox("Acciones")
        layout = QVBoxLayout()

        # Botones principales
        self.boton_ocultar = QPushButton("Ocultar →")
        self.boton_mostrar = QPushButton("← Mostrar")

        # Botones adicionales
        self.boton_ocultar_todos = QPushButton("Ocultar Todos →")
        self.boton_mostrar_todos = QPushButton("← Mostrar Todos")
        self.boton_intercambiar = QPushButton("↔ Intercambiar")

        # Botones de información
        self.boton_info = QPushButton("Información")

        layout.addWidget(self.boton_ocultar)
        layout.addWidget(self.boton_mostrar)
        layout.addStretch(1)
        layout.addWidget(self.boton_ocultar_todos)
        layout.addWidget(self.boton_mostrar_todos)
        layout.addWidget(self.boton_intercambiar)
        layout.addStretch(1)
        layout.addWidget(self.boton_info)

        grupo.setLayout(layout)
        return grupo

    def conectar_señales(self):
        """Conecta todas las señales de los botones"""
        self.boton_ocultar.clicked.connect(self.ocultar_seleccionados)
        self.boton_mostrar.clicked.connect(self.mostrar_seleccionados)
        self.boton_ocultar_todos.clicked.connect(self.ocultar_todos)
        self.boton_mostrar_todos.clicked.connect(self.mostrar_todos)
        self.boton_intercambiar.clicked.connect(self.intercambiar_listas)
        self.boton_info.clicked.connect(self.mostrar_informacion)

        # Conectar señales de cambio en los modelos
        self.modelo_visibles.rowsInserted.connect(self.actualizar_contadores)
        self.modelo_visibles.rowsRemoved.connect(self.actualizar_contadores)
        self.modelo_ocultas.rowsInserted.connect(self.actualizar_contadores)
        self.modelo_ocultas.rowsRemoved.connect(self.actualizar_contadores)

    def ocultar_seleccionados(self):
        """Mueve los elementos seleccionados de visibles a ocultos"""
        self.mover_elementos(self.modelo_visibles, self.modelo_ocultas, self.lista_visibles)

    def mostrar_seleccionados(self):
        """Mueve los elementos seleccionados de ocultos a visibles"""
        self.mover_elementos(self.modelo_ocultas, self.modelo_visibles, self.lista_ocultas)

    def ocultar_todos(self):
        """Mueve todos los elementos de visibles a ocultos"""
        self.mover_todos(self.modelo_visibles, self.modelo_ocultas)

    def mostrar_todos(self):
        """Mueve todos los elementos de ocultos a visibles"""
        self.mover_todos(self.modelo_ocultas, self.modelo_visibles)

    def intercambiar_listas(self):
        """Intercambia todos los elementos entre las dos listas"""
        # Guardar elementos actuales
        elementos_visibles = []
        elementos_ocultos = []

        # Recopilar elementos visibles
        for row in range(self.modelo_visibles.rowCount()):
            item = self.modelo_visibles.item(row)
            elementos_ocultos.append(QStandardItem(item.text()))

        # Recopilar elementos ocultos
        for row in range(self.modelo_ocultas.rowCount()):
            item = self.modelo_ocultas.item(row)
            elementos_visibles.append(QStandardItem(item.text()))

        # Limpiar modelos
        self.modelo_visibles.clear()
        self.modelo_ocultas.clear()

        # Añadir elementos intercambiados
        for item in elementos_visibles:
            self.modelo_visibles.appendRow(item)

        for item in elementos_ocultos:
            self.modelo_ocultas.appendRow(item)

    def mostrar_informacion(self):
        """Muestra información detallada de los modelos"""
        visibles = self.modelo_visibles.rowCount()
        ocultos = self.modelo_ocultas.rowCount()
        total = visibles + ocultos

        info = f"""
        Información de los Modelos:
        • Elementos visibles: {visibles}
        • Elementos ocultos: {ocultos}
        • Total de elementos: {total}
        """

        print(info)

    def mover_elementos(self, origen_modelo, destino_modelo, lista_view):
        """Mueve elementos seleccionados de un modelo a otro"""
        indexes = lista_view.selectionModel().selectedIndexes()

        if not indexes:
            print("No hay elementos seleccionados")
            return

        # Ordenar filas de mayor a menor para no alterar índices durante la eliminación
        rows = sorted({index.row() for index in indexes}, reverse=True)

        elementos_movidos = 0
        for row in rows:
            # Tomar la fila completa del modelo origen
            items_fila = origen_modelo.takeRow(row)
            if items_fila:  # Verificar que la fila no esté vacía
                destino_modelo.appendRow(items_fila)
                elementos_movidos += 1

        print(f"Se movieron {elementos_movidos} elementos")

    def mover_todos(self, origen_modelo, destino_modelo):
        """Mueve todos los elementos de un modelo a otro"""
        # Contar elementos antes de mover
        elementos_a_mover = origen_modelo.rowCount()

        # Mover todos los elementos
        while origen_modelo.rowCount() > 0:
            items_fila = origen_modelo.takeRow(0)
            destino_modelo.appendRow(items_fila)

        print(f"Se movieron {elementos_a_mover} elementos")

    def actualizar_contadores(self):
        """Actualiza los contadores de elementos en las etiquetas"""
        self.info_lista_visibles.setText(f"Elementos: {self.modelo_visibles.rowCount()}")
        self.info_lista_ocultas.setText(f"Elementos: {self.modelo_ocultas.rowCount()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaListasAvanzada()
    sys.exit(app.exec())