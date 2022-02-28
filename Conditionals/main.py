def main():
    """
    Calculate the average of three numbers
    :return:
    """
    pass

    num1 = float(input("Enter 1st number:  "))
    num2 = float(input("Enter 2nd number:  "))
    num3 = float(input("Enter 3rd number:  "))

    summation = num1 + num2 + num3

    if summation == 0:
        print("Average is zero")
    else:
        ave = summation/3.0
        print(f"Average is {ave:.2f}")


if __name__ == "__main__":
    main()
