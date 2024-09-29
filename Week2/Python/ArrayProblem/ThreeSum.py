"""
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
    and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.

    https://leetcode.com/problems/3sum/
"""


def threeSum(nums):
    """Time Limit issue"""
    """ T(c) -> O(n^3) , S(c) -> O(n) """
    result = []
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                
                if nums[i] + nums[j] + nums[k] == 0:
                    
                    # create triplet and sort it to discard duplicates
                    triplet = [nums[i], nums[j], nums[k]]
                    triplet.sort()
                    
                    if triplet not in result:
                        result.append(triplet)
    
    return result


def threeSumBetter(nums):
    """ T(c) -> O(n^2) , S(c) -> O(n) """
    result = set()
    
    for i in range(len(nums)):
        seen = set()
        for j in range(i+1, len(nums)):
            another_num = -nums[i] - nums[j]
            
            if another_num in seen:
                # create triplet and sort it to discard duplicates
                triplet = tuple(sorted((nums[i], nums[j], another_num)))
                result.add(triplet)
            
            # add current element in seen set
            seen.add(nums[j])


    return [list(triple) for triple in result]


def threeSumOptimal(nums):
    """ T(c) -> O(n^2) , S(c) -> O(n) """

    nums.sort()
    
    result = []
    n = len(nums)
    
    # fix i pointer
    for i in range(n):

        # skip duplicates of i
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # take 2 pointers left and right
        left = i + 1
        right = n -1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # move both pointers and avoid duplicates
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                    
                left += 1
                right -= 1
                
            # move left pointer to increase sum
            elif total < 0:
                left += 1

            # move right pointer to decrease sum
            else:
                right -= 1

    return result


arr = [-1,0,1,2,-1,-4]
print(threeSum(arr))

print(threeSumBetter(arr))

print(threeSumOptimal(arr))
