"""
Author: Alex Alvarado
Program: inner_functions_assignment.py
Date: 10-3-20
Description: the function accepts a list that contains measurements or a rectangle or square and it returns the area and
 perimeter
"""


def measures(rect_measures):
    a_value = 0.0
    p_value = 0.0

    def area(a_measure):
        if len(a_measure) == 1:
            return a_measure[0] * a_measure[0]
        elif len(a_measure) == 2:
            return a_measure[0] * a_measure[1]
        else:
            return IndexError

    def perimeter(p_measure):
        if len(p_measure) == 1:
            return p_measure[0]*4
        elif len(p_measure) == 2:
            return p_measure[0] *2 + p_measure[1] * 2
        else:
            raise IndexError
    try:
        a_value = area(rect_measures)
        p_value = perimeter(rect_measures)
    except IndexError:
        raise IndexError

    return "Perimeter = {} Area = {}".format(p_value, a_value)






