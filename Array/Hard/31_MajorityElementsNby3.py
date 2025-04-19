"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

https://leetcode.com/problems/majority-element-ii/description/
"""

from typing import List

def majorityElement(nums: List[int]) -> List[int]:
    """ T(C) -> O(N^2), S(C) -> O(1) """

    result = []

    # iterate through each number and check how many times it appears, at max 2 elements can be present which appear more tha n/3 times.
    for i in range(len(nums)):
        count = 0
        # if list is empty, check for that number count
        # otherwise make sure number is not matching with already existing element in list.
        if len(result) == 0 or nums[i] != result[0]:
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1

            # if it is majority element. add in list
            if count > (len(nums) // 3):
                result.append(nums[i]) 

        if len(result) == 2:
            break

    return result


def majorityElementBetter(nums: List[int]) -> List[int]:
    """ T(C) -> O(N), S(C) -> O(N) """

    result = []
    mapp = {}
    min_count = (len(nums) // 3) + 1

    # iterate each number, and put that element and it's count in map
    for i in range(len(nums)):
        mapp[nums[i]] = mapp.get(nums[i], 0) + 1

        # if count of that element is > [n/3], add that in result
        if mapp.get(nums[i]) == min_count:
            result.append(nums[i])

        # incase we find the answer, stop iterating
        if len(result) == 2:
            break
 
    return result


def majorityElementOptimal(nums: List[int]) -> List[int]:
    """ T(C) -> O(N), S(C) -> O(1) """

    elem1 = float("-inf")
    elem2 = float("-inf")
    cnt1 = 0
    cnt2 = 0

    for i in range(len(nums)):

        # elem1 and elem2 should be unique
        # if cnt1 became zero, assign current element, increase count to 1
        if cnt1 == 0 and nums[i] != elem2:
            cnt1 = 1
            elem1 = nums[i]

        # if cnt2 became zero, assign current element, increase count to 1
        elif cnt2 == 0 and nums[i] != elem1:
            cnt2 = 1
            elem2 = nums[i]

        # if current element matching with elem1, increase count
        elif nums[i] == elem1:
            cnt1 += 1
        
        # if current element matching with elem2, increase count
        elif nums[i] == elem2:
            cnt2 += 1

        # decrease both count
        else:
            cnt1 -= 1
            cnt2 -= 1
            

    cnt1 = 0
    cnt2 = 0        
    # iterate through array, and check count of elem1 and elem2
    for i in range(len(nums)):
        if nums[i] == elem1:
            cnt1 += 1

        if nums[i] == elem2:
            cnt2 += 1

    result = []
    # check if elem1 and elem2 count is greater than [n/3]
    if cnt1 > (len(nums) // 3):
        result.append(elem1)
    
    if cnt2 > (len(nums) // 3):
        result.append(elem2)

    return result


if __name__ == "__main__":
    arr = [1,1,1,3,3,2,2,2]
    print(majorityElement(arr))
    print(majorityElementBetter(arr))
    
    # arr = [2,1,1,3,1,4,5,6]
    arr = [0,0,0]
    print(majorityElementOptimal(arr))
