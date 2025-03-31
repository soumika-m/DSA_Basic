"""
https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
"""

def rearrangeArray(nums):
    """ T(C) -> O(N) + O(N/2), S(C) -> O(N) """

    pos = []
    neg = []

    # take elements and put it in positive or negative array after checking
    for num in nums:
        if num < 0:
            neg.append(num)
        else:
            pos.append(num)

    # take element from pos and neg array and put those in alternate places
    for i in range(len(nums)//2):
        nums[i*2] = pos[i]
        nums[i*2+1] = neg[i]

    return nums


def rearrangeArrayOptimal(nums):
    """ T(C) -> O(N), S(C) -> O(N) """

    res = [0] * len(nums)
    posIdx = 0
    negIdx = 1

    # take elements and put it in alternate place
    for num in nums:
        if num > 0:
            res[posIdx] = num
            posIdx += 2
        else:
            res[negIdx] = num
            negIdx += 2

    return res


def rearrangeArrayVariety2(nums):
    """ T(C) -> O(N) + O(N) = O(2N), S(C) -> O(N) """

    # when positive and negative numbers are not equally stored
    pos = []
    neg = []

    # put elements from array to positive or negative array
    for num in nums:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)
    
    # check equal elements first from array, then remaining elements
    if len(pos) > len(neg):
        for i in range(len(neg)):
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]

        idx = len(neg) * 2
        j = len(neg)
        while j < len(pos):
            nums[idx] = pos[j]
            idx += 1
            j += 1
        
    else:
        for i in range(len(pos)):
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]

        idx = len(pos) * 2
        j = len(pos)
        while j < len(neg):
            nums[idx] = neg[j]
            idx += 1
            j += 1

    return nums


if __name__ == "__main__":
    arr = [3,1,-2,-5,2,-4]
    print("=========>", arr)
    print(rearrangeArray(arr))
    print(rearrangeArrayOptimal(arr))
    print("============================")
    arr = [-1,2,3,4,-3,1,-2,-5,6,7]
    print("=========>", arr)
    print(rearrangeArrayVariety2(arr))
