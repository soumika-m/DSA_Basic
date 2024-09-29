"""
Print numbers from 1 to n without the help of loops. You only need to complete the function printNos() that takes N as 
parameter and prints number from 1 to N recursively.

https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1
"""

def printNos(N):
    """ T(c) -> O(n), S(c) -> O(n) """
    # base case
    if N < 1:
        return
    
    printNos(N-1)
    
    print(N, end=" ")


N = 5
printNos(N)