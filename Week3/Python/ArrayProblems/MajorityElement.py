"""
    Given an array nums of size n, return the majority element. The majority element is the element that appears more than 
    ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

    https://leetcode.com/problems/majority-element/
"""


def majorityElement(nums):
    """ T(c) -> O(n), S(c) -> O(n) """
    count_map = {}
    # calculate count and add it into a dictionary with key
    for num in nums:
        if count_map.get(num):
            count_map[num] += 1
        else:
            count_map[num] = 1
    
    # if count is greater than n/2, return that
    for key in count_map:
        if count_map[key] > len(nums)//2:
            return key
        
    return -1


def majorityElementOptimal(nums):
    """ T(c) -> O(n), S(c) -> O(1) """
    # using moore's voting algo
    majority_elem = -1
    cnt = 0
    
    for i in range(len(nums)):
        # if cnt is 0, make current element as majority
        if cnt == 0:
            majority_elem = nums[i]
        
        # if number matched with majority increase the count
        if nums[i] == majority_elem:
            cnt = cnt + 1
        
        # otherwise decrease the count
        else:
            cnt = cnt - 1
            
    return majority_elem


arr = [2,2,1,1,1,2,2]
print(arr)
print(majorityElement(arr))
print(majorityElementOptimal(arr))
