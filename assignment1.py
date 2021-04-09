"""
Replace the contents of this module docstring with your own details
Name: Nishant
Date started: 30/03/31
GitHub URL: https://github.com/Nishantranaa/starter_a1_places
"""
from csv import reader
import csv
import pandas as pd # importing the pandas library to update a single column value in this csv file.




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
        # Passing the csv_reader object to list() to get a list of lists
        places = list(csv_reader)
        places.sort(key=lambda places: places[2])  # sorted the list in an ascending order from smallest to largest number.
        counter = 0                                # the sort fuction result would be affected if the row numeric digit does not have a space
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
        if letter_input == "L":
            # print("test") # used the print statement to test the first sequence.
            i = 0
            counter_unvisited = 0
            counter_visited = 0
            #while i <= counter - 1:
            for n_or_v in places[i][3]:
                    i += 1
                    if n_or_v == 'n':
                        counter_unvisited += 1
                        # print(counter_unvisited) tester
                    else:
                        counter_visited += 1
                        # print(counter_visited) tester

            counter = 0
            counter_unvisited = 0
            for index, total_destination in enumerate(places):
                # to sort list of list by given index
                # using sort() + lambda
                # sort by third index

                counter += 1
                if total_destination[3] == 'n':
                    # print("test1")
                    counter_unvisited += 1
                    print("* {} {} in {} priority {}".format(index + 1, total_destination[0], total_destination[1],
                                                             total_destination[2]))

                else:

                    # counter_visited += 1
                    # print("test")
                    print("  {} {} in {} priority {}".format(index + 1, total_destination[0], total_destination[1],
                                                             total_destination[2]))
            print("{} places. You still want to visit {} places.".format(counter, counter_unvisited))
            continue

        elif letter_input == "A":
            if letter_input == "A":
                name = str(input("Name:"))
                country = str(input("Country: "))
                visited = str("n")

                try:
                    priority = int(input("Priority: "))
                except ValueError:
                    print("Invalid input; enter a valid number")
                while priority <= 0:
                    if priority > 0:
                        break
                    else:
                        print("Number must be > 0")
                        continue

                print("{} in {} (priority {}) added to Travel Tracker".format(name, country, priority))
                with open('places.csv', 'a', newline='') as csv_w_file:
                    writer = csv.writer(csv_w_file)
                    writer.writerow([name, country, priority, visited])

            else:
                print("Input cannot be blank")
                continue

        elif letter_input == "M":
            counter = 0
            counter_unvisited = 0
            total_destinations = []

            for index, total_destination in enumerate(places):
                counter += 1
                total_destinations += total_destination
                if total_destination[3] == 'n':
                    # print("test1")
                    counter_unvisited += 1
                    print("* {} {} in {} priority {}".format(index + 1, total_destination[0], total_destination[1],
                                                             total_destination[2]))
                else:

                  # counter_visited += 1
                  # print("test")
                  print("  {} {} in {} priority {}".format(index + 1, total_destination[0], total_destination[1],
                                                         total_destination[2]))

            print("{} places. You still want to visit {} places.".format(counter, counter_unvisited))
            # print(total_destinations) # prints entire file as one list


            try:
                print("Places prefixed with an '*' have not yet been visited.")
                place_number = int(
                    input("Enter the number of a place with an asterisk to be marked as visited. \n >>> "))
                place_number -= 1
            except ValueError:
                print("Number must be > 0")

            tem_file = []

            if places[place_number][3] == 'n':
                places[place_number][3] = 'v' # modified the file
                tem_file = places[place_number]
                places.remove(places[place_number])



                with open('places.csv', 'w', newline= '') as writeFile:

                    writer = csv.writer(writeFile)

                    writer.writerows(places) # places[] is written back after removing that row.

                # print(tem_file) # print tester
                print("{} in {} visited!".format(tem_file[0], tem_file[1]))
                # CAN TRY CATCH THE IndexError: if index is out of range.
                with open("places.csv", "a", newline = '') as f:

                        # Use CSV Index to remove a column from CSV
                        # r[3] = r['year']

                    a = csv.writer(f)
                    a.writerow(tem_file)






            else:
                print("That place is already visited")
            continue
             # overwrite old file

        else:
            print("Invalid menu choice")



main()
