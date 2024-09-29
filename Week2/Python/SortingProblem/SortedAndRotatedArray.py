"""
    Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number 
    of positions (including zero). Otherwise, return false. There may be duplicates in the original array.

    Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], 
    where % is the modulo operation.

    https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
"""


def check(nums):
    """ T(c) -> O(n), S(c) -> O(1) """
    changeIdx = -1
    # find where order is changed
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            changeIdx = i+1
            break
    
    # if no order changed, means array is sorted
    if changeIdx == -1:
        return True
    
    # check if order is fine from changeIndex till first element
    for i in range(changeIdx, len(nums)):
        if nums[i] > nums[(i+1) % len(nums)]:
            return False
        
    return True


arr = [3,4,5,1,2]
print(arr)
print(check(arr))
