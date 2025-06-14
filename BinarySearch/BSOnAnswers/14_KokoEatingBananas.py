"""
Return the min integer k such that koko can eat all bananas within h hours.

https://leetcode.com/problems/koko-eating-bananas/description/
"""

import math

def koko_banana_eating_min(piles, h):
    """ T(C) -> O(max(piles) * n), S(C) -> O(1) """

    # find how much minimum hour will help koko finish bananas, find number of bananas per hour
    for i in range(1, max(piles)+1):
        reqtime = find_required_time(piles, i)
        if reqtime <= h:
            return i


def find_required_time(piles, hourly):
    # total hours required for koko to finish bananas
    total_hour = 0
    for i in range(len(piles)):
        total_hour += math.ceil(piles[i]/hourly)
    
    return total_hour


def koko_banana_eating_min_binary_search(piles, h):
    """ T(C) -> O(N * log(max(piles)), S(C) -> O(1) """

    ans = -1
    # using binary search on answers
    low = 1
    # max element from piles array
    high = max(piles)
    while low <= high:
        mid = (low + high) // 2
        total_hours = find_required_time(piles, mid)
        if total_hours <= h:
            ans = mid 
            # check if any more smaller element present
            high = mid - 1
        # check for right side (eat more bananas in hours)
        else:
            low = mid + 1

    return ans


if __name__ == "__main__":
    piles = [3,6,7,11]
    h = 8
    print(koko_banana_eating_min(piles, h))
    piles = [30,11,23,4,20]
    h = 5
    print(koko_banana_eating_min(piles, h))
    piles = [30,11,23,4,20]
    h = 6
    print(koko_banana_eating_min_binary_search(piles, h))
