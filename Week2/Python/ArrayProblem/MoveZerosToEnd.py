"""
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

    https://leetcode.com/problems/move-zeroes/
"""


def moveZeroes(nums):
    """ T(c) -> O(n) , S(c) -> O(1) """

    # using 2 pointer approach
    # i will keep track of non zero places
    i = 0
    j = 0
    
    # j will iterate the array
    while j < len(nums):
        
        # if number is not zero, move it to starting nonzero place, make that number to zero
        if nums[i] == 0 and nums[j] != 0:
            nums[i] = nums[j]
            nums[j] = 0
            i += 1
            j += 1
        
        # if both i and j contains 0, check for next element in the array
        elif nums[i] == 0 and nums[j] == 0:
            j += 1
        
        # if i and j contains nonzero, or i contains nonzero and j contains 0, skip
        else:
            i += 1
            j += 1


arr = [0,1,0,3,12]
moveZeroes(arr)
print(arr)

arr = [0]
moveZeroes(arr)
print(arr)

arr = [1,0]
moveZeroes(arr)
print(arr)

arr = [1]
moveZeroes(arr)
print(arr)
