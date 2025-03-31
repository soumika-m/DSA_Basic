"""
https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1
"""


def leaders(arr):
    """ T(C) -> O(), S(C) -> O() """

    n = len(arr)
    # store all leaders
    leader = []
    
    # last element will be always leader
    leader.append(arr[n-1])
    
    max_elem = arr[n-1]
    # iterate array from right, find if any element is >= max elem found from right
    for i in range(n-2, -1, -1):
        if arr[i] >= max_elem:
            leader.append(arr[i])
            max_elem = arr[i]

    # reverse list while returning       
    return leader[::-1]


if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    print(arr)
    print(leaders(arr))
    print("================")
    arr = [61, 61, 17]
    print(arr)
    print(leaders(arr))
