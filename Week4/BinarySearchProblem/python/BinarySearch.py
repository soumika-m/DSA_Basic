"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search 
target in nums. If target exists, then return its index. Otherwise, return -1.

https://leetcode.com/problems/binary-search/description/
"""

from typing import List

def search(nums: List[int], target: int) -> int:
    """ T(c) -> O(logn), S(c) -> O(1) """

    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid+1
        elif nums[mid] > target:
            high = mid-1
        else:
            return mid
        
    return -1


nums = [-1,0,3,5,9,12]
target = 9
print(nums, target)
print(search(nums, target))
