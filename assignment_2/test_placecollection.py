"""(Incomplete) Tests for PlaceCollection class."""
from traveltrackerassignment2schifilitimatthew.assignment_2.placecollection import PlaceCollection
from traveltrackerassignment2schifilitimatthew.assignment_2.place import Place





def run_tests():
    """Test PlaceCollection class."""

    # Test empty PlaceCollection (defaults)
    print("Test empty PlaceCollection:")
    place_collection = PlaceCollection()
    print(place_collection)
    assert not place_collection.data  # an empty list is considered False

    # Test loading places
    print("Test loading places:")
    place_collection.load_places('places.csv')
    print(place_collection)
    assert place_collection.data  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Place with values
    print("Test adding new place:")
    place_collection.add_place(Place("Smithfield", "Australia", 5, False))
    print(place_collection)

    # # Test sorting places
    # print("Test sorting - priority:")
    # place_collection.sort("priority")
    # print(place_collection)
    #
    # # Test sorting places
    # print("Test sorting - country:")
    # place_collection.sort("country")
    # print(place_collection)
    #
    # # Test sorting places
    # print("Test sorting - visited:")
    # place_collection.sort("visited")
    # print(place_collection)
    #
    # # Test sorting places
    # print("Test sorting - name:")
    # place_collection.sort("name")
    # print(place_collection)

    # Test saving places
    print("Test Saving places: (check manually)")
    place_collection.save_places("places.csv")

    print("Test length of data:")
    result = place_collection.length()
    print("place_collection.length() - Expected {}. Got {}".format("4", result))

run_tests()
