# File test_place.py

"""(Incomplete) Tests for Place class."""
from place import Place
# is the name of the file
# Place is the class name in that file.

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
    # TODO: Write tests to show this initialisation works

    new_place = Place("Nishant", "Durban", 2, True)

    # TODO: Add more tests, as appropriate, for each method


run_tests()
