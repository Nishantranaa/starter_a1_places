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

    def press_entry(self, instance):
        """
        Handler for pressing entry buttons
        :param instance: the Kivy button instance
        :return: None
        """
        place = instance.place
        place.visited_status = not place.visited_status
        instance.text = place.__str__() + " (visited)" if place.visited_status else place.__str__()

        if place.is_important():
            if place.visited_status:
                self.status_text = "You visited {}. Great travelling!".format(place.name)
                instance.state = "down"
            else:
                self.status_text = "You need to visit {}. Get going!".format(place.name)
                instance.state = "normal"
        else:
            if place.visited_status:
                self.status_text = "You visited {}.".format(place.name)
                instance.state = "down"
            else:
                self.status_text = "You need to visit {}.".format(place.name)
                instance.state = "normal"

        self.visited_status_text = "Places to visit: {}".format(self.pc.get_number_of_unvisited_places())

    def press_clear(self):
        """
        Clear any buttons that have been selected (visually) and reset status text
        :return: None
        """
        self.status_text = ""
        self.visited_status_text = ""
        self.clear_fields()

    def press_add(self, name, country, priority):
        """
        Handler for pressing the add button
        :return: None
        """
        if (not name) or (not country) or (not priority):
            self.status_text = "All fields must be completed"
        else:

            try:
                priority = int(priority)
                if priority < 1:
                    self.status_text = "Priority must be > 0"
                else:
                    # Adding widget
                    p = Place(name=name, country=country, priority=priority, visited_status=False)
                    temp_str = p.__str__() + " (visited)" if p.visited_status else p.__str__()
                    temp_button = Button(text=temp_str)
                    temp_button.bind(on_release=self.press_entry)
                    temp_button.place = p
                    temp_button.state = "down" if p.visited_status else "normal"
                    # add the button to the "entries_box" using add_widget()
                    self.root.ids.entries_box.add_widget(temp_button)
                    self.clear_fields()
                    # Adding to place collection
                    self.pc.add_place(p)
            except:
                self.status_text = "Please enter a valid number"

    def clear_fields(self):
        """
        Clear the text input fields
        """
        self.root.ids.name_input.text = ""
        self.root.ids.country_input.text = ""
        self.root.ids.priority_input.text = ""


TravelTrackerApp().run()
