"""
https://leetcode.com/problems/max-consecutive-ones/description/
"""

def findMaxConsecutiveOnes(nums):
    """ T(C) -> O(N), S(C) -> O(1) """

    # keep count of 1
    current_count = 0
    # keep count of max 1
    max_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count


if __name__ == "__main__":
    arr = [1,0,1,1,0,1]
    print(arr)
    print(findMaxConsecutiveOnes(arr))
