"""
    Given two integers a and b, write a function lcmAndGcd() to compute their LCM and GCD. The function takes two integers a and 
    b as input and returns a list containing their LCM and GCD.

    https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1
"""

def lcmAndGcd(A , B):
    """ T(c) -> O(log(min(a,b))) , S(c) -> O(1) """
    divisor = min(A, B)
    divident = max(A, B)
    
    # using euclidean algorithm or division method to find GCD
    while divident % divisor != 0:
        remainder = divident % divisor
        divident = divisor
        divisor = remainder
        
    gcd = divisor
    
    # using GCD(A,B) * LCM(A,B) = A*B for calculating LCM
    lcm = (A * B) // gcd
    
    return lcm, gcd


arr = lcmAndGcd(14, 8)
print(f"LCM = {arr[0]} and GCD = {arr[1]}")