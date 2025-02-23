"""
contains positive number
"""

def longestSubarrayWithSumK(nums, k):
    """ T(c) -> O(N^2), S(c) -> O(1)"""

    n = len(nums)
    max_len = 0

    # generate subarray
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            # calculate sum of each element in subarray
            current_sum += nums[j]
            # check for max length
            if current_sum == k:
                max_len = max(max_len, j-i+1)

    return max_len


def longestSubarrayWithSumKBetter(nums, k):
    """ T(C) -> O(N), S(C) -> O(N) """

    n = len(nums)

    # using hashing with prefix sum
    pre_sum_map = {}

    prefix_sum = 0
    max_len = 0

    for i in range(n):

        prefix_sum += nums[i]
        # if sum if equal to k, update maxlen
        if prefix_sum == k:
            # length of that subarray
            max_len = max(max_len, i+1)
        
        # check if x-k is present in map, then k is present in that subarray
        remaining = prefix_sum - k

        if remaining in pre_sum_map:
            map_idx = pre_sum_map.get(remaining)
            length = i - map_idx

            # calculate max length
            max_len = max(max_len, length)

        # adding sum and index in map
        # incase of zero, check if that sum if present or not in map, if not present, then only add that in map
        if prefix_sum not in pre_sum_map:
            pre_sum_map[prefix_sum] = i

    return max_len


def longestSubarrayWithSumKOptimal(nums, k):
    """ T(C) -> O(2N), S(C) -> O(1) """

    n = len(nums)
    # using 2 pointer
    left = 0
    right = 0

    max_len = 0
    # sum will contain first element at first
    sum = nums[0]

    # iterate through the array
    while right < n:
        # if subarray exist, discard left element from sum. if sum > k
        while left <= right and sum > k:
            sum -= nums[left]
            left += 1

        # check for maximum length
        if sum == k:
            max_len = max(max_len, right-left+1)

        # move right pointer
        right += 1
        # edge case after last element
        if right < n:
            sum += nums[right]

    return max_len


if __name__ == "__main__":
    arr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
    k = 3
    print(arr, k)
    print(longestSubarrayWithSumK(arr, k))
    arr = [10, 5, 2, 7, 1, -10]
    print(longestSubarrayWithSumKBetter(arr, k=15))
    arr = [2, 0, 0, 3]
    print(longestSubarrayWithSumKOptimal(arr, k))