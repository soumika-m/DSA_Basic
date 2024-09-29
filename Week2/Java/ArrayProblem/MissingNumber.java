public class MissingNumber {
/*
* Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range
* that is missing from the array.
* https://leetcode.com/problems/missing-number/
* T(c) -> O(n), S(c) -> O(1)
*/    
    static int missingNumber(int[] nums) {
        int n = nums.length;
        int naturalSum = (n*(n+1))/2;
        
        int actualSum = 0;
        for(int i=0;i<n;i++)
        {
            actualSum += nums[i];
        }
        
        int missingNum = naturalSum - actualSum;
        return missingNum;
    } 

    public static void main(String[] args) {
        int nums[] = {9,6,4,2,3,5,7,0,1};
        System.out.println(missingNumber(nums));
    }
}
