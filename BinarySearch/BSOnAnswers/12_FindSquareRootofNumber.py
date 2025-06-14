import math
print(math.sqrt(36))

def find_square_root(num):
    """ T(C) -> O(n), S(C) -> O(1) """

    ans = 1
    for i in range(num):
        if i*i <= num:
            ans = i
        else:
            break
    
    return ans


def find_square_root_optimal(num):
    """ T(C) -> O(logn), S(C) -> O(n) """

    ans = 0
    low = 1
    high = num


    while low <= high:
        mid = (low + high) // 2
        # if square is less than number given, we are in the portion where valid answers present
        if mid * mid <= num:
            ans = mid
            # check for more answers in right part
            low = mid + 1
        # we are in the part, where valid answer is not present, look for left part
        else:
            high = mid - 1

    
    # return ans
    return high


if __name__ == "__main__":
    num = 37
    print(find_square_root(num))
    print(find_square_root_optimal(num))