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
    assert new_place.name == "South Africa"
    assert new_place.country == "Durban"
    assert new_place.priority == 5
    assert not new_place.is_visited
    print("Success!")


run_tests()
