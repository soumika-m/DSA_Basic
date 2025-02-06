"""
Given a sorted array arr[] and a number target, the task is to find the lower bound of the 
target in this given array. The lower bound of a number is defined as the smallest index in 
the sorted array where the element is greater than or equal to the given number.

Note: If all the elements in the given array are smaller than the target, the lower 
bound will be the length of the 
array. 

Input:  arr[] = [2, 3, 7, 10, 11, 11, 25], target = 9
Output: 3

https://www.geeksforgeeks.org/problems/implement-lower-bound/0
"""

def lowerBound(arr, target):
    """ T(C) -> O(logn), S(C) -> O(1) """
    low = 0
    high = len(arr)-1
    ans = len(arr)

    while low <= high:
        mid = (low+high) // 2
        # smallest index element >= target
        if arr[mid] >= target:
            ans = mid
            # check more smaller index (left side)
            high = mid-1
        else:
            # if element is smaller, go to right side
            low = mid+1

    return ans


arr = [2, 3, 7, 10, 11, 11, 25]
target = 9
print(arr)
print(target , " -> ", lowerBound(arr, target))

target = 100
print(target , " -> ", lowerBound(arr, target))