"""
https://www.geeksforgeeks.org/problems/implement-upper-bound/0
"""

def upperBound(arr, target):
    """ T(C) -> O(logn), S(C) -> O(1) """

    # if arr[mid] > target not found, return length of array
    ans = len(arr)

    low = 0
    high = len(arr) - 1

    # smallest index such that arr[mid] > target (upperbound)
    while low <= high:
        mid = (low+high) // 2

        if arr[mid] > target:
            ans = mid
            # go to left side and check if any other small element present which is greater
            high = mid - 1
        
        # if element is <= target, go to right side
        else:
            low = mid + 1 

    return ans


if __name__ == "__main__":
    arr = [2, 3, 7, 10, 11, 11, 25]
    target = 11
    print(arr, target)
    # 6 is the smallest index in arr[], at which element (arr[6] = 25) is larger than 11.
    print(upperBound(arr, target))
