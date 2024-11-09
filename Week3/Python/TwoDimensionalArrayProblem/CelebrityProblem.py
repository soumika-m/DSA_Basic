"""
    A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by some 
    people.  A square matrix mat (n*n) is used to represent people at the party such that if an element of row i and column 
    j is set to 1 it means ith person knows jth person. You need to return the index of the celebrity in the party, if the 
    celebrity does not exist, return -1.

    https://www.geeksforgeeks.org/problems/the-celebrity-problem/1?page=1&difficulty%255B%255D=1
"""

def celebrity(mat):
    """ T(c) -> O(N*N) + O(N), S(c) -> O(N+N) => O(2N)"""
    n = len(mat)
    # knowme array will keep count of how many persons knows that index
    knowme_arr = [0] * n
    # iknow array will keep count of how many persons known by that index
    iknow_arr = [0] * n
    
    for i in range(n):
        for j in range(n):
            # might be celebrity, add in corresponding array
            if mat[i][j] == 1:
                knowme_arr[j] += 1
                iknow_arr[i] += 1
    
    # check which index is known by n-1 persons and who knows 0 persons            
    for i in range(n):
        if knowme_arr[i] == n-1 and iknow_arr[i] == 0:
            return i
    
    return -1


def celebrityEfficient(mat):
    """ T(c) -> O(N) + O(N) => O(2N), S(c) -> O(1)"""
    n = len(mat)
    # using top and down pointer
    top = 0
    down = n-1

    while top < down:
        # top knows down, top can not be a celebrity
        if mat[top][down] == 1:
            top = top + 1
        # down know top, down can not be my celebrity
        elif mat[down][top] == 1:
            down = down - 1
        # top don't know down and down don't know top, both can not become celebrity
        else:
            top = top + 1
            down = down - 1
            
    # no celebrity found
    if top > down:
        return -1
        
    # check celebrity row and column, top don't know i, but i knows top
    for i in range(n):
        if i != top:
            if mat[top][i] == 0 and mat[i][top] == 1:
                continue
            else:
                return -1
            
    return top


m1 = [[0, 1, 0],[0, 0, 0], [0, 1, 0]]
print(m1)
print(celebrity(m1))
m2 = [[0, 1],[1, 0]]
print(m2)
print(celebrityEfficient(m2))
