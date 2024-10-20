"""
    You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative 
    integers.
    You should return the array of nums such that the the array follows the given conditions:
    Every consecutive pair of integers have opposite signs.
    For all integers with the same sign, the order in which they were present in nums is preserved.
    The rearranged array begins with a positive integer.

    Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

    https://leetcode.com/problems/rearrange-array-elements-by-sign/
"""

def rearrangeArray(nums):
    """ T(c) -> O(n), S(c) -> O(n) """
    # add positive elements in positive array
    positive = []
    # add negative elements in negative array
    negative = []
    
    for i in range(len(nums)):
        # positive
        if nums[i] >= 0:
            positive.append(nums[i])
        # negative
        else:
            negative.append(nums[i])       

    # rearrange nums array by sign
    for j in range(len(nums)//2):
        nums[2*j] = positive[j]
        nums[2*j+1] = negative[j]
        
    return nums


def rearrangeArray2(nums):
    """ T(c) -> O(n), S(c) -> O(n) """

    res = [-1] * len(nums)
    
    # positive element will be in even index, and negative will be in odd index
    posIndex = 0
    negIndex = 1
    
    # using 2 pointers
    for i in range(len(nums)):
        if nums[i] >= 0:
            res[posIndex] = nums[i]
            posIndex += 2
        else:
            res[negIndex] = nums[i]
            negIndex += 2
            
    return res


arr = [-4,1,-2,-5,2,3]
print(rearrangeArray(arr))

arr = [-4,1,-2,-5,2,3]
print(rearrangeArray2(arr))
