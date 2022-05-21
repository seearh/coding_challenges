"""
Given five positive integers, find the minimum and maximum values that can be 
calculated by summing exactly four of the five integers. Then print the 
respective minimum and maximum values as a single line of two space-separated 
long integers.

Example
    arr = [1, 3, 5, 7, 9]
    The minimum sum is 1 + 3 + 5 + 7 = 16 and 
    the maximum sum is 3 + 5 + 7 + 9 = 24. 
    The function prints
    16 24

Constraints
    1 <= arr[i] <= 10**9
"""
def miniMaxSum(arr):
    """
    Print two space-separated long integers denoting the respective minimum and 
    maximum values that can be calculated by summing exactly four of the five integers.
    Parameters:
        arr: an array of 5 integers
    Returns:
        None
    """
    print(f'{sum(arr) - max(arr)} {sum(arr) - min(arr)}')
