"""
https://leetcode.com/problems/palindrome-number/description/
"""

def isPalindrome(x):
    """ T(c) -> O(log10N + 1), S(c) -> O(1) """
    # if negative, not palindrome
    if x < 0:
        return False

    num = x

    rev = 0
    while num > 0:
        ld = num % 10
        rev = (rev * 10) + ld
        num = num // 10

    if x == rev:
        return True
    else:
        return False
