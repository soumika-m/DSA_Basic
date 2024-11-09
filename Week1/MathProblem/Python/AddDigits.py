"""
    Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
    
    https://leetcode.com/problems/add-digits/
"""

def addDigits(num):
    """ T(c) -> O(log(n)^2), space -> O(1) """
    # untill number becomes 1 digit number
    while num > 9:
        total = 0
        
        # add all digits
        while num > 0:
            digit = num % 10
            total += digit
            num //= 10
        
        num = total

    return num


def addDigitsEfficient(num):
    """ T(c) -> O(1), S(c) -> O(1) """
    # using digital root formula
    if num == 0:
        return 0
    else:
        return 1 + (num - 1) % 9


N = 38
print("N =" , N, "->", addDigits(N))
print("N =" , N, "->", addDigitsEfficient(N))
