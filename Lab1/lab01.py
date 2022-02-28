"""
Name:       Nicholas Loehrke

Course:     CS 1430, Section: 2

Assignment: Lab 01

Purpose:    This program reads in an integer temperature in Celsius
            and converts it to Fahrenheit.

Input:      An integer representing temperature in Celsius.

Output:     An integer representing the inputted temperature
            converted to Fahrenheit.
"""

"""
CONSTANTS
"""
_C_TO_F_CONV_NUMERATOR = 9
_C_TO_F_CONV_DENOMINATOR = 5
_C_TO_F_CONV_ADDITION = 32


def main():
    """
    This program reads in a temperature (an integer) in Celsius
    and converts it to Fahrenheit (a float).
    :return: None
    """

    celsius = float(input("Enter an integer temperature in Celsius: "))

    # Add an assignment statement that sets fahrenheit to celsius * 9 / 5 + 32

    tempf = float(celsius * (9 / 5) + 32)

    print(f'A temperature of {celsius} degrees in Celsius is {tempf:0.2f} '
          f'degrees in Fahrenheit.')


if __name__ == "__main__":
    main()
