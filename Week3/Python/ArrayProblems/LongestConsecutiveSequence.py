"""
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
    You must write an algorithm that runs in O(n) time.

    https://leetcode.com/problems/longest-consecutive-sequence/
"""

def longestConsecutive(nums):
    """ T(c) -> O(nlogn) + O(n), S(c) -> O(1)"""

    # empty array
    if len(nums) == 0:
        return 0

    nums.sort()

    longest_count = 1
    current_count = 1
    
    previous_num = nums[0]
    for i in range(1, len(nums)):
        current_num = nums[i]
        
        # if it is in sequence
        if current_num - 1 == previous_num:
            current_count += 1
            previous_num = current_num

        # if it is not in sequence, also not duplicate
        elif current_num != previous_num:
            current_count = 1
            previous_num = current_num
        
        longest_count = max(longest_count,  current_count)
        
    return longest_count


def longestConsecutiveEfficient(nums):
    """ T(c) -> O(n) + O(2*n), S(c) -> O(n)"""

    # to remove duplicate elements and making searching easy
    hashset = set(nums)

    current_cnt = 0
    longest_cnt = 0
        
    # iterate elements from set
    for elem in hashset:
        prev_elem = elem - 1
        
        # if current element is start of sequence
        if prev_elem not in hashset:
            current_cnt = 1
            next_elem = elem + 1
            
            # if next element is also present in set, it is in sequence
            while next_elem in hashset:
                current_cnt += 1
                next_elem = next_elem + 1
        
        # finding longest count
        longest_cnt = max(longest_cnt, current_cnt)
            
    return longest_cnt


arr = [0,3,7,2,5,8,4,6,0,1]
print(arr)
print(longestConsecutive(arr))
print(longestConsecutiveEfficient(arr))
