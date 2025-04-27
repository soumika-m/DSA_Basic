"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""

def search_in_duplicate(nums, target):
    """ T(C) -> O(logn) //average O(n/2) //worst, S(C) -> O(n) """

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        
        # trim down search space
        if nums[low] == nums[mid] == nums[high]:
            low = low + 1
            high = high - 1
            continue

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

    return False


if __name__ == "__main__":
    nums = [7,8,1,2,3,3,3,4,5,6]
    target = 3
    print(search_in_duplicate(nums, target))
