"""
    You are given an integer n, return the fibonacci series till the nth(0-based indexing) term. Since the terms can 
    become very large return the terms modulo 109+7.

    https://www.geeksforgeeks.org/problems/fibonacci-series-up-to-nth-term/1
"""

def series(n):
    """ T(c) -> O(n), S(c) -> O(n) """
    
    if n == 0:
        return [0]
    
    if n == 1:
        return [0,1]
    
    fib_series = []

    fib_series.append(0)
    fib_series.append(1)
    
    for i in range(2, n+1):
        fib = (fib_series[i-1] + fib_series[i-2]) % (10**9 + 7)
        fib_series.append(fib)
        
    return fib_series


""" Using recursion -> TLE for large n """
def seriesRecursive(n):
    """ T(c) -> O(2^n), S(c) -> O(n) """
    fib_series = []
    
    for i in range(n+1):    
        fib_series.append(fibonacci(i))
        
    return fib_series

def fibonacci(n):
    # base case
    if n == 0:
        return 0

    if n == 1:
        return 1
        
    return (fibonacci(n-1) + fibonacci(n-2)) % (10**9 + 7)



N = 5
print(series(N))

print(seriesRecursive(N))
