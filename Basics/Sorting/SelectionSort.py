"""
https://www.geeksforgeeks.org/problems/selection-sort/1
"""

def selectionSort(arr):
    """ T(c) -> O(n^2), S(c) -> O(1) """

    n = len(arr)

    # n-1 pass -> last element will be by default sorted at the end
    for i in range(n-1):
        min = i

        # find minimum
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        
        # swap minimum element with first element of unsorted array
        if min != i:
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp


arr = [41, 9, 9, 48, 11, 2, 11, 12, 28, 10, 15, 4, 16, 48]
print(arr)
selectionSort(arr)
print(arr)
