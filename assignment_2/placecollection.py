"""
Name: Matthew Schifilliti
Date: 11/10/20
Brief Project Description: Create the Place Collection class.
GitHub URL: https://github.com/cp1404-students/travel-tracker-assignment-2-schifilitimatthew
"""


# Create your PlaceCollection class in this file

from operator import itemgetter
from traveltrackerassignment2schifilitimatthew.assignment_2.place import Place


class PlaceCollection:
    """Represent a PlaceCollection"""
    def __init__(self):
        self.data = []

    def __str__(self):
        return str(self.data)

    def load_places(self, file):
        """reads data from file for use"""
        with open(file, "r") as in_file:
            file = in_file.readlines()
            in_file.close()
            for line in file:
                line = line.strip()  # Removing the \n
                parts = line.split(',')
                parts[2] = int(parts[2])
                self.data.append(parts)
        return self.data

    def save_places(self, file):
        """saves data to file for use"""
        with open(file, 'w') as out_file:
            for places in self.data:
                print("{},{},{},{}".format(*places), file=out_file)
            out_file.close()

    def add_place(self, Place):
        """ads data from input for use"""
        new_place = [Place.name, Place.country, Place.priority, "n"]
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
            self.data.sort(key=itemgetter(3))
        if criteria == "priority":
            for place in self.data:
                place[2] = int(place[2])
            self.data.sort(key=itemgetter(2))
        if criteria == "country":
            self.data.sort(key=itemgetter(1))
        if criteria == "name":
            self.data.sort(key=itemgetter(0))

    def length(self):
        """determines length of data"""
        return len(self.data)