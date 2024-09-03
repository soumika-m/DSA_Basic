"""
Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

https://leetcode.com/problems/smallest-even-multiple/
"""

def smallestEvenMultiple(n):
    """ T(c) -> O(1), S(c) -> O(1) """

    # if even, that is the smallest multiple
    if n % 2 == 0:
        return n
    # if odd, next mutiple is even, which is smallest mutiple
    else:
        return n*2
    

n = 5
print("smallest even mutiple of", n, "->", smallestEvenMultiple(n))
