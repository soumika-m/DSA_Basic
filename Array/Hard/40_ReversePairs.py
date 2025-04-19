"""
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where: 0 <= i < j < nums.length and nums[i] > 2 * nums[j].

https://leetcode.com/problems/reverse-pairs/description/
"""


def reversePairs(arr):
    """ T(C) -> O(n^2), S(C) -> O(1) """

    count = 0
    # generate all pairs
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > 2 * arr[j]:
                count += 1

    return count


def reversePairsOptimal(arr):
    """ T(C) -> O(logn * (n+n)) => O(2nlogn), S(C) -> O(n) """

    return mergesort(arr, 0, len(arr)-1)


def mergesort(arr, low, high):
    cnt = 0
    if low < high:
        mid = (low + high) // 2
        # left part
        cnt += mergesort(arr, low, mid)
        # right part
        cnt += mergesort(arr, mid+1, high)
        # count reverse pairs
        cnt += countReversePair(arr, low, mid, high)
        # merge both part
        merge(arr, low, mid, high)

    return cnt


def countReversePair(arr, low, mid, high):
    cnt = 0
    right = mid+1

    # for left part
    for left in range(low, mid+1):
        # for right part
        while right <= high and arr[left] > 2 * arr[right]:
            right += 1

        # calculate count
        cnt += right-(mid+1)

    return cnt


def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid+1

    # if elements present in both array
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # if elements present in left part
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # if elements present in right part
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    # copy elements from temp array to original array
    for i in range(len(temp)):
        arr[i+low] = temp[i]


if __name__ == "__main__":
    arr = [40,25,19,12,9,6,2]
    print(arr)
    print(reversePairs(arr))
    print(reversePairsOptimal(arr))
