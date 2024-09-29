"""
Given an array arr, return the second largest distinct element from an array. If the second largest 
element doesn't exist then return -1.

https://www.geeksforgeeks.org/problems/second-largest3735/1
"""

def print2ndlargest(arr):
    """ T(c) -> O(n) , S(c) -> O(1) """
    # Find largest element
    maxElem = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > maxElem:
            maxElem = arr[i]
            
    # Find second largest element
    secondElem = -1
    for j in range(len(arr)):
        # distinct second largest
        if arr[j] > secondElem and arr[j] != maxElem:
            secondElem = arr[j]

    return secondElem


""" Using one loop """
def print2ndlargest2(arr):
    """ T(c) -> O(n) , S(c) -> O(1) """

    maxElem = -1
    secondElem = -1
    
    for i in range(len(arr)):
        if arr[i] > maxElem:
            secondElem = maxElem
            maxElem = arr[i]
        
        # distinct second largest
        elif arr[i] > secondElem and arr[i] != maxElem:
            secondElem = arr[i]
        
    return secondElem


arr = [32011, 123, 1045, 1205, 254, 28763, 6537, 3161]
print(print2ndlargest(arr))
arr = [28078, 19451, 935, 28892, 2242, 3570, 5480, 231]
print(print2ndlargest2(arr))
