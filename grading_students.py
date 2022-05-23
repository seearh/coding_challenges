import math

"""
HackerLand University has the following grading policy:

Every student receives a grade in the inclusive range from 0 to 100.
Any grade less than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's 
grade according to these rules:

If the difference between the grade and the next multiple of 5 is less 
than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result 
will still be a failing grade.

Examples
    grade = 84 round to 85 (85 - 84 is less than 3)
    grade = 29 do not round (result is less than 40)
    grade = 57 do not round (50 - 57 is 3 or higher)

Constraints
    1 <= n <= 60
    0 <= grades[i] <= 100
"""
def gradingStudents(grades):
    """
    Function that performs rounding according to Sam's logic above
    Parameters
        int grades[n]: the grades before rounding
    Returns
        int[n]: the grades after rounding as appropriate
    """
    return [
        g if g < 38 or 5 - (g % 5) >= 3 else math.ceil(g/5) * 5
        for g in grades
    ]