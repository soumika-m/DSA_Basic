"""
Given an array nums. Find running sum of array as runningSum[i] = sum(nums[0]…nums[i])
For eg. nums = [1,2,3,4], Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

https://leetcode.com/problems/running-sum-of-1d-array/
"""

def runningSum(nums):
    """ T(c) -> O(n) , S(c) -> O(1) """
    total = 0
    
    for i in range(len(nums)):
        total += nums[i]
        nums[i] = total
    
    return nums


arr = [1,2,3,4]

for i in arr:
    print(i, end=" ")

print()

res = runningSum(arr)

for i in res:
    print(i, end=" ")
