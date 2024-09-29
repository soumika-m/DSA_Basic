"""
    Given a binary array nums, return the maximum number of consecutive 1's in the array.

    https://leetcode.com/problems/max-consecutive-ones/
"""

def findMaxConsecutiveOnes(nums):
    """ T(c) -> O(n) , S(c) -> O(1) """

    max_count = 0
    count = 0
    
    # using sliding window approach
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            # if 0 occured, check if that point contains max consecutive 1s
            if count > max_count:
                max_count = count
            count = 0
    
    # incase max consecutive ones are at the end
    if count > max_count:
        max_count = count
    
    return max_count


arr = [1,0,1,1,0,1]
print(findMaxConsecutiveOnes(arr))
