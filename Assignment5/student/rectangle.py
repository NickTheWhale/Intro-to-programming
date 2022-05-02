import time

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

    def perimeter(self):
        return (self.__length + self.__width) * 2

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, length):
        self.__length = length





def main():
    previous_time = time.time()
    num_of_rectangles = 5000000
    rect = [Rectangle() for i in range(num_of_rectangles)]
    elapsed_time = time.time() - previous_time
    print(elapsed_time)

    '''for i in range(num_of_rectangles):
        rect[i].print_rectangle()'''


if __name__ == "__main__":
    main()
