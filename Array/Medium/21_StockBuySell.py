"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""

def maxProfit(prices):
    """ T(C) -> O(N), S(C) -> O(1) """

    # find minimum buy price before today's sell date to get maximum profit
    min_price = prices[0]
    profit = 0

    # iterate through sell price
    for i in range(1, len(prices)):
        cost = prices[i] - min_price
        # find max profit
        profit = max(profit, cost)
        # find minimum buy price
        min_price = min(min_price, prices[i])

    return profit



if __name__ == "__main__":
    arr = [7,1,5,3,6,4]
    print(arr)

    # Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    #Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    print(maxProfit(arr))
