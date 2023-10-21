"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: 
- 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
-   s = '12:01:00PM'
    Return '12:01:00'
-   s = '12:01:00AM'
    Return '00:01:00'

Constraints
    All input times are valid
"""
def timeConversion(s):
    """
    Converts time string in 12-hour AM/PM to military (24-hour) time string.
    Parameters:
        string s: a time in 12 hour format
    Returns:
        string: the time in  hour format
    """
    hr = int(s[:2])
    am = s[-2:] == 'AM'
    if (am and hr != 12) or (not am and hr == 12):
        return s[:-2]
    elif am:
        return '00' + s[2:-2]
    else:
        return str(hr + 12) + s[2:-2]
        
