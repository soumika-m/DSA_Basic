"""
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

    https://leetcode.com/problems/rotate-image/
"""

from typing import List

def rotate(matrix: List[List[int]]) -> None:
    """ T(c) -> O(r*c) + O(r*c), S(c) -> O(r*c) """

    row = len(matrix)
    col = len(matrix[0])

    # initialize result matrix with 0
    result = [[0] * col for _ in range(row)]
    
    # map elements from original matrix to result matrix after rotation
    for i in range(row):
        for j in range(col):
            result[j][col-i-1] = matrix[i][j]
    
    # copy elements from result matrix to original matrix
    for i in range(row):
        for j in range(col):
            matrix[i][j] = result[i][j]


""" Without using extra space """
def rotateEfficient(matrix: List[List[int]]) -> None:
    """ T(c) -> O(n/2 * n/2) + O(n * n/2), S(c) -> O(1) """
    n = len(matrix)
    
    # transpose the matrix
    for i in range(n-1):
        for j in range(i+1, n):
            # swap elements
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    
    # reverse each row of matrix
    for i in range(n):
        p1 = 0
        p2 = n-1
        while p1 < p2:
            # swap elements
            temp = matrix[i][p1]
            matrix[i][p1] = matrix[i][p2]
            matrix[i][p2] = temp
            p1 += 1
            p2 -= 1


mat1 = [[1,2,3],[4,5,6],[7,8,9]]
print(mat1)
rotate(mat1)
print(mat1)
mat2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(mat2)
rotateEfficient(mat2)
print(mat2)
