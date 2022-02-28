"""
# DO_01: Fill in your name and section number below.
Name:       <Insert name here>

Course:     CS1430, Section <Insert section here>,  Spring 2022

Assignment: Lab 4

Purpose:    Poker Chip cash out program for Lab 4.
            This program processes the output of a poker
            chip sorter to determine the number of each chip
            type (only gold, silver, red, and blue) and the
            total dollars for all chips.

Input:      The input for this program are symbols that
            represent the type of each poker chip.  The variable
            is <chip> of type char and the symbols include:
                'G'   for golden chip worth $1000
                'S'   for silver chip worth $100
                'R'   for red chip worth $50
                'B'   for blue chip worth $10
            The program stops reading coins when an 'X' is read.
            You do not need to test for other coins.

Output:     The output for this program includes the labeled 
            counts for each of the chip types, and the total value
            of the cash out.  The output for the input:
                G
                G
                S
                S
                R
                B
                B
                X
            would be:
                Golden Chip = 2
                Silver Chip = 2
                Red chip    = 1
                Blue chip   = 2
                Cash out    = $2270

"""

"""
GLOBAL CONSTANTS
"""
_GOLD = 'G'    # Gold chip indicator
_SILVER = 'S'    # Silver chip indicators
_RED = 'R'    # Red chip indicators
_BLUE = 'B'    # Blue chip indicator
_EXIT = 'X'    # Exit flag, Sentinel

_VALUE_OF_GOLD_CHIP = 1000
_VALUE_OF_SILVER_CHIP = 100

# DO_02: Define two integers constants
#     _VALUE_OF_RED_CHIP for fifty
#     _VALUE_OF_BLUE_CHIP for ten


_OUTPUT_MESSAGE_GOLDEN_CHIPS = "Golden chips = {:d}"
_OUTPUT_MESSAGE_SILVER_CHIPS = "Silver chips = {:d}"
_OUTPUT_MESSAGE_RED_CHIPS = "Red chips = {:d}"

# DO_03: Write the output string for the blue chip count. {d} is for an int.


_OUTPUT_MESSAGE_CASH_OUT = "Cash out = $ {:d}"

def main():
    """
    Poker Chip cash out program for Lab 4. This program processes the output
    of a poker chip sorter to determine the number of each chip type
    (only gold, silver, red, and blue) and the total dollars for all chips.
    :return: None
    """

    # ----coin counters------
    gold_chips = 0
    silver_chips = 0
    red_chips = 0
    blue_chips = 0

    #------------------------------------------
    #  Sort chips until we get an "X" to exit 
    #------------------------------------------

    chip = input() # Read in the first chip

    # DO_04: Fill in the condition in while-loop to test when to exit the loop.
    while _____________________:
        if chip == _GOLD:
            gold_chips += 1
        elif chip == _SILVER:
            silver_chips += 1
        elif chip == _RED:
            red_chips += 1
        else: # it is blue
            # DO_05: Count here the chip type that has not been counted so far.


        # DO_06: Read the next chip from the input.


    # end while sorting and counting chips

    #----------------------------
    # Output the chip counts
    #----------------------------

    print()

    print(_OUTPUT_MESSAGE_GOLDEN_CHIPS.format(gold_chips))
    print(_OUTPUT_MESSAGE_SILVER_CHIPS.format(silver_chips))
    print(_OUTPUT_MESSAGE_RED_CHIPS.format(red_chips))
    # DO_07: Print the blue chip count.


    # DO_08: Calculate and print the cash-out amount.




"""
Do not remove the code below this line!
"""

if __name__ == '__main__':
    main()
