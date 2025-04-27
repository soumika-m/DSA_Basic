
def binarySearch(arr, target):
    """ T(C) -> O(logn), S(C) -> O(1) """

    n = len(arr)

    low = 0
    high = n-1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid-1
        else:
            low = mid+1

    return -1


def binarySearchRecursive(arr, low, high, target):
    """ T(C) -> O(logn), S(C) -> O(1) """

    # base case
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid] :
        return binarySearchRecursive(arr, low, mid-1, target)
    # else
    return binarySearchRecursive(arr, mid+1, high, target)


if __name__ == "__main__":
    arr = [-1,0,3,5,9,12]
    target = 9
    # 9 exists in nums and its index is 4
    print(binarySearch(arr, target))
    print(binarySearchRecursive(arr, 0, len(arr)-1, 10))
    