public class MaximumSubarraySum {

/*
 * Given an integer array nums, find the subarray with the largest sum, and return its sum.
 * https://leetcode.com/problems/maximum-subarray/
 * T(c) -> O(n^2), S(c) -> O(1)
 */
    static int maxSubArraySum(int[] nums) {
        int n = nums.length;
        int maxsum = Integer.MIN_VALUE;

        for(int i=0;i<n;i++)
        {
            int sum = 0;
            // check for each sub array sum, and find max sum
            for(int j=i;j<n;j++)
            {
                sum += nums[j];
                maxsum = Math.max(sum, maxsum);
            }
        }
        return maxsum;
    }

    /*
     * Using kadane's algorithm
     * T(c) -> O(n), S(c) -> O(1)
     */
    static int maxSubArraySumEfficient(int[] nums) {
        int maxsum = Integer.MIN_VALUE;
        int sum = 0;
        
        for(int i=0;i<nums.length;i++)
        {
            // calculate sum based on each element
            sum += nums[i];
            // assign sum to maximum if it is greater
            if(sum > maxsum){
                maxsum = sum;
            }
            // if sum is negative, no need to carry forwad it, as it will decrease the sum further
            if(sum < 0)
            {
                sum = 0;
            }
        }
        return maxsum;
    }

    /* 
    * print max subarray which is having largest sum  => using kadane's algorithm
    * T(c) -> O(n), S(c) -> O(1)
    */
    static void maxSubArrayPrintEfficient(int[] nums) {
        int maxsum = Integer.MIN_VALUE;
        int sum = 0;

        int startIndex = -1;
        int endIndex = -1;
        for(int i=0;i<nums.length;i++)
        {
            // if sum is zero, that is the start of sub array
            if(sum == 0)
            {
                startIndex = i;
            }
            // calculate sum based on each element
            sum += nums[i];
            // assign maximum of maxsum and sum
            if(sum > maxsum)
            {
                maxsum = sum;
                endIndex = i;
            }
            // if sum is negative, no need to carry forwad it, as it will decrease the sum further
            if(sum < 0)
            {
                sum = 0;
            }
        }
        System.out.println("startIndex = "+ startIndex  + " , endIndex = "+ endIndex);
        for(int i=startIndex;i<=endIndex;i++)
        {
            System.out.print(nums[i] + " ");
        }
        System.out.println();
    }


    public static void main(String[] args) {
        int arr[] = {-2,1,-3,4,-1,2,1,-5,4};
        System.out.println(maxSubArraySum(arr));
        System.out.println(maxSubArraySumEfficient(arr));
        maxSubArrayPrintEfficient(arr);
    }
    
}
