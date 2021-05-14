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
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from placecollection import PlaceCollection
from place import Place
# from operator import itemgetter # used to sort items from a list

VISITS = {'Visited': 1, 'Unvisited': 2}


class TravelTrackerApp(App):
    """
    Main program
    """
    status_text = StringProperty()  # Initializes status_text
    visited_status_text = StringProperty()
    place_codes = ListProperty()

    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super(TravelTrackerApp, self).__init__(**kwargs)
        self.pc = PlaceCollection()
        self.pc.load_places()
        self.visited_status_text = "Places to visit: {}".format(self.pc.get_number_of_unvisited_places())
        self.input_data = []

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Travel Tracker"
        self.root = Builder.load_file('app.kv')
        self.create_entry_buttons()
        self.place_codes = sorted(VISITS.keys())
        return self.root

    def on_stop(self):
        print('stopped')
        self.pc.save_places()

    def sort_by(self):
        """ handle change of spinner selection, output result to label widget """
        self.pc.sort("visited_status")

    def create_entry_buttons(self):
        """
        Create the entry buttons and add them to the GUI
        :return: None
        """
        for p in self.pc.places:
            # create a button for each place entry
            temp_str = p.__str__() + " (visited)" if p.visited_status else p.__str__()
            temp_button = Button(text=temp_str)
            temp_button.bind(on_release=self.press_entry)
            temp_button.place = p
            temp_button.state = "down" if p.visited_status else "normal"
            # add the button to the "entries_box" using add_widget()
            self.root.ids.entries_box.add_widget(temp_button)



TravelTrackerApp().run()
