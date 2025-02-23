"""
https://leetcode.com/problems/single-number/
"""

def singleNumber(nums):
    """ T(C) -> O(N^2), S(C) -> O(1) """

    n = len(nums)

    # check count of each number if array
    for num in nums:
        cnt = 0
        for i in range(n):
            if nums[i] == num:
                cnt += 1

        # if unique element found
        if cnt == 1:
            return num

    return 0


def singleNumberEfficient(nums):
    """ T(C) -> O(N) + O(N/2)+1 , S(C) -> O(N/2)+1 """

    n = len(nums)
    # Dictionary to store counts
    mapp = {}

    # First loop: Count occurrences of each number
    for i in range(n):
        mapp[nums[i]] = mapp.get(nums[i], 0) + 1
    
    # Second loop: Find the element that appears once
    for key,value in mapp.items():
        if value == 1:
            return key

    return 0


def singleNumberOptimal(nums):
    """ T(c) -> O(N), S(C) -> O(1) """

    xor = 0
    # xor of two same number will be 0, xor of 0 and number will be that number
    for num in nums:
        xor = xor ^ num

    return xor


if __name__ == "__main__":
    arr = [4,1,2,1,2]
    print(arr)
    print(singleNumber(arr))
    print(singleNumberEfficient(arr))
    print(singleNumberOptimal(arr))
