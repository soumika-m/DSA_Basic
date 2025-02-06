"""
https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0
"""

from typing import List

def largest(arr : List[int]) -> int:
    # code here
    largest = -1
    for elem in arr:
        if elem > largest:
            largest = elem

    return largest