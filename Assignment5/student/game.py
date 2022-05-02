class Game:
    """
    Game class simulates a game
    author(s):
    """
    def __init__(self):
        """
        Constructor creates an empty list of heaps and an empty list of players,
        and sets the turn_index to 0.
        turn_index represents which player's turn it is.
        """
        self.__heaps = []
        self.__players = []
        self.__turn_index = 0

    @property
    def turn_index(self):
        """
        Getter method that returns the current turn_index.
        """
        """
        :return: turn_index
        :rtype: int
        """
        pass

    def get_player(self, player_index):
        """
        Returns which player's turn it is based on player_index.
        :return
        :param
        :type
        :rtype
        """
        pass

    def get_heap(self, heap_index):
        """
        Returns the heap that is referenced by heap_index
        :return: heap that is referenced by heap_index
        :rtype: int
        :param: heap_index
        :type: int
        """
        return self.__heaps[heap_index]

    def get_number_of_heaps(self):
        """
        Returns the length of the heap list
        :return
        :rtype
        """
        pass

    def add_player(self, player):
        """
        Appends player to the end of the players list.
        :param
        :type
        :return: None
        """
        pass

    def increment_turn(self):
        """
        Increments the turn_index by 1. If the turn_index is greater than or equal to the number of players,
        it sets turn_index to 0.
        :return: None
        """
        pass

    def add_heap(self, heap):
        """
        appends heap to the end of the heap list.
        :param
        :type
        :return: None
        """
        pass

    def update_heap(self, heap_index, amount):
        """
        removes amount from the heap at the index indicated by heap_index.
        :param
        :type
        :param
        :type
        :return: None
        """
        pass

    def is_heap_empty(self, heap_index):
        """
        Checks if the heap has a value of 0 and returns a True if it is empty and a False otherwise.
        :param heap_index: Index of the heap
        :type
        :return: Returns true if the heap is empty, and false otherwise
        :rtype: boolean
        """
        pass

    def is_amount_valid(self, heap_index, amount):
        """
        testing `Game.turn_index`
        Checks if the amount to remove from the heap is less than or
        equal to the current heap size<br>
        :param heap_index: Index of the heap<br>
        :type heap_index: int<br>
        :param amount: The amount to remove from the heap<br>
        :type amount: int<br>
        :return: Returns true if the amount to remove from the heap
        is less than or equal to the heap amount, and false otherwise<br>
        :rtype: boolean<br>
        """
        pass

    def print_heaps(self):
        """
        Prints the following:
        Heap <heap number> size: <current heap size>
        :return: None
        """
        pass

    def is_game_over(self):
        """
        Boolean function returns if the game is over. Goes through all of the heaps to see if all of the heap
        sizes are 0.
        :return:
        :rtype
        """
        pass

    def reset(self):
        """
        Resets the heap sizes to the initial_size, and sets turn_index to 0.
        :return: None
        """
        pass

    def increment_player_score(self, player_index):
        """
        increments the player's score in the player list indicated by player_index by 1.
        :param player_index:
        :type
        :return: None
        """
        pass

    def print_player_scores(self):
        """
        Prints the player scores in the following format:
        Player <player index + 1> score: <score>
        :return: None
        """
        pass

    def print_round_winner(self):
        """
        Prints the player winner for the round in the following format:
        Player <player name> has won this round!
        :return: None
        """
        pass
