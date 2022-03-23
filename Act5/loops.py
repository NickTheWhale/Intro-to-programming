def letter_to_index(letter):
    """
    letter_to_index returns the index of the letter in the alphabet.
    Calls the .find() function.

    :param letter: one of the letters in the message
    :type letter: a string
    :return: the index of the parameter in the alphabet string
    :rtype: string
    """
    index = ord(letter) - 65
    return index

print(letter_to_index('A'))
