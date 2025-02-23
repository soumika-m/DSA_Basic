"""
https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1
"""

def linearSearch(arr, k):
    """ T(c) -> O(n), S(c) -> O(1) """

    for i in range(len(arr)):
        if arr[i] == k:
            return i
        
    return -1


def binarySearch(arr, k):
    """ T(c) -> O(logn), S(c) -> O(1) """

    # Using binary search
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            return True
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    
    return False


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6]
    k = 3
    print(linearSearch(arr, k))
    print(binarySearch(arr, k))
