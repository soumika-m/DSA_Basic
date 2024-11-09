import java.util.HashMap;

public class SubarraySumEqualsK {

/*
 * Given an array of integers nums and an integer k, return the total number of subarrays whose 
 * sum equals to k. A subarray is a contiguous non-empty sequence of elements within an array.
 * 
 * https://leetcode.com/problems/subarray-sum-equals-k/description/
 * T(c) -> o(n^2), S(c) -> O(1)
 */

    static int subarraySum(int[] nums, int k) {
        int n = nums.length;
        int count = 0;

        // generate all subarrays and check for sum of those elements
        for(int i=0;i<n;i++)
        {
            int sum = 0;
            for(int j=i;j<n;j++)
            {
                sum += nums[j];
                if(sum == k)
                {
                    count++;
                }
            }
        }
        return count;
    }

    /*
     * Using prefix sum and storing sum frequency
     * T(c) -> O(n),  S(c) -> O(n) 
     */
    static int subarraySumEfficient(int[] nums, int k) {
        // contains prefix sum and count
        HashMap<Integer, Integer> map = new HashMap<>();
        
        int n = nums.length;
        // calculate sum till current index
        int sum = 0;
        // contains subarray count
        int cnt = 0;
        
        // setting 0 and it's count 1 in map
        map.put(0,1);
        
        for(int i=0;i<n;i++)
        {
            // calculate sum
            sum += nums[i];
            
            // calculate prefix sum (remaining sum x-k, removing which we will get subarray of sum k)
            int prefixSumRemove = sum - k;
            
            // if prefix sum (x-k) found in map, we will add count from map in cnt variable
            if(map.containsKey(prefixSumRemove))
            {
                cnt += map.get(prefixSumRemove);
            }
            
            // add sum and count in map, if already present, increase count
            map.put(sum, map.getOrDefault(sum, 0)+1);
        }
        
        return cnt;
    }


    public static void main(String[] args) {
        int arr[] = {1,2,3};
        int k = 3;
        /* [1,2] [3] */
        System.out.println("Count of subarray sum equal to k = "+ subarraySum(arr,k));
        System.out.println("Count of subarray sum equal to k = "+ subarraySumEfficient(arr,k));
    }
    
}
