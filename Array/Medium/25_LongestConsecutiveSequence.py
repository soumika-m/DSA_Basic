"""
https://leetcode.com/problems/longest-consecutive-sequence/
"""

def longestConsecutive(nums):
    """ T(C) -> O(N^2), S(C) -> O(1) """

    # longest count should be atleast 1
    longest_count = 1

    # iterate through array, find in next number is present in array, count that
    for i in range(len(nums)):
        elem = nums[i]
        cnt = 1
        # if next element after elem is present in array, increase count
        while linearSearch(nums, elem + 1):
            elem = elem + 1
            cnt = cnt + 1
        
        # find longest count
        longest_count = max(longest_count, cnt) 

    return longest_count


def linearSearch(nums, elem):
    for i in range(len(nums)):
        if nums[i] == elem:
            return True
    
    return False


def longestConsecutiveBetter(nums):
    """ T(C) -> O(NlogN) + O(N), S(C) -> O(1) """

    # sort array
    nums.sort()
    print("nums = ", nums)

    last_found = float('-inf')
    current_count = 0
    longest_count = 0

    for i in range(len(nums)):

        # if previous element already found, then number is in sequence
        if last_found == nums[i] - 1:
            current_count += 1
            last_found = nums[i]

        # if duplicate present, don't consider, otherwise make it a new sequence
        elif last_found != nums[i]:
            current_count = 1
            last_found = nums[i]     

        # update longest count
        longest_count = max(longest_count, current_count)
    
    return longest_count


def longestConsecutiveOptimal(nums):
    """ T(C) -> O(N) + O(2N) = O(3N), S(C) -> O(N) """

    # if array is empty
    if len(nums) == 0:
        return 0

    longest_count = 1

    # using set data structure
    hash_set = set()
    # add all elements in set from array to remove duplicates
    for num in nums:
        hash_set.add(num)

    # iterate set and find consecutive sequence
    for it in hash_set:
        # if previous element not present in set, that is starting of sequence
        if it - 1 not in hash_set:
            # find consecutive numbers
            current_count = 1
            elem = it
            # if next number is also present in set
            while elem + 1 in hash_set:
                current_count += 1
                elem = elem + 1

            longest_count = max(longest_count, current_count)

    return longest_count


if __name__ == "__main__":
    arr = [100,4,200,1,3,2]
    print(arr)
    ### The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
    print(longestConsecutive(arr))
    print("=====================")
    arr = [100, 102, 100, 101, 101, 4, 3, 2, 3, 2, 1, 1, 1, 2]
    print(arr)
    print(longestConsecutiveBetter(arr))
    print(longestConsecutiveOptimal(arr))
