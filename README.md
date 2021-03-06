# OpenWithHack
Allows using any application you like for opening files in Gnome.

In Gtk+-3.11 (upward) opening files with GtkAppChooser does not allow choosing an application from disk anymore.
Gnome people do not consider this a bug, see https://bugzilla.gnome.org/show_bug.cgi?id=650284

Here are two small scripts to circumvent this.

## [openwith.py](/openwith.py)
Starts a file selection dialog and spawns the selected file, forwarding its commandline arguments.

Requires [pygobject](https://pygobject.readthedocs.io/en/latest/) to work. Tested with python-3.5.3 and pygobject-3.22.0.

## [openwith.desktop](/openwith.desktop)
Place (or symlink) this into `~/.local/share/applications/openwith.desktop` or `/usr/share/applications/openwith.desktop` for a local or global installation. It creates an entry in GtkAppChooser, which will then open openwith.py where you select the application to open your file with.

You need to adapt [Exec](/openwith.desktop#L7) according to your needs/file locations! The `%f` is the file name as selected by GtkAppChooser. It is documented [here](https://developer.gnome.org/integration-guide/stable/desktop-files.html.en).

## Contributions
Just open an issue and or pull-request. Especially distribution-specific packages might be nice.

