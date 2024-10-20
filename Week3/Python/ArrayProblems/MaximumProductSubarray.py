"""
    Given an integer array nums, find a subarray that has the largest product, and return the product.
    The test cases are generated so that the answer will fit in a 32-bit integer.

    https://leetcode.com/problems/maximum-product-subarray/
"""


"""TLE"""
def maxProduct(nums):
    """ T(c) -> O(n^2), S(c) -> O(1) """

    n = len(nums)
    # pre assigning smallest integer
    max_product = -11

    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= nums[j]
            if product > max_product:
                max_product = product

    return max_product


""" 
    * Using observation, array can contains either of these - 
    * all positives -> just multiply
    * even negatives, others positives -> just mutiply, as negative and negative will become positives
    * odd negatives, others positives -> discard one negative, will calculate prefix and suffix product
    * contains zeros -> calculate subarray product without including 0 as element 
"""
def maxProductEfficient(nums):
    """ T(c) -> O(n), S(c) -> O(1) """

    n = len(nums)
    # pre assigning smallest integer
    max_product = -11
    prefix = 1
    suffix = 1
    
    for i in range(n):
        # if prefix or suffix of number becomes zero, do not carry forward it
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
            
        # calculate prefix product from front of the array
        prefix *= nums[i]
        
        # calculate suffix product from back of the array
        suffix *= nums[n-1-i]
        
        # max product will be maximum of prefix or suffix
        max_product = max(max_product, max(prefix, suffix))

    return max_product


arr = [2,3,-2,4]
print(arr)
print(maxProduct(arr))
arr = [-2,0,-1]
print(arr)
print(maxProductEfficient(arr))
