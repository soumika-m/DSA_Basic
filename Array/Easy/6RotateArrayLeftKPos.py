def rotateLeft(nums, k):
    """ T(c) -> O(k) + O(n-k) + O(k) = O(n+k), S(c) -> O(k) """

    n = len(nums)

    # multiple of n will result in same array
    k = k % n

    # temp array
    temp = [0] * k

    # move starting k elements to temp array
    for i in range(0, k):
        temp[i] = nums[i]

    # move next n-k elements to left
    for i in range(k, n):
        nums[i-k] = nums[i]

    # move d elements from temp array to end
    for i in range(n-k, n):
        nums[i] = temp[i - (n-k)]


def rotateLeftOptimal(nums, k):
    """ T(c) -> O(k) + O(n-k) + O(n) = O(2n), S(c) -> O(1) """

    n = len(nums)

    # reverse left part of array k
    reverse(nums, 0, k-1)

    # reverse right part of array n-k
    reverse(nums, k, n-1)

    # reverse entire array n
    reverse(nums, 0, n-1)


def reverse(nums, start, end):
    while start <= end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    print(nums, k)
    rotateLeft(nums, k)
    print(nums)

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 2
    print(nums, k)
    rotateLeftOptimal(nums, k)
    print(nums)