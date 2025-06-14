"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

https://leetcode.com/problems/kth-missing-positive-number/description/ 
"""


from typing import List


def findKthPositive(arr: List[int], k: int) -> int:
    """ T(C) -> O(n), S(C) -> O(1) """

    for i in range(len(arr)):
        # if number present in range from array, then increase k value to adjust the missing number
        if arr[i] <= k:
            k += 1
        # if array number is greater than k, found the number, return
        else:
            break
    
    return k


def findKthPositive(arr: List[int], k: int) -> int:
    """ T(C) -> o(logn), S(C) -> O(1) """

    # using binary search (taking array index as range)
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        # at mid index, how many numbers are missing
        # find based on expected number at that place
        missing_number = arr[mid] - (mid+1)

        # if missing number is less than k, check on the right
        if missing_number < k:
            low = mid + 1
        else:
            # check on the left
            high = mid - 1
    
    # low and high will point to the index, between that missing number will be present
    # number = arr[high] + more = arr[high] + (k - missing) = arr[high] + (k - (arr[high] - (high+1)))
    return high + k + 1


if __name__ == "__main__":
    arr = [2,3,4,7,11]
    k = 5
    print(findKthPositive(arr, k))
