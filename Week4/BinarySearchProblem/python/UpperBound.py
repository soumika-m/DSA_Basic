"""
Given a sorted array arr[] and a number target, the task is to find the upper bound of the target in this given array.

The upper bound of a number is defined as the smallest index in the sorted array where the element is greater than the 
given number.

Note: If all the elements in the given array are smaller than or equal to the target, the upper bound will be the 
length of the array.

https://www.geeksforgeeks.org/problems/implement-upper-bound/0
"""

def upperBound(arr, target):
    """ T(C) -> O(logn), S(C) -> O(1) """
    low = 0
    high = len(arr)-1
    ans = len(arr)
    while low <= high:
        mid = (low+high) // 2
        # arr[mid] > target, that might be upper bound
        if arr[mid] > target:
            ans = mid
            # go to the left, to find smallest index
            high = mid-1
        else:
            # go to right
            low = mid+1
            
    return ans


arr = [2, 3, 7, 10, 11, 11, 25]
target = 9
print(arr)
print(target , " -> ", upperBound(arr, target))

target = 100
print(target , " -> ", upperBound(arr, target))
