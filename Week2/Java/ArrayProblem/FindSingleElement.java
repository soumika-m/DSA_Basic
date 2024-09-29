class FindSingleElement{
/*
 * Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
 * https://leetcode.com/problems/single-number/
 * T(c) -> O(n), S(c) -> O(1)
 */
    static int singleNumber(int[] nums) {
        /* using xor operation, xor of two same number is 0, xor of 0 and any number is that number itself */
        int result = 0;
        for(int i=0;i<nums.length;i++)
        {
            result = result ^ nums[i];
        }
        return result;
    }

    public static void main(String[] args) {
        int nums[] ={4,1,2,1,2};
        System.out.println(singleNumber(nums));
    }
}