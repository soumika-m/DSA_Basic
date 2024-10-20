"""
    Given an array of integers. Find the Inversion Count in the array.  Two elements arr[i] and arr[j] form an inversion 
    if arr[i] > arr[j] and i < j.
    Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array 
    is already sorted then the inversion count is 0.
    If an array is sorted in the reverse order then the inversion count is the maximum. 

    https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
"""


"""TLE"""
def inversionCount(arr):
    """ T(c) -> O(n^2), S(c) -> O(1) """
    inversion_count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inversion_count += 1

    return inversion_count


def inversionCountEfficient(arr):
    """ T(c) -> O(nlogn), S(c) -> O(n) """
    # using modified merge sort
    return mergeSort(arr, 0, len(arr)-1)


def mergeSort(arr, low, high):
    inversion_count = 0

    if low < high:
        mid = (low + high) // 2
        inversion_count += mergeSort(arr, low, mid)
        inversion_count += mergeSort(arr, mid+1, high)
        inversion_count += merge(arr, low, mid, high)

    return inversion_count


def merge(arr, low, mid, high):
    l = low
    r = mid + 1
    B = [0] * (high-low+1)
    k = 0
    cnt = 0
    
    while l <= mid and r <= high:
        if arr[l] <= arr[r]:
            B[k] = arr[l]
            l += 1
        else:
            B[k] = arr[r]
            r += 1
                # inversion found, from that index till last index, all can form pair
            cnt += (mid-l+1)
        k += 1
    
    # if only left array still contains element
    while l <= mid:
        B[k] = arr[l]
        k += 1
        l += 1
    
    # if only right array still contains element        
    while r <= high:
        B[k] = arr[r]
        k += 1
        r += 1
            
    for i in range(len(B)):
        arr[i+low] = B[i]
        
    return cnt


arr = [2, 4, 1, 3, 5]
print(arr)
# The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
print(inversionCount(arr))
print(inversionCountEfficient(arr))
