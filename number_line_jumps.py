"""
You are choreographing a circus show with various animals. For one act, 
you are given two kangaroos on a number line ready to jump in the positive 
direction (i.e, toward positive infinity).

The first kangaroo starts at location  and moves at a rate of  meters per jump.
The second kangaroo starts at location  and moves at a rate of  meters per jump.
You have to figure out a way to get both kangaroos at the same location at the 
same time as part of the show. If it is possible, return YES, otherwise return NO.

Example
    x1 = 2
    v1 = 1
    x2 = 1
    v2 = 2
    After one jump, they are both at 3, (x1 + v1 = 2 + 1, x2 + v2 = 1 + 2), 
    so the answer is YES.

Constraints
    0 <= x1 < x2 <= 10000
    1 <= v1 <= 10000
    1 <= v2 <= 10000
"""
def kangaroo(x1, v1, x2, v2):
    """
    Determines if it is possible to get both kangaroos at the same location 
    at the same time as part of the show
    Parameters:
        int x1, int v1: starting position and jump distance for kangaroo 1
        int x2, int v2: starting position and jump distance for kangaroo 2
    Returns
        string: either YES or NO
    """
    back, front = sorted([(x1, v1), (x2, v2)])
    return (
        'YES' if 
        back[1] > front[1]
        and (front[0] - back[0]) % (back[1] - front[1]) == 0
        else 'NO'
    )