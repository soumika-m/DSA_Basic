public class CapacityToShipPackagesWithinDdays {

    /*
     * A conveyor belt has packages that must be shipped from one port to another within days days. The ith 
     * package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on 
     * the conveyor belt (in the order given by weights). We may not load more weight than the maximum 
     * weight capacity of the ship. Return the least weight capacity of the ship that will result in all 
     * the packages on the conveyor belt being shipped within days days.
     * 
     * https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
     * T(c) -> O((sum-max)+1) * O(n) -> O(n^2), S(c) -> O(1) 
     */

    static public int shipWithinDays(int[] weights, int days) {
        int maxVal = findMax(weights);
        int sumVal = findSum(weights);
        
        // capacity will be within the range of maxvalue and total sum of array
        for(int cap=maxVal; cap<=sumVal; cap++)
        {
            int daysReq = findDaysRequired(weights, cap);
            if(daysReq <= days)
            {
                return cap;
            }
        }
        return 0;
    }
    
    static int findMax(int[] weights)
    {
        int maxVal = 0;
        for(int i=0;i<weights.length;i++)
        {
            maxVal = Math.max(maxVal, weights[i]);
        }
        return maxVal;
    }
    
    static int findSum(int[] weights)
    {
        int sum = 0;
        for(int i=0;i<weights.length;i++)
        {
            sum += weights[i];
        }
        return sum;
    }
    
    static int findDaysRequired(int[] weights, int capacity)
    {
        int day = 1;
        int load = 0;
        for(int i=0;i<weights.length;i++)
        {
            if(load+weights[i] > capacity)
            {
                day += 1;
                load = weights[i];
            }
            else{
                load += weights[i];
            }
        }
        return day;
    }

    /*
     * Using binary search
     * T(c) -> O(log(sum-max+1))*O(n), S(c) -> O(1)
     */
    static public int shipWithinDaysEfficient(int[] weights, int days) {
        int low = findMax(weights);
        int high = findSum(weights);
        int ans = 0;
        
        while(low <= high)
        {
            int mid = (low + high)/2;
            int daysReq = findDaysRequired(weights, mid);
            // possible, go for least (left)
            if(daysReq <= days)
            {
                ans = mid;
                high = mid-1;
            }
            // not possible, go to right
            else{
               low = mid+1; 
            }
        }
        // or low
        return ans;
    }
    
    public static void main(String[] args) {
        int weights[] = {3,2,2,4,1,4};
        int days = 3;
        /*
         * 1st day: 3, 2
         * 2nd day: 2, 4
         * 3rd day: 1, 4
         */
        System.out.println(shipWithinDays(weights, days));
        System.out.println(shipWithinDaysEfficient(weights, days));
    }
}
