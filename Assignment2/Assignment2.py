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

    total_dist = 0
    route_count = 0
    total_routes = 0
    total_short_dist = 0
    total_long_dist = 0
    short_route = 0
    long_route = 0
    short_flag = True
    long_flag = True

    num_of_routes_raw = input("Num of routes: ")
    while num_of_routes_raw != "":
        x_prev = 0
        y_prev = 0
        short_dist = 0
        long_dist = 0
        total_route_dist = 0
        num_of_routes = int(num_of_routes_raw)
        total_routes += num_of_routes
        for i in range(num_of_routes):
            x, y = input("Input x and y: ").split()
            x = int(x)
            y = int(y)
            route_dist = abs(x_prev - x) + abs(y_prev - y)
            total_route_dist += route_dist
            total_dist += route_dist
            if route_dist > long_dist:
                long_dist = route_dist
            if i > 0:
                if route_dist < short_dist:
                    short_dist = route_dist
            else:
                short_dist = route_dist
            x_prev = x
            y_prev = y
        route_count += 1
        avg_distance = total_route_dist / num_of_routes
        if short_flag:
            short_route = route_count
            total_short_dist = total_route_dist
            short_flag = False
        else:
            if short_dist < total_short_dist:
                short_route = route_count
                total_short_dist = total_route_dist
        if long_flag:
            long_route = route_count
            total_long_dist = total_route_dist
            long_flag = False
        else:
            if long_dist > total_long_dist:
                long_route = route_count
                total_long_dist = total_route_dist

        print(f'**Statistics for route #{route_count}**')
        print(f'Shortest distance between deliveries: {short_dist}')
        print(f'Longest distance between deliveries: {long_dist}')
        print(f'Distance traveled: {total_route_dist}')
        print(f'Average distance between deliveries: {avg_distance:.2f}')
        num_of_routes_raw = input("Num of routes: ")

    print(f'Total number of delivery routes: {route_count}')
    print(f'Total number of deliveries: {total_routes}')
    print(f'Total distance traveled: {total_dist}')

    print(f'Route #{short_route} has the shortest travel distance: {total_short_dist}')
    print(f'Route #{long_route} has the longest travel distance: {total_long_dist}')




#Do not remove the code below this line!

if __name__ == '__main__':
    main()
