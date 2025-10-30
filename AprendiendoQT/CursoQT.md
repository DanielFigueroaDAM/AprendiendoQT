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


Perfecto, voy a expandir la guía con este nuevo código de formulario de login:

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

