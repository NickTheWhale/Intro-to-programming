"""
Name:           <Fill in your name>
Course:         CS1430, Section <Insert section here>,  Spring 2022
Assignment:     Lab 06
Purpose:        Simple functions and string manipulation.
Description:    In this lab you will create a program that will map a telephone
                number to a letter, and a letter to a number.

                Prompt the user to enter a phone number as a string.
                The input number may contain letters, and it may not.
                The program translates a letter (upper- or lowercase) to a digit
                and leaves all other characters intact. It prints the result.
                You may need to use the string functions .upper(), .strip(),
                and .isalpha().

Input:          A phone number as digits or numbers. Number may have dashes.
Output:         A phone number as digits. If the number had dashes in the input,
                the dashes are printed.
"""
#########################
# IMPORTS
#########################


#########################
# CONSTANTS
#########################



def main():
    """
    Program will map a telephone number to a letter on the telephone keypad.
    If the character is not a letter, it prints it.
    :return:
    """
    # Read in the string with the prompt "Enter a string: "
    # assign to variable number.
    number = input("Enter a string: ")

    # Use .strip() to remove the whitespace, assign to number.
    number = number.strip()

    # Use .upper() to make the letters uppercase, assign to number.
    number = number.upper()

    # loop through the string, reading one character at a time
    count = 0
    while count < len(number):
        # Check if the character is alphabetic.
        if number[count].isalpha():
            # if so, call get_number and then print the number.
            print(getNumber(number[count]), end='')
        # else just print the number
        else:
            print(number[count], end='')
        count += 1

    # Check if the character is alphabetic.
    # if so, call get_number and then print the number.


    # else just print the number


def getNumber(uppercase_letter):
    """
    The getNumber function takes the parameter uppercase_letter and translates
    it to it's corresponding phone number, returning that number.
    :param uppercase_letter: a letter to convert to a number
    :type: string
    :return: the mapped number as an integer
    :rtype: integer
    """
    number = 0
    # check the uppercase_letter to see which letter it is.
    if uppercase_letter in ('A B C'):
        number = 2
    elif uppercase_letter in ('D E F'):
        number = 3
    elif uppercase_letter in ('G H I'):
        number = 4
    elif uppercase_letter in ('J K L'):
        number = 5
    elif uppercase_letter in ('M N O'):
        number = 6
    elif uppercase_letter in ('P Q R S'):
        number = 7
    elif uppercase_letter in ('T U V'):
        number = 8
    elif uppercase_letter in ('W X Y Z'):
        number = 9

    # return the number associated with the letter.
    return number
   


main()
