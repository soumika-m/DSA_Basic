"""
    Given an integer array A of size N. You have to pick exactly B elements from either left or right end of the array A to 
    get the maximum sum. Find and return this maximum possible sum.
    NOTE: Suppose B = 4 and array A contains 10 elements then
    You can pick the first four elements or can pick the last four elements or can pick 1 from the front and 3 from the 
    back etc. you need to return the maximum possible sum of elements you can pick.

    https://www.interviewbit.com/problems/pick-from-both-sides/
"""

def solve(A, B):
    """ T(c) -> O(B), S(c) -> O(1) """
    max_sum = 0
    current_sum = 0
    i = 0
    # find sum of first B elements (left side)
    while i<B:
        current_sum += A[i]
        i = i + 1
    
    # i will point to the last num of left set
    i = i-1
    max_sum = current_sum
    
    j = len(A) - 1
    # find sum of right side (B elememnts), after discarding num of left set (sliding window)
    while j >= len(A)-B:
        current_sum += A[j]
        current_sum -= A[i]
        i = i-1
        j = j-1
        max_sum = max(max_sum, current_sum)
    
    return max_sum


arr = [5, -2, 3 , 1, 2]
B = 3
print(arr)
# Pick element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8
max_sum = solve(arr, B)
print(max_sum)
