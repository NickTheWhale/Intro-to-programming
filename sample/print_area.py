def sort(number1, number2):
    if number1 > number2:
        temp = number1
        number1 = number2
        number2 = temp
    return number1, number2


def printArea(width = 1, height = 2):
    area = width * height
    print("width:", width, "\theight:", height, "\tarea:", area)

def main():
    printArea() # Default arguments width = 1 and height = 2
    printArea(4, 2.5) # Positional arguments width = 4 and height = 2.5
    printArea(height = 5, width = 3) # Keyword arguments width
    printArea(width = 1.2) # Default height = 2
    printArea(height = 6.2) # Default width = 1

    n1, n2 = sort(3, 2)
    print("n1 is", n1)
    print("n2 is", n2)

if __name__ == "__main__":
    main()