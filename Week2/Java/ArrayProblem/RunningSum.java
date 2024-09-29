public class RunningSum {
/*
 * Given an array nums. Find running sum of array as runningSum[i] = sum(nums[0]…nums[i])
 * For eg. nums = [1,2,3,4], Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
 * https://leetcode.com/problems/running-sum-of-1d-array/
 * T(c) -> O(n), S(c) -> O(n)
 */
    static int[] runningSum(int[] nums) {
        int n = nums.length;
        int[] output = new int[n];
        int sum = 0;
        for(int i=0;i<n;i++)
        {
            sum += nums[i];
            output[i] = sum;
        }
        return output;
    }

    public static void main(String[] args) {
        int arr[] = {1,2,3,4};
        int output[] = runningSum(arr);
        for(int i=0;i<output.length;i++)
        {
            System.out.print(output[i] + " ");
        }
    }
}
