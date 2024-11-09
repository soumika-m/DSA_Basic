"""
    You are given a 2D array consisting of only 1's and 0's, where each row is sorted in non-decreasing order. You need to 
    find and return the index of the first row that has the most number of 1s. If no such row exists, return -1.

    https://geeksforgeeks.org/problems/row-with-max-1s0023/1
"""


def rowWithMax1s(arr):
    """ T(c) -> O(r*c), S(c) -> O(1) """
    row = len(arr)
    col = len(arr[0])

    count_row = 0
    # max count should be 0 - note
    max_count = 0
    row_idx =  -1
    
    # count number of 1's in each row
    for i in range(row):
        j = col-1
        while j >= 0:
            if arr[i][j] == 1:
                count_row += 1
            # as row is sorted, if 0 found, before that also all 0 will be present
            else:
                break
            j -= 1

        # check which row is having highest count        
        if count_row > max_count:
            max_count = count_row
            row_idx = i
            
        count_row = 0
    
    if row_idx == -1:
        return -1
    else:
        return row_idx


""" Using binary search """
def rowWithMax1sEfficient(arr):
    """ T(c) -> O(n * logn), S(c) -> O(1) """

    row = len(arr)
    col = len(arr[0])
    max_count = 0
    idx = -1

    for i in range(row):
        # count number of 1's in each row and find max count and row number
        count_ones = col - findFirstOccurance(arr[i], col, 1)
        if count_ones > max_count:
            max_count = count_ones
            idx = i

    return idx
        
def findFirstOccurance(array, n, key):
    pos = n
    low = 0
    high = n-1

    while low <= high:
        mid = (low + high) // 2
        # go to more left part to find first occurance tracking the current index
        if array[mid] == key:
            pos = mid
            high = mid-1
        elif array[mid] > key:
            high = mid-1
        else:
            low = mid+1

    return pos
    

arr1 = [[0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]]
print(arr1)
print(rowWithMax1s(arr1))

arr2  = [[0,0], [0,0]]
print(arr2)
print(rowWithMax1sEfficient(arr2))
