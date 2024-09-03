"""
Given two numbers as strings s1 and s2. Calculate their Product.

Note: The numbers can be negative and You are not allowed to use any built-in function or convert the 
strings to integers. There can be zeros in the begining of the numbers. You don't need to specify '+' sign 
in the begining of positive numbers.

https://www.geeksforgeeks.org/problems/multiply-two-strings/1
"""

def multiplyStrings(s1,s2):
    """ T(c) -> O(n1 * n2) , S(c) -> O(n1 + n2) """
    # return the product string
    
    isNeg = False
    
    # if s1 is negative
    if s1[0] == '-':
        isNeg = not isNeg
        # remove negative symbol
        s1 = s1[1:]
    # if s2 is negative
    if s2[0] == '-':
        isNeg = not isNeg
        #remove negative symbol
        s2 = s2[1:]
        
    result = [0] * (len(s1) + len(s2))
    
    for i in range(len(s1)-1, -1, -1):
        for j in range(len(s2)-1, -1, -1):
            # ord will convert character into ascii value
            digit1 = ord(s1[i]) - ord('0')
            digit2 = ord(s2[j]) - ord('0')
            
            product = digit1 * digit2
            _sum = product + result[i+j+1]
            
            # carry handling
            result[i+j] += _sum // 10
            # placing mutiplication digit in correct position
            result[i+j+1] = _sum % 10
    
    final_result = []
    
    # removing extra zeros present at the beginning
    for d in result:
        if not(len(final_result) == 0 and d == 0):
            final_result.append(str(d))
    
    # adding negative symbol if required
    if isNeg and len(final_result) != 0:
        final_result.insert(0, '-')
    
    return "".join(final_result) if final_result else "0"


s1 = "11"
s2 = "23"
print(multiplyStrings(s1, s2))
