"""
    Given an Integer n and a list arr. Sort the array using bubble sort algorithm.

    https://www.geeksforgeeks.org/problems/bubble-sort/1
"""

def bubbleSort(arr, n):
    """ T(c) -> O(n^2), S(c) -> O(1) """
    # number of passes
    for i in range(n-1):
        # number of comparison
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


arr = [5,4,3,2,1]
print(arr)
bubbleSort(arr, len(arr))
print(arr)