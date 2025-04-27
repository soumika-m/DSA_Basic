"""
https://www.geeksforgeeks.org/problems/implement-lower-bound/0
"""

def lowerBound(arr, target):
    """ T(C) -> O(logn), S(C) -> O(1) """

    # incase lower bound not found, return array size as last index
    ans = len(arr)

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        # smallest index such that arr[ind] >= target (lowerbound)
        if arr[mid] >= target:
            ans = mid
            # find more smaller element than current
            high = mid - 1
        # if mid is smaller, go to right side
        else:
            low = mid + 1

    return ans


if __name__ == "__main__":
    arr = [2, 3, 7, 10, 11, 11, 25]
    target = 9
    print(arr, target)
    # 3 is the smallest index in arr[] where element (arr[3] = 10) is greater than or equal to 9.
    print(lowerBound(arr, target))
    # As no element in arr[] is greater than or equal to 100, return the length of array
    print(lowerBound(arr, 100))