"""
    You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your 
    profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

def maxProfit(prices):
    """ T(c) -> O(n), S(c) -> O(n) """
    # using extra profit array, it will contain max sell price for corresponding buy price
    profit_arr = [0] * len(prices)
    
    maxi = 0
    i = len(prices)-1
    # generate profirr array
    while i >= 0:
        # find maximum between max element and current element
        if prices[i] > maxi:
            profit_arr[i] = prices[i]
            maxi = prices[i]
        else:
            profit_arr[i] = maxi
        i = i - 1
    
    max_profit = 0
    j = 0
    while j < len(prices):
        # find max profit based on profit array
        current_profit = profit_arr[j] - prices[j]
        if current_profit > max_profit:
            max_profit = current_profit
        j = j + 1
    
    return max_profit


def maxProfitEfficient(prices):
    """ T(c) -> O(n), S(c) -> O(1) """
    # find minimum buy price before today's sell date to get maximum profit
    min_price = prices[0]
    profit = 0
    
    for i in range(1, len(prices)):
        current_profit = prices[i] - min_price
        # find max profit
        profit = max(profit, current_profit)
        # find minimum buy price
        min_price = min(min_price, prices[i])
    
    return profit


arr = [7,5,3,6,4,1]
# Buy on day 2 (price = 3) and sell on day 4 (price = 6), profit = 6-3 = 3.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
print(maxProfit(arr))

print(maxProfitEfficient(arr))
