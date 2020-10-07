"""
Author: Alex Alvarado
Program: validate_input_in_functions
Date: 9-29-20
Description: prompts user for name and score, prints values to console if valid.
"""


def score_input(test_name, test_score=0, invalid_message = "Invalid test score, try again!"):
    """
    Function that acceptrs params and returns a string...
    :param test_name: The name of a test/exam
    :param test_score: A value between 0 and 100 representing a test/exam
    :param invalid_message: Message displayed when an invalid score is provided.
    :return: Formatted string that returns the test name and score.
    """
    try:
        if 0 <= test_score <= 100:
            return "{}: {}".format(test_name, test_score)
        else:
            return invalid_message
    except TypeError:
        raise TypeError


if __name__ == '__main__':
    #try:
        print(score_input("Python1!"))
  #  except TypeError:
        #print("not a valid input")


