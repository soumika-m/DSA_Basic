"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

from typing import List


def removeDuplicates(nums):
    """T(c) -> O(nlogn) + O(n), S(c) -> O(n)"""

    # add elements in set after sorting
    unique_set = sorted(set(nums))

    k = len(unique_set)

    # take from set and add it to array from starting
    for j in range(k):
        nums[j] = unique_set[j]

    # return number of unique elements
    return k


def removeDuplicatesOptimal(nums: List[int]) -> int:
    """T(c) -> O(n), S(c) -> O(1)"""

    # using 2 pointer approach
    i = 0
    j = 1
    while j < len(nums):

        # element is different, place it in correct place
        if nums[i] != nums[j]:
            nums[i+1] = nums[j]
            i += 1
            j += 1
        else:
            j += 1

    return i+1


arr = [0,0,1,1,1,2,2,3,3,4]
print(arr)
print(removeDuplicates(arr))
print(arr)
print("=====================")
arr = [1,1,2]
print(arr)
print(removeDuplicatesOptimal(arr))
print(arr)
