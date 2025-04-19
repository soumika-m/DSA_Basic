"""
https://leetcode.com/problems/pascals-triangle/description/
"""

### given row and column number, return number present at that place 
def getPascalNumber(n, r):
    """ T(C) -> O(r), S(C) -> O(1) """

    # n-1Cr-1
    n = n - 1
    r = r - 1

    result = 1
    
    # Using formula ncr = n! / (r! * (n-r)!)
    for i in range(r):

        # 10/1 * 9/2 * 8/3
        result = result * (n-i)
        result = result // (i+1)

    return result

### given row number, print that row from pascal triangle
def printPascalRow(n):
    """ T(C) -> O(n * r), S(C) -> O(1) """

    for c in range(1, n+1):
        print(getPascalNumber(n, c), end=" ")

    print()


### given row number, print that row from pascal triangle
def printPascalRowOptimal(row):
    """ T(C) -> O(n), S(C) -> O(1) """

    ans = 1
    print(1, end=' ')

    # using fomula after analysing
    for col in range(1, row):
        ans = ans * (row - col)
        ans = ans // col
        print(ans, end=' ')

    print()


### given row number, print that whole traingle
def printPascalTriangle(n):
    """ T(C) -> O(n*n*r) => O(n^3),  S(C) -> O(1) //as we are just returning answer """

    result = []
    # row
    for r in range(1, n+1):
        temp_list = []
        # column
        for c in range(1, r+1):
            temp_list.append(getPascalNumber(r, c))

        result.append(temp_list)
    
    return result


### given row number, print that whole traingle
def printPascalTriangleOptimal(n):
    """ T(C) -> O(n*n) => O(n^2),  S(C) -> O(1) """

    for r in range(1, n+1):
        printPascalRowOptimal(r)



if __name__ == '__main__':
    # 0 based indexing
    row = 11
    column = 4
    print(getPascalNumber(row, column))
    printPascalRow(5)
    printPascalRowOptimal(5)
    print(printPascalTriangle(6))
    printPascalTriangleOptimal(6)

