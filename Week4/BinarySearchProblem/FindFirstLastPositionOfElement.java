public class FindFirstLastPositionOfElement {

/*
 * Given an array of integers nums sorted in non-decreasing order, find the starting and 
 * ending position of a given target value. 
 * If target is not found in the array, return [-1, -1].
 * 
 * https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
 * T(c) -> O(logn)+O(logn) = O(logn), S(c) -> O(1)
 */

    public static int[] searchRange(int[] nums, int target) {
        int[] result = new int[2];
        result[0] = binarySearchFindFirstOccurance(nums, target);
        result[1] = binarySearchFindLastOccurance(nums, target);
        return result;
    }
    
    static int binarySearchFindFirstOccurance(int[] nums, int target)
    {
        int firstIndex = -1;
        int low = 0;
        int high = nums.length-1;
        while(low <= high)
        {
            int mid = low + (high-low)/2;
            // go to left part
            if(nums[mid] > target)
            {
                high = mid-1;
            }
            // go to right part
            else if(nums[mid] < target)
            {
                low = mid+1;
            }
            // element found, check for more left element to find first index, keep track of that element
            else{
                firstIndex = mid;
                high = mid-1;
            }
        }
        return firstIndex;
    }
    
    static int binarySearchFindLastOccurance(int[] nums, int target)
    {
        int lastIndex = -1;
        int low = 0;
        int high = nums.length-1;
        while(low <= high)
        {
            int mid = low + (high-low)/2;
            // go to left part
            if(nums[mid] > target)
            {
                high = mid-1;
            }
            // go to right part
            else if(nums[mid] < target)
            {
                low = mid+1;
            }
            // element found, check for more left element to find first index, keep track of that element
            else{
                lastIndex = mid;
                low = mid+1;
            }
        }
        return lastIndex;
    }

    public static void main(String[] args) {
        int arr[] = {5,7,7,8,8,10};
        int target = 8;
        int[] result = searchRange(arr, target);
        System.out.println("["+result[0]+", "+result[1]+"]");
    }

}
