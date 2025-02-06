"""
https://www.geeksforgeeks.org/problems/merge-sort/1
"""

def mergeSort(arr, l, r):
    """ T(c) -> O(nlogn) , S(c) -> O(n) """
    # if more than one number present
    if l < r:
        mid = (l + r) // 2
        # sort left part
        mergeSort(arr, l, mid)
        # sort right part
        mergeSort(arr, mid+1, r)
        # merge left and right part
        merge(arr, l, mid, r)
        
def merge(arr, low, mid, high):
    l = low
    k = 0
    r = mid+1
    
    # temp array
    temp = [0] * (high-low+1)
    
    # if elements present in both left and right part
    while l <= mid and r <= high:
        if arr[l] <= arr[r]:
            temp[k] = arr[l]
            l += 1
        else:
            temp[k] = arr[r]
            r += 1
        k += 1
    
    # if only left array elements left
    while l <= mid:
        temp[k] = arr[l]
        k += 1
        l += 1
    
    # if only right array elements left
    while r <= high:
        temp[k] = arr[r]
        k += 1
        r += 1
    
    # put elements from temp array to main array (low to high)
    p = low
    while p <= high:
        arr[p] = temp[p-low]
        p += 1
    