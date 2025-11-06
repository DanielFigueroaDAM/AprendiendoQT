# Índice Detallado del Curso PyQt6

## 📚 **FUNDAMENTOS BÁSICOS**

### 1. **Configuración Inicial y Ventana Básica**
- **📍 Sección**: 1. Creación de una Ventana Básica
- **Temas**:
  - Estructura básica de una aplicación PyQt6
  - Importación de módulos (sys, QApplication, QWidget)
  - Método `__init__` y herencia de QWidget
  - Configuración de ventana: `setGeometry()`, `setWindowTitle()`, `show()`
  - Bloque principal de ejecución

### 2. **Widgets Básicos de Formulario**
- **📍 Sección**: 2-3. Formulario de Login y Elementos Explicados
- **Widgets cubiertos**:
  - **QLabel**: Etiquetas de texto con fuentes personalizadas
  - **QLineEdit**: Campos de entrada (modos: Normal, Password, NoEcho)
  - **QPushButton**: Botones con conexión de señales
  - **QCheckBox**: Casillas de verificación

## 🎨 **SISTEMAS DE DISEÑO Y LAYOUTS**

### 3. **Posicionamiento Absoluto**
- **📍 Sección**: 5. Diseño y Posicionamiento
- **Métodos**: `move()`, `resize()`, `setGeometry()`
- **Uso**: Para interfaces simples con posiciones fijas

### 4. **Layouts Automáticos**
- **📍 Sección**: 18-23. Diferentes tipos de Layouts
- **Tipos**:
  - **QHBoxLayout** (Sección 18): Disposición horizontal
  - **QVBoxLayout** (Sección 19): Disposición vertical
  - **QGridLayout** (Sección 21): Cuadrícula para interfaces complejas
  - **QFormLayout** (Sección 22): Especializado para formularios

### 5. **Layouts Anidados**
- **📍 Sección**: 20. Layouts Anidados
- **Concepto**: Combinar múltiples layouts para diseños complejos
- **Métodos**: `addLayout()`, organización jerárquica

## 🔧 **WIDGETS ESPECIALIZADOS**

### 6. **Widgets de Selección**
- **📍 Sección**: 23. Widgets de Selección
- **Tipos**:
  - **QRadioButton**: Selección única (opciones excluyentes)
  - **QCheckBox**: Selección múltiple
  - **QComboBox**: Listas desplegables
  - **QSpinBox**: Selectores numéricos

### 7. **Widgets de Fecha y Texto Avanzados**
- **📍 Sección**: 22. QFormLayout
- **Widgets**:
  - **QDateEdit**: Selector de fechas con calendario
  - **QTextEdit**: Área de texto multilínea

## 💾 **MANEJO DE DATOS Y PERSISTENCIA**

### 8. **Sistema de Archivos**
- **📍 Sección**: 8. Persistencia de Datos con Archivos
- **Temas**:
  - Lectura/escritura de archivos de texto
  - Modos de apertura ("a+", "r")
  - Manejo de excepciones (FileNotFoundError)

### 9. **Validación de Datos**
- **📍 Sección**: 4. Implementando las Funciones
- **Técnicas**:
  - Validación de campos vacíos
  - Verificación de credenciales
  - Mensajes de error personalizados

## 🔄 **INTERACCIÓN Y SEÑALES**

### 10. **Manejo de Eventos**
- **📍 Sección**: 19. Manejo de Señales
- **Conceptos clave**:
  - **sender()**: Identificar el widget que emitió la señal
  - **clicked vs toggled**: Diferencia en señales de checkboxes
  - Conexión múltiple a una misma función

### 11. **Comunicación entre Ventanas**
- **📍 Sección**: 9. Integración entre Ventanas
- **Patrones**:
  - Ventanas modales vs no modales
  - Apertura y cierre de ventanas
  - Paso de datos entre ventanas

## 🚀 **PROYECTOS COMPLETOS**

### 12. **Sistema de Login Completo**
- **📍 Sección**: 12-16. Implementación Completa del Sistema
- **Componentes**:
  - Autenticación con archivo de usuarios
  - Navegación entre ventanas (Login → Principal)
  - Manejo de errores robusto

### 13. **Calculadora Funcional**
- **📍 Sección**: 21-22. Calculadora
- **Características**:
  - Interfaz con QGridLayout
  - Lógica de operaciones matemáticas
  - Manejo de estado y memoria

## 🛠 **BUENAS PRÁCTICAS Y TÉCNICAS AVANZADAS**

### 14. **Manejo de Errores**
- **📍 Sección**: 13-16. Manejo de Errores Mejorado
- **Estrategias**:
  - Excepciones específicas vs genéricas
  - Mensajes de error informativos
  - Validación proactiva

### 15. **Organización de Código**
- **📍 Sección**: 23. Organización Modular
- **Patrones**:
  - Separación en métodos especializados
  - Layouts organizados por funcionalidad
  - Nomenclatura consistente

## 📋 **BÚSQUEDA RÁPIDA POR WIDGET**

### **Widgets Básicos**
- **QLabel**: Secciones 2, 3, 20, 22
- **QLineEdit**: Secciones 2, 3, 18, 20, 22, 23
- **QPushButton**: Secciones 2, 3, 18, 19, 20, 21, 22

### **Widgets de Selección**
- **QCheckBox**: Secciones 2, 3, 23
- **QRadioButton**: Sección 23
- **QComboBox**: Secciones 22, 23
- **QSpinBox**: Sección 23

### **Widgets Especializados**
- **QDateEdit**: Sección 22
- **QTextEdit**: Secciones 21, 23

### **Layouts**
- **QHBoxLayout**: Secciones 18, 20, 22, 23
- **QVBoxLayout**: Secciones 19, 20, 23
- **QGridLayout**: Sección 21
- **QFormLayout**: Sección 22

## 🔍 **BÚSQUEDA POR FUNCIONALIDAD**

### **Para crear formularios**:
- Básicos: Secciones 2-5
- Avanzados: Secciones 20, 22
- Con validación: Secciones 4, 8, 12

### **Para diseño de interfaces**:
- Layouts simples: Secciones 18-19
- Interfaces complejas: Secciones 20-21
- Formularios profesionales: Sección 22

### **Para manejo de datos**:
- Persistencia: Sección 8
- Validación: Secciones 4, 12
- Estado de aplicación: Secciones 12, 21

### **Para interacción de usuario**:
- Señales y eventos: Secciones 3, 19
- Navegación: Sección 9
- Feedback: Secciones 4, 10



# Guía de PyQt6 - Creación de Interfaces Gráficas

## 1. Creación de una Ventana Básica

### Código Base
```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget

class VentanaVacia(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100, 100, 250, 250)  # posición x,y y tamaño ancho,alto
        self.setWindowTitle("Mi primera ventana vacía")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaVacia()
    sys.exit(app.exec())
```

### Explicación del Código

#### Importaciones Necesarias
```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget
```
- **sys**: Módulo estándar para interactuar con el sistema
- **QApplication**: Maneja el bucle principal de la aplicación
- **QWidget**: Clase base para todos los elementos de interfaz

#### Clase Principal
```python
class VentanaVacia(QWidget):
```
Crea una clase que hereda de QWidget, permitiendo crear ventanas personalizadas.

#### Método Constructor
```python
def __init__(self):
    super().__init__()
    self.inicializarUI()
```
- `super().__init__()`: Llama al constructor de la clase padre (QWidget)
- `self.inicializarUI()`: Llama al método que configura la interfaz

#### Configuración de la Interfaz
```python
def inicializarUI(self):
    self.setGeometry(100, 100, 250, 250)
    self.setWindowTitle("Mi primera ventana vacía")
    self.show()
```

**Métodos clave:**
- `setGeometry(x, y, ancho, alto)`: Posición y tamaño de la ventana
- `setWindowTitle("texto")`: Título de la ventana
- `show()`: Hace visible la ventana

#### Bloque Principal
```python
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaVacia()
    sys.exit(app.exec())
```

**Flujo de ejecución:**
1. `QApplication(sys.argv)`: Crea la aplicación
2. `VentanaVacia()`: Instancia la ventana
3. `app.exec()`: Inicia el bucle de eventos
4. `sys.exit()`: Garantiza una salida limpia



# Guía de PyQt6 - Formulario de Login

## 2. Creación de un Formulario de Login

### Código del Formulario
```python
import sys
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit, QPushButton, QMessageBox, QCheckBox)

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("Mi login")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.is_logged = False

        # Etiqueta y campo de usuario
        user_label = QLabel(self)
        user_label.setText("Usuario:")
        user_label.setFont(QFont('Arial', 10))
        user_label.move(20, 54)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 24)
        self.user_input.move(90, 50)

        # Etiqueta y campo de contraseña
        password_label = QLabel(self)
        password_label.setText("Password:")
        password_label.setFont(QFont('Arial', 10))
        password_label.move(20, 86)

        self.password_input = QLineEdit(self)
        self.password_input.resize(250, 34)
        self.password_input.move(90, 82)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Botones
        login_button = QPushButton("Login", self)
        login_button.resize(320, 24)
        login_button.move(20, 140)
        login_button.clicked.connect(self.iniciar_mainview)

        register_button = QPushButton("Register", self)
        register_button.resize(320, 34)
        register_button.move(20, 180)
        register_button.clicked.connect(self.iniciar_register)

        # Checkbox para mostrar contraseña
        self.check_view_password = QCheckBox("Mostrar password", self)
        self.check_view_password.move(90, 112)
        self.check_view_password.clicked.connect(self.mostar_comtrasena)

    def mostar_comtrasena(self):
        pass

    def iniciar_mainview(self):
        pass

    def iniciar_register(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())
```

## 3. Elementos de Formulario Explicados

### QLabel - Etiquetas de Texto
```python
user_label = QLabel(self)
user_label.setText("Usuario:")
user_label.setFont(QFont('Arial', 10))
user_label.move(20, 54)
```
- **QLabel**: Muestra texto estático
- **setText()**: Define el texto a mostrar
- **setFont()**: Configura la fuente y tamaño
- **move()**: Posiciona el elemento (x, y)

### QLineEdit - Campos de Entrada
```python
self.user_input = QLineEdit(self)
self.user_input.resize(250, 24)
self.user_input.move(90, 50)
```

#### Campo de Contraseña
```python
self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
```
**Modos disponibles:**
- `Normal`: Muestra el texto normalmente
- `Password`: Muestra puntos en lugar del texto
- `NoEcho`: No muestra nada
- `PasswordEchoOnEdit`: Muestra texto mientras se escribe, luego puntos

### QPushButton - Botones
```python
login_button = QPushButton("Login", self)
login_button.resize(320, 24)
login_button.move(20, 140)
login_button.clicked.connect(self.iniciar_mainview)
```
- **clicked.connect()**: Conecta el evento click a una función

### QCheckBox - Casillas de Verificación
```python
self.check_view_password = QCheckBox("Mostrar password", self)
self.check_view_password.move(90, 112)
self.check_view_password.clicked.connect(self.mostar_comtrasena)
```

## 4. Implementando las Funciones

### Función para Mostrar/Ocultar Contraseña
```python
def mostar_comtrasena(self):
    if self.check_view_password.isChecked():
        self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
    else:
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
```

### Función de Login Básica
```python
def iniciar_mainview(self):
    usuario = self.user_input.text()
    password = self.password_input.text()
    
    # Validación básica
    if usuario == "admin" and password == "1234":
        QMessageBox.information(self, "Login", "¡Login exitoso!")
        self.is_logged = True
        # Aquí iría la lógica para abrir la ventana principal
    else:
        QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")
```

### Función de Registro
```python
def iniciar_register(self):
    QMessageBox.information(self, "Registro", "Aquí iría el formulario de registro")
```

## 5. Diseño y Posicionamiento

### Métodos de Posicionamiento
- **move(x, y)**: Posiciona el widget en coordenadas absolutas
- **resize(ancho, alto)**: Define el tamaño del widget
- **setGeometry(x, y, ancho, alto)**: Combina posición y tamaño

### Ejemplo de Layout Organizado
```python
# Posiciones calculadas para mejor organización
x_label = 20
x_input = 90
y_start = 50
y_increment = 36

user_label.move(x_label, y_start)
self.user_input.move(x_input, y_start)

password_label.move(x_label, y_start + y_increment)
self.password_input.move(x_input, y_start + y_increment)
```
# Guía de PyQt6 - Nuevas Características y Cambios

## 6. Nuevas Implementaciones y Cambios

### Cambio en la Señal del Checkbox
```python
# ANTES:
self.check_view_password.clicked.connect(self.mostar_comtrasena)

# AHORA:
self.check_view_password.toggled.connect(self.mostar_comtrasena)
```
**Explicación del cambio:**
- `toggled` envía el estado actual (True/False) como parámetro
- `clicked` solo indica que fue clickeado, sin el estado

### Implementación Completa de mostrar_contrasena
```python
def mostar_comtrasena(self, clicked):
    if clicked:
        self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
    else:
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
```
**Mejora:** Recibe el parámetro `clicked` que indica el estado del checkbox

## 7. Nueva Clase: RegistrarUsuarioView (QDialog)

### Características Principales de QDialog
```python
class RegistrarUsuarioView(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)  # ¡NUEVO!
        self.generar_formulario()
```

**setModal(True):**
- Bloquea la ventana principal hasta que se cierre el diálogo
- El usuario debe interactuar con el diálogo primero

### Formulario de Registro Mejorado
```python
# Campos de verificación de contraseña
password_1_label = QLabel(self)
password_1_label.setText("Password: ")
# ...
password_2_label = QLabel(self)
password_2_label.setText("Password: ")
```

**Validación de contraseñas:** Se pide la contraseña dos veces para verificar

### Botones de Acción Específicos
```python
create_button = QPushButton(self)
create_button.setText("Crear")
create_button.clicked.connect(self.crear_usuario)

cancel_button = QPushButton(self)
cancel_button.setText("Cancelar")
cancel_button.clicked.connect(self.cancelar_creacion)
```

## 8. Persistencia de Datos con Archivos

### Manejo de Archivos para Usuarios
```python
def crear_usuario(self):
    user_path = "usuarios.txt"
    # ...
    try:
        with open(user_path, "a+") as f:
            f.write(f"{usuario},{password_1}\n")
```

**Modo "a+":**
- **a**: Append (agregar al final)
- **+**: Crear el archivo si no existe

### Validaciones Mejoradas
```python
if password_1 == "" or password_2 == "" or usuario == "":
    QMessageBox.warning(
        self,
        "Error",
        "Ningun campo puede estar vacio",
        QMessageBox.StandardButton.Close,  # ¡NUEVO!
        QMessageBox.StandardButton.Close
    )
```

**QMessageBox.StandardButton:** Especifica botones estándar para el diálogo

### Manejo de Errores con FileNotFoundError
```python
except FileNotFoundError as e:
    QMessageBox.critical(
        self,
        "Error",
        f"La base de datos de usuarios no se ha encontrado.{e}",
        QMessageBox.StandardButton.Close,
        QMessageBox.StandardButton.Close
    )
```

## 9. Integración entre Ventanas

### Llamada desde Login a RegistrarUsuarioView
```python
def iniciar_register(self):
    self.new_user_form = RegistrarUsuarioView()
    self.new_user_form.show()
```

**Flujo de la aplicación:**
1. Ventana Login principal
2. Al hacer click en "Register" se abre RegistrarUsuarioView (modal)
3. El usuario interactúa con el diálogo de registro
4. Al cerrarse, vuelve al Login

## 10. Mejoras en los Mensajes al Usuario

### Tipos de QMessageBox
```python
# Para advertencias
QMessageBox.warning()

# Para información positiva  
QMessageBox.information()

# Para errores críticos
QMessageBox.critical()
```

### Estructura de Parámetros
```python
QMessageBox.tipo(
    parent,           # Ventana padre
    "Título",         # Título del diálogo
    "Mensaje",        # Contenido del mensaje
    botón_por_defecto,
    botones_aceptados
)
```

## 11. Próximos Pasos Sugeridos

### Para Completar la Aplicación
1. **Implementar `iniciar_mainview`** con verificación de credenciales
2. **Leer el archivo usuarios.txt** para validar login
3. **Crear ventana principal** después del login exitoso
4. **Manejar encriptación** de contraseñas (no almacenar en texto plano)



# Guía de PyQt6 - Implementación Completa del Sistema

## 12. Cambios y Nuevas Funcionalidades Implementadas

### Cambio en el Método de Login
```python
# ANTES:
login_button.clicked.connect(self.iniciar_mainview)

# AHORA:
login_button.clicked.connect(self.login)  # Método renombrado y completamente implementado
```

### Implementación Completa del Sistema de Login
```python
def login(self):
    users = []
    user_path = "usuarios.txt"

    try:
        with open(user_path, "r") as f:
            for line in f:
                users.append(line.strip("\n"))
            
            # FORMATO CORREGIDO: "usuario,contraseña"
            login_information = f"{self.user_input.text()},{self.password_input.text()}"

            if login_information in users:
                QMessageBox.information(self, "Inicio de sesión", 
                                      "Inicio de sesión exitoso", 
                                      QMessageBox.StandardButton.Ok, 
                                      QMessageBox.StandardButton.Ok)
                self.is_logged = True
                self.close()
                self.open_main_window()  # ¡NUEVO!
            else:
                QMessageBox.warning(self, "Error Message", 
                                  "Usuario o contraseña incorrectos", 
                                  QMessageBox.StandardButton.Close, 
                                  QMessageBox.StandardButton.Close)
```

**Mejoras en la validación:**
- Lee el archivo `usuarios.txt` línea por línea
- Compara el formato `usuario,contraseña` exacto
- Maneja múltiples excepciones de forma específica

### Nueva Clase: MainWindow - Ventana Principal

```python
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUi()

    def inicializarUi(self):
        self.setGeometry(100, 100, 500, 500)  # Ventana más grande
        self.setWindowTitle("Ventana Principal")
        self.generar_contenido()
        self.show()
```

## 13. Manejo de Imágenes con QPixmap

### Carga y Visualización de Imágenes
```python
def generar_contenido(self):
    image_path = "galiciaFondo.jpg"
    try:
        with open(image_path):
            image_label = QLabel(self)
            image_label.setPixmap(QPixmap(image_path))
```

**Nuevos elementos utilizados:**
- **QPixmap**: Clase para manejar imágenes
- **setPixmap()**: Método para asignar imagen a QLabel
- **Manejo de errores específico** para archivos de imagen

### Manejo de Errores Mejorado
```python
except FileNotFoundError as e:
    QMessageBox.warning(
        self,
        "Error",
        f"No se pudo cargar la imagen: {e}",
        QMessageBox.StandardButton.Close,
        QMessageBox.StandardButton.Close
    )
except Exception as e:
    QMessageBox.warning(
        self,
        "Error", 
        f"Ocurrió un error inesperado: {e}",
        QMessageBox.StandardButton.Close,
        QMessageBox.StandardButton.Close
    )
```

## 14. Flujo Completo de la Aplicación

### Secuencia de Ventanas
1. **Login** → **MainWindow** (al login exitoso)
2. **Login** → **RegistrarUsuarioView** (al hacer click en Register)

### Cierre y Apertura de Ventanas
```python
self.close()           # Cierra la ventana actual (Login)
self.open_main_window() # Abre la nueva ventana (MainWindow)
```

## 15. Estructura de Archivos del Proyecto

### Módulos Importados
```python
from registro import RegistrarUsuarioView
from main import MainWindow
```

**Estructura sugerida:**
```
proyecto/
├── main.py           # Clase MainWindow
├── registro.py       # Clase RegistrarUsuarioView  
├── login.py          # Clase Login (archivo actual)
├── usuarios.txt      # Base de datos de usuarios
└── galiciaFondo.jpg  # Imagen de fondo
```

## 16. Mejoras de Robustez en el Código

### Manejo de Excepciones Específico
```python
except FileNotFoundError as e:
    # Error específico: archivo no encontrado
    QMessageBox.warning(self, "Error Message", 
                       f"No se ha encontrado el archivo de usuarios {e}")

except Exception as e:
    # Error genérico como fallback
    QMessageBox.warning(self, "Error Message", 
                       f"Ha ocurrido un error inesperado {e}")
```

### Validación de Formato de Datos
El código ahora espera el formato exacto en el archivo:
```
usuario1,contraseña1
usuario2,contraseña2
```

## 17. Próximas Mejoras Sugeridas

### Para la Imagen en MainWindow
```python
# Podrías añadir para que la imagen se ajuste al tamaño de la ventana
image_label.setScaledContents(True)
image_label.resize(self.width(), self.height())
```

### Para el Sistema de Login
- **Encriptación** de contraseñas en el archivo
- **Sesiones** con tiempo de expiración
- **Recuperación** de contraseñas

### Para la Interfaz
- **Layouts** para mejor posicionamiento automático
- **Estilos CSS** para personalizar apariencia
- **Iconos** en los botones


## 18. Introducción a QHBoxLayout

### Código de Layout Horizontal
```python
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setMinimumWidth(600)
        self.setFixedHeight(80)
        self.setWindowTitle('Layout Horizontal')
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        correo_label = QLabel("Correo electrónico: ")
        correo_input = QLineEdit()
        enviar_button = QPushButton("Enviar")

        layout = QHBoxLayout()
        layout.addWidget(correo_label)
        layout.addWidget(correo_input)
        layout.addWidget(enviar_button)

        self.setLayout(layout) # Definimos nuestro layout como el layout principal de la ventana

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())
```

### Explicación del Código

#### Importación de QHBoxLayout
```python
from PyQt6.QtWidgets import QHBoxLayout
```
- **QHBoxLayout**: Layout que organiza widgets en una fila horizontal

#### Creación del Layout
```python
layout = QHBoxLayout()
```
Crea un nuevo layout horizontal vacío.

#### Agregar Widgets al Layout
```python
layout.addWidget(correo_label)
layout.addWidget(correo_input)
layout.addWidget(enviar_button)
```
- **addWidget()**: Añade un widget al layout en orden secuencial

#### Establecer el Layout Principal
```python
self.setLayout(layout)
```
- **setLayout()**: Define este layout como el principal de la ventana

### Métodos Útiles de QHBoxLayout

#### Espaciado entre Widgets
```python
layout.setSpacing(10)  # 10 píxeles entre cada widget
```

#### Configurar Márgenes
```python
layout.setContentsMargins(20, 10, 20, 10)  # izquierda, arriba, derecha, abajo
```

#### Agregar Espacio Elástico
```python
layout.addStretch()  # Espacio que se expande para empujar widgets
```

### Ejemplo Mejorado con Funcionalidad
```python
def generar_formulario(self):
    correo_label = QLabel("Correo electrónico: ")
    self.correo_input = QLineEdit()  # Guardar referencia
    self.correo_input.setPlaceholderText("ejemplo@correo.com")
    
    enviar_button = QPushButton("Enviar")
    enviar_button.clicked.connect(self.enviar_correo)  # Conectar señal

    layout = QHBoxLayout()
    layout.setSpacing(15)  # Espacio entre widgets
    layout.setContentsMargins(20, 20, 20, 20)  # Márgenes
    
    layout.addWidget(correo_label)
    layout.addWidget(self.correo_input)
    layout.addWidget(enviar_button)
    
    self.setLayout(layout)

def enviar_correo(self):
    correo = self.correo_input.text()
    if correo:
        QMessageBox.information(self, "Éxito", f"Correo enviado a: {correo}")
    else:
        QMessageBox.warning(self, "Error", "Por favor ingrese un correo electrónico")
```

### Ventajas de Usar Layouts vs Posicionamiento Absoluto

#### Con Layouts (Recomendado)
```python
layout = QHBoxLayout()
layout.addWidget(QLabel("Texto"))
layout.addWidget(QLineEdit())
self.setLayout(layout)
```

#### Con Posicionamiento Absoluto (Menos Flexible)
```python
label = QLabel("Texto", self)
label.move(10, 10)
input = QLineEdit(self)
input.move(60, 10)
input.resize(200, 25)
```

**Beneficios de los layouts:**
- Se adaptan automáticamente al redimensionar la ventana
- Mantienen las proporciones entre widgets
- Más fácil de mantener y modificar
- Mejor organización del código

### Nota sobre la Importación Duplicada
En tu código hay:
```python
from PyQt6.QtWidgets import (..., QHBoxLayout, QHBoxLayout)
```
Puedes eliminar la duplicidad:
```python
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout)
```


## 19. QVBoxLayout y Manejo de Señales

### Código de Layout Vertical
```python
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setMinimumHeight(200)
        self.setFixedWidth(200)
        self.setWindowTitle('Layout Vertical')
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        boton1 = QPushButton("Botón #1")
        boton2 = QPushButton("Botón #2")
        boton3 = QPushButton("Botón #3")
        boton4 = QPushButton("Botón #4")

        boton1.clicked.connect(self.imprimir_nombre_boton)
        boton2.clicked.connect(self.imprimir_nombre_boton)
        boton3.clicked.connect(self.imprimir_nombre_boton)
        boton4.clicked.connect(self.imprimir_nombre_boton)

        layout = QVBoxLayout()
        layout.addWidget(boton1)
        layout.addWidget(boton2)
        layout.addWidget(boton3)
        layout.addWidget(boton4)

        self.setLayout(layout)  # Definimos nuestro layout como el layout principal de la ventana

    def imprimir_nombre_boton(self):
        boton = self.sender() # Obtiene el botón que envió la señal
        QMessageBox.information(self,"Boton press",f"Has presionado el {boton.text()}", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())
```

### Explicación del Código

#### Importación de QVBoxLayout
```python
from PyQt6.QtWidgets import QVBoxLayout
```
- **QVBoxLayout**: Layout que organiza widgets en una columna vertical

#### Configuración de la Ventana
```python
self.setMinimumHeight(200)
self.setFixedWidth(200)
```
- **setMinimumHeight()**: Establece la altura mínima de la ventana
- **setFixedWidth()**: Fija el ancho de la ventana (no redimensionable)

#### Creación de Botones
```python
boton1 = QPushButton("Botón #1")
boton2 = QPushButton("Botón #2")
# ...
```

#### Conexión Múltiple a la Misma Función
```python
boton1.clicked.connect(self.imprimir_nombre_boton)
boton2.clicked.connect(self.imprimir_nombre_boton)
# ...
```
Los 4 botones están conectados a la misma función `imprimir_nombre_boton`

#### Creación del Layout Vertical
```python
layout = QVBoxLayout()
layout.addWidget(boton1)
layout.addWidget(boton2)
layout.addWidget(boton3)
layout.addWidget(boton4)
self.setLayout(layout)
```

### La Función sender() - Concepto Importante

```python
def imprimir_nombre_boton(self):
    boton = self.sender() # Obtiene el botón que envió la señal
    QMessageBox.information(self,"Boton press",f"Has presionado el {boton.text()}", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
```

#### ¿Qué hace sender()?
- **sender()**: Retorna el objeto que emitió la señal
- Permite identificar qué widget específico activó la función
- Útil cuando múltiples widgets están conectados a la misma función

### Métodos Útiles de QVBoxLayout

#### Espaciado entre Widgets
```python
layout.setSpacing(10)  # 10 píxeles entre cada widget
```

#### Configurar Márgenes
```python
layout.setContentsMargins(20, 20, 20, 20)  # izquierda, arriba, derecha, abajo
```

#### Agregar Espacio Elástico
```python
layout.addStretch()  # Espacio que se expande para empujar widgets
```

### Ejemplo Mejorado con Más Configuraciones
```python
def generar_formulario(self):
    boton1 = QPushButton("Botón #1")
    boton2 = QPushButton("Botón #2")
    boton3 = QPushButton("Botón #3")
    boton4 = QPushButton("Botón #4")
    
    # Configurar tamaño de botones
    for boton in [boton1, boton2, boton3, boton4]:
        boton.setFixedHeight(40)
        boton.clicked.connect(self.imprimir_nombre_boton)

    layout = QVBoxLayout()
    layout.setSpacing(10)  # Espacio entre botones
    layout.setContentsMargins(20, 20, 20, 20)  # Márgenes
    
    layout.addWidget(boton1)
    layout.addWidget(boton2)
    layout.addStretch()  # Espacio elástico entre botón 2 y 3
    layout.addWidget(boton3)
    layout.addWidget(boton4)
    
    self.setLayout(layout)
```

### Comparación: QHBoxLayout vs QVBoxLayout

#### QHBoxLayout (Anterior)
```python
layout = QHBoxLayout()
layout.addWidget(widget1)  # ← Widget1 | Widget2 | Widget3 →
layout.addWidget(widget2)
layout.addWidget(widget3)
```

#### QVBoxLayout (Actual)
```python
layout = QVBoxLayout()
layout.addWidget(widget1)  # ↑ Widget1
layout.addWidget(widget2)  #   Widget2
layout.addWidget(widget3)  #   Widget3 ↓
```

### Ventajas de QVBoxLayout

1. **Organización vertical**: Ideal para formularios, listas de opciones
2. **Escalabilidad**: Fácil agregar más elementos sin recalcular posiciones
3. **Responsive**: Se adapta automáticamente al contenido

### Casos de Uso Comunes para QVBoxLayout

- Formularios de registro/login
- Listas de opciones/configuración
- Paneles de control verticales
- Menús de navegación


## 20. Layouts Anidados

### Código de Layouts Anidados
```python
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QLabel, QLineEdit)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100,100,400,150)
        self.setWindowTitle('Layouts Anidados')
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        mensaje_principal = QLabel("Por favor ingrasa sus datos: ")

        nombre_label = QLabel("Nombre: ")
        self.nombres_input = QLineEdit()
        apellido_label = QLabel("Apellido: ")
        self.apellidos_input = QLineEdit()
        edad_label = QLabel("Edad: ")
        self.edad_input = QLineEdit()
        correo_label = QLabel("Correo: ")
        self.correo_input = QLineEdit()
        direccion_label = QLabel("Dirección: ")
        self.direccion_input = QLineEdit()
        telefono_label = QLabel("Teléfono: ")
        self.telefono_input = QLineEdit()
        
        
        # Ajustamos el ancho de las etiquetas para que queden alineadas
        nombre_label.setFixedWidth(90)
        apellido_label.setFixedWidth(90)
        edad_label.setFixedWidth(90)
        correo_label.setFixedWidth(90)
        direccion_label.setFixedWidth(90)
        telefono_label.setFixedWidth(90)

        enviar_boton = QPushButton("Enviar")

        # creamos el layout vertical principal
        vertical_layout_main = QVBoxLayout()

        # creamos los layouts horizontales
        h_layout_1 = QHBoxLayout()
        h_layout_2 = QHBoxLayout()
        h_layout_3 = QHBoxLayout()

        # agregamos los widgets a los layouts horizontales
        h_layout_1.addWidget(nombre_label)
        h_layout_1.addWidget(self.nombres_input)
        h_layout_1.addWidget(correo_label)
        h_layout_1.addWidget(self.correo_input)

        h_layout_2.addWidget(apellido_label)
        h_layout_2.addWidget(self.apellidos_input)
        h_layout_2.addWidget(direccion_label)
        h_layout_2.addWidget(self.direccion_input)

        h_layout_3.addWidget(edad_label)
        h_layout_3.addWidget(self.edad_input)
        h_layout_3.addWidget(telefono_label)
        h_layout_3.addWidget(self.telefono_input)

        # agregamos los layouts horizontales al layout vertical principal
        vertical_layout_main.addWidget(mensaje_principal)
        vertical_layout_main.addLayout(h_layout_1)
        vertical_layout_main.addLayout(h_layout_2)
        vertical_layout_main.addLayout(h_layout_3)
        vertical_layout_main.addWidget(enviar_boton)

        self.setLayout(vertical_layout_main)  # Definimos nuestro layout como el layout principal de la ventana

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())
```

### Explicación del Código

#### Concepto de Layouts Anidados
Los layouts anidados consisten en combinar diferentes tipos de layouts (verticales y horizontales) para crear interfaces más complejas y organizadas.

#### Estructura de Layouts en Este Ejemplo
```
QVBoxLayout (principal)
├── QLabel (mensaje_principal)
├── QHBoxLayout (h_layout_1)
│   ├── QLabel (nombre)
│   ├── QLineEdit (nombres)
│   ├── QLabel (correo)
│   └── QLineEdit (correo)
├── QHBoxLayout (h_layout_2)
│   ├── QLabel (apellido)
│   ├── QLineEdit (apellidos)
│   ├── QLabel (dirección)
│   └── QLineEdit (dirección)
├── QHBoxLayout (h_layout_3)
│   ├── QLabel (edad)
│   ├── QLineEdit (edad)
│   ├── QLabel (teléfono)
│   └── QLineEdit (teléfono)
└── QPushButton (enviar_boton)
```

#### Configuración de Ancho Fijo para Etiquetas
```python
nombre_label.setFixedWidth(90)
apellido_label.setFixedWidth(90)
# ...
```
- **setFixedWidth()**: Establece un ancho fijo para el widget
- **Propósito**: Alinear verticalmente todos los labels para una apariencia más ordenada

#### Creación de Layouts Anidados
```python
# Layout vertical principal
vertical_layout_main = QVBoxLayout()

# Layouts horizontales anidados
h_layout_1 = QHBoxLayout()
h_layout_2 = QHBoxLayout()
h_layout_3 = QHBoxLayout()
```

#### Agregar Layouts Dentro de Otros Layouts
```python
vertical_layout_main.addLayout(h_layout_1)
vertical_layout_main.addLayout(h_layout_2)
vertical_layout_main.addLayout(h_layout_3)
```
- **addLayout()**: Agrega un layout dentro de otro layout

### Ventajas de los Layouts Anidados

1. **Organización compleja**: Permiten crear interfaces con estructuras más elaboradas
2. **Mantenimiento fácil**: Cada sección puede modificarse independientemente
3. **Responsive**: Se adaptan mejor al redimensionamiento
4. **Código más limpio**: Mejor organización y legibilidad

### Métodos Útiles para Mejorar los Layouts Anidados

#### Configurar Espaciado Consistente
```python
# Configurar espaciado para todos los layouts
vertical_layout_main.setSpacing(10)
h_layout_1.setSpacing(15)
h_layout_2.setSpacing(15)
h_layout_3.setSpacing(15)
```

#### Establecer Márgenes
```python
vertical_layout_main.setContentsMargins(20, 20, 20, 20)
```

#### Agregar Stretch para Controlar Espacios
```python
# Para que los campos de entrada ocupen más espacio
h_layout_1.addWidget(nombre_label)
h_layout_1.addWidget(self.nombres_input, 1)  # Proporción 1
h_layout_1.addWidget(correo_label)
h_layout_1.addWidget(self.correo_input, 2)   # Proporción 2 (más espacio)
```

### Ejemplo Mejorado con Validación
```python
def generar_formulario(self):
    # ... (código anterior de creación de widgets)
    
    enviar_boton.clicked.connect(self.validar_formulario)
    
    # ... (código anterior de layouts)

def validar_formulario(self):
    # Validar que todos los campos estén completos
    campos = [
        ("Nombre", self.nombres_input.text()),
        ("Apellido", self.apellidos_input.text()),
        ("Edad", self.edad_input.text()),
        ("Correo", self.correo_input.text()),
        ("Dirección", self.direccion_input.text()),
        ("Teléfono", self.telefono_input.text())
    ]
    
    campos_vacios = [nombre for nombre, valor in campos if not valor.strip()]
    
    if campos_vacios:
        QMessageBox.warning(self, "Campos vacíos", 
                           f"Los siguientes campos están vacíos: {', '.join(campos_vacios)}")
    else:
        QMessageBox.information(self, "Éxito", "Formulario enviado correctamente")
```

### Consejos para Diseñar con Layouts Anidados

1. **Planificar la estructura**: Dibujar la interfaz en papel antes de codificar
2. **Usar nombres descriptivos**: Para los layouts y variables
3. **Mantener la consistencia**: Mismos márgenes y espaciado en todos los layouts
4. **Probar el redimensionamiento**: Verificar que la interfaz se vea bien en diferentes tamaños

### Casos de Uso Comunes para Layouts Anidados

- Formularios complejos con múltiples secciones
- Paneles de control con agrupaciones lógicas
- Interfaces de aplicaciones con barras de herramientas y áreas de contenido
- Cuadros de diálogo con múltiples opciones organizadas


## 21. QGridLayout - Diseño en Cuadrícula

### Código de Calculadora con QGridLayout
```python
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QTextEdit, QPushButton, QGridLayout, QMessageBox)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100,100,600, 400)
        self.setWindowTitle("Calculadora Simple")
        self.generar_interfaz()
        self.show()

    def generar_interfaz(self):
        self.pantalla = QTextEdit(self)
        self.pantalla.setDisabled(True)
        boton_1 = QPushButton("1")
        boton_2 = QPushButton("2")
        boton_3 = QPushButton("3")
        boton_4 = QPushButton("4")
        boton_5 = QPushButton("5")
        boton_6 = QPushButton("6")
        boton_7 = QPushButton("7")
        boton_8 = QPushButton("8")
        boton_9 = QPushButton("9")
        boton_0 = QPushButton("0")
        boton_00 = QPushButton("00")
        boton_punto = QPushButton(".")
        boton_suma = QPushButton("+")
        boton_resta = QPushButton("-")
        boton_multiplicacion = QPushButton("*")
        boton_division = QPushButton("/")
        boton_igual = QPushButton("=")
        boton_clear = QPushButton("CE")
        boton_borrar = QPushButton("<-")

        self.main_grid = QGridLayout()
        self.main_grid.addWidget(self.pantalla,0,0,2,4) # 0 fila, 0 columna, ocupa 2 filas y 4 columnas
        self.main_grid.addWidget(boton_clear, 2,0, 1,2) # 2 fila, 0 columna, ocupa 1 fila y 2 columnas
        self.main_grid.addWidget(boton_borrar,2,2) # 2 fila, 2 columna(ocupa 1 fila y 1 columna por defecto)
        self.main_grid.addWidget(boton_suma,2,3) # 2 fila, 3 columna
        self.main_grid.addWidget(boton_7,3,0) # 3 fila 0 columna
        self.main_grid.addWidget(boton_8,3,1) # 3 fila 1 columna
        self.main_grid.addWidget(boton_9,3,2) # 3 fila 2 columna
        self.main_grid.addWidget(boton_division,3, 3) # 3 fila 3 columna
        self.main_grid.addWidget(boton_4,4,0) # 4 fila 0 columna
        self.main_grid.addWidget(boton_5,4,1) # 4 fila
        self.main_grid.addWidget(boton_6,4,2) # 4 fila 2 columna
        self.main_grid.addWidget(boton_multiplicacion,4,3) # 4 fila 3 columna
        self.main_grid.addWidget(boton_1,5,0) # 5 fila 0 columna
        self.main_grid.addWidget(boton_2,5,1) # 5 fila 1 columna
        self.main_grid.addWidget(boton_3,5,2) # 5 fila 2 columna
        self.main_grid.addWidget(boton_resta,5,3) # 5 fila 3 columna
        self.main_grid.addWidget(boton_0,6,0) # 6 fila 0 columna
        self.main_grid.addWidget(boton_00,6,1) # 6 fila 1 columna
        self.main_grid.addWidget(boton_punto,6,2) # 6 fila 2 columna
        self.main_grid.addWidget(boton_igual,6,3) # 6 fila 3 columna

        self.setLayout(self.main_grid)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())
```

### Explicación del Código

#### QGridLayout - Layout de Cuadrícula
```python
self.main_grid = QGridLayout()
```
- **QGridLayout**: Organiza widgets en una cuadrícula de filas y columnas
- Ideal para interfaces que necesitan disposición tabular como calculadoras, teclados, etc.

#### Sintaxis de addWidget en QGridLayout
```python
self.main_grid.addWidget(widget, fila, columna, rowSpan, colSpan)
```

**Parámetros:**
- **widget**: El widget a agregar
- **fila**: Número de fila (empieza en 0)
- **columna**: Número de columna (empieza en 0)
- **rowSpan**: Cuántas filas ocupa (opcional, default: 1)
- **colSpan**: Cuántas columnas ocupa (opcional, default: 1)

#### Ejemplos del Código

**Pantalla que ocupa 2 filas y 4 columnas:**
```python
self.main_grid.addWidget(self.pantalla, 0, 0, 2, 4)
```
- Fila: 0
- Columna: 0
- Ocupa 2 filas
- Ocupa 4 columnas

**Botón CE que ocupa 1 fila y 2 columnas:**
```python
self.main_grid.addWidget(boton_clear, 2, 0, 1, 2)
```

**Botón normal (ocupa 1x1):**
```python
self.main_grid.addWidget(boton_7, 3, 0)
```

### Estructura de la Cuadrícula de la Calculadora

```
Fila 0-1: [          Pantalla (4 columnas)          ]
Fila 2:   [ CE (2 cols) ] [ <- ] [ + ]
Fila 3:   [ 7 ] [ 8 ] [ 9 ] [ / ]
Fila 4:   [ 4 ] [ 5 ] [ 6 ] [ * ]
Fila 5:   [ 1 ] [ 2 ] [ 3 ] [ - ]
Fila 6:   [ 0 ] [ 00 ] [ . ] [ = ]
```

### QTextEdit como Pantalla
```python
self.pantalla = QTextEdit(self)
self.pantalla.setDisabled(True)
```
- **QTextEdit**: Widget de texto multilínea
- **setDisabled(True)**: Hace que la pantalla sea de solo lectura
- Alternativa: `QLineEdit` para una sola línea o `QLabel`

### Métodos Útiles de QGridLayout

#### Configurar Espaciado
```python
self.main_grid.setSpacing(5)  # Espacio entre celdas
```

#### Configurar Márgenes
```python
self.main_grid.setContentsMargins(10, 10, 10, 10)
```

#### Obtener Información de la Cuadrícula
```python
row_count = self.main_grid.rowCount()
column_count = self.main_grid.columnCount()
```

### Ejemplo Mejorado con Configuraciones Adicionales
```python
def generar_interfaz(self):
    # Configurar pantalla
    self.pantalla = QTextEdit(self)
    self.pantalla.setDisabled(True)
    self.pantalla.setMaximumHeight(80)  # Limitar altura
    
    # Crear botones (código existente)
    # ...
    
    self.main_grid = QGridLayout()
    self.main_grid.setSpacing(5)  # Espacio entre botones
    self.main_grid.setContentsMargins(15, 15, 15, 15)  # Márgenes
    
    # Agregar widgets (código existente)
    # ...
    
    # Configurar tamaño de botones
    botones = [boton_0, boton_1, boton_2, boton_3, boton_4, 
               boton_5, boton_6, boton_7, boton_8, boton_9,
               boton_00, boton_punto, boton_suma, boton_resta,
               boton_multiplicacion, boton_division, boton_igual,
               boton_clear, boton_borrar]
    
    for boton in botones:
        boton.setFixedSize(60, 50)  # Tamaño uniforme para todos los botones
    
    self.setLayout(self.main_grid)
```

### Ventajas de QGridLayout

1. **Precisión**: Control exacto de la posición de cada widget
2. **Flexibilidad**: Widgets pueden ocupar múltiples celdas
3. **Organización**: Ideal para interfaces con estructura de tabla
4. **Escalabilidad**: Fácil agregar más filas/columnas

### Casos de Uso Comunes para QGridLayout

- Calculadoras
- Teclados numéricos
- Interfaces de tablero de instrumentos
- Formularios complejos con etiquetas y campos alineados
- Juegos de tablero

### Comparación con Otros Layouts

| Layout | Uso Ideal | Ventajas |
|--------|-----------|----------|
| **QGridLayout** | Interfaces tabulares | Máximo control de posición |
| **QHBoxLayout** | Filas horizontales | Simple, orden lineal |
| **QVBoxLayout** | Columnas verticales | Simple, orden vertical |
| **Anidados** | Interfaces complejas | Combinación de estructuras |


## 22. Calculadora Funcional - Lógica Completa

### Código Completo de la Calculadora Funcional

```python
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QTextEdit, QPushButton, QGridLayout, QMessageBox)
import operator

# Diccionario para mapear los operadores a las funciones correspondientes
# Esto trabaja con strings para facilitar la selección del operador
operation = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.primerValor = ""
        self.segundoValor = ""
        self.operacion = ""
        self.pointer_flag = "1"
        self.after_equal = False
        self.after_operator = False

    def inicializarUI(self):
        self.setGeometry(100,100,600, 400)
        self.setWindowTitle("Calculadora Simple")
        self.generar_interfaz()
        self.show()

    def generar_interfaz(self):
        self.pantalla = QTextEdit(self)
        self.pantalla.setDisabled(True)
        boton_1 = QPushButton("1")
        boton_2 = QPushButton("2")
        boton_3 = QPushButton("3")
        boton_4 = QPushButton("4")
        boton_5 = QPushButton("5")
        boton_6 = QPushButton("6")
        boton_7 = QPushButton("7")
        boton_8 = QPushButton("8")
        boton_9 = QPushButton("9")
        boton_0 = QPushButton("0")
        boton_00 = QPushButton("00")
        boton_punto = QPushButton(".")

        # Conectamos los botones numéricos a la función ingresar_datos
        boton_1.clicked.connect(self.ingresar_datos)
        boton_2.clicked.connect(self.ingresar_datos)
        boton_3.clicked.connect(self.ingresar_datos)
        boton_4.clicked.connect(self.ingresar_datos)
        boton_5.clicked.connect(self.ingresar_datos)
        boton_6.clicked.connect(self.ingresar_datos)
        boton_7.clicked.connect(self.ingresar_datos)
        boton_8.clicked.connect(self.ingresar_datos)
        boton_9.clicked.connect(self.ingresar_datos)
        boton_0.clicked.connect(self.ingresar_datos)
        boton_00.clicked.connect(self.ingresar_datos)
        boton_punto.clicked.connect(self.ingresar_datos)

        boton_suma = QPushButton("+")
        boton_resta = QPushButton("-")
        boton_multiplicacion = QPushButton("*")
        boton_division = QPushButton("/")
        boton_igual = QPushButton("=")
        boton_clear = QPushButton("CE")
        boton_borrar = QPushButton("<-")

        boton_suma.clicked.connect(self.ingresar_operador)
        boton_resta.clicked.connect(self.ingresar_operador)
        boton_multiplicacion.clicked.connect(self.ingresar_operador)
        boton_division.clicked.connect(self.ingresar_operador)

        boton_clear.clicked.connect(self.borrar_todo)
        boton_borrar.clicked.connect(self.borrar_parcial)
        boton_igual.clicked.connect(self.calcular_resultado)

        self.main_grid = QGridLayout()
        self.main_grid.addWidget(self.pantalla,0,0,2,4) # 0 fila, 0 columna, ocupa 2 filas y 4 columnas
        self.main_grid.addWidget(boton_clear, 2,0, 1,2) # 2 fila, 0 columna, ocupa 1 fila y 2 columnas
        self.main_grid.addWidget(boton_borrar,2,2) # 2 fila, 2 columna(ocupa 1 fila y 1 columna por defecto)
        self.main_grid.addWidget(boton_suma,2,3) # 2 fila, 3 columna
        self.main_grid.addWidget(boton_7,3,0) # 3 fila 0 columna
        self.main_grid.addWidget(boton_8,3,1) # 3 fila 1 columna
        self.main_grid.addWidget(boton_9,3,2) # 3 fila 2 columna
        self.main_grid.addWidget(boton_division,3, 3) # 3 fila 3 columna
        self.main_grid.addWidget(boton_4,4,0) # 4 fila 0 columna
        self.main_grid.addWidget(boton_5,4,1) # 4 fila
        self.main_grid.addWidget(boton_6,4,2) # 4 fila 2 columna
        self.main_grid.addWidget(boton_multiplicacion,4,3) # 4 fila 3 columna
        self.main_grid.addWidget(boton_1,5,0) # 5 fila 0 columna
        self.main_grid.addWidget(boton_2,5,1) # 5 fila 1 columna
        self.main_grid.addWidget(boton_3,5,2) # 5 fila 2 columna
        self.main_grid.addWidget(boton_resta,5,3) # 5 fila 3 columna
        self.main_grid.addWidget(boton_0,6,0) # 6 fila 0 columna
        self.main_grid.addWidget(boton_00,6,1) # 6 fila 1 columna
        self.main_grid.addWidget(boton_punto,6,2) # 6 fila 2 columna
        self.main_grid.addWidget(boton_igual,6,3) # 6 fila 3 columna

        self.setLayout(self.main_grid)

    def ingresar_datos(self):
        boton_text = self.sender().text()
        if self.after_equal:
            self.primerValor = ""
            self.pantalla.setText(self.primerValor)
            self.after_equal = False
            self.pointer_flag = "1"
        if self.pointer_flag == "1":
            self.primerValor += boton_text
            self.pantalla.setText(self.primerValor)
        else:
            self.segundoValor += boton_text
            self.pantalla.setText(self.pantalla.toPlainText()+boton_text)

    def ingresar_operador(self):
        boton_text = self.sender().text()
        self.operacion = boton_text
        self.pointer_flag = "2"

        if self.after_operator == True and self.segundoValor != "":
            self.calcular_resultado()
            self.pantalla.setText(self.primerValor + " "+self.sender().text()+"" + self.operacion + " ")
        else:
            self.pantalla.setText(self.pantalla.toPlainText() + " " + self.operacion + " ")

        self.after_operator = True
        self.after_equal = False

    def borrar_todo(self):
        self.primerValor = ""
        self.segundoValor = ""
        self.operacion = ""
        self.pointer_flag = "1"
        self.after_equal = False
        self.after_operator = False
        self.pantalla.setText("")

    def borrar_parcial(self):
        if self.after_equal:
            self.borrar_todo()
        if self.pointer_flag == "1":
            self.primerValor = self.primerValor[:-1]
            self.pantalla.setText(self.primerValor)
        else:
            self.segundoValor = self.segundoValor[:-1]
            self.pantalla.setText(self.segundoValor)

    def calcular_resultado(self):
        resultado = str(operation[self.operacion](float(self.primerValor), float(self.segundoValor)))
        self.pantalla.setText(resultado)
        self.primerValor = resultado
        self.segundoValor = ""
        self.operacion = ""
        self.after_equal = True
        self.after_operator = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())
```

### Explicación de la Lógica de la Calculadora

#### Variables de Estado
```python
self.primerValor = ""        # Primer número de la operación
self.segundoValor = ""       # Segundo número de la operación  
self.operacion = ""          # Operador actual (+, -, *, /)
self.pointer_flag = "1"      # Indica si estamos en el primer o segundo valor
self.after_equal = False     # Indica si acabamos de presionar "="
self.after_operator = False  # Indica si acabamos de presionar un operador
```

#### Uso del Módulo Operator
```python
import operator

operation = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
```
- **operator**: Módulo de Python que proporciona funciones para operadores aritméticos
- **operation**: Diccionario que mapea símbolos de operadores a funciones

#### Función `ingresar_datos`
```python
def ingresar_datos(self):
    boton_text = self.sender().text()
    if self.after_equal:
        self.primerValor = ""
        self.pantalla.setText(self.primerValor)
        self.after_equal = False
        self.pointer_flag = "1"
    if self.pointer_flag == "1":
        self.primerValor += boton_text
        self.pantalla.setText(self.primerValor)
    else:
        self.segundoValor += boton_text
        self.pantalla.setText(self.pantalla.toPlainText()+boton_text)
```

**Flujo:**
1. Obtiene el texto del botón presionado con `self.sender().text()`
2. Si se acaba de presionar "=", reinicia el estado
3. Dependiendo de `pointer_flag`, concatena al primer o segundo valor
4. Actualiza la pantalla

#### Función `ingresar_operador`
```python
def ingresar_operador(self):
    boton_text = self.sender().text()
    self.operacion = boton_text
    self.pointer_flag = "2"

    if self.after_operator == True and self.segundoValor != "":
        self.calcular_resultado()
        self.pantalla.setText(self.primerValor + " "+self.sender().text()+"" + self.operacion + " ")
    else:
        self.pantalla.setText(self.pantalla.toPlainText() + " " + self.operacion + " ")

    self.after_operator = True
    self.after_equal = False
```

**Funcionamiento:**
- Cambia `pointer_flag` a "2" para comenzar a recibir el segundo valor
- Si ya hay una operación en curso, calcula el resultado primero
- Actualiza la pantalla con el operador

#### Función `borrar_todo` (CE)
```python
def borrar_todo(self):
    self.primerValor = ""
    self.segundoValor = ""
    self.operacion = ""
    self.pointer_flag = "1"
    self.after_equal = False
    self.after_operator = False
    self.pantalla.setText("")
```
Reinicia completamente el estado de la calculadora.

#### Función `borrar_parcial` (<-)
```python
def borrar_parcial(self):
    if self.after_equal:
        self.borrar_todo()
    if self.pointer_flag == "1":
        self.primerValor = self.primerValor[:-1]
        self.pantalla.setText(self.primerValor)
    else:
        self.segundoValor = self.segundoValor[:-1]
        self.pantalla.setText(self.segundoValor)
```
Elimina el último carácter del valor actual.

#### Función `calcular_resultado` (=)
```python
def calcular_resultado(self):
    resultado = str(operation[self.operacion](float(self.primerValor), float(self.segundoValor)))
    self.pantalla.setText(resultado)
    self.primerValor = resultado
    self.segundoValor = ""
    self.operacion = ""
    self.after_equal = True
    self.after_operator = False
```

**Proceso:**
1. Usa el diccionario `operation` para obtener la función del operador
2. Convierte los valores a float y realiza la operación
3. Muestra el resultado
4. Guarda el resultado en `primerValor` para operaciones consecutivas
5. Actualiza las banderas de estado

### Conexión de Señales

#### Botones Numéricos
```python
boton_1.clicked.connect(self.ingresar_datos)
boton_2.clicked.connect(self.ingresar_datos)
# ... todos los botones numéricos
```

#### Botones de Operación
```python
boton_suma.clicked.connect(self.ingresar_operador)
boton_resta.clicked.connect(self.ingresar_operador)
# ... todos los operadores
```

#### Botones de Control
```python
boton_clear.clicked.connect(self.borrar_todo)
boton_borrar.clicked.connect(self.borrar_parcial)
boton_igual.clicked.connect(self.calcular_resultado)
```

### Flujo de una Operación Completa

**Ejemplo: 5 + 3 =**

1. **Presionar "5"**: `primerValor = "5"`, pantalla muestra "5"
2. **Presionar "+"**: `operacion = "+"`, `pointer_flag = "2"`, pantalla muestra "5 +"
3. **Presionar "3"**: `segundoValor = "3"`, pantalla muestra "5 + 3"
4. **Presionar "="**: Calcula 5+3=8, pantalla muestra "8", `primerValor = "8"`

### Mejoras Potenciales

1. **Manejo de errores**: División por cero, números muy grandes
2. **Validación de entrada**: Evitar múltiples puntos decimales
3. **Operaciones con decimales**: Mejor manejo de números flotantes
4. **Historial**: Mostrar la operación completa
5. **Teclado**: Soporte para entrada por teclado

## 23. QFormLayout - Diseño Especializado para Formularios

### Código del Formulario con QFormLayout
```python
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
```

### Explicación del Código

#### QFormLayout - Layout Especializado para Formularios
```python
main_form = QFormLayout()
```
- **QFormLayout**: Diseñado específicamente para formularios con etiquetas y campos
- Organiza automáticamente las etiquetas y los campos de entrada
- Ideal para formularios de registro, configuración, etc.

#### Estructura del QFormLayout
```
[Etiqueta] [Campo/Widget]
[Etiqueta] [Campo/Widget]
...
```

#### Agregar Filas al FormLayout
```python
main_form.addRow(titulo)  # Fila con un solo widget
main_form.addRow("Nombre y Apellido: ", primer_h_box)  # Fila con etiqueta y layout
main_form.addRow("Género: ", self.genero_selection)  # Fila con etiqueta y widget
```

### Nuevos Widgets Introducidos

#### QComboBox - Lista Desplegable
```python
self.genero_selection = QComboBox()
self.genero_selection.addItems(["Masculino", "Femenino", "Otro"])
```
- **QComboBox**: Widget de selección desplegable
- **addItems()**: Añade múltiples opciones a la lista

#### QDateEdit - Selector de Fecha
```python
self.fechaNacimiento = QDateEdit()
self.fechaNacimiento.setDisplayFormat("yyyy-MM-dd")
self.fechaNacimiento.setMaximumDate(QDate.currentDate())
self.fechaNacimiento.setCalendarPopup(True)
self.fechaNacimiento.setDate(QDate.currentDate())
```

**Configuraciones:**
- **setDisplayFormat()**: Formato de visualización de la fecha
- **setMaximumDate()**: Fecha máxima permitida
- **setCalendarPopup(True)**: Muestra un calendario desplegable
- **setDate()**: Fecha inicial

#### Placeholder Text
```python
self.nombreEdit.setPlaceholderText("Nombre")
```
- **setPlaceholderText()**: Texto de ejemplo que desaparece al escribir

### Configuraciones de Texto y Fuente

#### QFont - Configuración de Fuente
```python
titulo.setFont(QFont('Arial',18))
```
- **QFont**: Clase para configurar fuentes tipográficas
- Parámetros: familia de fuente y tamaño

#### Alineación de Texto
```python
titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
```
- **AlignmentFlag.AlignCenter**: Centra el texto horizontalmente

### Combinación de Layouts

#### QHBoxLayout dentro de QFormLayout
```python
primer_h_box = QHBoxLayout()
primer_h_box.addWidget(self.nombreEdit)
primer_h_box.addWidget(self.apellidoEdit)

main_form.addRow("Nombre y Apellido: ", primer_h_box)
```
- Se puede incluir cualquier layout dentro de una fila de QFormLayout
- Útil para agrupar múltiples widgets en una misma fila

### Métodos Útiles de QFormLayout

#### Agregar Diferentes Tipos de Filas
```python
# Fila con etiqueta de texto y widget
main_form.addRow("Etiqueta:", widget)

# Fila con QLabel y widget
main_form.addRow(QLabel("Etiqueta"), widget)

# Fila con solo un widget (ocupa ambas columnas)
main_form.addRow(widget)

# Fila con layout
main_form.addRow("Etiqueta:", layout)
```

#### Configurar Espaciado y Márgenes
```python
main_form.setSpacing(10)  # Espacio entre filas
main_form.setContentsMargins(20, 20, 20, 20)  # Márgenes
```

#### Configurar Alineación de Etiquetas
```python
main_form.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
```

### Función de Mostrar Información
```python
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
```

**Métodos utilizados:**
- **text()**: Obtiene el texto de QLineEdit
- **currentText()**: Obtiene el texto seleccionado en QComboBox
- **date().toString()**: Convierte QDate a string

### Ventajas de QFormLayout

1. **Organización automática**: Alinea perfectamente etiquetas y campos
2. **Código más limpio**: Menos código para lograr el mismo resultado
3. **Consistencia visual**: Todas las etiquetas tienen el mismo ancho y alineación
4. **Adaptabilidad**: Se ajusta automáticamente al contenido

### Ejemplo Mejorado con Validación
```python
def crearFormulario(self):
    # ... (código anterior)
    
    submit_button.clicked.connect(self.validar_y_mostrar)
    # ...

def validar_y_mostrar(self):
    # Validar campos obligatorios
    if not self.nombreEdit.text().strip() or not self.apellidoEdit.text().strip():
        QMessageBox.warning(self, "Error", "Nombre y Apellido son obligatorios")
        return
    
    # Validar teléfono (solo números)
    if not self.telefono.text().replace("-", "").isdigit():
        QMessageBox.warning(self, "Error", "El teléfono debe contener solo números")
        return
    
    self.mostrar_info()
```

### Casos de Uso Ideales para QFormLayout

- Formularios de registro de usuarios
- Configuraciones de aplicación
- Paneles de administración
- Diálogos de preferencias
- Formularios de contacto

### Comparación con Otros Layouts para Formularios

| Layout | Ventajas para Formularios |
|--------|---------------------------|
| **QFormLayout** | Automático, etiquetas alineadas, menos código |
| **QGridLayout** | Control total, posiciones exactas |
| **QVBoxLayout** | Simple pero requiere más configuración manual |

# Guía de PyQt6 - Continuación

## 23. Widgets de Selección y Layouts Anidados Avanzados

### Código de la Aplicación con Múltiples Widgets
```python
import sys

from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit, QPushButton, QCheckBox, QRadioButton,
                             QVBoxLayout, QComboBox, QSpinBox, QHBoxLayout, QTextEdit)

class Limitador(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

        self.show()

    def inicializarUI(self):

        self.cajaVerticalRadioButton()

        self.cajaVerticalCheckButton()

        self.cajaVerticalImputs()

        self.cajaHorizontal = QHBoxLayout()

        self.cajaHorizontal.addLayout(self.verticalCaja1)
        self.cajaHorizontal.addLayout(self.verticalCaja2)
        self.cajaHorizontal.addLayout(self.cajaImputs)


        self.texto = QTextEdit()
        self.texto.setPlaceholderText("Original")
        self.texto.setReadOnly(True)
        self.texto.setFixedHeight(35)
        self.cajaV = QVBoxLayout()

        self.cajaV.addWidget(self.texto)
        self.cajaV.addLayout(self.cajaHorizontal)


        self.setLayout(self.cajaV)



    def cajaVerticalImputs(self):
        self.inputText = QLineEdit()
        self.desplegable = QComboBox()
        self.inputNumber = QSpinBox()

        self.desplegable.addItems(["Item 1", "Item 2", "Item 3"])

        self.cajaImputs = QVBoxLayout()

        self.cajaImputs.addWidget(self.inputText)
        self.cajaImputs.addWidget(self.desplegable)
        self.cajaImputs.addWidget(self.inputNumber)


    def cajaVerticalCheckButton(self):
        self.cuadroCheck1 = QCheckBox("Opcion 4")
        self.cuadroCheck2 = QCheckBox("Opcion 5")
        self.cuadroCheck3 = QCheckBox("Opcion 6")

        self.verticalCaja2 = QVBoxLayout()

        self.verticalCaja2.addWidget(self.cuadroCheck1)
        self.verticalCaja2.addWidget(self.cuadroCheck2)
        self.verticalCaja2.addWidget(self.cuadroCheck3)



    def cajaVerticalRadioButton(self):
        self.boton1 = QRadioButton("Opcion 1")
        self.boton2 = QRadioButton("Opcion 2")
        self.boton3 = QRadioButton("Opcion 3")

        self.verticalCaja1 = QVBoxLayout()
        self.verticalCaja1.addWidget(self.boton1)
        self.verticalCaja1.addWidget(self.boton2)
        self.verticalCaja1.addWidget(self.boton3)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Limitador()
    sys.exit(app.exec())
```

### Explicación del Código

#### Estructura de Layouts Anidados
```
QVBoxLayout (principal)
├── QTextEdit (área de texto)
└── QHBoxLayout (horizontal)
    ├── QVBoxLayout (radio buttons)
    ├── QVBoxLayout (check boxes)
    └── QVBoxLayout (campos de entrada)
```

### Nuevos Widgets de Selección

#### QRadioButton - Botones de Opción Única
```python
self.boton1 = QRadioButton("Opcion 1")
self.boton2 = QRadioButton("Opcion 2")
self.boton3 = QRadioButton("Opcion 3")
```
- **QRadioButton**: Permite seleccionar una sola opción de un grupo
- Solo un RadioButton puede estar seleccionado a la vez dentro del mismo grupo padre

#### QCheckBox - Casillas de Verificación Múltiples
```python
self.cuadroCheck1 = QCheckBox("Opcion 4")
self.cuadroCheck2 = QCheckBox("Opcion 5")
self.cuadroCheck3 = QCheckBox("Opcion 6")
```
- **QCheckBox**: Permite seleccionar múltiples opciones independientemente
- Cada casilla puede estar activada o desactivada sin afectar a las demás

#### QSpinBox - Selector Numérico
```python
self.inputNumber = QSpinBox()
```
- **QSpinBox**: Widget para seleccionar valores numéricos
- Permite incrementar/decrementar el valor con flechas o escribiendo

#### QComboBox - Lista Desplegable
```python
self.desplegable = QComboBox()
self.desplegable.addItems(["Item 1", "Item 2", "Item 3"])
```
- **QComboBox**: Lista desplegable de opciones
- **addItems()**: Añade múltiples elementos a la lista

### Configuraciones Específicas de Widgets

#### QTextEdit Configurado como Solo Lectura
```python
self.texto = QTextEdit()
self.texto.setPlaceholderText("Original")
self.texto.setReadOnly(True)
self.texto.setFixedHeight(35)
```
- **setReadOnly(True)**: Impide que el usuario edite el texto
- **setFixedHeight()**: Establece una altura fija
- **setPlaceholderText()**: Texto que aparece cuando está vacío

### Organización Modular del Código

#### Ventajas de Separar en Métodos
```python
def cajaVerticalRadioButton(self):
def cajaVerticalCheckButton(self):
def cajaVerticalImputs(self):
```
- **Mantenibilidad**: Cada sección es independiente y fácil de modificar
- **Reutilización**: Los métodos pueden ser llamados múltiples veces
- **Legibilidad**: Código más organizado y fácil de entender

### Métodos Útiles para los Widgets

#### Para QRadioButton
```python
# Verificar si está seleccionado
if self.boton1.isChecked():
    print("Opción 1 seleccionada")

# Seleccionar programáticamente
self.boton1.setChecked(True)

# Conectar a una función cuando cambie el estado
self.boton1.toggled.connect(self.radio_cambiado)
```

#### Para QCheckBox
```python
# Verificar estado
if self.cuadroCheck1.isChecked():
    print("Checkbox 1 activado")

# Cambiar estado programáticamente
self.cuadroCheck1.setChecked(True)

# Conectar cuando cambie el estado
self.cuadroCheck1.stateChanged.connect(self.checkbox_cambiado)
```

#### Para QSpinBox
```python
# Configurar rango de valores
self.inputNumber.setRange(0, 100)  # Mínimo 0, máximo 100

# Configurar paso de incremento
self.inputNumber.setSingleStep(5)  # Incrementa de 5 en 5

# Obtener valor actual
valor = self.inputNumber.value()

# Conectar cuando cambie el valor
self.inputNumber.valueChanged.connect(self.numero_cambiado)
```

#### Para QComboBox
```python
# Obtener texto seleccionado
seleccion = self.desplegable.currentText()

# Obtener índice seleccionado
indice = self.desplegable.currentIndex()

# Agregar un item individual
self.desplegable.addItem("Nuevo Item")

# Conectar cuando cambie la selección
self.desplegable.currentTextChanged.connect(self.combo_cambiado)
```

### Ejemplo Mejorado con Funcionalidades

```python
def inicializarUI(self):
    # ... código existente ...
    
    # Conectar señales
    self.conectar_señales()
    
    # ... resto del código ...

def conectar_señales(self):
    # Conectar radio buttons
    self.boton1.toggled.connect(self.actualizar_texto)
    self.boton2.toggled.connect(self.actualizar_texto)
    self.boton3.toggled.connect(self.actualizar_texto)
    
    # Conectar check boxes
    self.cuadroCheck1.stateChanged.connect(self.actualizar_texto)
    self.cuadroCheck2.stateChanged.connect(self.actualizar_texto)
    self.cuadroCheck3.stateChanged.connect(self.actualizar_texto)
    
    # Conectar otros widgets
    self.inputText.textChanged.connect(self.actualizar_texto)
    self.desplegable.currentTextChanged.connect(self.actualizar_texto)
    self.inputNumber.valueChanged.connect(self.actualizar_texto)

def actualizar_texto(self):
    # Recopilar información de todos los widgets
    radio_seleccionado = ""
    if self.boton1.isChecked():
        radio_seleccionado = "Opción 1"
    elif self.boton2.isChecked():
        radio_seleccionado = "Opción 2"
    elif self.boton3.isChecked():
        radio_seleccionado = "Opción 3"
    
    checks_seleccionados = []
    if self.cuadroCheck1.isChecked():
        checks_seleccionados.append("Opción 4")
    if self.cuadroCheck2.isChecked():
        checks_seleccionados.append("Opción 5")
    if self.cuadroCheck3.isChecked():
        checks_seleccionados.append("Opción 6")
    
    texto = f"Radio: {radio_seleccionado}\n"
    texto += f"Checks: {', '.join(checks_seleccionados) if checks_seleccionados else 'Ninguno'}\n"
    texto += f"Texto: {self.inputText.text()}\n"
    texto += f"Combo: {self.desplegable.currentText()}\n"
    texto += f"Número: {self.inputNumber.value()}"
    
    self.texto.setPlainText(texto)
```

### Diferencias Entre RadioButton y CheckBox

| Característica | QRadioButton | QCheckBox |
|----------------|--------------|-----------|
| **Selección** | Única | Múltiple |
| **Grupo** | Excluyente | Independiente |
| **Uso** | Opciones mutuamente excluyentes | Opciones que pueden combinarse |
| **Estado** | Solo uno activo | Cualquier combinación |

### Consejos para el Diseño de Interfaces

1. **Agrupar lógicamente**: Radio buttons para opciones excluyentes, checkboxes para opciones múltiples
2. **Usar labels descriptivos**: Los textos deben ser claros y concisos
3. **Organizar visualmente**: Agrupar elementos relacionados
4. **Proporcionar feedback**: Mostrar cómo afectan las selecciones

### Casos de Uso Típicos

- **QRadioButton**: Selección de género, tipo de usuario, categoría única
- **QCheckBox**: Selección de intereses, características, permisos
- **QSpinBox**: Edad, cantidad, valores numéricos discretos
- **QComboBox**: Selección de país, categoría, opciones predefinidas
