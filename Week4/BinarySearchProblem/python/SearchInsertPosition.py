"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return 
the index where it would be if it were inserted in order.

Input: nums = [1,3,5,6], target = 2
Output: 1

https://leetcode.com/problems/search-insert-position/description/
"""

from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    """ T(c) -> O(logn), S(c) -> O(1) """
    low = 0
    high = len(nums)-1
    ans = len(nums)
    # using lower bound method to find which index can contain the search element 
    while low <= high:
        mid = (low+high) // 2
        # first occurance (smallest index num >= target)
        if nums[mid] >= target:
            ans = mid
            # go to left side
            high = mid-1
        else:
            # go to right side
            low = mid+1

    return ans


nums = [1,3,5,6]
target = 2
print(nums)
print(target , " -> ", searchInsert(nums, target))
