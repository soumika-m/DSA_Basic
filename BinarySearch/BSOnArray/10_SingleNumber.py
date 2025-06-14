"""
https://leetcode.com/problems/single-element-in-a-sorted-array/
"""

def singleNonDuplicate(arr):
    """ T(C) -> O(n), S(C) -> O(1) """

    n = len(arr)

    # if only 1 element present in array
    if n == 1:
        return arr[0]

    for i in range(n):
        # for first index
        if i == 0:
            if arr[i] != arr[i+1]:
                return arr[i]
        # for last index
        elif i == n-1:
            if arr[i] != arr[i-1]:
                return arr[i]
        # if arr[i] is not equal to arr[i+1] and arr[i-1], that is single number
        else:  
            if (arr[i] != arr[i-1] and arr[i] != arr[i+1]):
                return arr[i]
            
    
def singleNonDuplicateBinarySearch(arr):
    """ T(C) -> O(logn), S(C) -> O(1) """

    n = len(arr)

    # edge case
    # if only 1 element present in array
    if n == 1:
        return arr[0]

    # if first element is single element
    if arr[0] != arr[1]:
        return arr[0]
    
    # if last element is single element
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    
    low = 1
    high = n - 2

    while low <= high:
        mid = (low + high) // 2
        # mid is single number
        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        
        # if mid is even and mid is equal to next element, currently at left half
        # or mid is odd and mid is equal to previous element, currently at left half
        if (
            (mid % 2 == 0 and arr[mid] == arr[mid + 1]) or 
            (mid % 2 == 1 and arr[mid] == arr[mid - 1])
        ):
            # go to right half for single element
            low = mid + 1

        # if mid is odd and mid is equal to next element, currently at right half
        # or mid is even and mid is equal to previous element, currently at right half
        ## if mid % 2 == 1 and arr[mid] == arr[mid + 1] or mid % 2 == 0 and arr[mid] == arr[mid - 1]
        else:
            # go to left half for single element
            high= mid - 1
        
    # if no single number found
    return -1
 

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 5]
    print(singleNonDuplicate(arr)) # Expected output: 4
    arr = [1, 1, 2, 2, 3]
    print(singleNonDuplicate(arr)) # Expected output: 3
    arr = [1]
    print(singleNonDuplicate(arr)) # Expected output: 1

    arr = [1,1,2,3,3,4,4,8,8]
    print(singleNonDuplicateBinarySearch(arr)) # Expected output: 2
    arr = [1,2,2,3,3,4,4,8,8]
    print(singleNonDuplicateBinarySearch(arr)) # Expected output: 1
    arr = [1,1,2,2,3,3,4,4,8]
    print(singleNonDuplicateBinarySearch(arr)) # Expected output: 8
   