"""
Name: Nicholas Loehrke

Course:  CS 1430, section 2

Assignment: Lab 02

Purpose: This program calculates a sale given the unit price,
    quantity, discount, and tax rate.

Input :  This program accepts the following prompted input
    for the three sides of a given triangle:
    quantity - as an int
    unit_price - as a float
    discount_rate - as a float

Output:  This program provides the calculations for the subtotal,
    the discount amount, the discounted total, the sales tax,
    and the total sale.
    subtotal - as a float
    discount_amount - as a float
    subtotal_taxable - as a float
    tax_amount - as a float
    total - as a float
"""

"""
CONSTANTS
"""
_PERCENT = 100.0
_TAX_RATE = 8.50


def main():
    """

    """
    quantity = int(input("Enter number of items sold: "))
    unit_price = float(input("Enter the unit price: "))
    discount_rate = float(input("Enter the discount rate (enter 7% as 7.0): "))

    # DO_02: Complete the input statements for unit_price and discount_rate
    
    # DO_03: Complete the formulas for the calculations, see the lab description
    sub_total = quantity * unit_price
    discount_am = sub_total * discount_rate / _PERCENT
    sub_taxable = sub_total - discount_am
    tax_am = sub_taxable * _TAX_RATE / _PERCENT
    total = sub_taxable + tax_am
    discounted_total = sub_total - discount_am

    # D0_04: Print out the results, see the lab for details on exact output.
    #         print quantity as a whole number.
    #         print the rest of the output with two digits of precision.
    print(f"Quantity sold: {quantity}")
    print(f"Unit Price of items: {unit_price:.2f}")
    print(f"Subtotal: {sub_total:.2f}")
    print(f"Discount: {discount_am:.2f}")
    print(f"Discounted total: {discounted_total:.2f}")
    print(f"Sales tax: {tax_am:.2f}")
    print(f"Total sale: {total:.2f}")


if __name__ == "__main__":
    main()
