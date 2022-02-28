def main():
    """
    calculate if input is multiple of 5
    :return:
    """

    num = int(input("Input an integer: "))
    if not(num % 5):
        print("HiFive")
    if not(num % 2):
        print("HiEven")


if __name__ == "__main__":
    main()
