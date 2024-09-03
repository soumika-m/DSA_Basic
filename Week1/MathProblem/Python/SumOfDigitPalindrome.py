"""
    Given a number n. Find if the digit sum(or sum of digits) of n is a Palindrome number or not.
    
    https://www.geeksforgeeks.org/problems/sum-of-digit-is-pallindrome-or-not2751/1
"""

def isDigitSumPalindrome(n):
    """ T(c) -> O(log(n)) , space -> O(1) """
    sum_digit = 0
    # find sum of digits
    while n > 0:
        sum_digit += n % 10
        n //= 10
    
    return isPalindrome(sum_digit)


def isPalindrome(n):
    rev = 0
    num = n
    # reverse that number
    while n > 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n = n // 10
    
    # number is same as reverse
    if num == rev:
        return 1
    else:
        return 0
    

print(isDigitSumPalindrome(56))
