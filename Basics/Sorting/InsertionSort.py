"""
https://www.geeksforgeeks.org/problems/insertion-sort/0
"""

def insertionSort(arr):
    """ T(c) -> O(n^2), S(c) -> O(1) """
    n = len(arr)
    
    # unsorted list
    for i in range(1, n):
        temp = arr[i]
        j = i-1
        
        # sorted list, comparison
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = temp
            

arr = [41, 9, 9, 48, 11, 2, 11, 12, 28, 10, 15, 4, 16, 48]
print(arr)
insertionSort(arr)
print(arr)
