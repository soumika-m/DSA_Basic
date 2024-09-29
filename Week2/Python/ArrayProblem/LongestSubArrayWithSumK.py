"""
    Given an array arr containing n integers and an integer k. Your task is to find the length of the longest Sub-Array 
    with the sum of the elements equal to the given value k.

    https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1
"""


"""Time limit issue"""
def lenOfLongSubarr(arr, n, k) : 
    """ T(c) -> O(n^2), S(c) -> O(1) """

    max_len = 0
    
    for i in range(n):
        total = 0
        
        for j in range(i, n):
            total += arr[j]
            
            # if subarray sum is equal to k, check if that is maxlen
            if total == k:
                max_len = max(max_len, j-i+1)

    return max_len



def lenOfLongSubarrEfficeint(arr, n, k) : 
    """ T(c) -> O(n), S(c) -> O(n) """

    # it stores commulative sum and it's index
    prefix_map = {}
    max_len = 0
    current_sum = 0
    
    for i in range(n):
        current_sum += arr[i]
        
        # if subarray sum is equal to k
        if current_sum == k:
            max_len = i+1
        
        # calculate prefix sum
        prefix_sum = current_sum - k
        
        # if prefix sum exist
        if prefix_sum in prefix_map:
            curr_len = i - prefix_map[prefix_sum]
            max_len = max(max_len, curr_len)
        
        # if current sum not exist in map, add it
        if current_sum not in prefix_map:
            prefix_map[current_sum] = i

    return max_len



n = 6
arr = [10, 5, 2, 7, 1, 9]
k = 15
print(lenOfLongSubarr(arr, n,  k))

print(lenOfLongSubarrEfficeint(arr, n, k))
