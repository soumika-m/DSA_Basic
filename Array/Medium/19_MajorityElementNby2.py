"""
https://leetcode.com/problems/majority-element/

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
"""

def majorityElement(nums):
    """ T(C) -> O(N^2), S(C) -> O(1) """
    N = len(nums)
    for i in range(N):
        cnt = 0
        for j in range(N):
            if nums[j] == nums[i]:
                cnt += 1
        
        # if element present more than N/2 times, return that
        if cnt > (N//2):
            return nums[i]
        

def majorityElementBetter(nums):
    """ T(C) -> O(N) + O(M), S(C) -> O(M) """
    # store element and it's count in hashmap
    mp = {}

    for num in nums:
        mp[num] = mp.get(num, 0) + 1

    # if count is more than n/2, return that element
    for key,value in mp.items(): 
        if value > (len(nums)//2):
            return key
    
    return -1


def majorityElementOptimal(nums):
    """ T(C) -> O(N) + O(N), S(C) -> O(1) """

    # using boyer moore's voting algo
    majority_elem = -1
    cnt = 0
    # if same element found, increase count, otherwise decrease count
    for num in nums:
        # if count is zero, assign next element value
        if cnt == 0:
            cnt = 1
            majority_elem = num
        elif num == majority_elem:
            cnt += 1
        else:
            cnt -= 1

    # check count of the elem
    cnt2 = 0
    for num in nums:
        if num == majority_elem:
            cnt2 += 1

    # if element appearing more than n/2, that is majority element
    if cnt2 > (len(nums) // 2):
        return majority_elem

    return -1


if __name__ == "__main__":
    arr = [2,2,1,1,1,2,2]
    print(arr)
    print(majorityElement(arr))
    print(majorityElementBetter(arr))
    print(majorityElementOptimal(arr))
