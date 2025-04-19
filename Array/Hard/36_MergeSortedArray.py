"""
Merge two sorted array, put elements in arr1 and arr2 after sorting
[1,3,5,7] [0,2,6,8,9] => [0,1,2,3] [5,6,7,8,9]
"""

def mergeArray(nums1, m, nums2, n):
    """ T(C) -> O(n+m) + O(n+m), S(C) -> O(n+m) """

    left = 0
    right = 0
    index = 0
    # taking a buffer array of size m+n
    temp = [0] * (m+n)

    # if both array element exist
    while left<m and right<n:
        # put smaller element in buffer array
        if nums1[left] <= nums2[right]:
            temp[index] = nums1[left]
            index += 1
            left += 1
        else:
            temp[index] = nums2[right]
            index += 1
            right += 1

    # if element left in first array, put in buffer
    while left<m:
        temp[index] = nums1[left]
        index += 1
        left += 1

    # if element left in second array, put in buffer
    while right<n:
        temp[index] = nums2[right]
        index += 1
        right += 1

    # copy elements from temp array to nums1 and nums2 array
    for p in range(len(temp)):
        if p < m:
            nums1[p] = temp[p]
        else:
            nums2[p-m] = temp[p]

    
def mergeArrayOptimal1(nums1, m, nums2, n):
    """ T(C) -> O(min(m,n)) + O(mlogm) + O(nlogn), S(C) -> O(1) """

    # put one pointer on last element of arr1, and another on first element of arr2
    left = m-1
    right = 0

    # compare, left element should be lesser than right, otherwise swap
    while left >= 0 and right < n:
        if nums1[left] > nums2[right]:
            nums1[left], nums2[right] = nums2[right], nums1[left]
            left -= 1
            right += 1
        # if lesser, as array is sorted, other elements also will be fine, break
        else:
            break

    # sort array 1
    nums1.sort()
    # sort array 2
    nums2.sort()


def mergeArrayOptimal2(nums1, m, nums2, n):
    """ T(C) -> O(log(m+n)) * O(m+n) , S(C) -> O(1) """

    # using shell sort gap method, consider both array as a single array
    # len of the imaginary single array
    length = m+n
    # ceil of 5/2 = 2.5 = 3
    gap = (length // 2) + (length % 2)

    # iterate until gap > 0
    while gap > 0:
        # use 2 pointer
        left = 0
        right = left + gap

        # check until right cross boundary
        while right < length:

            # left should be lesser and right should be greater, else swap
            # case 1: when left is on arr1, right is on arr2
            if left < m and right >= m:
                # swap if left is greater
                if nums1[left] > nums2[right-m]:
                    nums1[left], nums2[right-m] = nums2[right-m], nums1[left]
            
            # case 2: both are on arr2
            # left-m as both are in arr2
            elif left >= m:
                # swap if left is greater
                if nums2[left-m] > nums2[right-m]:
                    nums2[left-m], nums2[right-m] = nums2[right-m], nums2[left-m]
            
            # case 3: both are on arr1
            else:
                # swap if left is greater
                if nums1[left] > nums1[right]:
                    nums1[left], nums1[right] = nums1[right], nums1[left]

            left += 1
            right += 1

        # break if iteration gap=1 is completed
        if gap == 1:
            break

        # Otherwise, calculate new gap
        gap = (gap // 2) + (gap % 2)


if __name__ == "__main__":
    arr1 = [1,2,3]
    m = 3
    arr2 = [2,5,6]
    n = 3
    print(arr1, arr2)
    mergeArray(arr1, m, arr2, n)
    print(arr1, arr2)
    print("=====================")
    arr1 = [1,3,5,7]
    arr2= [0,2,6,8,9]
    print(arr1, arr2)
    mergeArrayOptimal1(arr1, 4, arr2, 5)
    print(arr1, arr2)
    print("=====================")
    arr1 = [1,3,5,7]
    arr2= [0,2,6,8,9]
    print(arr1, arr2)
    mergeArrayOptimal2(arr1, 4, arr2, 5)
    print(arr1, arr2)
    print("=====================")
