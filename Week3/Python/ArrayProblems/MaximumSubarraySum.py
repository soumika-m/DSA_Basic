"""
    Given an integer array nums, find the subarray with the largest sum, and return its sum.
    https://leetcode.com/problems/maximum-subarray/
"""

def maxSubArray(nums):
    """ T(c) -> O(n^2), S(c) -> O(1) """
    largest_sum = nums[0]
    # create subarray sum
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            largest_sum = max(largest_sum, total)
            
    return largest_sum


def maxSubArrayEfficient(nums):
    """ T(c) -> O(n), S(c) -> O(1) """
    # using kadane's algo
    max_sum = nums[0]
    total = 0

    # create subarray sum
    for i in range(len(nums)):
        total += nums[i]
        
        # if total is greater than max_sum, assign that to max_sum
        if total > max_sum:
            max_sum = total

        # if sum is negative, don't carry that, to make it max sum
        if total < 0:
            total = 0

    return max_sum


arr = [-2,1,-3,4,-1,2,1,-5,4]
# The subarray [4,-1,2,1] has the largest sum 6.
print(arr)
print(maxSubArray(arr))
print(maxSubArrayEfficient(arr))
