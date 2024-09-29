"""
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    https://leetcode.com/problems/two-sum/
"""


def twoSum(nums, target):
    """ T(c) -> O(n^2), S(c) -> O(1) """

    n = len(nums)

    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return [i,j]
    
    return []


def twoSumEfficient(nums, target):
    """ T(c) -> O(n), S(c) -> O(n) """

    # key will contains number, and value wll contain index
    seen_map = {}

    for i, num in enumerate(nums):
        # find the another number
        another_num = target - num
        
        # if that number is present in dictionary, then return
        if another_num in seen_map:
            return [seen_map[another_num], i]
        
        # otherwise store that current number with index
        seen_map[num] = i
    
    return []


arr = [2,5,5,11]
target = 10
print(twoSum(arr, target))

arr = [2,7,11,15]
target = 9
print(twoSumEfficient(arr, target))
