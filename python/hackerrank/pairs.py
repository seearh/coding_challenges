from typing import List


'''
Given an array of integers and a target value, determine the number
of pairs of array elements that have a difference equal to the target 
value.

Constraints
- 2 <= n <= 10**5
- 0 < k < 10**9
- 0 < arr[i] < 2**31 - 1
- each integer arr[i] will be unique
'''
def pairs(k: int, arr: List[int]) -> int:
    '''
    Parameters
        k: an integer, the target difference
        arr[n]: an array of integers
    Returns
        the number of pairs that satisfy the criterion
    '''
    arr = set(arr)
    return len(arr.intersection({i+k for i in arr}))