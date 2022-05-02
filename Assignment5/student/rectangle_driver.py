import time
from rectangle import Rectangle
from rectangle_list import Rectangle_list


def main():

    rect_list = Rectangle_list()
    rect = Rectangle(2, 5)
    rect_list.add_rectangle(rect)
    rect1 = Rectangle(3, 4)
    rect_list.add_rectangle(rect1)
    rect_list.print_rect_list()


if __name__ == "__main__":
    main()
