"""
Given an array, arr. The task is to find the largest element in it.

https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1
"""

from typing import List


def largest(arr : List[int]) -> int:
    """ T(c) -> O(n) , S(c) -> O(1) """
    
    maxNum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > maxNum:
            maxNum = arr[i]
    
    return maxNum


arr = [1, 8, 7, 56, 90, 76]
print(largest(arr))
