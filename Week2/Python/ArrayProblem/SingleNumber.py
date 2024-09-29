"""
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space.

    https://leetcode.com/problems/single-number/
"""

def singleNumber(nums):
    """ T(c) -> O(n) , S(c) -> O(1) """
    xor = nums[0]
    # doing xor with same numbers will give 0, so unique number will be in xor variable
    for i in range(1, len(nums)):
        xor = xor ^ nums[i]
        
    return xor


arr = [4,1,2,1,2]
print(singleNumber(arr))
