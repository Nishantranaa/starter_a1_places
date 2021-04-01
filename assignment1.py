"""
Replace the contents of this module docstring with your own details
Name: Nishant
Date started: 30/03/31
GitHub URL: https://github.com/Nishantranaa/starter_a1_places
"""


def main():
    print("Welcome to Travel Tracker version 1.0 - by Nishant_Rana")
    file()

# if __name__ == '__main__':


def file():
    counter = 0
    destinations = open("places.csv", "r+")
    for places in destinations:
        counter += 1
    print("{} places loaded from places.csv".format(counter))
    destinations.close()

def menu():
    print()


main()
