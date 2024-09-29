"""
    Given an array arr[], its starting position l and its ending position r. Sort the array using merge sort algorithm.
    
    https://www.geeksforgeeks.org/problems/merge-sort/1
"""
    
def mergeSort(arr, l, r):
    """ T(c) -> O(nlogn), S(c) ->  O(n) """
    if l<r:
        # find middle index
        m = (l+r)//2
        # sort left part
        mergeSort(arr, l, m)
        # sort right part
        mergeSort(arr, m+1, r)
        # merge both sorted list
        merge(arr, l, m, r)


def merge(arr, l, m, r): 

    temp = [0] * (r-l+1)
    k = 0
    i = l
    j = m+1
    
    # compare and merge both halves using temp array
    while i <= m and j <= r:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    # copy remaining elements of left half, if any   
    while i <= m:
        temp[k] = arr[i]
        i += 1
        k += 1

    # copy remaining elements from right half, if any  
    while j <= r:
        temp[k] = arr[j]
        j += 1
        k += 1
    
    # shift elements from temp arr to original array
    tp = 0
    ptr = l
    while ptr <= r:
        arr[ptr] = temp[tp]
        ptr += 1
        tp += 1


arr = [5, 4, 3, 2, 1]
print(arr)
mergeSort(arr, 0, len(arr)-1)
print(arr)
