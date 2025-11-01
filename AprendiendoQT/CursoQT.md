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

# Guía de PyQt6 - Continuación

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

