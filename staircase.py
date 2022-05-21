"""
This is a staircase of size n = 4.

   #
  ##
 ###
####

Its base and height are both equal to n. It is drawn using # symbols and spaces. 
The last line is not preceded by any spaces.

Write a program that prints a staircase of size n.

Constraints
    0 < n <= 100
"""
def staircase(n):
    """
    Prints a staircase of size n using # symbols and spaces.
    Parameters:
        int n: an integer
    Returns:
        None
    """
    for i in range(1, n+1):
        print(f"{'#'*i:>{n}}")