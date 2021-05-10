# File test_place.py

"""(Incomplete) Tests for Place class."""
from place import Place
# is the name of the file
# Place is the class name in that file.

def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("\nTest empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited
    # TODO: Write tests to show this initialisation works
    print("Success!")

    # Test initial-value place
    print("\nTest initial-value place:")

    new_place = Place("Malagar", "Spain", 1, True)
    print(new_place)
    assert new_place.name == "Malagar"
    assert new_place.country == "Spain"
    assert new_place.priority == 1
    assert new_place.is_visited
    print("Success!")

    new_place = Place("Durban", "South Africa", 5, False)
    print(new_place)
    assert new_place.name == "Durban"
    assert new_place.country == "South Africa"
    assert new_place.priority == 5
    assert not new_place.is_visited
    print("Success!")

    # Testing Methods
    print("\nTest class methods")

    print("\nTesting is_visited()")
    place1 = Place("Zimbabwe", "Harare", 8, False)
    print(place1)
    print(place1.is_visited)
    assert not place1.is_visited
    # Calling mark_visited method
    place1.mark_visited()
    print(place1.is_visited)
    assert place1.is_visited

    place2 = Place("Zimbabwe", "Harare", 8, True)
    print(place2)
    print(place2.is_visited)
    assert place2.is_visited
    # Calling unmark_visited method
    place2.mark_unvisited()
    print(place2.is_visited)
    assert not place2.is_visited

    print("\nTesting is_important()")
    place3 = Place("Kenya", "Nairobi", 5, True)
    print(place3)
    assert not place3.is_important()
    place4 = Place("Kenya", "Nairobi", 1, True)
    print(place4)
    assert place4.is_important()

    place5 = Place("Penang", "Malaysia", 3, False)
    print(place5)
    place5.mark_visited()
    assert not place5.is_important()


run_tests()
