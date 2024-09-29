public class SortedAndRotatedArray {
/*
 * Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions
 * (including zero). Otherwise, return false. There may be duplicates in the original array.
 * 
 * https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
 * T(c) -> O(n), S(c) -> O(1)
 */

    static boolean checkSortedAndRotated(int[] nums) {
        int changeIndex = -1;
        // check the index where order changes in array
        for(int i=0;i<nums.length-1;i++)
        {
            if(nums[i]>nums[i+1])
            {
                changeIndex = i+1;
                break;
            }
        }
        
        // everything is sorted
        if(changeIndex == -1)
        {
            return true;
        }
        
        // check from that index everything is sorted or not (included last and first element also)
        for(int j = changeIndex; j<nums.length;j++)
        {
            if(nums[j]>nums[(j+1) % nums.length])
            {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int arr[] = {3,4,5,1,2};
        int arr2[] = {2,1,3,4};
        System.out.println(checkSortedAndRotated(arr));
        System.out.println(checkSortedAndRotated(arr2));
    }
}
