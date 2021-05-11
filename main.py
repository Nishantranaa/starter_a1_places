# File main.py

"""
Name: Nishant
Date: 24/04/2021
Brief Project Description: A travel tracker program with a graphical user interface using kivy.
To create classes which have reusable methods to develop the program in a modular manner which is
easy to read and understand.
GitHub URL: https://github.com/Nishantranaa/starter_a1_places
"""
# Create your main program in this file, using the TravelTrackerApp class
# kivy.app denotes a python package. A package is a collection of related modules.
# Both App and Widget are modules within the app package.

from kivy.app import App
from kivy.app import Builder


class TravelTrackerApp(App):
    """The TravelTrackerApp class overrides App.build() to return an empty Widget instance
self.root comes from the App class, it refers to the main widget of our
Kivy program. All other widgets get added to this main root widget"""

    def build(self):
        self.title = "Hello world!"  # The title of the main window is set using self.title
        self.root = Builder.load_file('app.kv')  # Builder.load_file() is used to read Kv code from a Kv file
        # load_file() returns the GUI layout declared in the Kv file
        return self.root


""""Every class/method has a variable called self, which refers to the current object 
(also known as an instance).When you want to create or access a variable that your Kivy 
app should know about in multiple functions, use self.variable
"""

if __name__ == '__main__':
    TravelTrackerApp().run()

    """"We call App.run() on this (anonymous) instance
    That’s how Kivy knows to make the GUI program visible
    Kivy uses the widget returned by build()
    """
