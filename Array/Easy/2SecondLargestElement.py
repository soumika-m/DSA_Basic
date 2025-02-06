"""
https://www.geeksforgeeks.org/problems/second-largest3735/1
"""

def getSecondLargest(arr):
    second_largest = -1
    largest = -1
    
    for elem in arr:
        # find largest element
        if elem > largest:
            second_largest = largest
            largest = elem

        # if distinct second largest
        elif elem < largest and elem > second_largest:
            second_largest = elem
            
    return second_largest