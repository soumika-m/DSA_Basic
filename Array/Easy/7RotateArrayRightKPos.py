"""
https://leetcode.com/problems/rotate-array/
"""

def rotate(nums, k):
    """ T(c) -> O(n+k), S(c) -> O(k) """

    n = len(nums)

    # multiple of n will result in same array
    k = k % n
    
    # create temp array of size k
    temp = [0] * k
    
    # copy last k elements in temp array
    for i in range(0, k):
        temp[i] = nums[n-k+i]

    # shift remaining elements n-k from starting by k poition to the right
    for i in range(n-k-1, -1, -1):
        nums[k+i] = nums[i]

    # copy elements from temp array to original from beginning
    for i in range(0, k):
        nums[i] = temp[i]


def rotateOptimal(nums, k):
    """ T(c) -> O(2n), S(c) -> O(1) """

    n = len(nums)
    
    # multiple of n will result in same array
    k = k % n
    
    # if k is 0, it will be the same array
    if k == 0:
        return
    
    # reverse entire array
    reverse_array_inplace(nums, 0, n-1)
    
    # reverse first part k elements
    reverse_array_inplace(nums, 0, k-1)
    
    # reverse last part n-k elements
    reverse_array_inplace(nums, k, n-1)    
    
def reverse_array_inplace(nums, start, end):
    while start <= end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

