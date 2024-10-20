"""
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
    There is only one repeated number in nums, return this repeated number.
    You must solve the problem without modifying the array nums and using only constant extra space.

    https://leetcode.com/problems/find-the-duplicate-number/
"""

def findDuplicate(nums):
    """ T(c) -> O(n), S(c) -> O(n)"""

    freq = {}
    
    # calculate frequency of elements
    for i in range(len(nums)):
        elem = nums[i]
        if freq.get(elem):
            freq[elem] += 1
        else:
            freq[elem] = 1
            
    repeated = -1
    
    # check of repeated number
    for key, value in freq.items():
        if value > 1:
            repeated = key
    
    return repeated


def findDuplicateEfficient(nums):
    """ T(c) -> O(n), S(c) -> O(1)"""

    # using floyd's cycle detection or tortoise and hare algo
    # slow and fast pointer will point to the first element
    slow = nums[0]
    fast = nums[0]
    
    # slow will move one step and fast will move two step until both meet again
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
            
    # both met at a point, so cycle exist, reset fast pointerto start of array
    fast = nums[0]
    # this time move fast and slow both one step until it meet again
    while fast != slow:
        fast = nums[fast]
        slow = nums[slow]
    
    # that point where both meet again, is the duplicate number
    return slow


arr = [3,1,3,4,3,2]
print(arr)
print(findDuplicate(arr))
print(findDuplicateEfficient(arr))
