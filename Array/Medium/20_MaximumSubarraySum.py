"""
https://leetcode.com/problems/maximum-subarray/description/
"""

def maxSubArray(nums):
    """ T(C) -> O(N^3), S(C) -> O(1) """

    max_sum = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            total = 0
            for k in range(i, j):
                total += nums[k]

            max_sum = max(max_sum, total)

    return max_sum


def maxSubArrayBetter(nums):
    """ T(c) -> O(N^2), S(C) -> O(1) """

    max_sum = float('-inf')

    # check each subarray and find maximum sum
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            max_sum = max(max_sum, total)

    return max_sum


def maxSubArrayOptimal(nums):
    """ T(C) -> O(N), S(C) -> O(1) """

    # using kadane's algo to check max subarray sum
    max_sum = float('-inf')
    current_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        # if current_sum is more than max, replace max with current_sum
        if current_sum > max_sum:
            max_sum = current_sum

        # if current_sum < 0, no need to carry forward, make it 0
        if current_sum < 0:
            current_sum = 0
    
    return max_sum


def PrintmaxSubArray(nums):
    """ T(C) -> O(N), S(C) -> O(N) """

    ans_start = -1
    ans_end = -1
    # using kadane's algo
    max_sum = float('-inf')
    current_sum = 0

    for i in range(len(nums)):
        # starting of new subarray
        if current_sum == 0:
            ans_start = i

        current_sum += nums[i]

        # if current sum is greater than max sum, replace max_sum with current_sum
        if current_sum > max_sum:
            max_sum = current_sum
            # can be end of max subarray
            ans_end = i

        # if current_sum < 0, we will not carry forward it, make it 0
        if current_sum < 0:
            current_sum = 0
    
    print([ans_start, ans_end])
    return [ans_start, ans_end]


if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(arr)
    # The subarray [4,-1,2,1] has the largest sum 6.
    print(maxSubArray(arr))  
    print(maxSubArrayBetter(arr))          
    print(maxSubArrayOptimal(arr))

    start, end = PrintmaxSubArray(arr)
    for i in range(start, end+1):
        print(arr[i], end=" ")
    print()