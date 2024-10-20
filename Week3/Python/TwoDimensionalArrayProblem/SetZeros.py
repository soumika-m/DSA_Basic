"""
    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
    You must do it in place.

    https://leetcode.com/problems/set-matrix-zeroes/
"""

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


matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(matrix)
setZeroes(matrix)
print(matrix)
