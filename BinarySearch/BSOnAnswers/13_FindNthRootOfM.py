"""
M = 27, N = 3, 3root27 = 3 | 3*3*3 = 27
M = 69, N = 4, 4root69 = -1 | 1*1*1*1 = 1, 2*2*2*2 = 16, 3*3*3*3 = 81
"""

def find_nth_root_of_m(m, n):
    """ T(C) -> O(m * n) or O(m * logn), S(C) -> O(1) """

    # check which number nth root is matching with m
    for i in range(1, m):
        if(find_pow_optimized(i, n) == m):
            return i
        elif(find_pow_optimized(i, n) > m):
            break
        
    return -1


def find_pow(elem, num):
    """ T(C) -> O(n) """
    res = 1
    for _ in range(num):
        res *= elem
    return res


def find_pow_optimized(elem, pw):
    """ T(C) -> O(logn) """
    ans = 1
    while pw > 0:
        # if power is odd
        if pw % 2 == 1:
            ans = ans * elem
            pw = pw - 1
        # if power is even
        else:
            pw = pw // 2
            elem = elem * elem

        # if power is negative
        if pw < 0:
            ans = 1 / ans
    
    return ans


def find_nth_root_of_m_binary_search(m, n):
    """ T(C) -> O(logm * logn), S(C) -> O(1) """

    # using binary search on answers
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        ans = find_pow_optimized(mid, n)
        # found root
        if ans == m:
            return mid
        # go to left, move high
        elif ans > m:
            high = mid - 1
        # go to right
        else:
            low = mid + 1
    
    return -1


def find_pow_large_number(elem, num, m):
    """ T(C) -> O(n) """
    res = 1
    for _ in range(num):
        res *= elem
        # if answer larger than m, break
        if res > m:
            return 2
    # if root found
    if res == m:
        return 1
    # if res < m
    return 0


def find_nth_root_of_m_binary_search_overflow(m, n):
    """ T(C) -> O(logm * n), S(C) -> O(1) """

    # for larger test cases
    # using binary search on answers
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        mid_ans = find_pow_large_number(mid, n, m)
        # found root
        if mid_ans == 1:
            return mid
        # go to left, move high
        elif mid_ans == 2:
            high = mid - 1
        # go to right
        else:
            low = mid + 1
    
    return -1


if __name__ == "__main__":
    m = 27
    n = 3
    print(find_nth_root_of_m(m, n))
    print(find_nth_root_of_m_binary_search(m, n))
    print(find_nth_root_of_m_binary_search_overflow(m,n))
    m = 69
    m = 4
    print(find_nth_root_of_m(m, n))
    print(find_nth_root_of_m_binary_search(m, n))
    print(find_nth_root_of_m_binary_search_overflow(m,n))
