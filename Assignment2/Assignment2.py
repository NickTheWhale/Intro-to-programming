"""
Name:       Nicholas Loehrke

Course:     CS1430, Section 02,  Spring 2022

Assignment: Assignment2

Purpose:

Input:      

Output:     

"""

##################################
#CONSTANTS
##################################

import math

def main():
    """
    This is your docstring - replace this with a description of the program.
    :return:
    """
    # remove the word pass below. All of your code should be here in main().
    pass

    # constants

    # x, y = input("Input x and y: ").split()

    x_total = 0
    y_total = 0
    x_prev = 0
    y_prev = 0
    prev_route_dist = 0
    short_dist = 0
    long_dist = 0
    ave_distance = 0
    route_dist = 0
    total_dist = 0

    num_of_routes_raw = input("Num of routes: ")
    while num_of_routes_raw != "":
        num_of_routes = int(num_of_routes_raw)
        for i in range(num_of_routes):
            x, y = input("Input x and y: ").split()
            x = int(x)
            y = int(y)
            x_total += x
            y_total += y
            route_dist = math.sqrt((x*x)+(y*y))
            total_dist += route_dist
            if route_dist > prev_route_dist:
                long_dist = route_dist
            if i > 0:
                if route_dist < prev_route_dist:
                    short_dist = route_dist
            else:


            prev_route_dist = route_dist
            print("route distance: ", route_dist)
        num_of_routes_raw = input("Num of routes: ")

    print("shortest distance: ", short_dist)
    print("longest distance: ", long_dist)




#Do not remove the code below this line!

if __name__ == '__main__':
    main()
