import gi
gi.require_version("GTK","3.0")
from gi.repository import Gtk, Gdk, GObject

class ExemploBoxColor(GTK.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo de uso de box layout")



        caixa = Gtk.Box (orientation = Gtk.Orientation.HORIZONTAL, spacing = 10)
        caixav1 = Gtk.Box (orientation = Gtk.Orientation.VERTICAL, spacing = 10)
        caixav1.pack_start(caixaCor.CaixaCor('red'), True, True, 5)
        caixav1.pack_start(caixaCor.CaixaCor('blue'), True, True, 5)
        caixav1.pack_start(caixaCor.CaixaCor('green'), True, True, 5)

        caixa.pack_start(caixav1, True,True, 5)

        caixa.pack_start(caixaCor.CaixaCor('yellow'), True, True, 5)

        caixav2 = Gtk.Box (orientation = Gtk.Orientation.VERTICAL, spacing = 10)
        caixav2.pack_start (caixaCor.CaixaCor('orange'), True, True, 5)
        caixav2.pack_start (caixaCor.CaixaCor('purple'), True, True, 5)

        caixa.pack_start(caixav2, True, True, 5)

        self.add(caixa)
        self.connect ("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    ExemploBoxColor()
    Gtk.paint()