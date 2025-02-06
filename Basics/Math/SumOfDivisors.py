"""
https://www.geeksforgeeks.org/problems/sum-of-all-divisors-from-1-to-n4738/1
"""

import math

""" TLE """
def sumOfDivisors(n):
    """ T(c) -> O(n*sqrt(n)), S(c) -> O(sqrt(n)) """

    list_of_sum = []

    for i in range(1, n+1):

        total = 0

        # go till sqrt(n) 
        for j in range(1, int(math.sqrt(i))+1):

            # if divisor found
            if i % j == 0:
                total += j
                
                # if not same number eg. 6 * 6
                if j != i//j:
                    total += i//j

        list_of_sum.append(total)

    return sum(list_of_sum)


def sumOfDivisorsOptimal(n):
    """ T(c) -> O(n), S(c) -> O(1) """

    sum = 0
    # ans = (1 x (N/1)) + (2 x (N/2)) + (3x(N/3)) + ... + (Nx(N/N)) 
    for i in range(1, n+1):
        sum += (i * (n//i))

    return sum
