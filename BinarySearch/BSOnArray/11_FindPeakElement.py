"""
A peak element is an element that is strictly greater than its neighbors.

 arr[i-1] < arr[i] > arr[i+1]

https://leetcode.com/problems/find-peak-element/description/
"""

def find_peak_element(arr):
    """ T(C) -> O(n), S(C) -> O(1) """

    print(arr)
    n = len(arr)

    # arr[i-1] < arr[i] > arr[i+1]
    # iterate through array, find which is peak element
    for i in range(len(arr)):
        # for first and last element added edge case
        if (i == 0 or arr[i] > arr[i-1]) and (i == n-1 or arr[i] > arr[i+1]):
            return arr[i]


def find_peak_element_optimal(arr):
    """ T(C) -> O(logn), S(C) -> O(1) """

    print(arr)
    n = len(arr)
    # edge cases
    # if only one element present in array
    if n == 1:
        return arr[0]

    # if first element is peak
    if arr[0] > arr[1]:
        return arr[0]
    
    # if last element is peak
    if arr[n-1] > arr[n-2]:
        return arr[n-1]

    # using binary search to find peak element index
    low = 1
    high = n-2

    while low <= high:
        mid = (low + high) // 2

        # if mid is peak element
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return arr[mid]
        # increasing curve, peak will be on the right side
        elif arr[mid] > arr[mid-1]:
            low = mid + 1
        # decreasing curve, peak will be on the left side
        # else if arr[mid] > arr[mid+1]
        # for multiple peak elements we are not checking any condition, otherwise it will go to infinite loop eg.[1,2,1,2,1]
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,5,1]
    print(find_peak_element(arr))
    print(find_peak_element_optimal(arr))
    arr = [1,2,3,4,5]
    print(find_peak_element(arr))
    arr = [5,4,3,2,1]
    print(find_peak_element(arr))
    # multiple peak
    arr = [1,2,1,2,1]
    print(find_peak_element_optimal(arr))