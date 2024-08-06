"""
    count perfect square -> You are given a number N, you have to count the number of perfect squares less than N
    https://www.geeksforgeeks.org/problems/count-squares3649/155
"""

import math

def countSquares(N):
    """ T(c) -> O(sqrt(n)) , S(c) -> O(1) """
    # count = 0
    # i = 1
    # # check till sqrt(n), all are perfect square
    # while i*i < N:
    #     count += 1
    #     i += 1

    # return count
    
    return int(math.sqrt(N-1))


N = 9
print("Number of perfect square less than N =", countSquares(N))