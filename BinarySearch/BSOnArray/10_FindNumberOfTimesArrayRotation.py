def find_number_of_times_array_rotation(arr):
    """ T(C) -> O(logn), S(C) -> O(1) """

    # using find minimum number solution
    mini = arr[0]
    index = -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        # if search space is already sorted
        if arr[low] <= arr[high]:
            if arr[low] < mini:
                mini = arr[low]
                index = low
            break

        # find which part is sorted left/right
        if arr[low] <= arr[mid]:
            # if left part is sorted, then arr[low] will be minimum
            if arr[low] < mini:
                mini = arr[low]
                index = low
            # eliminate left part, check at right part
            low = mid + 1
        # if right part is sorted, then arr[mid] will be minimum
        else:
            if arr[mid] < mini:
                mini = arr[low]
                index = low
            # eliminate right part, check at left part
            high = mid - 1

    return index


if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2]
    print(find_number_of_times_array_rotation(arr)) # Expected output: 4
    arr = [3, 4, 5, 1, 2]
    print(find_number_of_times_array_rotation(arr)) # Expected output: 3
