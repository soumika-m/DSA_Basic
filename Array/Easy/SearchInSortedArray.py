"""
https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1
"""

def searchInSorted(arr, k):
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