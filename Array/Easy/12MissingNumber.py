"""
https://leetcode.com/problems/missing-number/description/
"""

def missingNumber(nums):
    """ T(C) -> O(n^2), S(C) -> O(1) """

    n = len(nums)

    # check which number is missing in array from 0 to n
    for i in range(n+1):
        found = 0
        for j in range(n):
            if i == nums[j]:
                found = 1
                break
        
        # missing number
        if found == 0:
            return i
            
    return 0


def missingNumberBetter(nums):
    """ T(C) -> O(n) + O(n) = O(2n), S(C) -> O(n) """

    n = len(nums)

    # using hash array to keep track of missing element
    hash_arr = [0] * (n+1)

    # check and mark element in hash array, if it is present
    for i in range(n):
        hash_arr[nums[i]] = 1
    
    # iterate hash array and check which is missing
    for i in range(n+1):
        if hash_arr[i] == 0:
            return i
    
    return 0


def missingNumberOptimal1(nums):
    """ T(C) -> O(n), S(C) -> O(1) """

    n = len(nums)

    # calculate sum of first n natural numbers
    sum_of_num_range = n * (n+1) // 2

    sum_of_arr_num = 0
    # calculate sum of array numbers
    for i in range(n):
        sum_of_arr_num += nums[i]

    return sum_of_num_range - sum_of_arr_num


def missingNumberOptimal2(nums):
    """ T(C) -> O(n), S(C) -> O(1) """

    # using xor operator
    n = len(nums)

    xor1 = 0
    xor2 = 0        
    
    for i in range(n):
        # xor of first n number
        xor1 = xor1 ^ i
        # xor of array elements
        xor2 = xor2 ^ nums[i]

    # add n to xor1
    xor1 = xor1 ^ n

    return xor1 ^ xor2


if __name__ == "__main__":
    arr = [9,6,4,2,3,5,7,0,1]
    print(arr)
    print("Missing number = ", missingNumber(arr))
    print("Missing number = ", missingNumberBetter(arr))
    print("Missing number = ", missingNumberOptimal1(arr))
    print("Missing number = ", missingNumberOptimal2(arr))
