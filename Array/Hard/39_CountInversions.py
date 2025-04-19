"""
count inversion where the condition was a[i] > a[j], the index i < j.

https://leetcode.com/problems/reverse-pairs/description/
"""

def countInversion(arr):
    """ T(C) -> O(n^2), S(C) -> O(1) """

    count = 0

    # check all pairs
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                print(f"({arr[i]}, {arr[j]})", end=" ")
                count += 1
    
    print()
    return count


def countInversionOptimal(arr):
    """ T(C) ->O(nlogn) , S(C) -> O(n) """

    # alter array
    return mergesort(arr, 0, len(arr)-1)


def mergesort(arr, low, high):
    
    cnt = 0
    # using merge sort
    if low < high:
        mid = (low + high) // 2
        # left part of array
        cnt += mergesort(arr, low, mid)
        # right part of array
        cnt += mergesort(arr, mid+1, high)
        # merge left and right part
        cnt += merge(arr, low, mid, high)
    
    return cnt


def merge(arr, low, mid, high):
    temp = []

    left = low
    right = mid+1

    cnt = 0

    # compare both arrays and merge after sorting
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += (mid-left+1)
            right += 1
    
    # if element present in left array
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # if element present in right array
    while right <= high:
        temp.append(arr[right])
        right += 1

    # copy elements from temp to original array
    for i in range(len(temp)):
        arr[i+low] = temp[i]

    return cnt


if __name__ == "__main__":
    arr = [5,3,2,4,1]
    print(arr)
    print(countInversion(arr))
    print(countInversionOptimal(arr))
    print(arr)
