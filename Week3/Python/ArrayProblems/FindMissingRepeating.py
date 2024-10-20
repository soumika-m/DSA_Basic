"""
    Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2,....,N} is missing and 
    one number 'B' occurs twice in array. Find these two numbers.

    https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1
"""


"""Giving TLE"""
def findTwoElement(arr): 
    """ T(c) -> O(n^2), S(c) -> O(1)"""
    duplicate = -1
    missing = -1
    
    # count which element is missing and duplicate
    for i in range(1, len(arr)+1):
        count = 0
        for j in range(len(arr)):
            if i == arr[j]:
                count += 1
        
        # missing element found    
        if count == 0:
            missing = i
        # duplicate element found
        elif count == 2:
            duplicate = i
            
        # if missing and duplicate both found, break
        if duplicate != -1 and missing != -1:
            break
    
    return [duplicate, missing]


def findTwoElementBetter(arr): 
    """ T(c) -> O(n), S(c) -> O(n) """
    frequency = {}
    
    # count occurance of elements
    for i in range(len(arr)):
        if frequency.get(arr[i]):
            frequency[arr[i]] += 1
        else:
            frequency[arr[i]] = 1

    missing = -1
    duplicate = -1
        
    # finding missing and repeating numbers       
    for i in range(1, len(arr)+1):
        value = frequency.get(i)
        if value == 2:
            duplicate = i
        elif value == None:
            missing = i
            
        # elements already found    
        if missing != -1 and duplicate != -1:
            break
    
    return [duplicate, missing]


def findTwoElementEfficient(arr): 
    """ T(c) -> O(n), S(c) -> O(1) """
    n = len(arr)
    
    # using math formula
    expected_sum = (n * (n+1)) // 2
    expected_square_sum = (n * (n+1) * (2*n+1)) // 6
    
    current_sum = 0
    current_square_sum = 0
    
    # calculate current sum and current square sum
    for num in arr:
        current_sum += num
        current_square_sum += (num * num)
    
    # D is for duplicate, M is for missing
    # using current_sum = expected_sum + D - M
    # D-M = current_sum - expected_sum
    # sum difference is D-M
    sum_diff = current_sum - expected_sum
    # sum square difference is D^2-M^2 => (D+M)(D-M)
    sum_square_diff = current_square_sum - expected_square_sum
    
    # sum plus is D+M
    sum_plus = sum_square_diff // sum_diff
    
    # after solving sum_diff and sum  plus equation (we will add it)
    D = (sum_diff + sum_plus) // 2
    # using D-M = sum_diff
    M = D - sum_diff
    
    return [D, M]


arr = [1, 3, 3]
print("------------",arr)
print(findTwoElement(arr))

arr = [1, 1]
print("------------",arr)
print(findTwoElementBetter(arr))
print(findTwoElementEfficient(arr))
