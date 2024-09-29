class RemoveDuplicateSortedInplace{
/*
 * Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
 * The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
 * https://leetcode.com/problems/remove-duplicates-from-sorted-array/
 * T(c) -> O(n), S(c) -> O(1)
 */
    static int removeDuplicates(int[] nums) {
        
        /* using 2 pointer approach, i points to unique element, j points to current element */
        int i = 0;
        int j = 1;
        /* we will shift unique elements at the first part of array */
        while(j<nums.length)
        {
            /* incase of non duplicate element j, shift it to next element of unique i */
            if(nums[i] != nums[j])
            {
                nums[i+1] = nums[j];
                i++;
            }
            /* if dupicate, skip current element */
            j++;
        }
        return i+1;
    }

    public static void main(String[] args) {
        int nums[] = {0,0,1,1,1,2,2,3,3,4};
        int k = removeDuplicates(nums);
        for(int i=0;i<k;i++)
        {
            System.out.print(nums[i]+" ");
        }
    }
}