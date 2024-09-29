"""
    Print numbers from N to 1 (space separated) without the help of loops.

    https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/1
"""

def printNos(n):
    """ T(c) -> O(n), S(c) -> O(n) """
    # base case
    if n < 1:
        return
    
    print(n, end=" ")
    
    printNos(n-1)


N = 10
printNos(N)
