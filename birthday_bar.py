'''
Source: https://www.hackerrank.com/challenges/the-birthday-bar/problem

Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:
- The length of the segment matches Ron's birth month, and,
- The sum of the integers on the squares is equal to his birth day.

Determine how many ways she can divide the chocolate.

Example
s = [2, 2, 1, 3, 2]
d = 4
m = 2
Lily wants to find segments summing to Ron's birth day, d = 4 with a length equalling his 
birth month, m = 2. In this case, there are two segments meeting her criteria:
[2, 2] and [1, 3].

Constraints
1 <= n <= 100
1 <= s[i] <= 5, where (0 <= i < n)
1 <= d <= 31
1 <= m <= 12
'''
def birthday(s, d, m):
    '''
    Parameters:
        int s[n]: the numbers on each of the squares of chocolate
        int d: Ron's birth day
        int m: Ron's birth month
    Returns:
        int: the number of ways the bar can be divided
    '''
    start, end, segs = 0, m, 0
    while end <= len(s):
        if sum(s[start:end]) == d:
            segs += 1
        start += 1
        end += 1
    return segs