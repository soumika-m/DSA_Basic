"""
    Sum of all prime numbers between 1 and N.

    https://www.geeksforgeeks.org/problems/sum-of-all-prime-numbers-between-1-and-n4404/1
"""

""" giving time limit error """
def prime_Sum(n):
    """ T(c) -> O(n * sqrt(n)), S(c) -> O(1) """
    # Code here
    total = 0
    # 1 is not prime
    i = 2
    # finding prime number between 2 to n
    while i<=n:
        if isPrime(i):
            total += i
        i += 1

    return total
            
def isPrime(num):
    j = 2
    while j*j<=num:
        if num % j == 0:
            return False
        j += 1
    
    return True


""" using sieve of eratosthenes algo """ 
def prime_Sum_Efficient(n):
    """ T(c) -> O(n * log(logn)), S(c) -> O(n) """
    if n<=1:
        return 0

    # initialize the prime boolean array (all as prime, true)
    prime = [True] * (n+1)
    # 0 and 1 are nonprime
    prime[0] = False
    prime[1] = False
    
    # if number is prime, make all multiple of that number to non prime, false
    i = 2
    # go till sqrt(n)
    while i*i<=n:
        if prime[i]:
            j = i*i
            while j<=n:
                prime[j] = False
                j += i
        i += 1
        
    
    # get all prime number and sum it up
    sum = 0
    for p in range(2, n+1):
        if prime[p]:
            sum += p

    return sum


print(prime_Sum(5))
print(prime_Sum_Efficient(303))