# File placecollection.py


from place import Place
from operator import attrgetter


# Create your PlaceCollection class in this file


class PlaceCollection:
    """..."""
    """This class will contain a single attribute: list of place objects, and following methods."""

    def __init__(self):
        self.places = []  # loading csv content into this place_objects list.

    def load_places(self):
        with open('places.csv', 'r') as csv_r_file:
            csv_reader = reader(csv_r_file)
            # Passing the csv_reader object to list() to get a list of lists
            places_list = list(csv_reader)
        for p in places_list:
            self.places.append(Place(name=p[0], country=p[1], priority=int(p[2]), visited_status=p[3]))

    def save_places(self):
        places_list = self.to_place_list()
        with open('places.csv', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(places_list)

    def to_place_list(self):
        place_list = []
        for i in self.places:
            place_list.append([i.name, i.country, str(i.priority), i.visited_status])
        return place_list

    def add_place(self, place):
        self.places.append(place)

    def get_number_of_unvisited_places(self):
        count = 0
        for i in self.places:
            if i.visited_status == 'n':
                count += 1
        return count

    def sort(self, key):
        """"Sort places list by key passed in then by priority"""
        self.places = sorted(self.places, key=attrgetter(key, 'priority'))
        return