"""
    Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] 
    such that:
    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target
    You may return the answer in any order.

    https://leetcode.com/problems/4sum/
"""


"""Giving TLE"""
def fourSum(nums, target):
    """ T(c) -> O(n^4), S(c) -> (2 * number of quadtruples) for set and array"""
    n = len(nums)
    result_set = set()

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()
                        result_set.add(tuple(temp))

    return [list(item) for item in result_set]


def fourSumBetter(nums, target):
    """ T(c) -> O(n^3), S(c) -> O(2 * number of quadtruples) for both a set and an array of quadruplets + O(n) for seen set element"""
    n = len(nums)
    # set for holding final result
    result_set = set()

    for i in range(n):
        for j in range(i+1, n):
            # set for finding the forth number
            seen = set()
            for k in range(j+1, n):
                another_num = target - (nums[i] + nums[j] + nums[k])
                if another_num in seen:
                    temp = [nums[i], nums[j], nums[k], another_num]
                    temp.sort()
                    result_set.add(tuple(temp))
                
                # add in the set
                seen.add(nums[k])

    return [list(item) for item in result_set]


def fourSumOptimal(nums, target):
    """ T(c) -> O(n^3), S(c) -> O(n^2) due to the storage of quadruplets in the result list """
    n = len(nums)
    
    # sort the array
    nums.sort()
    
    result = []
    
    # using two pointers approach
    for i in range(n):
        # skip duplicates of i
        if i > 0 and nums[i-1] == nums[i]:
            continue
            
        for j in range(i+1, n):
            # skip duplicates of j
            if j > i+1 and nums[j-1] == nums[j]:
                continue
                
            k = j+1
            l = n-1
            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]
                # total is less than target
                if total < target:
                    k += 1
                
                # total is greater than target
                elif total > target:
                    l -= 1
                
                # element found
                else:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    result.append(temp)
                    k += 1
                    l -= 1
                    
                    # skip duplicates of k
                    while k < l and nums[k-1] == nums[k]:
                        k += 1
                    
                    # skip duplicates of l
                    while k < l and nums[l+1] == nums[l]:
                        l -= 1

    return result


arr = [1,0,-1,0,-2,2]
target = 0
print(arr, target)
print(fourSum(arr, target))
print(fourSumBetter(arr, target))
print(fourSumOptimal(arr, target))
