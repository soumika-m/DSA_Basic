"""
    You are given a rectangular matrix, and your task is to return an array while traversing the matrix in spiral form.

    https://www.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1
"""

def spirallyTraverse(mat):
    """ T(c) -> O(r*c), S(c) -> O(r*c) for storing result """
    result = []
    row = len(mat)
    col = len(mat[0])

    left = 0
    right = col-1
    top  = 0
    down = row-1

    # if atleast one row and column left travarse
    while left <= right and top <= down:
        # left to right
        for i in range(left, right+1):
            result.append(mat[top][i])
        top += 1
        
        # top to bottom
        for i in range(top, down+1):
            result.append(mat[i][right])
        right -= 1   
        
        # right to left (if atleast one row present)
        if top <= down:
            for i in range(right, left-1, -1):
                result.append(mat[down][i])
            down -= 1
        
        # bottom to top (if atleast one column present)
        if left <= right:
            for i in range(down, top-1, -1):
                result.append(mat[i][left])
            left += 1
    
    return result


mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15,16]]
print(mat)
res = spirallyTraverse(mat)
print(res)
