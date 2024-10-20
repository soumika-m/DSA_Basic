"""
    Given an array of positive numbers, the task is to find the number of possible contiguous subarrays having product 
    less than a given number k.

    https://www.geeksforgeeks.org/problems/count-the-subarrays-having-product-less-than-k1708/1
"""


"""TLE"""
def countSubArrayProductLessThanK(a, n, k):
    """ T(c) -> O(n^2), S(c) -> O(1) """

    # Number of possible subarray
    count = 0
    
    for i in range(n):
        product = 1
        
        for j in range(i, n):
            product *= a[j]
            
            if product < k:
                count += 1
            
            # if product >= k, break loop, as it will increase product further
            else:
                break
    
    return count


def countSubArrayProductLessThanKEfficient(a, n, k):
    """ T(c) -> O(n), S(c) -> O(1) """

    # Number of possible subarray
    count = 0
    product = 1
    
    # using sliding window (2 pointer)
    left = 0
    right = 0
    
    while right < n:
        product *= a[right]
        
        # discard elements from left, to maintain product < k
        while product >= k and left < right:
            product = product // a[left]
            left += 1
        
        # calculate count
        if product < k:
            count += (right-left+1)
        
        right += 1
        
    return count


arr = [1, 2, 3, 4]
k = 10
print(arr)
print(countSubArrayProductLessThanK(arr, len(arr), k))
print(countSubArrayProductLessThanKEfficient(arr, len(arr), k))
