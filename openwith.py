import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
import os
import sys

class CustomExecutable(Gtk.Window):
    def __init__(self, toOpen):
        Gtk.Window.__init__(self, title="")
        self.hide()
        dialog = Gtk.FileChooserDialog("Choose executable", self,
                Gtk.FileChooserAction.OPEN,
                (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                 Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            if (os.fork() == 0):
                os.execv(dialog.get_filename(), 
                        [dialog.get_filename()] + toOpen[1:])

        dialog.destroy()
        Gio.g_application_quit()

win = CustomExecutable(sys.argv)
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

