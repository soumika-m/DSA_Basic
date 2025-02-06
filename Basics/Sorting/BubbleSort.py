"""
https://www.geeksforgeeks.org/problems/bubble-sort/1
"""

def bubbleSort(arr):
    """ T(c) -> O(n^2) , S(c) -> O(1) """

    n = len(arr)
    
    # passes
    for i in range(n-1):
        # comparison
        for j in range(n-1-i):
            # swap element
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


def bubbleSortEfficient(arr):
    """ T(c) -> O(n^2) // best case O(n) , S(c) -> O(1) """
    n = len(arr)
    
    # passes
    for i in range(n-1):
        did_swap = 0
        # comparison
        for j in range(n-1-i):
            # swap element
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                did_swap = 1
        
        # if no swap done, array already sorted
        if did_swap == 0:
            break


arr = [41, 9, 9, 48, 11, 2, 11, 12, 28, 10, 15, 4, 16, 48]
print(arr)
bubbleSortEfficient(arr)
print(arr)
