"""
Given an array arr containing both positive and negative integers, the task is to compute the length of the largest subarray that has a sum of 0.

https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
"""

def longestSubarray(arr):
    """ T(C) -> O(n^2), S(C) -> O(1) """

    n = len(arr)
    maxlen = 0

    # generate all subarray and calculate max length
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            if total == 0:
                # calculate max length
                maxlen = max(maxlen, j-i+1)
    
    return maxlen


def longestSubarrayBetter(arr):
    """ T(C) -> O(n), S(C) -> O(n) """

    n = len(arr)
    maxlen = 0
    total = 0
    # store prefixsum and index
    hmap = {}

    for i in range(n):
        total += arr[i]
        # if zero sum found, calculate max length
        if total == 0:
            maxlen = i+1
        else:
            # if sum exist in hashmap, get index, calculate max len
            if total in hmap:
                idx = hmap.get(total)
                maxlen = max(maxlen, i-idx)
            else:
                # add element in hash map with index
                hmap[total] = i
    
    return maxlen


if __name__ == "__main__":
    arr = [15, -2, 2, -8, 1, 7, 10, 23]
    # The largest subarray with a sum of 0 is [-2, 2, -8, 1, 7].
    print(arr)
    print(longestSubarray(arr))
    print(longestSubarrayBetter(arr))


