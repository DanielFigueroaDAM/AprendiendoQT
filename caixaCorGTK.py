import gi
gi.require_version("GTK","3.0")
from gi.repository import Gtk, Gdk, GObject

class CaixaCor (Gtk.DrawingArea):
    def __init__(self,color):
        super().__init__()
        self.set_size_request(50,50)
        rgba = Gdk.RGBA()
        rgba.parse(color)
        self.color = rgba
        self.connect("draw",self.on_draw)

    def on_draw (self,control,cr):
        cr.set_source_rgba(self.color)
        cr.paint()