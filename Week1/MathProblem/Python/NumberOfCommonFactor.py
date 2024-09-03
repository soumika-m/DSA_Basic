"""
Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.

https://leetcode.com/problems/number-of-common-factors/
"""

def commonFactors(a, b):
    """ T(c) -> O(min(a,b)), S(c) -> O(1) """
    
    # maximum common factor is minimum of both number
    num = min(a,b)
    
    count = 0
    
    for i in range(1, num+1):
        # counting common factor
        if a%i == 0 and b%i == 0:
            count += 1
    
    return count


# The common factors of 12 and 6 are 1, 2, 3, 6.
print(commonFactors(12,6))
