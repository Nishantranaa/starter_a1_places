"""
Replace the contents of this module docstring with your own details
Name: Nishant
Date started: 30/03/31
GitHub URL: https://github.com/Nishantranaa/starter_a1_places
"""
from csv import reader
import csv

def main():
    print("Welcome to Travel Tracker version 1.0 - by Nishant_Rana")
    menu()


# def read_file():
#     with open('places.csv', 'r+') as csv_file:
#         csv_reader = reader(csv_file)
#         # Passing the cav_reader object to list() to get a list of lists
#         places = list(csv_reader)
#         # value = places[0][1]
#     counter = 0
#     for total_destination in places:
#         counter += 1
#     print("{} places loaded from places.csv".format())
#     return counter


def menu():
    # with open('places.csv', 'r') as csv_r_file:
    with open('places.csv', 'r') as csv_r_file:
        csv_reader = reader(csv_r_file)
        # Passing the cav_reader object to list() to get a list of lists
        places = list(csv_reader)
        # value = places[0][1]
    counter = 0
    for total_destination in places:
        counter += 1

    print("{} places loaded from places.csv".format(counter))
    # repeated the above read_file method to get the value of the count.

    print("Menu: \n L - List places \n A - Add new place \n M - Mark a place as visited \n Q - Quit")
    letter_input = str(input(">>> ").upper())
    # v - visited, n - unvisited
    if letter_input == "L":
        # print("test") # used the print statement to test the first sequence.
        i = 0
        counter_unvisited = 0
        counter_visited = 0
        while i <= counter - 1:
            for n_or_v in places[i][3]:
                i += 1
                if n_or_v == 'n':
                    counter_unvisited += 1
                    # print(counter_unvisited) tester
                else:
                    counter_visited += 1
                    # print(counter_visited) tester

        counter = 0
        for total_destination in places:
            counter += 1
            print("{} in {} priority {}".format(total_destination[0], total_destination[1], total_destination[2]))
        print("{} places. You still want to visit {} places.".format(counter, counter_unvisited))

    elif letter_input == "A":
        if letter_input == "A":
            name = str(input("Name:"))
            country = str(input("Country: "))
            visited = str("n")
            try:
                while priority <= 0:
                    priority = int(input("Priority: "))
                    if priority > 0:
                        break
                    else:
                        print("Number must be > 0")
                    continue
            except ValueError:
                print("Invalid input; enter a valid number")

            print("{} in {} (priority {}) added to Travel Tracker".format(name, country, priority))
            with open('places.csv', 'a', newline='') as csv_w_file:
             writer = csv.writer(csv_w_file)
             writer.writerow([name, country, priority, visited])

        else:
          print("Input cannot be blank")

    else:
     print("Invalid menu choice")


main()
