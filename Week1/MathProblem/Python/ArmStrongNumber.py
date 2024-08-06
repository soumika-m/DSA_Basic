"""
    For a given 3 digit number, find whether it is armstrong number or not. 
    An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the 
    number itself. Return "Yes" if it is a armstrong number else return "No".

    https://practice.geeksforgeeks.org/problems/armstrong-numbers2727/1
"""


def armstrongNumber (n):
    """ T(c) -> O(1) // as n will be always 3 digit number (constant)
        if n is not constant (variable in nature), T(c) -> O(logn)
    """
    num = n
    cube_sum = 0
    while num > 0:
        digit = num % 10
        cube_sum += (digit * digit * digit)
        num = num // 10

    if cube_sum == n:
        return "true"
    else:
        return "false"
    

N = 153
print("Armstrong Number?", N , "=", armstrongNumber(N))
