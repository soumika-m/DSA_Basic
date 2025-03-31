"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

https://leetcode.com/problems/subarray-sum-equals-k/description/
"""

def subarraySum(nums, k):
    """ T(C) -> O(N^2), S(C) -> O(1) """

    count = 0

    # genarate all subarray
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]

            # if sum of k found
            if total == k:
                count += 1

    return count


def subarraySumOptimal(nums, k):
    """ T(C) -> O(N), S(C) -> O(N) """

    # using prefix sum and hashmap approach
    count = 0
    total = 0

    # for holding prefix sum and it's count
    prefixSumMap = {}

    # initially add 0 with count 1 (incase we are getting k, x-k should be zero which will be present in map)
    prefixSumMap[0] = 1

    for i in range(len(nums)):
        total += nums[i]

        # calculate prefix sum (x-k, removing which we will get subarray of sum k) [sum(i,j)=sum(0,j)-sum(0,i)]
        rem = total - k

        # if prefix sum found in map, add that count
        if rem in prefixSumMap:
            count += prefixSumMap.get(rem)

        # add sum and count in map
        prefixSumMap[total] = prefixSumMap.get(total, 0) + 1

    return count


if __name__ == "__main__":
    arr = [1,2,3,-3,1,1,1,4,2,-3]
    k = 3
    print(subarraySum(arr, k))
    print(subarraySumOptimal(arr, k))
 