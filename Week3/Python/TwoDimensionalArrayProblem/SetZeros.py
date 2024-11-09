"""
    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
    You must do it in place.

    https://leetcode.com/problems/set-matrix-zeroes/
"""

from typing import List

"""It will not work for negative values"""
def setZeroes(matrix):
    """ T(c) -> (O(m*n) * O(m+n)) + O(m*n), S(c) -> O(1) """
    row = len(matrix)
    col = len(matrix[0])
    
    # identify where 0 is present, make corresponding row and column elements -1, except existing 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                makeRowZero(matrix, i)
                makeColZero(matrix, j)
    
    # resetting those -1 to 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == -1:
                matrix[i][j] = 0

# make entire row as -1, except 0 values
def makeRowZero(matrix, row_num):
    col = len(matrix[0])
    for i in range(col):
        if matrix[row_num][i] != 0:
            matrix[row_num][i] = -1

# make entire column as -1, except 0 values
def makeColZero(matrix, col_num):
    row = len(matrix)
    for i in range(row):
        if matrix[i][col_num] != 0:
            matrix[i][col_num] = -1


""" Using extra row and column array """
def setZeroesBetter(matrix: List[List[int]]) -> None:
    """ T(c) -> O(m*n) + O(m*n) => O(2*m*n), S(c) -> O(m) + O(n) """
    row = len(matrix)
    col = len(matrix[0])
    
    # for tracking which row and col index contains 0
    track_row = [0]*row
    track_col = [0]*col
    
    # identify where 0 present, keep track of row and column number in separate array
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                track_row[i] = 1
                track_col[j] = 1

    # reiterate the matrix and check row and column array to know if we need mark element as 0
    for i in range(row):
        for j in range(col):
            if track_row[i] == 1 or track_col[j] == 1:
                matrix[i][j] = 0


""" Without using extra space """
def setZeroesOptimal(matrix: List[List[int]]) -> None:
    """ T(c) -> O(m*n) + O(m*n) + O(n) + O(m), S(c) -> O(1) """
    row = len(matrix)
    col = len(matrix[0])
    
    # rowarray -> matrix[0][....]
    # colarray -> matrix[...][0]
    
    # for tracking first column
    col0 = 1
    
    # identify where 0 present, mark 0 in first row, first column and col0 variable
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                # marking in row array
                matrix[i][0] = 0
                # marking in column array or col0 variable
                if j == 0:
                    col0 = 0
                else:
                    matrix[0][j] = 0

    # reiterate matrix and make change, except first row and first column, by looking at rowarray or colarray 
    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][j] != 0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
    
    # make entire first row as 0 based on matrix[0][0] element
    if matrix[0][0] == 0:
        for j in range(1, col):
            matrix[0][j] = 0
    
    # make entire first column as 0 based on col0 variable
    if col0 == 0:
        for i in range(row):
            matrix[i][0] = 0


m1 = [[1,1,1],[1,0,1],[1,1,1]]
print("Original Matrix = ", m1)
setZeroes(m1)
print("Modified Matrix = ", m1)
m2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print("Original Matrix = ", m2)
setZeroesBetter(m2)
print("Modified Matrix = ", m2)
m3 = [[1,1,1,1],[1,0,1,1],[1,1,0,1],[0,1,1,1]]
print("Original Matrix = ", m3)
setZeroesOptimal(m3)
print("Modified Matrix = ", m3)
