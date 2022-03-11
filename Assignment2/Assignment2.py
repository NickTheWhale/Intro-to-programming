"""
Name:       Nicholas Loehrke

Course:     CS1430, Section 02,  Spring 2022

Assignment: Assignment2

Purpose:    You find yourself as the manager of a small fleet of FedEx delivery trucks, and you wanted to track the
            statistics of the deliveries so that you can help the company to improve the delivery routes.
            You will write a Python program whose purpose is to analyze a set of delivery routes. We will make the
            assumption that each delivery route is associated with a different delivery truck driver. Your program will take
            as input a sequence of delivery routes and then compute, for each delivery route, the following statistics.
            1. The shortest distance traveled between consecutive deliveries.
            2. The longest distance traveled between consecutive deliveries.
            3. The total distance traveled.
            4. The average distance traveled between consecutive deliveries.
            Your program should also keep track of the total distance traveled and the total number of deliveries made in
            the fleet. After all the delivery routes are processed, your program will output the following statistics.
            1. The total number of delivery routes.
            2. The total number of deliveries made in the fleet.
            3. The total distance traveled for all delivery routes in the fleet.
            4. The route number that has the shortest travel distance in the fleet.
            5. The route number that has the longest travel distance in the fleet.

Input:      The input to your program will consist of some unknown number of delivery routes that each correspond to a
            different delivery truck. Since delivery trucks are constantly in and out of the maintenance shop, you do not
            know in advance how many delivery routes will be input to the program. The order of the delivery routes in the
            input matters so that the first route is route #1, the second route is route #2, and so on.

Output:     Your program must output statistics for each delivery route including the following.
            1. The shortest distance traveled between consecutive deliveries.
            2. The longest distance traveled between consecutive deliveries.
            3. The total distance traveled.
            4. The average distance traveled between consecutive deliveries (a float with two digits of precision for the
            decimal).
            After the statistics for each delivery route have been displayed, your program must print the following FedEx-
            level statistics.
            1. The total number of delivery routes.
            2. The total number of deliveries made in the FedEx branch.
            3. The total distance traveled for all delivery routes in the FedEx branch.
            4. The route number that has the shortest travel distance in the fleet.
            5. The route number that has the longest travel distance in the fleet.

"""


def main():
    """
    This program reads in data using input() and displays statistics about the data
    """
    # remove the word pass below. All of your code should be here in main().
    pass

    # variables
    total_dist = 0
    route_count = 0
    total_routes = 0
    total_short_dist = 0
    total_long_dist = 0
    short_route = 0
    long_route = 0
    short_flag = True
    long_flag = True

    num_of_routes_raw = input()
    while num_of_routes_raw != "":
        x_prev = 0
        y_prev = 0
        short_dist = 0
        long_dist = 0
        total_route_dist = 0
        num_of_routes = int(num_of_routes_raw)
        total_routes += num_of_routes
        for i in range(num_of_routes):
            x, y = input().split()
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
            if total_route_dist < total_short_dist:
                short_route = route_count
                total_short_dist = total_route_dist
        if long_flag:
            long_route = route_count
            total_long_dist = total_route_dist
            long_flag = False
        else:
            if total_route_dist > total_long_dist:
                long_route = route_count
                total_long_dist = total_route_dist
        print(f'**Statistics for route #{route_count}**')
        print(f'Shortest distance between deliveries: {short_dist}')
        print(f'Longest distance between deliveries: {long_dist}')
        print(f'Distance traveled: {total_route_dist}')
        print(f'Average distance between deliveries: {avg_distance:.2f}')
        num_of_routes_raw = input()

    print(f'Total number of delivery routes: {route_count}')
    print(f'Total number of deliveries: {total_routes}')
    print(f'Total distance traveled for all routes: {total_dist}')

    print(f'Route #{short_route} has the shortest travel distance: {total_short_dist}')
    print(f'Route #{long_route} has the longest travel distance: {total_long_dist}')

    #Do not remove the code below this line!

if __name__ == '__main__':
    main()
