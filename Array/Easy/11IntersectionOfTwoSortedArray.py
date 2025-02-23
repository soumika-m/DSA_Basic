"""
In insertion duplicate elements are allowed
"""

def findIntersection(arr1, arr2):
    """ T(c) -> O(m * n), S(c) -> O(n) + O(m+n) // for returning result array """

    resultArr = []
    visitedArr = [0]*len(arr2)

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            # if element of arr2 is not matched with some other element of arr1
            if arr1[i] == arr2[j] and visitedArr[j] == 0:
                resultArr.append(arr1[i])
                visitedArr[j] = 1
                break

            # if element of arr2 is greater that arr1, stop the loop as it is sorted
            if arr2[j] > arr1[i]:
                break

    return resultArr


def findIntersectionEfficient(arr1, arr2):
    """ T(c) -> O(m+n), S(c) -> O(m+n) // for returning result array """
    # using 2 pointer
    i = 0
    j = 0

    unionArr = []

    while i<len(arr1) and j<len(arr2):
        if arr1[i] == arr2[j]:
            unionArr.append(arr1[i])
            i += 1
            j += 1
        
        elif arr1[i] < arr2[j]:
            i += 1

        else:
            j += 1

    return unionArr


A = [1,2,2,3,3,4,5,6]
B = [2,3,3,5,6,6,7]

print("A = ", A)
print("B = ", B)
print("Result = ", findIntersection(A, B))
print("Result = ", findIntersectionEfficient(A, B))
