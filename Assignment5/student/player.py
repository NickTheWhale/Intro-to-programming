class Player:
    """
    Class to store player name and score
    author(s): Nicholas Loehrke and Dylan Brodie
    :param
    :type
    """
    def __init__(self, player_name):
        """
        :param
        :type
        """
        self.__name = player_name
        self.__score = 0

    @property
    def name(self):
        """
        :return
        :rtype
        """
        return self.__name

    @property
    def score(self):
        """
        :return
        :rtype
        """
        return self.__score

    def increment_score(self):
        """
        increment_score updates the player's `Player.score` by one point<br>
        :return: updated score<br>
        :return: None
        """
        self.__score += 1
