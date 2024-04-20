public class MoveZerosToEnd {
/*
 * Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
 * https://leetcode.com/problems/move-zeroes/
 * T(c) -> O(n), S(c) -> O(1)
 */
    static void moveZeroes(int[] nums) {
        int i = 0;
        int j = 1;
        /* using two pointer */
        while(j < nums.length)
        {
            /* we are trying to move number at beginning, so zero will move at end */
            if(nums[i] == 0 && nums[j]!=0)
            {
                nums[i]=nums[j];
                nums[j] = 0;
                i++;
                j++;
            }
            else if(nums[i] == 0 && nums[j] == 0)
            {
                j++;
            }
            else{
                i++;
                j++;
            }
        }
    }

    public static void main(String[] args) {
        int nums[] = {0,1,0,3,12};
        moveZeroes(nums);
        for(int i=0;i<nums.length;i++)
        {
            System.out.print(nums[i]+" ");
        }
        System.out.println();
    }    
}
