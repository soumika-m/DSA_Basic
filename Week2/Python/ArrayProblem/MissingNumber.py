"""
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range 
    that is missing from the array.

    https://leetcode.com/problems/missing-number/
"""


def missingNumber(nums):
    """ T(c) -> O(n) , S(c) -> O(1) """
    n = len(nums)
    current_total = 0
        # total will contain sum of numbers range from 0 to n
    total = (n * (n + 1)) / 2
    
    for i in range(len(nums)):
        # current_total will contain sum of all numbers inside nums array
        current_total += nums[i]
    
    missing_num = total - current_total
    
    return missing_num


arr = [9,6,4,2,3,5,7,0,1]
print(missingNumber(arr))
