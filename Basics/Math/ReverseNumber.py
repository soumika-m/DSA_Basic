"""
https://leetcode.com/problems/reverse-integer/description/
"""

def reverse(x):
    """ T(c) -> O(log10N + 1), S(c) -> O(1) """
    neg = False
    if x < 0:
        neg = True
        x = abs(x)

    rev = 0
    while x > 0:
        last_digit = x % 10
        rev = (rev * 10) + last_digit
        x = x // 10
        if rev > 2**31 - 1:
            return 0

    if neg:
        rev = -1 * rev

    return rev