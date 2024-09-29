"""
    Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.

    https://www.geeksforgeeks.org/problems/selection-sort/1
"""

def selectionSort(arr, n):
    """ T(c) -> O(n^2), S(c) -> O(1)"""
    # number of passes
    for i in range(n):
        # find minimum number index
        mini = select(arr, n, i)

        # if mimimum is different, shift minimum to correct position using swaping
        if mini != i:
            temp = arr[mini]
            arr[mini] = arr[i]
            arr[i] = temp


def select(arr, n, i):
    mini = i
    # find minimum
    for j in range(i+1, n):
        if arr[j] < arr[mini]:
            mini = j

    return mini



arr = [5, 4, 3, 2, 1]
print(arr)
selectionSort(arr, len(arr))
print(arr)
