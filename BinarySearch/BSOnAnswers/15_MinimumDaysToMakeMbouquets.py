"""
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1

https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
"""

def minDays(bloomDay, m, k):
    """ T(C) -> O(max-min+1)*O(n), S(C) -> O(1) """

    n = len(bloomDay)

    # not possible to make m bouquets
    if m * k > n:
        return -1
    
    for i in range(min(bloomDay), max(bloomDay)+1):
        if isPossible(bloomDay, i, m, k):
            return i
    
    # if not possible
    return -1
    

def isPossible(bloomDay, day, m, k):

    # check how many pair is possible from array
    # if we can make consecutive k elements of m bucket
    n = len(bloomDay)
    cnt = 0
    num_of_bucket = 0
    # iterate through array, and count number of buckets contains k element
    for i in range(0, n):
        # which flowers are bloomed on that day
        if(bloomDay[i] <= day):
            cnt += 1
        else:
            num_of_bucket += (cnt//k)
            cnt = 0

    # at last, count number of buckets again
    num_of_bucket += (cnt//k)

    # if number of bucket atleast m, return true, else false
    if num_of_bucket >= m:
        return True
    else:
        return False
    

def minDaysBinarySearch(bloomDay, m, k):
    """ T(C) -> O(log(max-min+1)) * O(n) , S(C) -> O(1) """

    n = len(bloomDay)
    if (m*k) > n: 
        return -1 

    ans = -1
    # using binary search on answers
    low = min(bloomDay)
    high = max(bloomDay)

    while low <= high:
        mid = (low + high) // 2
        # if during mid day we can make m bonquets, check for more smaller ans
        if isPossible(bloomDay, mid, m, k):
            ans = mid
            # if possible answer found, check for minimum element (left side)
            high = mid - 1
        else:
            # check for larger element , right side
            low = mid + 1

    return ans


if __name__ == "__main__":
    bloomDay = [7,7,7,7,12,7,7]
    m = 2
    k = 3
    ###
    # Explanation: We need 2 bouquets each should have 3 flowers.
    # Here is the garden after the 7 and 12 days:
    # After day 7: [x, x, x, x, _, x, x]
    # We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
    # After day 12: [x, x, x, x, x, x, x]
    # It is obvious that we can make two bouquets in different ways.
    ###
    print(minDays(bloomDay, m, k))
    print(minDaysBinarySearch(bloomDay, m, k))

    bloomDay = [1,10,3,10,2]
    m = 3
    k = 2
    print(minDays(bloomDay, m, k))
    print(minDaysBinarySearch(bloomDay, m, k))
