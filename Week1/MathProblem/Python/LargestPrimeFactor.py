"""
Given a number N, the task is to find the largest prime factor of that number.

https://www.geeksforgeeks.org/problems/largest-prime-factor2601/1
"""


def largestPrimeFactor(N):
    """ T(c) -> O(sqrt(n)) , S(c) -> O(1) """
    largest_prime = -1
    i = 2
    # a prime factor of number can not be more than sqrt(n)
    while i*i <= N:
        # if number is divisible by i, keep track of that i (2,3,...), divide that number with the divisor to get a odd number.
        while N % i == 0:
            largest_prime = i
            N = N//i
        
        i += 1
    
    # if number is greater than 1, that is prime factor
    if N > 1:
        largest_prime = N
        
    return largest_prime


def largestPrimeFactor2(N):
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
N  = 5
print(largestPrimeFactor2(N))
