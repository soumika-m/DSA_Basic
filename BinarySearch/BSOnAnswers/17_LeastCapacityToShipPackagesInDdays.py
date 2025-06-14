"""
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. 
Each day, we load the ship with packages on the conveyor belt (in the order given by weights). 
We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped 
within d days.

https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
"""

def shipWithinDays(weights, days):
    """ T(C) -> O(sum-max+1) * O(n), S(C) -> O(1) """

    # capacity range will be from maximum num of array till sum of all elements from array
    for cap in range(max(weights), sum(weights)+1):
        daysRequired = findDaysRequired(weights, cap)

        if daysRequired <= days:
            return cap
        
    return -1


def findDaysRequired(weights, cap):

    load = 0
    day = 1
    for i in range(len(weights)):
        # if on particular day, load is more than capacity, we need to do it in the next day
        if (load + weights[i]) > cap:
            day += 1
            load = weights[i]
        else:
            load = load + weights[i]
    
    return day


def shipWithinDaysOptimal(weights, days):
    """ T(C) -> O(log(sum-max+1)) * O(n), S(C) -> O(1) """

    # using binary search on answers
    # capacity range will be from maximum num of array till sum of all elements from array
    low = max(weights)
    high = sum(weights)

    while low <= high:
        mid = (low + high) // 2

        # check with mid capacity, how many days will be required to ship all weights
        daysReq = findDaysRequired(weights, mid)

        if daysReq <= days:
            # find smaller capacity on left
            high = mid - 1
        else:
            # find greater capacity on right
            low = mid + 1
    
    return low


if __name__ == "__main__":
    weights = [1,2,3,4,5,6,7,8,9,10]
    days = 5
    print(shipWithinDays(weights, days))
    print(shipWithinDaysOptimal(weights, days))
