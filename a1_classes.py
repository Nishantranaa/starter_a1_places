"""
Replace the contents of this module docstring with your own details
Name: Nishant
Date started: 30/03/31
GitHub URL: https://github.com/Nishantranaa/starter_a1_places
"""
from csv import reader
import csv
import pdb
import pandas as pd  # importing the pandas library to update a single column value in this csv file.


def main():
    print("Welcome to Travel Tracker version 1.0 - by Nishant_Rana")
    menu()


def print_info(places):
    counter = 0
    counter_visited = 0
    counter_unvisited = 0
    for index, total_destination in enumerate(places):
        counter += 1
        if total_destination[3] == 'n':
            # print("test1")
            counter_unvisited += 1
            print("* {} {} in {} priority {}".format(index + 1, total_destination[0], total_destination[1],
                                                     total_destination[2]))
        else:
            counter_visited += 1
            # print("test")
            print("  {} {} in {} priority {}".format(index + 1, total_destination[0], total_destination[1],
                                                     total_destination[2]))
    return counter, counter_unvisited, counter_visited


def menu():
    # with open('places.csv', 'r') as csv_r_file:
    with open('places.csv', 'r') as csv_r_file:
        csv_reader = reader(csv_r_file)
        # Passing the csv_reader object to list() to get a list of lists
        places = list(csv_reader)
        places.sort(key=lambda places: int(places[2]))  # sorted the list in an ascending order from smallest to largest
        # number.
        counter = 0  # the sort function result would be affected if the row numeric
        # digit does not have a space
        # prefixed.
    for total_destination in places:
        counter += 1

    print("{} places loaded from places.csv".format(counter))
    # repeated the above read_file method to get the value of the count.
    menu_loop = "loop"
    while menu_loop == "loop":
        print("Menu: \n L - List places \n A - Add new place \n M - Mark a place as visited \n Q - Quit")
        letter_input = str(input(">>> ").upper())
        # v - visited, n - unvisited
        if letter_input == "L":  # // L: this selection would list all the countries in the list and mark those which
            # have been visited.
            # print("test") # used the print statement to test the first sequence.

            counter, counter_unvisited, counter_visited = print_info(places)

            if counter_unvisited == 0:
                print("{} place(s) in total . No places left to visit. Why not add a new place?".format(counter,
                                                                                                        counter_visited))
                # print(total_destinations) # prints entire file as one list
            else:
                print("{} total place(s). You still want to visit {} place(s).".format(counter, counter_unvisited))
            continue

        elif letter_input == "A":  # // The A selection will display inputs asking the user to enter the places they
            # would like to visit this will be appended to the file as a new row. Checking for user input until valid
            while True:
                name = str(input("Name: "))
                if name != "":
                    break
                else:
                    print("Input cannot be blank")
                    continue

            # Checking for user input until valid
            while True:
                country = str(input("Country: "))
                if country != "":
                    break
                else:
                    print("Input cannot be blank")
                    continue

            # Checking for user input until valid
            while True:
                try:
                    priority = int(input("Priority: "))
                    if priority > 0:
                        break
                    else:
                        print("Number must be > 0")
                        continue
                except ValueError:
                    print("Invalid input; enter a valid number")
                    continue

            visited = str("n")

            print("{} in {} (priority {}) added to Travel Tracker".format(name, country, priority))
            with open('places.csv', 'a', newline='') as csv_w_file:
                writer = csv.writer(csv_w_file)
                writer.writerow([name, country, priority, visited])
                continue

        elif letter_input == "M":  # // The M selection would mark countries which have not been visited to be indicated visited and appended to the places.csv.

            counter, counter_visited, counter_unvisited = print_info(places)

            if counter_unvisited == 0:
                print("No unvisited places")

            else:
                print("{} places in total. You still want to visit {} place(s).".format(counter, counter_visited))

            continue
            place_number = 0
            loop = 'start'
            while loop == 'start':
                try:
                    print("Places prefixed with an '*' have not yet been visited.")
                    place_number = int(
                        input("Enter the number of a place with an asterisk to be marked as visited. \n >>> "))

                except ValueError:
                    print("Invalid input; enter a valid number")
                    continue
                except UnboundLocalError:
                    print("Invalid place number")
                    continue

                if place_number < 0:
                    print("Number must be > 0")
                    continue

                elif place_number > counter:
                    print("Invalid place number")
                    continue

                else:
                    break

            place_number -= 1
            tem_file = []
            if places[place_number][3] == 'n':
                places[place_number][3] = 'v'  # modified the file
                tem_file = places[place_number]
                places.remove(places[place_number])

                with open('places.csv', 'w', newline='') as writeFile:
                    writer = csv.writer(writeFile)
                    writer.writerows(places)  # places[] is written back after removing that row.

                # print(tem_file) # print tester
                print("{} in {} marked as visited!".format(tem_file[0], tem_file[1]))
                # CAN TRY CATCH THE IndexError: if index is out of range. - will work on this in future.
                with open("places.csv", "a", newline='') as write:

                    a = csv.writer(write)
                    a.writerow(tem_file)
            else:
                print("That place is already visited")
                continue
            # overwrite old file

        elif letter_input == "Q":  # // This Q selection will print the total number of rows in the file.
            # // Using with is an context manager, this context manager I
            # don't need to close the file - it will close it for me.
            counter = 0
            for total_destination in places:
                counter += 1
            menu_loop = "stop_loop"

        else:
            print("Invalid menu choice")

    print("{} places saved to places.csv".format(counter))
    print("Have a nice day :)")


main()
