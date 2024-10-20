"""
    Given a sorted array A containing N integers both positive and negative.
    You need to create another array containing the squares of all the elements in A and return it in non-decreasing order.
    Try to this in O(N) time.

    https://www.interviewbit.com/problems/sort-array-with-squares/
"""

def solve(A):
    """ T(c) -> O(n), S(c) -> O(1) """

    # result array
    result = [0] * len(A)

    left = 0
    right = len(A) - 1
    k = len(result) - 1

    # using 2 pointer approach
    while left <= right:
        # place elements from greater to smaller element
        if((A[left] ** 2) > (A[right] ** 2)):
            result[k] = A[left] ** 2
            left = left+1
        else:
            result[k] = A[right] ** 2
            right = right-1
        k = k-1
    
    return result


arr = [-6, -3, -1, 2, 4, 5]
print(arr)
result = solve(arr)
print(result)
