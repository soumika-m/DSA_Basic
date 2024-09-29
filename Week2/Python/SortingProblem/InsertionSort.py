"""
    The task is to complete the insert() function which is used to implement Insertion Sort.

    https://www.geeksforgeeks.org/problems/insertion-sort/1
"""

# Function to sort the list using insertion sort algorithm.    
def insertionSort(alist, n):
    """ T(c) -> O(n^2), S(c) -> O(1) """

    # unsorted list iteration
    for i in range(1, n):
        temp = alist[i]
        j = i-1
        
        insert(alist, j, temp)


def insert(alist, index, var):
    j = index
    temp = var

    # sorted list iteration, and finding elements correct place
    while j >= 0 and temp < alist[j]:
        alist[j+1] = alist[j]
        j -= 1

    # insert element at correct place
    alist[j+1] = temp



# Function to sort the list using recursive insertion sort algorithm.    
def insertionSortRecursive(alist, n):
    """ T(c) -> O(n^2), S(c) -> O(n) """
    # base case
    if n == 1:
        return
    
    # using recursion
    insertionSortRecursive(alist, n-1)
    
    i = n-1
    temp = alist[i]
    j = i-1
        
    insert(alist, j, temp)


    
arr = [5, 4, 3, 2, 1]
print(arr)
insertionSort(arr, len(arr))
print(arr)
print("-----------------------")
arr = [4, 1, 3, 9, 7]
print(arr)
insertionSort(arr, len(arr))
print(arr)