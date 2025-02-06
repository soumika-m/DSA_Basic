"""
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
"""

from typing import List


def check(nums: List[int]) -> bool:
    n = len(nums)
    breakpoint = -1

    # find where is rotating point / where order is changed
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            breakpoint = i+1
            break
    
    # if array is not rotated / no order change, then it is sorted
    if breakpoint == -1:
        return True
    
    # check if second part is sorted (first part we have already checked as sorted)
    return is_sorted(nums, breakpoint, n-1)


def is_sorted(nums, start, end):

    # check if order is fine from breakpoint index to first element
    for i in range(start, end+1):
        if nums[i] > nums[(i+1) % len(nums)]:
            return False

    return True
            