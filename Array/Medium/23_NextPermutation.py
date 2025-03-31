"""
https://leetcode.com/problems/next-permutation/description/
"""

def nextPermutation(nums):
    """ T(C) -> O(N) + O(N) + O(N) = O(3N), S(C) -> O(1) """

    # using longest prefix match
    n = len(nums)

    # find breakpoint from end where num[i] < num[i+1]
    breakpoint_idx = -1
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            breakpoint_idx = i
            break
    
    # if breakpoint not present, that is last permutation, just reverse that number
    if breakpoint_idx == -1:
        nums = reverseArr(nums, 0, n-1)
        return nums

    # find next greater permutation, check from end of array, and find minimum number which is greater than breakpoint, swap it with breakpoint
    for i in range(n-1, breakpoint_idx, -1):
        if nums[i] > nums[breakpoint_idx]:
            temp = nums[i]
            nums[i] = nums[breakpoint_idx]
            nums[breakpoint_idx] = temp
            break

    # reverse the right half
    nums = reverseArr(nums, breakpoint_idx+1, n-1)

    return nums


def reverseArr(nums, start, end):
    i = start
    j = end
    while i < j:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i += 1
        j -= 1

    return nums


if __name__ == "__main__":
    arr1 = [1,3,2]
    print(arr1)
    print(nextPermutation(arr1))
    print("======================")
    arr2 = [3,2,1]
    print(arr2)
    print(nextPermutation(arr2))