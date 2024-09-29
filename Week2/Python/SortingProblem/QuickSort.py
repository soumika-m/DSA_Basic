"""
    Quick Sort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the 
    picked pivot. Given an array arr[], its starting position is low (the index of the array) and its ending position is 
    high(the index of the array).

    Note: The low and high are inclusive.
    Implement the partition() and quickSort() functions to sort the array.

    https://www.geeksforgeeks.org/problems/quick-sort/1
"""


#Function to sort a list using quick sort algorithm.
def quickSort(arr,low,high):
    """ T(c) -> O(nlogn), S(c) -> O(1) """
    # code here
    if low < high:
        loc = partition(arr, low, high)
        # sort left part of partition
        quickSort(arr, low, loc-1)
        # sort right part of partition
        quickSort(arr, loc+1, high)


def partition(arr,low,high):
    # we are considering pivot as first element
    pivot = low
    
    # find where is the correct place of pivot , place it there
    while low <= high:
        # left of pivot will be smaller element
        while low <= high and arr[low] <= arr[pivot]:
            low += 1
        # right of pivot will be larger element
        while low <= high and arr[high] > arr[pivot]:
            high -= 1
        
        if low <= high:
            # swap low and high
            temp = arr[low]
            arr[low] = arr[high]
            arr[high] = temp
        
    # swap high and pivot (move pivot to correct position)
    temp = arr[pivot]
    arr[pivot] = arr[high]
    arr[high] = temp
    
    # return where the pivot element is placed
    return high


arr = [6, 5, 4, 3, 2, 1]
print(arr)
quickSort(arr, 0, len(arr)-1)
print(arr)