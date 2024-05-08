public class BestTimeToBuySellStock {
/*
 * You are given an array prices where prices[i] is the price of a given stock on the ith day.
 * You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future 
 * to sell that stock.
 * Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
 * 
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
 * T(c) -> O(n^2), S(c) -> O(1)
 */

    static int maxProfit(int[] prices) {
        int profit = 0;
        for(int i=0;i<prices.length;i++)
        {
            for(int j=i+1;j<prices.length;j++)
            {
                int buyPrice = prices[i];
                int sellPrice = prices[j];
                int currentprofit = sellPrice - buyPrice;
                if(sellPrice > buyPrice && currentprofit > profit)
                {
                    profit = currentprofit;
                }
            }
        }
        return profit;
    }

    /* 
    * Using extra array for calculating profits of each stock, and later take decision based on that
    * T(c) -> O(n), S(c) -> O(n)
    */
    static int maxProfitEfficient(int[] prices) {
        int profit = 0;
        int maxi = 0;
        int profitArr[] = new int[prices.length];
        
        // profit array will contain max sell price for corresponding stock buy price
        for(int i=prices.length-1;i>=0;i--)
        {
            if(prices[i]>maxi)
            {
                profitArr[i] = prices[i];
                maxi = prices[i]; 
            }
            else{
                profitArr[i] = maxi;
            }
        }

        // finding max profit based on profit array
        for(int i=0;i<prices.length;i++)
        {
            int currentprofit = profitArr[i] - prices[i];
            if(currentprofit > profit)
            {
                profit = currentprofit;
            }
        }

        return profit;
    }

    /*
     * By finding minimum price before sell day, to get max profit
     * T(c) -> O(n), S(c) -> O(1) 
     */
    static int maxProfitOptimal(int[] prices) {
        int profit = 0;
        int minPrice = prices[0];
        // check for minimum price with which we can buy before today's sell date
        for(int i=1;i<prices.length;i++)
        {
            int currentProfit = prices[i] - minPrice;
            // find maximum profit
            profit = Math.max(profit, currentProfit);
            // find minimum price to buy that stock, before sell date
            minPrice = Math.min(minPrice, prices[i]);
        }
        return profit;
    }
   
    public static void main(String[] args) {
        int arr[] = {7,1,5,3,6,4};
        int arr1[] = {7,6,4,3,1};
        System.out.println(maxProfit(arr));
        System.out.println(maxProfitEfficient(arr1));
        System.out.println(maxProfitOptimal(arr));
    }
}
