public class MaxConsecutiveOnes {
/*
 * Given a binary array nums, return the maximum number of consecutive 1's in the array.
 * https://leetcode.com/problems/max-consecutive-ones/
 * T(c) -> O(n), S(c) -> O(1)
 */
    static int findMaxConsecutiveOnes(int[] nums) {
        /* using sliding window */
        int maxConsecutiveOnes = 0;
        int currentConsecutiveOnes = 0;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i] == 1)
            {
                currentConsecutiveOnes++;
                maxConsecutiveOnes = Math.max(currentConsecutiveOnes,maxConsecutiveOnes);
            }
            else{
                currentConsecutiveOnes = 0;
            }
        }
        return maxConsecutiveOnes;
    }

    public static void main(String[] args) {
        int nums[] = {1,0,1,1,0,1};
        System.out.println(findMaxConsecutiveOnes(nums));
    }
}
