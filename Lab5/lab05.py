"""
------------------------------------------------------------------------
CS 1430 Lab5

DO_1:       Insert your name and section

Name:       Nicholas Loehrke

Course:     CS 1430, Section 02,  Spring 2022

Assignment: Lab 05

Purpose:    Process the readings of systolic blood pressure a person
            measured during a week. One may have 0 or multiple readings
            during a day, and may not have readings everyday. The program
            processes the readings until the end-of-file is reached.

Input:      List of readings of the systolic blood pressure, terminated
            by end-of-file. Each line of the input data is the readings of
            the blood pressure measured during a day.
            A line of input data begins with the number of readings of
            that day followed by the readings. For example, the following
            input data shows that there are 5 readings in that day.
                5
                120
                113
                142
                111
                109

Output:     For each day of the readings processed, display the
                1. Day number. For example, Day 1, or Day 2, etc.
                2. Highest reading of the day.
                3. Average reading of the day.
            After all the readings are processed, display
                1. The number of days the reading were recorded in the week.
                2. The average reading of the week.
                3. A message that identifies the blood pressure stages based
                    on the average reading of the week.

                Average Reading       Blood Pressure Stages
                =========================================
                0.0				       Unknown
                < 120.0               Normal
                >= 120.0 and < 140.0  Prehypertension
                > 140.0 and < 180.0   Hypertension
                > 180.0               Hypertensive Crisis
------------------------------------------------------------------------
"""

# constants
_PREHYPERTENSION = 120.0
_HYPERTENSION = 140.0
_CRISIS = 180.0


def main():
    """
    Process the readings of systolic blood pressure a person
    measured during a week. One may have 0 or multiple readings
    during a day, and may not have readings everyday. The program
    processes the readings until the end-of-file is reached.
    :return:
    """
    num_days = 0
    week_readings = 0
    reading = 0
    highest = 0
    day_sum = 0
    week_sum = 0
    day_average = 0.0
    week_average = 0.0

    # DO_2: Priming read; the first data item is the number of readings
    #       in a day. Do not convert it to an int data type.

    num_readings = input()
    # DO_3: Check if end-of-file has been reached.
    # stop when num_readings is empty
    while num_readings != "":
        num_readings = int(num_readings)
        # DO_4: Set the day_sum of readings and the highest reading of
        #       a day to zero.
        day_sum = 0
        highest = 0
        count_readings = 0

        # DO_5: Write the logical expression for the count-controlled loop.
        #       Use the count_readings to control the iterations.
        while count_readings < num_readings:
            reading = int(input())
            if count_readings == 0: # set the first reading as the highest
                highest = reading
            # DO_6: Write the logical expression to check if the reading is
            #       greater than the saved highest reading.
            if reading > highest:
                highest = reading

            day_sum += reading
            # DO_7: increase the loop counter count_reading by 1
            count_readings += 1

        num_days += 1
        print(f"Day {num_days}")
        print(f"Highest Reading: {highest}")

        # DO_8: Compute the average reading day_average
        #       only if the number of readings
        #       is NOT zero.
        if num_readings != 0:
            day_average = day_sum / num_readings
        else:
            day_average = 0

        print(f"Average Reading: {day_average:.2f}")

        week_sum += day_sum
        week_readings += num_readings
        # DO_9: Read the next number of readings of a day.
        num_readings = input()

    print(f"Number of days the readings were recorded: {num_days}")

    # DO_10: Compute the average reading of a week  week_readings
    #        only if the number of readings in a week is NOT zero.
    if week_readings != 0:
        week_average = week_sum / week_readings
    else:
        week_readings = 0

    print(f"Average Reading of the Week: {week_average:.2f}")
    print("Blood Pressure Stage: ", end="")

    # DO_11: Complete the if/else statement so the program outputs a proper
    #        message for the blood pressure stage.
    if week_average == 0.0:
        print("Unknown.")
    elif week_average < 120:
        print("Normal.")
    elif (week_average >= 120) and (week_average < 140):
        print("Prehypertension.")
    elif (week_average >= 140) and (week_average < 180):
        print("Hypertension.")
    else:
        print("Hypertensive Crisis!")


if __name__ == "__main__":
    main()
