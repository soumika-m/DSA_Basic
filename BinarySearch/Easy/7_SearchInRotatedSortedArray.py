"""
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""

def search(nums, target):
    """ T(C) -> O(logn), S(C) -> O(n) """

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        
        # check if left part is sorted
        if nums[low] <= nums[mid]:
            # check if number is present in left sorted part
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # check if right part is sorted
        else:
            # check if number is present in right sorted part
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(search(nums, target))
