"""
    Given an integer array nums, return the number of reverse pairs in the array.
    A reverse pair is a pair (i, j) where:
    0 <= i < j < nums.length and nums[i] > 2 * nums[j]

    https://leetcode.com/problems/reverse-pairs/
"""


def reversePairs(nums):
    """ T(c) -> O(n^2), S(c) -> O(1) """
    count = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > 2 * nums[j]:
                count += 1
                
    return count


def reversePairsEfficient(nums):
    """ T(c) -> O(nlogn), S(c) -> O(n) """

    # using merge sort
    return mergeSort(nums, 0, len(nums)-1)
    
def mergeSort(nums, low, high):
    count = 0
    
    if low < high:
        mid = (low+high) // 2
        count += mergeSort(nums, low, mid)
        count += mergeSort(nums, mid+1, high)
        count += countReversePairs(nums, low, mid, high)
        merge(nums, low, mid, high)
    
    return count

def countReversePairs(nums, low, mid, high):
    cnt = 0
    j = mid+1
    
    for i in range(low, mid+1):
        # check second part element with first part element
        while j <= high and nums[i] > 2* nums[j]:
            j += 1
    
        cnt += j - (mid+1)
    
    return cnt
        
def merge(nums, low, mid, high):
    l = low
    r = mid+1
    k = 0
    B = [0] * (high-low+1)        
    
    while l <= mid and r <= high:
        if nums[l] <= nums[r]:
            B[k] = nums[l]
            l += 1
        else:
            B[k] = nums[r]
            r += 1
        k += 1
    
    # elements present in left part
    while l <= mid:
        B[k] = nums[l]
        k += 1
        l += 1
    
    # elements present in right part
    while r <= high:
        B[k] = nums[r]
        k += 1
        r += 1
        
    # shift elements from B array to original array
    for i in range(len(B)):
        nums[i+low] = B[i]


arr = [1,3,2,3,1]
print(arr)
# The reverse pairs are:
# (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
print(reversePairs(arr))

arr = [2,4,3,5,1]
print(arr)
print(reversePairs(arr))
