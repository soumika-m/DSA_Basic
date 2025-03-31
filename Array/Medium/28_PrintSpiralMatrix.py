"""
https://leetcode.com/problems/spiral-matrix/description/
m X n matrix
"""

def spiralOrder(matrix):
    """ T(C) -> O(M X N), S(C) -> O(M X N) """

    row = len(matrix)
    col = len(matrix[0])

    result = []

    # using 4 pointers
    top = 0
    bottom = row-1
    left = 0
    right = col-1

    # if atleast one row and one column present
    while top <= bottom and left <= right:
        # go to right side
        for i in range(left, right+1):
            result.append(matrix[top][i])

        top += 1

        # go to down
        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        
        right -= 1

        # if atleast one row left
        if top <= bottom:
            # go to left
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            
            bottom -= 1

        # if atleast one column left
        if left <= right:
            # go to top
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])

            left += 1

    return result


if __name__ == "__main__":
    mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(mat)
    res = spiralOrder(mat)
    print(res)
