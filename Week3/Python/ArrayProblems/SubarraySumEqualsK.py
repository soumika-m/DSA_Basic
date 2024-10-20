"""
"""

"""TLE"""
def subarraySum(nums, k):
    """ T(c) -> O(n^2), S(c) -> O(1) """
    num_of_subarrays = 0
    n = len(nums)
    
    # generate every subarray
    for i in range(n):
        total = 0
        
        # check for each subarray
        for j in range(i, n):
            total += nums[j]

            # if total is k, count that subarray
            if total == k:
                num_of_subarrays += 1
                
    return num_of_subarrays



def subarraySumEfficient(nums, k):
    """ T(c) -> O(n), S(c) -> O(n)"""

    # using prefix sum and storing sum frequencies
    total = 0
    cnt = 0
    
    # for holding prefix sum and it's count
    prefix_sum_cnt = {}
    # initially add 0 and count as 1
    prefix_sum_cnt[0] = 1
    
    for i in range(len(nums)):
        total += nums[i]
        
        # calculate prefix sum (x-k, removing which we will get subarray of sum k) [sum(i,j)=sum(0,j)-sum(0,i)]
        prefix_remove = total - k
        
        # if prefix sum found, add that count
        cnt += prefix_sum_cnt.get(prefix_remove, 0)
        
        # add total sum and cnt in dictionary
        prefix_sum_cnt[total] = prefix_sum_cnt.get(total, 0) + 1
                
    return cnt


arr = [1,2,3]
k = 3
print(arr, k)
print(subarraySum(arr, k))
arr = [-1,1,0]
k = 0
print(arr, k)
print(subarraySumEfficient(arr, k))
