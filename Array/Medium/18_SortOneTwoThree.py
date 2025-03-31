"""
http://leetcode.com/problems/sort-colors/description/
"""

def sortColors(nums):
    """ T(C) -> o(N log N), S(C) -> O(N) """

    # using merge sort
    mergeSort(nums, 0, len(nums)-1)
    

def mergeSort(nums, low, high):
    
    # if atleast 2 elements present
    if low < high:
        mid = (low + high) // 2
        # sort left part
        mergeSort(nums, low, mid)
        
        # sort right part
        mergeSort(nums, mid+1, high)

        # merge both part
        merge(nums, low, mid, high)


def merge(nums, low, mid, high):
    left = low
    right = mid+1

    temp = []

    # if element present in both parts
    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1

    # if elements present in left part
    while left <= mid:
        temp.append(nums[left])
        left += 1

    # if elements present in right part
    while right <= high:
        temp.append(nums[right])
        right += 1

    # insert from temp array to original array
    for i in range(low, high+1):
        nums[i] = temp[i-low]


def sortColorsBetter(nums):
    """ T(C) -> O(N) + O(N) = O(2N), S(C) -> O(1) """

    # count 0, 1, 2 using counter
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            cnt0 += 1
        elif nums[i] == 1:
            cnt1 += 1
        else:
            cnt2 += 1
    
    # replace elements in array
    for i in range(cnt0):
        nums[i] = 0
    for j in range(cnt0, cnt0+cnt1):
        nums[j] = 1
    for k in range(cnt0+cnt1, cnt0+cnt1+cnt2):
        nums[k] = 2


def sortColorsOptimal(nums):
    """ T(C) -> O(N), S(C) -> O(1) """

    # using dutch national flag algorithm
    low = 0
    mid = 0
    high = len(nums)-1

    # [0......low-1] 0 extreme left, [low.......mid-1] 1, [high+1......n-1] extreme right 2
    # [mid.......high] unsorted part  
    while mid <= high:
        # if number is 0, swap it with low, increase low and mid
        if nums[mid] == 0:
            swap(nums, low, mid)
            low += 1
            mid += 1

        # if number is 1, do nothing, increase mid
        elif nums[mid] == 1:
            mid += 1
        
        # if number is 2, swap it with high, decrease high
        elif nums[mid] == 2:
            swap(nums, mid, high)
            high -= 1


def swap(arr, fidx, sidx):
    arr[fidx], arr[sidx] = arr[sidx], arr[fidx]


if __name__ == "__main__":

    nums = [0,1,1,0,1,2,1,2,0,0,0]
    print(nums)
    sortColors(nums)
    print(nums)
    print()

    nums = [0,1,1,0,1,2,1,2,0,0,0]
    print(nums)
    sortColorsBetter(nums)
    print(nums)
    print()

    nums = [2,0,1,0,2,2,0,0,1,1,0]
    print(nums)
    sortColorsOptimal(nums)
    print(nums)
