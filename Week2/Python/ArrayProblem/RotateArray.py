"""
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

    https://leetcode.com/problems/rotate-array/
"""


def rotate(nums, k):
    """ T(c) -> O(n) , S(c) -> O(n) """

    temp = []
    n = len(nums)
    idx = n - (k % n)

    # move number from idx to n into temp array
    for i in range(idx, n):
        temp.append(nums[i])
    
    # move number from 0 to idx-1 into temp array
    for j in range(idx):
        temp.append(nums[j])
    
    # copy elements from temp array to original array
    for i in range(n):
        nums[i] = temp[i]


def rotateOptimal(nums, k):
    """ T(c) -> O(n) , S(c) -> O(1) """
    n = len(nums)
    pos = n - (k % n)

    # reverse first part till pos-1
    reverseArr(nums, 0, pos)
    
    # reverse last part from pos
    reverseArr(nums, pos, n)
    
    # reverse entire array
    reverseArr(nums, 0, n)

def reverseArr(nums, pos_from, pos_to):
    i = pos_from
    j = pos_to - 1
    
    while i<j:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i += 1
        j -= 1



arr = [1,2,3,4,5,6,7]
k = 10
print("original array = ", arr)
rotate(arr, k)
print("after reversal = ", arr)

arr = [-1,-100,3,99]
k = 2
print("original array = ", arr)
rotate(arr, k)
print("after reversal = ", arr)
