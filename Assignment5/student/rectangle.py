class Rectangle:
    """
    author: Nick
    """

    def __init__(self, new_length=1, new_width=1):
        self.__length = new_length
        self.__width = new_width

    def print_rectangle(self):
        print(f'Length is {self.__length}, width is {self.__width}')

    def set_width(self, width):
        self.__width = width

    def set_length(self, length):
        self.__length = length

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

    def area(self):
        return self.__length * self.__width


def main():
    rect = [Rectangle() for i in range(5)]
    for i in range(5):
        rect[i].print_rectangle()


if __name__ == "__main__":
    main()
