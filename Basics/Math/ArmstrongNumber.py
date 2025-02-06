"""
https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1
"""

def armstrongNumber(n):
    """ T(c) -> O(log10N + 1), S(c) -> O(1)"""
    k = len(str(n))
    num = n
    total = 0
    while n > 0:
        ld = n % 10
        total += (ld ** k)
        n = n // 10
        
    if num == total:
        return True
    else:
        return False