"""
Name: Matthew Schifilliti
Date: 22/10/20
Brief Project Description: Use other classes code in previous TravelTracker.
GitHub URL: https://github.com/cp1404-students/travel-tracker-assignment-2-schifilitimatthew
"""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from traveltrackerassignment2schifilitimatthew.assignment_2.placecollection import PlaceCollection
from traveltrackerassignment2schifilitimatthew.assignment_2.place import Place

menu = "Menu:\nL - List of Places\nA - Add new place\nM - Mark a place as visited\nQ - Quit"
FILENAME = "places.csv"

place_collection = PlaceCollection()
default_place = Place()


def main():
    print("Travel Tracker 2.0 - by Matthew Schifilliti")
    data = place_collection.load_places(FILENAME)
    lines = place_collection.length()
    print("{} places is loaded from {}".format(lines, FILENAME))
    print(menu)
    choice = get_valid_choice(">>> ", "Invalid menu choice")
    while choice != "Q":
        if choice == "L":
            display_list(data)
            print(menu)
        if choice == "A":
            add_to_list(data)
            print(menu)
        if choice == "M":
            mark_place(data)
            print(menu)
        choice = get_valid_choice(">>> ", "Invalid menu choice")
    place_collection.save_places(FILENAME)
    print("Have a nice day :)")



def get_valid_choice(prompt, invalid_prompt):
    """get a valid response"""
    choice = input(prompt).upper()
    while choice != "L" and choice != "A" and choice != "M" and choice != "Q":
        print(invalid_prompt)
        print(menu)
        choice = input(prompt).upper()
    return choice


def display_list(data):
    """display the list of places"""
    from operator import itemgetter
    place_count = 0
    not_visited_count = 0
    for places in data:
        places[2] = int(places[2])  # change priority values to int so can sorted correctly
    place_collection.sort('priority')  # sorting the list by priority
    place_collection.sort('visited')  # sorting the list by visited (goes first)
    for places in data:
        places[2] = str(places[2])  # change priority values to string so can determine max length
    column_length_0 = max((len(places[0]) for places in data))  # determine max character of each section
    column_length_1 = max((len(places[1]) for places in data))
    column_length_2 = max((len(places[2]) for places in data))
    for places in data:
        place_count += 1    # counting overall places
        if places[3] == "n":    # determining if visited or not
            if_visited = "*"
            not_visited_count += 1
        else:
            if_visited = ""
        print("{:1}{}. {:{}} in {:{}} priority {:>{}}".format(if_visited, place_count, places[0], column_length_0,
                                                              places[1], column_length_1, places[2], column_length_2))
    if not_visited_count > 0:
        print("{} places. You still want to visit {} places".format(place_count, not_visited_count))
    else:
        print("{} places. No places left to visit. Why not add a new place?".format(place_count))


def add_to_list(data):
    """Add new place to list"""
    new_place = []
    name = get_valid_place("Name: ", "Input can't be blank").title()    # collecting information
    country = get_valid_place("Country: ", "Input can't be blank").title()
    priority = get_valid_priority("Priority: ")
    new_place.append(name)  # adding information to list in title format
    new_place.append(country)
    new_place.append(priority)
    place_collection.add_place(Place(name, country, priority))
    print("{} in {} (priority {}) added to Travel Tracker".format(name, country, priority))
    return data


def get_valid_place(prompt, invalid_prompt):
    """get a valid response"""
    choice = input(prompt).upper()
    while choice == "":
        print(invalid_prompt)
        choice = input(prompt).upper()
    return choice


def get_valid_priority(prompt):
    """get a valid response"""
    is_valid_input = False
    while not is_valid_input:
        try:
            choice = int(input(prompt))
            if choice < 0:
                print("Number must be > 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return choice


def mark_place(data):
    """Mark place as visited"""
    not_visted_places = 0
    place_count = 0
    for places in data:  # assist with error checking
        if places[3] == 'n':
            not_visted_places += 1
        place_count += 1
    if not_visted_places == 0:
        print("No unvisited places")
    else:
        display_list(data)
        print("Enter the number of a place to mark as visited")
        place_to_mark = get_valid_mark(">>> ", place_count)  # collecting information
        if data[place_to_mark - 1][3] == "v":   # determine if already visited
            print("That place is already visited")
        else:
            data[place_to_mark - 1][3] = "v"
            print("{} in {} visited!".format(data[place_to_mark - 1][0], data[place_to_mark - 1][1]))



def get_valid_mark(prompt, maximum):
    """get a valid response"""
    is_valid_input = False
    while not is_valid_input:
        try:
            choice = int(input(prompt))
            if choice < 0:
                print("Number must be > 0")
            elif choice > maximum:
                print("Invalid place number")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return choice


main()
