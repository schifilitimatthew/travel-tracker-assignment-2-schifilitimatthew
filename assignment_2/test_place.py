"""(Incomplete) Tests for Place class."""
from traveltrackerassignment2schifilitimatthew.assignment_2.place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    print(new_place)

    # Test initialisation works
    print("Test initialisation works:")
    place = Place()
    print(place.name)
    print(place.country)
    print(place.priority)
    print(place.is_visited)


    # Test determine visited places (Boolean)
    print("Test determine visited places:")
    test_visit = False
    result = Place.determine_visited_places_boolean(default_place, test_visit)
    print("determine_visited_places_boolean() - Expected {}. Got {}".format("*", result))

    # Test determine visited places (string)
    print("Test determine visited places:")
    test_visit = "n"
    result = Place.determine_visited_places_string(default_place, test_visit)
    print("determine_visited_places_string() - Expected {}. Got {}".format("*", result))

    # Test determine place is important
    print("Test determine visited places:")
    test_visit = 1
    result = Place.determine_important_place(default_place, test_visit)
    print("determine_important_place() - Expected {}. Got {}".format("True", result))




run_tests()
