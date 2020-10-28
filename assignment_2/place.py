"""
Name: Matthew Schifilliti
Date: 11/10/20
Brief Project Description: Create the Place class.
GitHub URL: https://github.com/cp1404-students/travel-tracker-assignment-2-schifilitimatthew
"""

# Create your Place class in this file


class Place:
    """Represent a Place object."""

    def __init__(self, name="", country="", priority=0, is_visited=False):
        """Initialise a place instance.

        name: string, reference name for place
        country: string, reference country for place
        priority: integer, orders the places
        visited_status: if a place has been visited
        """
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        """Return a string representation of a Place object."""
        if self.is_visited is True:
            return "{} in {} priority {}, Visited" .format(self.name, self.country, self.priority)
        else:
            return "{} in {} priority {}, Not Visited".format(self.name, self.country, self.priority)

    def determine_visited_places_boolean(self, data):
        """Determines if a place is visited in boolean form"""
        if data == False:  # determining if visited or not
            return "*"
        else:
            return ""

    def determine_visited_places_string(self, data):
        """Determines if a place is visited in string form"""
        if data == "n":  # determining if visited or not
            return "*"
        else:
            return ""

    def determine_important_place(self, data):
        """Determines if a place is important"""
        if data <= 2:
            return True
        else:
            return False
