"""
https://leetcode.com/problems/maximum-product-subarray/description/
"""

def maxProduct(nums):
    """ T(C) -> O(n^2), S(C)-> O(1) """

    # generate all subarray, calculate product
    maxi = float('-inf')
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):
            product *= nums[j]
            maxi = max(maxi, product)

    return maxi


def maxProductOptimal(nums):
    """ T(C) -> O(n), S(C) -> O(1) """

    # using observation
    # case1: all positive - multiple all
    # case2: even negative - multiply all
    # case3: odd negative - discard one negative to make it even negative
    # case4: zero - ignore, make product 1

    n = len(nums)

    # using suffix, prefix method
    maxi = float('-inf')
    prefix = 1
    suffix = 1

    # iterate array
    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1

        # calculate prefix from starting
        prefix = prefix * nums[i]
        # calculate suffix from end
        suffix = suffix * nums[n-i-1]

        # calculate max product
        maxi = max(maxi, max(prefix, suffix))

    return maxi


if __name__ == "__main__":
    # arr = [1, 2, -3, 0, -4, -5]
    arr = [1, 2, -3, 0, -4, 25]
    print(arr)
    print(maxProduct(arr))
    arr = [3,0,2,-1,4,-6,3,-2,6]
    print(arr)
    ### max product subarray is [4,-6,3,-2,6] 
    print(maxProductOptimal(arr))
