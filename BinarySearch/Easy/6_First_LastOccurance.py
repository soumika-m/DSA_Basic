"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""

from typing import List


def find_first_last_occurance(nums: List[int], target: int) -> List[int]:
    """ T(C) -> O(n), S(C) -> O(1) """

    first = -1
    last = -1

    # iterate through array, find first and last occurance index
    for i in range(len(nums)):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i

    return [first, last]


def lowerbound(nums, target):

    # if number not found, lower bound will be length of the array
    ind = len(nums)

    # smallest index such that arr[mid] >= x
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            ind = mid
            # check for more smallest index of that target
            high = mid - 1
        else:
            # if element is smaller that target, check right part
            low = mid + 1

    return ind

def upperbound(nums, target):

    # if number not found, upper bound will be length of the array
    ind = len(nums)

    # smallest index such that arr[mid] > x
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ind = mid
            # check for more smallest index of that target
            high = mid - 1
        else:
            # if element is smaller that target, check right part
            low = mid + 1

    # if element not present in array
    if nums[ind-1] != target:
        return -1
    
    return ind

def find_first_last_occurance_better1(nums, target):
    """ T(C) -> O(2logn), S(C) -> O(1) """

    # first occurance is lowerbound of that number
    first = lowerbound(nums, target)

    # last occurence is upperbound index of that number - 1
    last = upperbound(nums, target)

    # if element not found, return -1
    if last == -1:
        return [-1, -1]

    return [first, last - 1]


def first_occurance(nums, target):

    first = -1
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            first = mid
            # check for smaller index
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        ## if nums[mid] > target
        else:
            high = mid - 1
    
    return first

def last_occurance(nums, target):

    last = -1
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            last = mid
            # check for larger
            low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        ## if nums[mid] > target
        else:
            high = mid - 1
    
    return last

def find_first_last_occurance_better2(nums, target):
    """ T(C) -> O(2logn), S(C) -> O(1) """

    # first occurance
    first = first_occurance(nums, target)

    # last occurence
    last = last_occurance(nums, target)

    return [first, last]


def count_occurance(nums, target):
    """ T(C) -> O(2logn), S(C) -> O(1) """

    first = first_occurance(nums, target)
    last = last_occurance(nums, target)

    if first == -1:
        return 0
    
    return last - first + 1


if __name__ == "__main__":
    nums = [2,8,8,8,8,8,11,13]
    # nums = [5,7,7,8,8,10]
    target = 8
    # target = 6
    print(find_first_last_occurance(nums, target))
    print(find_first_last_occurance_better1(nums, target))
    print(find_first_last_occurance_better2(nums, target))
    print(count_occurance(nums, target))
