"""
Name:       Nicholas Loehrke
Course:     CS1430, Section 2,  Spring 2022
Assignment: Lab 07
Purpose:    This program implements a Stroop effect. The Stroop effect is a
            demonstration of cognitive interference where a delay in the reaction
            time of a task occurs due to a mismatch in stimuli. The corresponding
            paper is one of the most cited in the history of Psychology.
            We are going to implement a working version of a Stroop test. Our
            stroop test has two phases:
            The first phase is the “control phase”. The user is shown color names
            written in the same font-color. Each time the user has to write the
            name of the color.
            The second phase is the “experiment phase”. The user is shown color
            names written in a font color which is different from the color name.
            Each time the user has to write the name of the font-color.
            If you are colorblind and are having trouble with this example, see
            the instructor for an alternate lab: Animal Association Test
            (which is truly similar to the Stroop Test).

            Milestone 1: Runs Phase 1 four times, and Phase 2 four times.
            Milestone 2: Runs both tests for a total of 10 seconds.

            Install termcolor by running the following in PyCharm's terminal:
            pip install termcolor

            Install colorama by running the following in PyCharm's terminal:
            pip install colorama

Input:      A color name written in a font color. Phase 1 displays the color name
            written in the same font color. Phase 2 displays the color name
            written in a font color which is different from the color name.
Output:     If the user answer is incorrect, displays the message:
            "Correct answer was: <font color>".
            At the end, the following is displayed:
            "The number of correct responses in phase 1 was: <count>"
            "The number of correct responses in phase 2 was: <count>"
"""
#########################
# IMPORTS
#########################
import random
import time
from termcolor import colored
from colorama import init

init(autoreset=True)

#########################
# CONSTANTS
#########################
_SEED = 30  # run_phase_random_false -> 27, run_phase_random_true -> 30
_RNG = random.Random(_SEED)
_TIME_OFFSET = 0


def main():
    """

    :return:
    """
    random.seed(_SEED)
    phase = input("run phase: true or false: ")
    phase = phase.upper()
    if phase == "TRUE":
        print(run_phase(True))
        main()
    elif phase == "FALSE":
        print(run_phase(False))
        main()
    elif phase == "STOP":
        pass
    elif phase == "TEST":
        print(get_font_color(False, False))
        main()
    elif phase == "TIMED":
        run_phase_timed(False)
        main()
    elif phase == "SINGLE":
        print(run_single_test(False))
        main()
    else:
        print("invalid input")
        main()
    # print_intro()
    # Your solution goes here
    # run_single_test(False)
    # input("delay")
    # print(time.time())


def run_phase(is_phase_1):
    """
    Ask a user questions four times for both Phase 1 and Phase 2.
    Returns how many questions the user got correct.
    :param is_phase_1:  True if phase 1 (control phase), false if phase 2
                        (experimental phase)
    :type is_phase_1: boolean
    :return: n_correct
    :rtype: int
    """
    n_correct = 0
    for i in range(4):
        if run_single_test(is_phase_1):
            n_correct += 1
    return n_correct


def run_phase_timed(is_phase_1):
    time_to_answer = 10  # how long you get to answer in seconds
    n_correct = 0
    test_count = 0
    cumulative_time = 0
    previous_answer_time = time.time()
    while time.time() - previous_answer_time <= time_to_answer:
        if not is_phase_1:
            name_color = random_color_name()
            font_color = random_color_name()
            while font_color == name_color:
                font_color = random_color_name()
            print_in_color(name_color, font_color)
            previous_time = time.time()
            answer_color = input("What color ink is the word written in? ")
            time_passed = time.time() - previous_answer_time
            if answer_color != font_color:
                current_time = time.time()
                print(f'Correct answer was: {name_color}')
            else:
                current_time = time.time()
                if current_time - previous_answer_time <= time_to_answer:
                    n_correct += 1
            interval = current_time - previous_time - _TIME_OFFSET
            interval *= 1000
            interval = round(interval)
            test_count += 1
            cumulative_time += time.time() - previous_time
            time_left = time_to_answer - cumulative_time
            if time_left < 0:
                time_passed = time_passed + time_left
                time_left = 0
            time_left = round(time_left, 2)
            print(f'Interval: {interval} milliseconds     '
                  f'Time left: {time_left} seconds')
    print('')
    print('')
    time_passed = round(time_passed, 1)
    print(f'You got {n_correct} out of {test_count} in {time_passed} seconds')


def run_single_test(is_phase_1):
    """
    Run a single test of a Stroop test. Takes in a boolean parameter
    is_phase_1 which is True if you are in phase 1 of the test. This
    function should return if the user was correct (again boolean).
    :param is_phase_1:  True if phase 1 (control phase), false if phase 2
                        (experimental phase)
    :type is_phase_1: boolean
    :return: True if response == font_color
    :rtype: boolean
    """
    print()
    if is_phase_1:
        name_color = random_color_name()
        print_in_color(name_color, name_color)
        answer_color = input("What color ink is the word written in? ")
        if answer_color != name_color:
            print(f'Correct answer was: {name_color}')
            output = False
        else:
            output = True
    elif not is_phase_1:
        font_color = random_color_name()
        name_color = random_color_name()
        while font_color == name_color:
            name_color = random_color_name()
        print_in_color(name_color, font_color)
        # previous_time = time.time()
        answer_color = input("What color ink is the word written in? ")
        if answer_color != font_color:
            # current_time = time.time()
            print(f'Correct answer was: {name_color}')
            output = False
        else:
            # current_time = time.time()
            output = True
        # interval = current_time - previous_time - _TIME_OFFSET
        # interval *= 1000
        # interval = round(interval)
        # print(f'Time: {interval} milliseconds')
    return output


def control_phase(is_phase_1):
    if is_phase_1:
        for i in range(10):
            name_color = random_color_name()
            print_in_color(name_color, name_color)
            answer_color = input("What color ink is the word written in? ")
            if answer_color != name_color:
                print(f'Correct answer was {name_color}.')


def get_font_color(color_name, is_phase_1):
    """
    Return a font color. If phase1, return the same color as the
    color_name. Otherwise chose a random color.
    :param color_name: a font color name
    :type color_name: string
    :param is_phase_1: True if phase 1 (control phase), false if phase 2
    (experimental phase)
    :type is_phase_1: boolean
    :return: next_choice
    :rtype: string
    """
    '''if not is_phase_1:
        color_name = random_color_name()
    return color_name'''

    final_color = color_name
    if not is_phase_1:
        final_color = random_color_name()
        while final_color == color_name:
            final_color = random_color_name()
    return final_color


def print_intro():
    """
    Prints a simple welcome message
    :return: None
    """
    print('This is the Stroop test! Name the font-color used:')
    print_in_color('red', 'red')
    print_in_color('blue', 'blue')
    print_in_color('pink', 'pink')


def random_color_name():
    """
    Returns a string (either red, blue or pink) with equal likelihood
    :return: a random string color
    :rtype: string
    """
    return _RNG.choice(['red', 'blue', 'pink'])


def print_in_color(text, font_color):
    """
    Prints the color name in it's font-color
    :param text: a color name
    :type text: string
    :param font_color: the font-color
    :type font_color: string
    :return: None
    """
    if font_color == 'pink':  # magenta is a lot to type...
        font_color = 'magenta'
    print(colored(text, font_color, attrs=['bold']))


if __name__ == '__main__':
    main()
