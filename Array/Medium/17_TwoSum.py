"""
https://leetcode.com/problems/two-sum/description/
"""

def two_sum(nums, target):
    """ T(C) -> O(N^2), S(C) -> O(1) """

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] ==  target:
                return [i,j]
            
    return [-1,-1]


def two_sum_better(nums, target):
    """ T(C) -> O(N), S(C) -> O(N) """

    # key will contains number, and value wll contain index
    seen_map = {}

    for i, num in enumerate(nums):
        # find that another number
        another_num = target - num
        
        # if that number is present in dictionary, then return
        if another_num in seen_map:
            return [seen_map[another_num], i]
        
        # otherwise store that current number with index
        seen_map[num] = i
    
    return []


def two_sum_optimal(nums, target):
    """ T(C) -> O(NlogN) + O(N), S(C) -> O(1) """
    
    # sort array, find 2 numbers using greedy approach
    nums.sort()

    # using 2 pointer approach, works best only where we need to return true/false.
    left = 0
    right = len(nums)-1

    while left < right:
        # increase left
        if nums[left] + nums[right] < target:
            left += 1
        # decrease right
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return "True"
        
    return "False"


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print("arr = " , nums, ", target = ",target)
    # Because nums[0] + nums[1] == 9, we return [0, 1].
    print(two_sum(nums, target))
    print(two_sum_better(nums, target))
    print(two_sum_optimal(nums, target))
