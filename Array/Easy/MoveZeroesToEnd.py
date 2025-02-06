"""
https://leetcode.com/problems/move-zeroes/
"""

def moveZeroes(nums):
    """ T(c) -> O(n), S(c) -> O(1) """

    n = len(nums)
    z_pointer = -1

    for i in range(n):
        if nums[i] == 0:
            z_pointer = i
            break
    
    if z_pointer == -1:
        return

    # non zero pointer will always move
    for nz_pointer in range(z_pointer+1, n):
        if nums[nz_pointer] != 0:
            # swap zero with non zero elements
            temp = nums[nz_pointer]
            nums[nz_pointer] = nums[z_pointer]
            nums[z_pointer] = temp
            z_pointer += 1
            nz_pointer += 1
