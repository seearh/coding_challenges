'''
Source: https://www.hackerrank.com/challenges/between-two-sets
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:
1. The elements of the first array are all factors of the integer being considered
2. The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

Example
a = [2, 6]
b = [24, 36]

There are two numbers between the arrays: 6 and 12.
6 % 2 = 0, 6 % 6 = 0, 24 % 6 = 0 and 36 % 6 = 0 for the first value.
12 % 2 = 0, 12 % 6 = 0, 24 % 12 = 0 and 36 % 12 = 0 for the second value. Return 2.

Constraints
1 <= n, m <= 10
1 <= a[i] <= 100
1 <= b[i] <= 100
'''
def getTotalX(a, b):
    '''
    Parameters:
        int a[n]: an array of integers
        int b[m]: an array of integers
    Returns:
        int: the number of integers that are between the sets
    '''
    n = 0
    for i in range(max(a), min(b) + 1):
        if all(i % factor == 0 for factor in a) and all(factorOf % i == 0 for factorOf in b):
            n += 1
    return n