"""
Given a positive integer n, return the nth row of pascal's triangle.
Pascal's triangle is a triangular array of the binomial coefficients formed by summing up the elements of previous row.
The elements can be large so return it modulo 10^9 + 7.

https://www.geeksforgeeks.org/problems/pascal-triangle0652/1?page=1
"""

def nthRowOfPascalTriangle(n):
    """ T(c) -> O(n^2) , S(c) -> O(n) """

    result = []
    
    MOD = 1000000007
    
    # row 0 will contains only one element 1
    result.append(1)
    
    for row in range(2, n+1):
        currentlist = []

        # 1st element will be 1
        currentlist.append(1)
        
        size = len(result)

        for col in range(size-1):
            total = (result[col] + result[col+1]) % MOD
            currentlist.append(total)
        
        # last element will be 1
        currentlist.append(1)
        
        result = currentlist
        
    return result



N  = 4
print(nthRowOfPascalTriangle(N))
