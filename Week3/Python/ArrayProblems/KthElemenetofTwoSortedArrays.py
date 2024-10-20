"""
"""

def kthElement(k, arr1, arr2):
    """ T(c) -> O(m+n), S(c) -> O(m+n) """
    # merge both array and return kth element from merge array
    merged_arr = [0] * (len(arr1) + len(arr2))
    i = 0
    j = 0
    p = 0
    while i < len(arr1) and j < len(arr2): 
        if arr1[i] < arr2[j]:
            merged_arr[p] = arr1[i]
            i += 1
        else:
            merged_arr[p] = arr2[j]
            j += 1
        p += 1

    # remaining of arr1    
    while i < len(arr1):
        merged_arr[p] = arr1[i]
        p += 1
        i += 1

    # remaining of arr2  
    while j < len(arr2):
        merged_arr[p] = arr2[j]
        p += 1
        j += 1

    return merged_arr[k-1]


arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
k = 5
print(arr1, arr2, k)
print(kthElement(k, arr1, arr2))
