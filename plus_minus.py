"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. 
The test cases are scaled to six decimal places, though answers with absolute error of up to 
10^-4 are acceptable.

Example
    arr = [1, 1, 0, -1, -1]
    There are n = 5 elements, two positive and one zero. Their ratios are
    2/5 = 0.400000, 2/5 = 0.400000, 1/5 = 0.200000. Results are printed as
    0.400000
    0.400000
    0.200000

Constraints
    0 < n < 100
    -100 <= arr[i] <= 100
"""
def plusMinus(arr):
    """
    Print the ratios of positive, negative and zero values in the array. 
    Each value should be printed on a separate line with 6 digits after 
    the decimal. The function should not return a value.
    Parameters:
        int arr[n]: an array of integers
    Returns:
        None
    """
    out_arr = [0] * 3
    denom = 0
    for n in arr:
        denom += 1
        if n > 0:
            out_arr[0] += 1
        elif n == 0:
            out_arr[2] += 1
        else:
            out_arr[1] += 1
    for out in out_arr:
        print(f'{out/denom:6f}')