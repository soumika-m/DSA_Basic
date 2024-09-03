"""
Given a number N, the task is to find the largest prime factor of that number.

https://www.geeksforgeeks.org/problems/largest-prime-factor2601/1
"""

def largestPrimeFactor(N):
    """ T(c) -> O(sqrt(n)) , S(c) -> O(1) """
    i=2
    # for non prime number we will have atleast one factor <= sqrt(n)
    while i*i<=N:
        # even number will never be prime, discard mutiple of 2, then 3 and others
        if N%i == 0:
            N = N//i
        else:    
            i += 1
    return N


N  = 24
print(largestPrimeFactor(N))