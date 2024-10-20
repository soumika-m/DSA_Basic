"""
    A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
    The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
    If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in 
    ascending order).

    https://leetcode.com/problems/next-permutation/
"""

def nextPermutation(nums):
    """ T(c) -> O(n), S(c) -> O(1) """
    # using longest prefix match
    break_point = -1
    
    i = len(nums)-2
    while i >= 0:
        if nums[i] < nums[i+1]:
            break_point = i
            break
        i = i - 1
    
    # no break point found
    if break_point == -1:
        # reverse the array, as that permutation is last permutation possible, make it as first permutation
        nums.reverse()
    else:
        j = len(nums)-1
        # find smallest number which is bigger than break_point number
        while j > i:
            if nums[j] > nums[break_point]:
                # swap elements
                nums[j] , nums[break_point] = nums[break_point] , nums[j]
                break
            j = j - 1
        
        # reverse remaining elements after breakpoint
        start = break_point + 1
        end = len(nums)-1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


arr = [2, 1, 5, 4, 3, 0, 0]
print(arr)
nextPermutation(arr)
print(arr)
arr = [3, 2, 1]
print(arr)
nextPermutation(arr)
print(arr)
