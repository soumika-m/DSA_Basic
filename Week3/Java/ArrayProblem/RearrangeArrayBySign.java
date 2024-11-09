public class RearrangeArrayBySign {

/*
 * You are given a 0-indexed integer array nums of even length consisting of an equal number of 
 * positive and negative integers. You should return the array of nums such that - 
 * 1. Every consecutive pair of integers have opposite signs. 
 * 2. For all integers with the same sign, the order in which they were present in nums is preserved.
 * 3. The rearranged array begins with a positive integer.
 * 
 * https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
 * T(c) -> O(n) + O(n/2), S(c) -> O(n)
 */

    static int[] rearrangeArray(int[] nums) {
        int n = nums.length;
        // half elements belongs to positive array and half belongs to negative array
        int positive[] = new int[n/2];
        int negative[] = new int[n/2];  
        // pointer for positive and negative array
        int pos = 0;
        int neg = 0;

        // putting positive numbers in positive array and negative numbers in negative array
        for(int i=0;i<n;i++)
        {
            // positive
            if(nums[i] >= 0)
            {
                positive[pos++] = nums[i];
            }
            // negative
            else{
                negative[neg++] = nums[i];
            }
        }
        
        // putting elements back to main array in alternate way (1 positive, 1 negative)
        for(int j=0;j<n/2;j++)
        {
            // even index will be positive
            nums[2*j] = positive[j];
            // odd index will be negative
            nums[2*j+1] = negative[j];
        }
        
        return nums;
    }

    /*
     * Using two pointers
     * T(c) -> O(n), S(c) -> O(n)
    */
    static int[] rearrangeArrayEfficient(int[] nums) {
        int n = nums.length;
        int ans[] = new int[n];
        int posIndex = 0;
        int negIndex = 1;
        
        // positive element wil be placed in even index, and negative in odd index
        for(int i=0;i<n;i++)
        {
            if(nums[i] >= 0)
            {
                ans[posIndex] = nums[i];
                posIndex += 2;
            }
            else{
                ans[negIndex] = nums[i];
                negIndex += 2;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        int arr[] = {3,1,-2,-5,2,-4};
        int res1[] = rearrangeArray(arr);
        for(int i=0;i<res1.length;i++)
        {
            System.out.print(res1[i]+" ");
        }
        System.out.println();

        int res2[] = rearrangeArrayEfficient(arr);
        for(int i=0;i<res2.length;i++)
        {
            System.out.print(res2[i]+" ");
        }
        System.out.println();
    }

}
