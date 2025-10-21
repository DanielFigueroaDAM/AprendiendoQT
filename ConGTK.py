import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class Ventana(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        self.set_title("Ventana GTK 4 en Python")
        self.set_default_size(400, 300)
        self.nome = ""

        # Caja vertical
        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        caja.set_margin_top(20)
        caja.set_margin_bottom(20)
        caja.set_margin_start(20)
        caja.set_margin_end(20)

        # Entry
        self.barraEsc = Gtk.Entry()
        self.barraEsc.set_placeholder_text("Escribe tu nombre aquí...")
        self.barraEsc.connect("changed", self.actualizar_label)  # Conecta la señal

        # Label
        self.label = Gtk.Label(label="¡Hola, " + self.nome + " mundo desde GTK 4!")

        # Añadir widgets a la caja
        caja.append(self.barraEsc)
        caja.append(self.label)

        # Añadir la caja a la ventana
        self.set_child(caja)


    def actualizar_label(self, entry):
        # Actualiza el nombre y el texto del label
        self.nome = entry.get_text()
        self.label.set_text(f"¡Hola, {self.nome} mundo desde GTK 4!")

class Aplicacion(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.ejemplo.ventana")

    def do_activate(self):
        ventana = Ventana(self)
        ventana.present()

app = Aplicacion()
app.run()
