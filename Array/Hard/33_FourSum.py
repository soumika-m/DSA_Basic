"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

https://leetcode.com/problems/4sum/description/
"""

from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    """ T(C) -> O(N^4), S(C) -> O(2* no. of unique quadruplets) """

    # use set for storing only unique quads
    st = set()

    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        # sort to avoid duplicate quads
                        temp.sort()
                        st.add(tuple(temp))
    
    # from set add in list for returning
    result = [list(item) for item in st]
    return result


def fourSumBetter(nums: List[int], target: int) -> List[List[int]]:
    """ T(C) -> O(N^3), S(C) -> O(2* no. of unique quadruplets) """

    # set for storing unique quads
    st = set()
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            # store elements between j and k
            hset = set()
            for k in range(j+1, n):
                forth = target - (nums[i] + nums[j] + nums[k])
                # if element present in hash set, make quads
                if forth in hset:
                    temp = [nums[i], nums[j], nums[k], forth]
                    # sort array elements to avoid duplicates
                    temp.sort()
                    st.add(tuple(temp))

                # add element in hash set
                hset.add(nums[k])

    result = [list(item) for item in st]
    return result


def fourSumOptimal(nums: List[int], target: int) -> List[List[int]]:
    """ T(C) -> O(N^2 * N) => O(N^3), S(C) -> O(no. of quadruplets) """

    n = len(nums)

    result = []

    # sort array
    nums.sort()

    # keep i and j fixed, move k and l
    for i in range(n):
        # if it is not first element of i, exclude repeated elements of i
        if i > 0 and nums[i] == nums[i-1]:
            continue 

        for j in range(i+1, n):
            # if it is not first element of j, exclude repeated elements of j
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            
            # using 2 pointer approach
            k = j + 1
            l = n - 1

            # until k and l will not cross each other
            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]

                # increase value
                if total < target:
                    k += 1

                # decrease value
                elif total > target:
                    l -= 1

                # found quadruplets
                else:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    result.append(temp)
                    # check for next elements
                    k += 1
                    l -= 1
                
                    # exclude repeated elements of k (if k<l)
                    while k < l and nums[k] == nums[k-1]:
                        k += 1

                    # exclude repeated elements of l (if k<l)
                    while k < l and nums[l] == nums[l+1]:
                        l -= 1

    return result


if __name__ == "__main__":
    arr = [1,0,-1,0,-2,2]
    target = 0
    print(arr, target)
    print(fourSum(arr, target))
    arr = [-3,-1,0,2,4,5]
    print(fourSumBetter(arr, 1))
    arr = [1,1,1,2,2,2,3,3,3,4,4,4,5,5]
    print(fourSumOptimal(arr, 8))
