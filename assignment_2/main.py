"""
Name: Matthew Schifilliti
Date: 26/10/20
Brief Project Description: Create the TravelTrackerApp with the use of classes and kivy
GitHub URL: https://github.com/cp1404-students/travel-tracker-assignment-2-schifilitimatthew
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from traveltrackerassignment2schifilitimatthew.assignment_2.placecollection import PlaceCollection
from traveltrackerassignment2schifilitimatthew.assignment_2.place import Place

place_collection = PlaceCollection()
VISITED_COLOUR = 0, 0, 0, 1
NOT_VISITED_COLOUR = 0, 0, 0, 0
CITY_INDEX = 0
COUNTRY_INDEX = 1
PRIORITY_INDEX = 2
IS_VISITED_INDEX = 3
SPINNER = {'Visited': "Visited", 'Priority': "Priority", 'Country': "Country", 'Name': "Name"}

class TravelTrackerApp(App):
    """Run the TravelTrackerApp"""
    current_option = StringProperty()
    spinner_options = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        displayed_places = []
        self.displayed_places = displayed_places

    def build(self):
        """bulid for TravelTrackerApp"""
        self.title = "TravelTracker"
        self.root = Builder.load_file('app.kv')
        self.display_places()
        self.spinner_options = sorted(SPINNER.keys())
        self.current_option = self.spinner_options[0]
        return self.root

    def display_places(self):
        for place in place_collection.data:
            if place not in self.displayed_places:
                if place[3] == "v":
                    temp_button = Button(background_color=VISITED_COLOUR,
                                         text=str("{} in {}, priority {} (visited)".format(place[CITY_INDEX],
                                                                                           place[COUNTRY_INDEX],
                                                                                           place[PRIORITY_INDEX])),
                                         id=str(place))
                if place[3] == "n":
                    temp_button = Button(background_color=NOT_VISITED_COLOUR,
                                         text=str("{} in {}, priority {}".format(place[CITY_INDEX],
                                                                                 place[COUNTRY_INDEX],
                                                                                 place[PRIORITY_INDEX])),
                                         id=str(place))
                temp_button.bind(on_release=self.press_entry)
                temp_button.place = place
                self.root.ids.places.addwidget(temp_button)
                self.displayed_places.append(place)
                self.root.ids.places_to_visit.text = "Places_to_visit: {}".format(len(place_collection.
                                                                                      get_unvisited_places()))
        return self.displayed_places

    def press_entry(self, instance):
        """release of button"""
        place = instance.place
        if place[IS_VISITED_INDEX] == "n":
            place[IS_VISITED_INDEX] = "v"
            if place[PRIORITY_INDEX] <= 2:
                self.root.ids.is_visted.text = "You visited {}. Great travelling!".format(place[CITY_INDEX])
            else:
                self.root.ids.is_visted.text = "You visited {}. ".format(place[CITY_INDEX])
        else:
            place[IS_VISITED_INDEX] = "n"
            if place[PRIORITY_INDEX] <= 2:
                self.root.ids.is_visted.text = "You need to visit {}. Get Going!".format(place[CITY_INDEX])
            else:
                self.root.ids.is_visted.text = "You need to visit {}. ".format(place[CITY_INDEX])
        if place[3] == "v":
            instance.text = str("{} in {}, priority, {} (visited)".format(place[CITY_INDEX], place[COUNTRY_INDEX],
                                                                          place[PRIORITY_INDEX]))
            instance.background.color = VISITED_COLOUR
        if place[3] == "n":
            instance.text = str("{} in {}, priority, {})".format(place[CITY_INDEX], place[COUNTRY_INDEX],
                                                                 place[PRIORITY_INDEX]))
            instance.background.color = NOT_VISITED_COLOUR
        self.root.ids.places_to_visit.text = ("Places to visit {}".format(len(place_collection.get_unvisited_places)))

    def get_name(self):
        """get name from kivy app"""
        name = str(self.root.ids.input_name.text)
        return name

    def get_country(self):
        """get name from kivy app"""
        country = str(self.root.ids.input_country.text)
        return country

    def get_priority(self):
        """get name from kivy app"""
        priority = self.root.ids.input_priority.text
        return priority

    def add_place(self):
        """add place action"""
        if not self.get_name() or not self.get_country() or not self.get_priority():
            self.root.ids.is_visted.text = "All fields must be completed"
            return place_collection
        try:
            priority = self.get_priority()
            priority = int(priority)
        except ValueError:
            self.root.ids.is_visted.text = "please enter a vaild number"
            return place_collection
        if priority > 0:
            self.root.ids.is_visted.text = "Priority must be > 0"
            return place_collection
        else:
            place_collection.add_place(Place(self.get_name(), self.get_country(), priority, "n"))
            self.display_places()
            self.root.ids.input_name.text = ""
            self.root.ids.input_country.text = ""
            self.root.ids.input_priority.text = ""
        return place_collection

    def clear(self):
        """clear action"""
        self.root.ids.input_name.text = ""
        self.root.ids.input_country.text = ""
        self.root.ids.input_priority.text = ""
        self.root.ids.is_visted.text = ""

    def rest_output(self):
        """rest place button"""
        self.root.ids.places.clear_widgets()
        return place_collection

    def sort_option(self, option):
        """ change of sorting option from spinner"""

    def change_sort(self, current_option):
        """Changes which sorting the spinner will be set to."""
        self.root.ids.output_label.text = SPINNER[current_option]
        print("changed to", current_option)


if __name__ == '__main__':
    TravelTrackerApp().run()
