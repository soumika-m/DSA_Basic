"""
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, 
divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
"""

import math
from typing import List


def smallestDivisor(nums, threshold):
    """ T(C) -> O(max * n), S(C) -> O(1) """

    # divisor range
    for divisor in range(1, max(nums)+1):
        total = 0

        # iterate array and find sum using divisor
        for i in range(len(nums)):
            total += math.ceil(nums[i]/divisor)

        if total <= threshold:
            return divisor
    
    return -1


def smallestDivisorOptimal(nums: List[int], threshold: int) -> int:
        """ T(C) -> O(log(max) * n), S(c) -> o(1) """

        # if minimum sum is greater than threshold, it is not possible
        if len(nums) > threshold:
            return -1

        # using binary search on answers
        ans = -1
        low = 1
        high = max(nums)

        while low <= high:
            mid = (low + high) // 2

            # find sum by divisor
            total = 0
            for i in range(len(nums)):
                total += math.ceil(nums[i]/mid)

            # if answer found, check for more smaller number in left side
            if total <= threshold:
                ans = mid
                high = mid - 1
            else:
                # if answer is greater, check for larger number in the right side
                low = mid + 1
        
        return ans


if __name__ == "__main__":
    nums = [1,2,5,9]
    threshold = 6
    print(smallestDivisor(nums, threshold))
    nums = [44,22,33,11,1]
    threshold = 5
    print(smallestDivisorOptimal(nums, threshold))
