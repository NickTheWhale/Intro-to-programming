
class Rectangle_list:
    """
    Class that represents a list of rectangles
    """
    def __init__(self):
        self.__rect_lst = []

    def add_rectangle(self, new_rectangle):
        self.__rect_lst.append(new_rectangle)

    def print_rect_list(self):
        '''for i in range(len(self.__rect_lst)):
            print(f'Rectangle {i+1}: ', end="")
            self.__rect_lst[i].print_rectangle()'''
        for i in self.__rect_lst:
            i.print_rectangle()

    def return_rect_list(self):
        lst = []
        for i in range(len(self.__rect_lst)):
            lst.append(self.__rect_lst[i])
        return lst

    @property
    def rect_lst(self):
        return self.__rect_lst
