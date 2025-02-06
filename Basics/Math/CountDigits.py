"""
https://www.geeksforgeeks.org/problems/count-digits5716/1
"""

def evenlyDivides(n):
    """ T(c) -> O(log10n + 1), S(c) -> O(1) """
    count = 0
    num = n
    while n>0:
        digit = n % 10
        if digit > 0 and num % digit == 0:
            count += 1
        n = n // 10
        
    return count
