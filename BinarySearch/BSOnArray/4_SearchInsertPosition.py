"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

https://leetcode.com/problems/search-insert-position/description/
"""

from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    """ T(C) -> O(logn), S(C) -> O(1) """

    n = len(nums)
    low = 0
    high = n-1
    ans = n

    # using lower bound condition smallest int arr[ind] >= target
    while low <= high:
        mid = (low + high) // 2
        # maybe answer
        if nums[mid] >= target:
            ans = mid
            # check more smaller value on left
            high = mid - 1

        # check on right part
        else:
            low = mid + 1

    return ans


if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 5
    print(nums, target)
    print(searchInsert(nums, target))
