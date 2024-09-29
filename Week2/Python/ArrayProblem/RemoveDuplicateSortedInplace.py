"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element 
appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

def removeDuplicates(nums):
    """ T(c) => O(n) , S(c) -> O(1) """
    # using 2 pointer approach
    # track unique element
    i = 0
    # point to current element till end
    j = 1
    
    n = len(nums)
    
    while j<n:
        # if not duplicate, shift current element after ith place
        if nums[i] != nums[j]:
            nums[i+1] = nums[j]
            # check with next unique element
            i += 1
        
        # if duplicate element, bypass duplicate and check for next one
        j += 1
        
    return i+1


arr = [0,0,1,1,1,2,2,3,3,4]

for i in range(len(arr)):
    print(arr[i] , end = " ")

print()

n = removeDuplicates(arr)
for i in range(n):
    print(arr[i] , end = " ")
