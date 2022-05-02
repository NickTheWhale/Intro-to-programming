class Heap:
    """
    Brief description of class
    author(s):
    :param
    :type
    """

    def __init__(self, size):
        """
        :param
        :type
        """
        self.__initial_size = size
        self.__current_size = self.__initial_size

    @property
    def initial_size(self):
        """
        :return
        :rtype
        """
        return self.__initial_size

    @property
    def current_size(self):
        """
        :return
        :rtype
        """
        pass

    @initial_size.setter
    def initial_size(self, initial_size):
        """
        :param
        :type
        :return: None
        """
        pass

    @current_size.setter
    def current_size(self, current_size):
        """
        :param
        :type
        """
        pass

    def remove(self, amount):
        """
        Removes the amount specified from this heap.
        Returns -1 if the current_size - amount is < 0.
        Otherwise it returns the new heap amount.
        :param amount: The amount to remove from the heap
        :type
        :return: Returns the new size of the heap or -1 if the amount
        was invalid
        :rtype
        """
        pass

    def reset(self):
        """
        Resets the current_size to the initial_size
        :return: None
        """
        pass
