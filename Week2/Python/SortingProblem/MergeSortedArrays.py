"""
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing 
    the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in 
    non-decreasing order. The final sorted array should not be returned by the function, but instead be stored inside the 
    array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that 
    should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

    https://leetcode.com/problems/merge-sorted-array/
"""

def merge(nums1, m, nums2, n):
    """ T(c) -> O(m + n), S(c) -> O(m + n) """
    result = []
    i = 0
    j = 0
    
    # compare and merge
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    
    # remaining elements of first array
    while i < m:
        result.append(nums1[i])
        i += 1

    # remaining elements of second array
    while j < n:
        result.append(nums2[j])
        j += 1
        
    # shift elements from result array to nums1
    for k in range(len(result)):
        nums1[k] = result[k]


def mergeInplace(nums1, m, nums2, n):
    """ T(c) -> O(m + n), S(c) -> O(1) """
    i = m-1
    j = n-1
    k = m+n-1
    
    # compare elements from last to first
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
        
    # remaining elements of array2, copy them to array1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
        


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(nums1, nums2)
merge(nums1, m, nums2, n)
print(nums1)

print("--------------------------------")

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(nums1, nums2)
mergeInplace(nums1, m, nums2, n)
print(nums1)
