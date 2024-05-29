public class BinarySearch {

/*
 * Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to 
 * search target in nums. If target exists, then return its index. Otherwise, return -1.
 * 
 * https://leetcode.com/problems/binary-search/
 * T(c) -> O(logn), S(c) -> O(1)
 */
    public static int search(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        while(low <= high)
        {
            int mid = low + (high-low)/2;
            // matched with target
            if(nums[mid] == target)
            {
                return mid;
            }
            // go to left part
            else if(nums[mid] > target)
            {
                high = mid-1;
            }
            // go to right part
            else{
                low = mid+1;
            }
        }
        return -1;
    }

    /*
     * Using recursion
     * T(c) -> O(logn), S(c) -> O(logn)
     */
    public static int searchRecursive(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        return recursiveBinarySearch(nums, low, high, target);
    }
    
    static int recursiveBinarySearch(int[] nums, int low, int high, int target)
    {
        // base case
        if(low > high)
        {
            return -1;
        }
        
        int mid = low + (high-low)/2;
        // element found
        if(nums[mid] == target)
        {
            return mid;
        }
        // go to left part
        else if(nums[mid] > target)
        {
            return recursiveBinarySearch(nums, low, mid-1, target);
        }
        // go to right part
        else{
            return recursiveBinarySearch(nums, mid+1, high, target);
        }
    }

    public static void main(String[] args) {
        int arr1[] = {-1,0,3,5,9,12};
        int target = 9;
        System.out.println("Index = "+ search(arr1, target));
        
        target = 2;
        System.out.println("Index = "+ searchRecursive(arr1, target));
    }
    
}
