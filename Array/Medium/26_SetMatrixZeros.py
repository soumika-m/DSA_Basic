"""
https://leetcode.com/problems/set-matrix-zeroes/description/
"""


def setMatrixZeros(matrix):
    """ T(C) -> (O(N*M) * O(N+M)) + O(N*M) => O(N^3) , S(C) -> O(1) """

    # it will only work if in matrix no negative element is present
    row = len(matrix)
    col = len(matrix[0])

    # make row and column as -1
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                markRow(matrix, i)
                markCol(matrix, j)

    # iterate matrix and make -1 to 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == -1:
                matrix[i][j] = 0


def markRow(matrix, row):
    # iterate column
    for j in range(len(matrix[0])):
        # if element is not 0, make it -1, whole row
        if matrix[row][j] != 0:
            matrix[row][j] = -1


def markCol(matrix, col):
    # iterarte row
    for i in range(len(matrix)):
        # if element is not 0, make it -1, whole column
        if matrix[i][col] != 0:
            matrix[i][col] = -1


def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()
    print("=======================")


def setMatrixZerosBetter(matrix):
    """ T(C) -> O(N*M) + O(N*M) => O(2*N*M), S(C) -> O(N) + O(M) """

    # take extra row and column array to keep track which elements to mark 0
    row_arr = [0] * len(matrix)
    col_arr = [0] * len(matrix[0])
    
    # iterate matrix and mark 1 in row_arr or col_arr
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row_arr[i] = 1
                col_arr[j] = 1

    # iterate matrix again and mark element in matrix based on row_arr or col_arr
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if row_arr[i] == 1 or col_arr[j] == 1:
                matrix[i][j] = 0


def setMatrixZerosOptimal(matrix):
    """ T(C) -> O(N*M) + O(N*M), S(C) -> O(1) """

    row = len(matrix)
    col = len(matrix[0])
    # rowarray = matrix[...][0], colarray = matrix[0][....] and col0

    # for tracking first column
    col0 = 1 
    # identify where 0 present, mark 0 in first row, first column and col0 variable
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                # mark in row array
                matrix[i][0] = 0
                if j != 0:
                    # marking in column array or col0 variable
                    matrix[0][j] = 0
                else:
                    col0 = 0
                

    # reiterate matrix except first row and first colum and make elements 0,, by looking at rowarray or colarray if 0 is present                
    for i in range(1, row):
        for j in range(1, col):
            # if current element is already not 0
            if matrix[i][j] != 0:
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

    # make entire first row as 0 based on matrix[0][0]
    if matrix[0][0] == 0:
        for j in range(1, col):
            matrix[0][j] = 0

    # make entire first column as 0 based on col0
    if col0 == 0:
        for i in range(row):
            matrix[i][0] = 0



if __name__ == "__main__":
    matrix = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
    printMatrix(matrix)
    setMatrixZeros(matrix)
    printMatrix(matrix)
    matrix = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
    print(matrix)
    setMatrixZerosBetter(matrix)
    printMatrix(matrix)
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print(matrix)
    setMatrixZerosOptimal(matrix)
    printMatrix(matrix)

    """
    [[1,1,1,1]      
     [1,0,0,1]
     [1,1,0,1]
     [1,1,1,1]
    ]
 
    => 

    [[1,0,0,1]      
     [0,0,0,0]
     [0,0,0,0]
     [1,0,0,1]
    ]

    """