"""
You are in charge of the cake for a child's birthday. You have decided 
the cake will have one candle for each year of their total age. 
They will only be able to blow out the tallest of the candles. 
Count how many candles are tallest.

Example
    candles = [4, 4, 1, 3]
    The maximum height candles are 4 units high. There are 2 of them, so return 2.

Constraints
    1 <= n <= 10**5
    1 <= candles[i] <= 10**7
"""
def birthdayCakeCandles(candles):
    """
    Count the number of candles that will be blown out (i.e.
    the number of candles that are of the maximum height)
    Parameters:
        int candles[n]: the candle heights
    Returns:
        int: the number of candles that are tallest
    """
    tallest = 0
    for c in candles:
        if c > tallest:
            tallest, count = c, 1
        elif c == tallest:
            count += 1
    return count