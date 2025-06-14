"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

def find_minimum_in_rotated_sorted_array(arr):
    """ T(C) -> O(logn), S(C) -> O(1) """

    # find the minimum element in rotated sorted array
    mini = arr[0]
    low = 0
    high = len(arr) - 1

    # sorted half may or may not have true answer

    while low <= high:
        mid = (low + high) // 2

        # if search is already sorted, arr[low] will be minimum always
        if arr[low] < arr[high]:
            mini = min(mini, arr[low])
            break

        # find which part is sorted
        # check if left part is sorted
        if arr[low] <= arr[mid]:
            # if left part is sorted, then the minimum element might be in left part
            mini = min(mini, arr[low])
            # eliminate left, check at the right part
            low = mid + 1
        else:
            # if right part is sorted, then minimum element might be in right part
            mini = min(mini, arr[mid])
            # eliminate right, check at the left part
            high = mid - 1
        
    return mini


def find_minimum_in_rotated_sorted_array_with_duplicate(arr):
    """ T(C) -> O(logn), S(C) -> O(1) """

    # if there are duplicates, then we need to check for duplicates
    mini = arr[0]
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        # if left part is sorted, then arr[low] will be minimum
        if arr[low] <= arr[mid]:
            mini = min(mini, arr[low])
            # eliminate left part, check at right part
            low = mid + 1
        # if right part is sorted, then arr[mid] will be minimum
        else:
            mini = min(mini, arr[mid])
            # eliminate right part, check at left part
            high = mid - 1

    return mini


if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2]
    print(find_minimum_in_rotated_sorted_array(arr)) # Expected output: 0
    arr = [3, 4, 5, 1, 2]
    print(find_minimum_in_rotated_sorted_array(arr)) # Expected output: 1
    arr = [11, 13, 15, 17]
    print(find_minimum_in_rotated_sorted_array(arr)) # Expected output: 11
    arr = [2, 2, 2, 0, 1]
    print(find_minimum_in_rotated_sorted_array_with_duplicate(arr)) # Expected output: 0
    arr = [3, 3, 3, 1, 2, 2, 2, 2, 3, 3]
    print(find_minimum_in_rotated_sorted_array_with_duplicate(arr)) # Expected output: 1