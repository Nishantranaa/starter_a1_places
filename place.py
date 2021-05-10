# File place.py

"""This place class will contain methods which can be be used to create reusable data types."""


# Create your Place class in this file


class Place:
    """Represents a place object"""

    def __init__(self, name="", country="", priority=0, visited_status=''):
        self.name = name
        self.country = country
        self.priority = priority
        self.visited_status = visited_status

    def __str__(self):
        return "{},  country={}, priority={}, visited={}".format(self.name, self.country, self.priority,
                                                                 self.visited_status)

    def mark_visited(self):
        """ Marks the place as visited """
        self.visited_status = 'v'
        return
        pass
