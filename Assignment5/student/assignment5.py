"""
Name: <Fill in your name>

Course: CS1430, Section <Insert section here>,  Fall 2021

Assignment: Assignment 5

Purpose:

Input:

Output:

"""


from distutils.util import strtobool

from Assignment5.student.game import Game
from Assignment5.student.heap import Heap
from Assignment5.student.player import Player


def main():
    """"""
    # assumes valid input
    number_of_players = int(input("Enter the number of players: "))

    # assumes valid input
    number_of_heaps = int(input("Enter the number of heaps: "))

    # Create an instance of a game class
    game = Game()

    add_players(number_of_players, game)
    add_heaps(number_of_heaps, game)

    # Call run_game
    run_game(game)

    boolean_string = input('Do you want to play another round? '
                           'True or False: ')
    user_continue = bool(strtobool(boolean_string))

    while user_continue:
        game.reset()
        run_game(game)

        boolean_string = input('Do you want to play another round? '
                               'True or False: ')
        user_continue = bool(strtobool(boolean_string))


def run_game(game):
    """
    Prints the current heaps
    While the game is not over, take turns
    Once the game is over, print the round winner and player scores.
    :param game: Current game object
    :type
    :return: None
    """
    pass



def take_turn(game):
    """
    This function simulates the turns for a player
    :param game: current game
    :type: Game object
    :return: None
    """
    turn_index = game.turn_index
    current_player = game.get_player(turn_index)
    current_player_name = current_player.name

    heap_index, amount = get_heap_amount(game)

    print_move(current_player_name, amount, heap_index)

    # update heap - currently ignoring the value returned
    game.update_heap(heap_index, amount)
    game.print_heaps()

    # increment turn if game is not over, otherwise increment current
    # player's score
    if not game.is_game_over():
        game.increment_turn()
    else:
        game.increment_player_score(turn_index)


def get_heap_amount(game):
    """
    Asks the user for a valid heap number and an amount to remove from the heap.
    :param game: current game
    :type: Game object
    :return heap_index
    :rtype int
    :return amount
    :rtype int
    """
    turn_index = game.turn_index
    current_player = game.get_player(turn_index)
    current_player_name = current_player.name

    valid_index = False
    heap_index = -1
    valid_amount = False
    amount = -1

    while not valid_amount:
        while not valid_index:
            heap_index = int(input(current_player_name
                                   + ": Choose a heap number: ")) - 1
            if heap_index < 0 or heap_index >= game.get_number_of_heaps() \
                    or game.is_heap_empty(heap_index):
                print(str(heap_index + 1) + ' is not a valid heap number.')
            else:
                valid_index = True

        amount = int(input(current_player_name +
                           ": Choose an amount to remove from heap "
                           + str(heap_index + 1) + ": "))
        if not game.is_amount_valid(heap_index, amount):
            print(str(amount) + ' is not a valid heap amount.')
            valid_index = False
        else:
            valid_amount = True
    return heap_index, amount


def add_players(number_of_players, game):
    """
    Creates the player objects and adds the player names to the game
    one name at a time based on the value in the parameter number_of_players.
    :param
    :type
    :param
    :type
    :return: None
    """
    pass


def add_heaps(number_of_heaps, game):
    """
    Creates the heap objects and adds the heap to the game one heap at a time
    based on the value in the parameter number_of_heaps.
    :param
    :type
    :param
    :type
    :return: None
    """
    pass


def print_move(player_name, amount, heap_index):
    """
    prints the player info in the following format:
    <Player name> takes <amount> from heap <heap number>
    :param
    :type
    :param
    :type
    :param
    :type
    :return: None
    """
    pass


if __name__ == '__main__':
    main()