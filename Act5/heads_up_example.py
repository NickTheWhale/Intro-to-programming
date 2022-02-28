import random


def main():
    """
    Heads up game
    How the game is played:
    When it is your turn, close your eyes. 
    A word will be displayed in the HeadsUp program.
    The rest of the section will try and describe it without saying the word.
    You have to guess the word as quickly as possible.
    """
    
    # Create a list of words
    my_list = ["algorithm", "syntax", "semantics", "program", "pseudocode"]
    
    # pick a random word
    correct_answer = random.choice(my_list) # comes with ‘import random’

    # Understand how to get a value by its index
    # get the item at the chosen index
    #correct_answer = names[index]
    
    print(f"Word is: {correct_answer}")
    # prompt a word and have someone describe the definition
    # prompt the user for an answer, check if it is correct
    guess = input("what is your guess? ") 

    while guess != correct_answer:

        print("incorrect guess ")
        guess = input("what is your guess? ")

    print("good job")


if __name__ == '__main__':
    main()
