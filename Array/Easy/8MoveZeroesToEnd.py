"""
https://leetcode.com/problems/move-zeroes/
"""

def moveZeroes(nums):
    """ T(c) -> O(n) + O(k) + O(n-k) = O(2n) , S(c) -> O(k) or O(n) """

    n = len(nums)
    temp = []

    # add non zero elements to temp array
    for num in nums:
        if num != 0:
            temp.append(num)

    non_zero = len(temp)

    # add elements from temp array to nums array from starting
    for i in range(non_zero):
        nums[i] = temp[i]

    # add zeros to remaining elements in nums
    for i in range(non_zero, n):
        nums[i] = 0


def moveZeroesOptimal(nums):
    """ T(c) -> O(n), S(c) -> O(1) """

    n = len(nums)

    z_pointer = -1
    # find zero element
    for i in range(n):
        if nums[i] == 0:
            z_pointer = i
            break
    
    # if no zero element found
    if z_pointer == -1:
        return

    # take 2 pointer z_pointer and nz_pointer, nz_pointer will point to non zero element after z_pointer
    # iterate the array, non zero pointer will always move
    for nz_pointer in range(z_pointer+1, n):
        if nums[nz_pointer] != 0:
            # swap zero with non zero elements in array
            nums[nz_pointer], nums[z_pointer] = nums[z_pointer], nums[nz_pointer]
            z_pointer += 1


if __name__ == "__main__":
    nums = [0,1,0,3,12]
    print(nums)
    moveZeroes(nums)
    print(nums)
    nums=[0,0,0,1,3,4]
    print(nums)
    moveZeroesOptimal(nums)
    print(nums)
