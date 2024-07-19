"""
For a given number N check if it is prime or not. A prime number is a number which is only divisible by 1 and itself.
https://www.geeksforgeeks.org/problems/prime-number2314/1
"""

def isPrime (N):
    """ T(c) ->O(sqrt(n)) """
    # edge case
    if N <= 1:
        return 0
        
    # finding if number is prime    
    i = 2
    # if not prime, it will be have atleast one factor <= sqrt(n)
    while i*i <= N:
        if N % i == 0:
            return 0
        i += 1
    return 1


N = 5
print("Is Prime =",isPrime(N))