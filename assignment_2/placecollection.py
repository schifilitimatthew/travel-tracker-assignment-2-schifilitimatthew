"""..."""


# Create your PlaceCollection class in this file

from operator import attrgetter
from traveltrackerassignment2schifilitimatthew.assignment_2.place import Place


class PlaceCollection:
    """Represent a PlaceCollection"""
    def __init__(self):
        self.data = []

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return "Place[{},{},{},{}]".format(*self.data)

    def load_places(self, file):
        """reads data from file for use"""
        with open(file, "r") as in_file:
            file = in_file.readlines()
            in_file.close()
            for line in file:
                line = line.strip()  # Removing the \n
                parts = line.split(',')
                reflection = parts[3] == "n"  # change n or v into Boolean
                places = Place(parts[0], parts[1], int(parts[2]), reflection)
                self.data.append(places)
        return self.data

    def save_places(self, file):
        """saves data to file for use"""
        with open(file, 'w') as out_file:
            for places in self.data:
                print("{},{},{},{}".format(self.data[1], self.data[2], self.data[3], self.data[4]), file=out_file)
            out_file.close()

    def add_place(self, Place):
        """ads data from input for use"""
        new_place = Place[self.data[1], self.data[2], self.data[3], self.data[4]]
        self.data.append(new_place)

    def get_unvisited_places(self):
        """collects the unvisited places"""
        place_unvisited = []
        for place in self.data:
            if place[3] == "n":
                place_unvisited.append(place)
        return place_unvisited

    def sort(self, criteria):
        """sorts data based on criteria"""
        if criteria == "visited":
            self.data.sort(key=attrgetter("is_visited"))
        if criteria == "priority":
            self.data.sort(key=attrgetter("priority"))
        if criteria == "country":
            self.data.sort(key=attrgetter("country"))
        if criteria == "name":
            self.data.sort(key=attrgetter("name"))

    def length(self):
        """determines length of data"""
        return len(self.data)
