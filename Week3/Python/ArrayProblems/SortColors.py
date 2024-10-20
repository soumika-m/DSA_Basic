"""
    Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color 
    are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the 
    color red, white, and blue, respectively. You must solve this problem without using the library's sort function.

    https://leetcode.com/problems/sort-colors/
"""


def sortColors(nums):
    """ T(c) -> O(n), S(c) -> O(1) """

    # using dutch national flag problem
    low = 0
    mid = 0
    high = len(nums)-1

    while mid <= high:
        # if number is 0, swap it with low, increase low and mid
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
            
        # if number is 1, do nothing, increase mid
        elif nums[mid] == 1:
            mid += 1
        
        # if number is 2, swap it with high, decrease high
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


arr = [2,0,2,1,1,0]
print(arr)
sortColors(arr)
print(arr)
