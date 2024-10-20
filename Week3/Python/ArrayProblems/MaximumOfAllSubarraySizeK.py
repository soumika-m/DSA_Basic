"""
    Given an array arr[] and an integer k. Find the maximum for each and every contiguous subarray of size k.

    https://www.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1
"""

"""TLE"""
def max_of_subarrays(k,arr):
    """ T(c) -> O((n-k+1)*k) => O(n*k), S(c) -> O(n-k+1) => O(n)"""
    n = len(arr)
    subarray_max = []
    
    # using sliding window (2 pointer)
    left = 0
    right = left+k-1
    
    # go through the array elements
    while right < n:
        i = left
        max_elem = 0
        
        # cover window size of k, subarray of size k
        while i <= right:
            # find max element in the subarray
            max_elem = max(max_elem, arr[i])
            i += 1
            
        # max element in that subarray  
        subarray_max.append(max_elem)
        
        # check for next window
        left += 1
        right += 1

    return subarray_max


arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3
print(arr, k)
print(max_of_subarrays(k, arr))

arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
k = 4
print(arr, k)
print(max_of_subarrays(k, arr))