"""
https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1
"""

def findUnion(a, b):
    """ T(c) -> O((m+n)log(m+n)) , S(c) -> O(m+n)"""
    freq = {}
    union = []
    
    for num in a:
        freq[num] = freq.get(num, 0) + 1
    
    for num in b:
        freq[num] = freq.get(num, 0) + 1
        
    # sort the dictionary and create a array
    union = sorted(freq.keys())
    
    return union


def findUnion2(a,b):
    """ T(c) -> O((m+n)log(m+n)) , S(c) -> O(m+n)"""
    st = set()
    union = []
    
    for num in a:
        st.add(num)
    
    for num in b:
        st.add(num)
    
    # sort the set and make one array
    union = sorted(st)
    
    return union


def findUnionEfficient(a,b):
    """ T(c) -> O(m+n), S(c) -> O(m+n) // for returning the array """
    # using 2 pointers
    i = 0
    j = 0
    
    unionArr = []

    while i<len(a) and j<len(b):
        if a[i] <= b[j]:
            # before inserting new element check if it is matching with last element in array
            if len(unionArr) == 0 or unionArr[-1] != a[i]:
                unionArr.append(a[i])
            i += 1
        else:
            if len(unionArr) == 0 or unionArr[-1] != b[j]:
                unionArr.append(b[j])
            j += 1
    
    # if any elements present in array a    
    while i<len(a):
        if unionArr[-1] != a[i]:
            unionArr.append(a[i])
        i += 1
    
    # if any elements present in array b
    while j<len(b):
        if unionArr[-1] != b[j]:
            unionArr.append(b[j])
        j += 1
            
    return unionArr