"""
Name: Nicholas Loehrke

Course:     CS1430, Section: 2, Fall 2021

Assignment: Lab 3

Purpose:    This program calculates course letter grades for this course
            from the numeric grades on each assignment, test, and quiz.

Input:      Grades for each assignment, test, and quiz.
Output:     A final letter grade

"""

""" 
CONSTANTS
"""
_QUIZ_POINTS = 24
_ASSIGNMENT1_POINTS = 15
_ASSIGNMENT2_POINTS = 20
_ASSIGNMENT3_POINTS = 25
_ASSIGNMENT4_POINTS = 30
_ASSIGNMENT5_POINTS = 30
_FINAL_EXAM_POINTS = 30

_A_THRESHOLD = 93.5
_A_MINUS_THRESHOLD = 89.5
_B_PLUS_THRESHOLD = 86.5
_B_THRESHOLD = 83.5
_B_MINUS_THRESHOLD = 79.5
_C_PLUS_THRESHOLD = 76.5
_C_THRESHOLD = 73.5
_C_MINUS_THRESHOLD = 69.5
_D_THRESHOLD = 64.5


_INPUT_MESSAGE_POINTS = "Enter the points earned for {:s} or -1 if " \
                        "there are no more {:s} grades to enter"
_OUTPUT_MESSAGE_GRADE = "Final numeric grade = {:.2f}"
_OUTPUT_MESSAGE_LETTER = "Final letter grade = {:s}"


def main():
    """
    This program calculates course letter grades for this course
    from the numeric grades on each assignment, test, and quiz.
    """

    earned_points = 0.0
    total_points = 0.0

    quiz2_points = -1
    quiz3_points = -1
    quiz4_points = -1

    assignment2_points = -1
    assignment3_points = -1
    assignment4_points = -1

    quiz1_points_raw = input(
        _INPUT_MESSAGE_POINTS.format("quiz 1", "quizzes"))
    quiz1_points = float(quiz1_points_raw)

    if quiz1_points != -1:
        earned_points += quiz1_points
        total_points += _QUIZ_POINTS
        quiz2_grade_raw = input(
            _INPUT_MESSAGE_POINTS.format("quiz 2", "quiz"))
        quiz2_points = float(quiz2_grade_raw)

        if quiz2_points != -1:
            earned_points += quiz2_points
            total_points += _QUIZ_POINTS
            quiz3_grade_raw = input(
                _INPUT_MESSAGE_POINTS.format("quiz 3", "quiz"))
            quiz3_points = float(quiz3_grade_raw)

            if quiz3_points != -1:
                earned_points += quiz3_points
                total_points += _QUIZ_POINTS
                quiz4_grade_raw = input(
                    _INPUT_MESSAGE_POINTS.format("quiz 4", "quiz"))
                quiz4_points = float(quiz4_grade_raw)

                if quiz4_points != -1:
                    earned_points += quiz4_points
                    total_points += _QUIZ_POINTS
                    quiz5_grade_raw = input(
                        _INPUT_MESSAGE_POINTS.format("quiz 5", "quiz"))
                    quiz5_points = float(quiz5_grade_raw)

                    if quiz5_points != -1:
                        earned_points += quiz5_points
                        total_points += _QUIZ_POINTS

    # DO_03: Complete the boolean statement below that checks to see if
    #        quiz2_points is not equal to -1.
    #        Follow the same pattern as the above nested if statements
    #        for quiz1_points and quiz2_points.
    # DO_04: Complete the boolean statement below that checks to see if
    #        quiz3_points is not equal to -1.
    #        Follow the same pattern as the above nested if statements
    #        for quiz2_points and quiz3_points.

    # DO_05: Complete the boolean statement below that checks to see if
    #        quiz4_points is not equal to -1.
    #        Follow the same pattern as the above nested if statements
    #        for quiz3_points and quiz4_points.

    assignment1_grade_raw = input(_INPUT_MESSAGE_POINTS.format(
        "assignment 1", "assignment"))
    assignment1_grade = float(assignment1_grade_raw)

    if assignment1_grade != -1:
        earned_points += assignment1_grade
        total_points += _ASSIGNMENT1_POINTS
        assignment2_grade_raw = input(_INPUT_MESSAGE_POINTS.format(
            "assignment 2", "assignment"))
        assignment2_grade = float(assignment2_grade_raw)

        if assignment2_grade != -1:
            earned_points += assignment2_grade
            total_points += _ASSIGNMENT2_POINTS
            assignment3_grade_raw = input(_INPUT_MESSAGE_POINTS.format(
                "assignment 3", "assignment"))
            assignment3_grade = float(assignment3_grade_raw)

            if assignment3_grade != -1:
                earned_points += assignment3_grade
                total_points += _ASSIGNMENT3_POINTS
                assignment4_grade_raw = input(_INPUT_MESSAGE_POINTS.format(
                    "assignment 4", "assignment"))
                assignment4_grade = float(assignment4_grade_raw)

                if assignment4_grade != -1:
                    earned_points += assignment4_grade
                    total_points += _ASSIGNMENT4_POINTS
                    assignment5_grade_raw = input(_INPUT_MESSAGE_POINTS.format(
                        "assignment 5", "assignment"))
                    assignment5_grade = float(assignment5_grade_raw)

                    if assignment5_grade != -1:
                        earned_points += assignment5_grade
                        total_points += _ASSIGNMENT5_POINTS

    earned_lab_points_raw = input("Enter the total lab points "
                                  "earned or -1 if there are no lab points")
    earned_lab_points = float(earned_lab_points_raw)

    if earned_lab_points != -1:
        earned_points = earned_points + earned_lab_points
        total_lab_points_raw = input("Enter the total lab points possible")
        total_points = total_points + float(total_lab_points_raw)

    earned_final_exam_points_raw = input("Enter the points earned on "
                "the final exam or -1 if there is not a final exam grade")
    earned_final_exam_points = float(earned_final_exam_points_raw)

    if earned_final_exam_points != -1:
        earned_points = earned_points + earned_final_exam_points
        total_points = total_points + _FINAL_EXAM_POINTS

    # assume total_points is not zero
    numeric_grade = earned_points / total_points * 100

    letter_grade = "undefined"

    if numeric_grade >= _A_THRESHOLD:
        letter_grade = "A"
    elif numeric_grade >= _A_MINUS_THRESHOLD:
        letter_grade = "A-"
    elif numeric_grade >= _B_PLUS_THRESHOLD:
        letter_grade = "B+"
    elif numeric_grade >= _B_THRESHOLD:
        letter_grade = "B"
    elif numeric_grade >= _B_MINUS_THRESHOLD:
        letter_grade = "B-"
    elif numeric_grade >= _C_PLUS_THRESHOLD:
        letter_grade = "C+"
    elif numeric_grade >= _C_THRESHOLD:
        letter_grade = "C"
    elif numeric_grade >= _C_MINUS_THRESHOLD:
        letter_grade = "C-"
    elif numeric_grade >= _D_THRESHOLD:
        letter_grade = "D"

    # DO_09: Complete the nested elif statements to set the value of
    #        letter_grade based on the numeric_grade value.
    #        Follow the same pattern as the above nested if statements above.

    else:
        letter_grade = "F"

    print(_OUTPUT_MESSAGE_GRADE.format(numeric_grade))
    print(_OUTPUT_MESSAGE_LETTER.format(letter_grade))


"""
Do not remove the code below this line!
"""

if __name__ == '__main__':
    main()
