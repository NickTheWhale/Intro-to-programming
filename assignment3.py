"""
Name: Dylan Brodie and Nick Loehrke

Course: CS1430, Section 02,  Spring 2022

Assignment: Assignment 3

Purpose:    To write a Python student that will encrypt and decrypt a message
            using a Vigenère cipher. Pseudocode to encrypt a message:
            1.	Initialize an empty string.
            2.	For each letter in the plaintext message:
                a.	Determine which letter of the key to use.
                b.	Using the key letter, look up the ciphertext letter in the
                    Vigenère square in the plaintext character column.
                c.	Add the ciphertext letter to the ciphertext message.
            3.	Return the resulting string as the ciphertext message.

Input: A message to encode/ a message to decode and what key word to use

Output:  Either a decoded message or coded message using the inputted key

"""

#########################
# IMPORTS
#########################
from string import ascii_uppercase

#########################
# CONSTANTS
#########################
_ALPHABET = ascii_uppercase
_LETTERS_IN_ALPHABET = len(_ALPHABET)


def valid_phrase(message):
    """
    valid_phrase checks that each character in the message is a letter
    in the alphabet. Calls the .find() function.
    Parameter message may have a space and letters of the alphabet.
    Returns a true if the message is alphabetic, and
    a false otherwise.

    :param message: a message to encrypt or decrypt
    :type message: a string
    :return: a boolean, false if any character in the message is not
    alphabetic, and true otherwise.
    :rtype: string
    """
    phrase = message.isalpha()
    if phrase:
        decider = True
    else:
        decider = False
    return decider


def letter_to_index(letter):
    """
    letter_to_index returns the index of the letter in the alphabet.
    Calls the .find() function.

    :param letter: one of the letters in the message
    :type letter: a string
    :return: the index of the parameter in the alphabet string
    :rtype: string
    """
    # TODO
    pass


def index_to_letter(idx):
    """
    index_to_letter returns the letter of the alphabet based on the
    parameter index. Calls the .find() function.

    :param idx: the index of the parameter in the alphabet string
    :type idx: a string
    :return: the letter from the alphabet at the index provided
    :rtype: string
    """
    # TODO
    pass


def vigenere_index(key_letter, plain_text_letter):
    """
    vigenere_index takes a letter from the key and a plaintext letter,
    and returns the encrypted letter. Calls the functions
    letter_to_index() and index_to_letter().

    :param key_letter: one letter from the key
    :type key_letter: String
    :param plain_text_letter:  one letter from the plain_text
    :type plain_text_letter: String
    :return: a single character as a string representing the
    encrypted letter
    :rtype: string
    """



def undo_vig(key_letter, ct_letter):
    """
    undo_vig takes a letter from the key, a ciphertext letter,
    and returns the plaintext letter. Calls the functions
    letter_to_index() and index_to_letter().

    :param key_letter: one letter from the key
    :type key_letter: string
    :param ct_letter:  one letter from the cypher text
    :type ct_letter: string
    :return: a string representing the unencrypted letter
    :rtype: string
    """
    # TODO
    pass


def decrypt_vigenere(key, cipher_text):
    """
    decrypt_vigenere takes a keyword, the cipher text for the
    message, and returns the plain text message. Calls the
    function undo_vig().

    :param key: The decryption key
    :type key: string
    :param cipher_text:  The cipher text
    :type cipher_text: string
    :return: Returns a string representing the decrypted text
    :rtype: string
    """
    # TODO
    pass


def encrypt_vigenere(key, plain_text):
    """
    encrypt_vigenere take a keyword and the plain text for the message,
    and returns the encrypted Vigenere cipher text. Calls the function
    vigenere_index().

    :param key: The encryption key
    :type key: string
    :param plain_text:  The plain text
    :type plain_text: string
    :return: Returns a string representing the encrypted text
    :rtype: string
    """
    # TODO
    pass


def get_message():
    """
    Prompts the user for the message to be encrypted.
    Calls the.upper() function. Returns the message
    to be encrypted.

    :return: the message to be encrypted
    :rtype: string
    """
    message_to_encrypt = input("Enter the message to be encrypted: ")
    message_to_encrypt = message_to_encrypt.upper()
    return message_to_encrypt

def get_cyphertext():
    """
    Prompts the user for the cipher text to decrypt. Returns
    the cipher text to decrypt. Calls the .upper() function.

    :return: the cipher text to decrypt
    :rtype: string
    """
    message_to_decrypt = input("Enter the cypher text to decrypt: ")
    message_to_decrypt = message_to_decrypt.upper()
    return message_to_decrypt


def get_key():
    """
    Prompts the user for the Vigenere key. Returns the Vigenere key.
    Calls the .upper() function.

    :return: the Vigenere key
    :rtype: string
    """
    key_word = input("Enter the Vigenere key: ")
    key_word = key_word.upper()
    if key_word.isalpha():
        return key_word
    else:
        print("Not a valid key. Letter must be in the alphabet.")
        get_key()


def get_choice():
    """
    Prompts the user for their choice of E, Q, or D. Does not check for
    case. Calls the .input(),.upper() and .strip() functions.
    Returns the choice.

    :return: A string "E", "Q", or "D" representing the choice
    :rtype: string
    """
    choice = input("Enter an E to encrypt a message, a D to decrypt a message, "
                   "and Q to quit: ")
    choice = choice.strip()
    choice = choice.upper()
    return choice


def main():
    """
    A Python student that will encrypt and decrypt a message
    using a Vigenère cipher.
    :return: none
    """
    choice = get_choice()
    if choice == 'E':
        if valid_phrase(get_message()):

        else:

    elif choice == 'D':
        if valid_phrase(get_cyphertext()):

        else:

    elif choice == 'Q':
        pass
    else:
        print("Invalid response!")
        main()


if __name__ == '__main__':
    main()
