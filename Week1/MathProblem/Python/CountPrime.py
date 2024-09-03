"""
Given an integer n, return the number of prime numbers that are strictly less than n.

https://leetcode.com/problems/count-primes/
"""

def countPrimes(n):
    """ T(c) -> O(n * log(logn)) , S(c) -> O(n) """
    if n<=1:
        return 0
    
    # using sieve of eratosthenes algo
    prime = [True] * (n+1)
    prime[0] = False
    prime[1] = False
    
    i = 2
    while i*i <= n:
        # if number is prime
        if prime[i]:
            # mark multiple of prime(i) as nonprime
            j = i*i
            while j <= n:
                prime[j] = False
                j += i

        i += 1
    
    prime_count = 0
    for p in range(2, len(prime)-1):
        # if prime, count that
        if prime[p]:
            prime_count += 1
        
    return prime_count


n = 10
# There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
print(countPrimes(n))
