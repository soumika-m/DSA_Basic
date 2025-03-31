"""
https://leetcode.com/problems/rotate-image/description/
n X n square matrix
"""

def rotate(matrix):
    """ T(C) -> O(N^2), S(C) -> O(N^2) """

    row = len(matrix)
    col = len(matrix[0])
    # using extra 2d matrix
    result = [[0] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            result[j][col-1-i] = matrix[i][j]
    
    return result


def rotateEfficient(matrix):
    """ T(C) -> O(N/2 * N/2) + O(N * N/2), S(c) -> O(1) """

    n = len(matrix)

    # transpose matrix
    for i in range(n-1):
        for j in range(i+1, n):
            # swap elements
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 

    # reverse each row of matrix using 2 pointer approach
    for i in range(n):
        # left = 0
        # right = n-1
        # while left<right:
        #     matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
        #     left += 1
        #     right -= 1

        matrix[i].reverse()

    return matrix


if __name__ == "__main__":
    mat = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print(mat)
    print(rotate(mat))

    print(rotateEfficient(mat))
