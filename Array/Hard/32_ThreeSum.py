"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

https://leetcode.com/problems/3sum/description/
"""

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """ T(C) -> O(N^3), S(C) -> O(2 * no. of unique triplets) """

    n = len(nums)
    st = set()

    # check for all possible triplets
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    # sorting it to understand which are duplicates
                    temp.sort()
                    # add in set to track unique triplets
                    st.add(tuple(temp))
    
    # take all unique elements from set and add it in result list
    res = [list(item) for item in st]
    return res


def threeSumBetter(nums: List[int]) -> List[List[int]]:
    """ T(C) -> O(N^2), S(C) -> O(N) [for storing in hashset] + O(2 * no. of unique triplets) """

    n = len(nums)
    # for storing unique triplets
    st = set()

    for i in range(n):
        hashset = set()
        for j in range(i+1, n):
            # calculate the third element
            third = - (nums[i] + nums[j])
            # if element present in set, make triplets
            if third in hashset:
                temp = [nums[i], nums[j], third]
                temp.sort()
                st.add(tuple(temp))

            # add jth element in set
            hashset.add(nums[j])

    # add elements from set to final result list
    res = [list(item) for item in st]
    return res


def threeSumOptimal(nums: List[int]) -> List[List[int]]:
    """ T(C) -> O(NlogN) + O(N^2), S(C) -> O(no. of unique triplets) """

    n = len(nums)

    # sort the entire array
    nums.sort()

    ans = []

    # i will keep track of first element, j and k will move as required
    for i in range(n):

        # if nums[i] is already > 0, not need to check further as it is sorted
        if nums[i] > 0:
            break

        # if nums[i] is same as nums[i-1], skip that
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # using 2 pointer approach
        j = i + 1
        k = n - 1
        while j < k:

            total = nums[i] + nums[j] + nums[k]
        
            # increase the sum
            if total < 0:
                j += 1

            # decrease the sum
            elif total > 0:
                k -= 1

            # if total == 0, then add that triplet in result list
            else:
                temp = [nums[i], nums[j], nums[k]]
                ans.append(temp)
                # check for next element
                j += 1
                k -= 1

                # discard duplicates, do this until j<k
                # if jth element is same as previous, skip
                while j < k and nums[j] == nums[j-1]:
                    j += 1

                # if kth element is same as previous, skip
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
                
    return ans


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    print(nums)
    ### nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    ### nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    ### nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    ### The distinct triplets are [-1,0,1] and [-1,-1,2].
    ### Notice that the order of the output and the order of the triplets does not matter.
    print(threeSum(nums))
    print(threeSumBetter(nums))
    nums = [-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]
    print(threeSumOptimal(nums))
