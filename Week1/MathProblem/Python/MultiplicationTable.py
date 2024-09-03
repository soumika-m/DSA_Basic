"""
    Create the multiplication table of a given number N and return the table as an array.
    https://www.geeksforgeeks.org/problems/print-table0303/1
"""

def getTable(N):
    """
        T(c) -> O(1), S(c) -> O(1)
    """
    res = []
    i = 1
    while i<=10:
        res.append(N*i)
        i += 1
    
    return res

print(getTable(9))