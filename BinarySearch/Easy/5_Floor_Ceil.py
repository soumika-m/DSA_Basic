"""
Floor -> largest number in array <= x
Ceil -> smallest number in array >= x
"""

def findFloor(arr, target):
    """ T(C) -> O(logn), S(C) -> O(1)"""

    n = len(arr)
    low = 0
    high = n-1
    ans = -1

    # largest element <= target
    while low <= high:
        mid = (low + high) // 2
        # may be answer
        if arr[mid] <= target:
            ans = arr[mid]
            # check for more larger element at right
            low = mid + 1
        # check at left for finding <= element
        else:
            high = mid - 1

    return ans


def findCeil(arr, target):
    """ T(C) -> O(logn), S(C) -> O(1)"""

    n = len(arr)
    low = 0
    high = n-1
    ans = -1

    # smallest element >= target
    while low <= high:
        mid = (low + high) // 2
        # may be answer
        if arr[mid] >= target:
            ans = arr[mid]
            # check for more smallest element at left
            high = mid - 1
        # check at right for finding >= element
        else:
            low = mid + 1

    return ans


if __name__ == "__main__":
    arr = [10,20,30,40,50]
    target = 25
    print(arr, target)
    print(findFloor(arr, target))
    print(findCeil(arr, target))
