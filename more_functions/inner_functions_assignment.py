"""
Author: Alex Alvarado
"""


def measures(rect_measures):
    a_value = 0.0
    p_value = 0.0

    def area(a_measure):
        return a_measure[0] * a_measure[1]
    def perimeter(p_measure):
        return p_measure[0] *2 + p_measure[1] * 2

    a_value = area(rect_measures)
    p_value = perimeter(rect_measures)
    return "Perimeter = {} Area = {}".format(p_value, a_value)


print(measures([2,3]))
