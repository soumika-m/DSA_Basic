"""
Find which  number is repeating and missing from 1 to n in array
"""

def findRepeatingMissing(arr, n):
    """ T(C) -> O(n^2), S(C) -> O(1) """

    missing = -1
    repeating = -1

    # check count of number from 1 to n
    for i in range(1, n+1):
        cnt = 0
        for j in range(len(arr)):
            if i == arr[j]:
                cnt += 1
        
        # find missing or repeating number
        if cnt == 2:
            repeating = i

        elif cnt == 0:
            missing = i

        # if both missing and repeating number found
        if repeating != -1 and missing != -1:
            break

    return [repeating, missing]   


def findRepeatingMissingBetter(arr, n):
    """ T(C) -> O(2n), S(C) -> O(n) """

    # take a hasharray for keeping value and key as index
    hasharr = [0] * (n+1)

    # check count of number from 1 to n
    for i in range(len(arr)):
        # count numbers in hasharray
        hasharr[arr[i]] += 1

    missing = -1
    repeating = -1
        
    # find missing or repeating number
    for i in range(1, len(hasharr)):
        if hasharr[i] == 2:
            repeating = i

        elif hasharr[i] == 0:
            missing = i

        # if both missing and repeating number found
        if repeating != -1 and missing != -1:
            break

    return [repeating, missing]


def findRepeatingMissingOptimal(arr, n):
    """ T(C) -> O(n), S(C) -> O(1) """

    # using math equations
    # S - SN = x - y
    SN = (n * (n+1)) // 2
    S2N = (n * (n+1) * ((2*n)+1)) // 6

    # sum of array number
    S = 0
    # sum of squares of array number
    S2 = 0
    
    for i in range(len(arr)):
        S += arr[i]
        S2 += (arr[i] * arr[i])
    
    # x - y = val1
    val1 = S-SN
    # x^2 - y^2 = (x+y)(x-y) = val2
    val2 = S2 - S2N
    # x + y = val2 / (x-y)
    val2 = val2 // val1

    # 2x = val1 + val2
    # rpeating = (val1 + val2) // 2
    x = (val1 + val2) // 2

    # x-y = val1 => y = x - val1
    # missing = repeating - val1
    y = x - val1

    # repeating, missing
    return [x, y]


if __name__ == "__main__":
    arr = [4,3,6,2,1,1]
    n = 6
    print("missing -> repeating")
    print(findRepeatingMissing(arr, n))
    print(findRepeatingMissingBetter(arr, n))
    print(findRepeatingMissingOptimal(arr, n))