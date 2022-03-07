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



def main():
    """
    This is your docstring - replace this with a description of the program.
    :return:
    """
    # remove the word pass below. All of your code should be here in main().
    pass

    # constants

    # x, y = input("Input x and y: ").split()
    '''
    num_of_routes = int(input("Input num of routes: "))
    x_list = [None] * num_of_routes
    y_list = [None] * num_of_routes
    x, y = input("Input x and y: ").split()
    for i in range(num_of_routes):
        print(i)
        x_list[i], y_list[i] = input("Input x and y: ").split()

    print(x_list)
    print(y_list)
    '''
    total_routes_raw = input("Input total number of routes: ")
    while total_routes_raw != "":
        total_routes = int(total_routes_raw)
        route_count = 0
        distance = 0
        total_distance = 0
        while route_count < total_routes:
            x, y = input("Input x and y: ").split()


#Do not remove the code below this line!

if __name__ == '__main__':
    main()
