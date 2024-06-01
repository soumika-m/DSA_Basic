public class SearchInRotatedSortedArray1 {

/*
 * There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your 
 * function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array 
 * is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] 
 * might be rotated at pivot index 3 and become [4,5,6,7,0,1,2]. Given the array nums after the possible rotation and 
 * an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
 * 
 * https://leetcode.com/problems/search-in-rotated-sorted-array/
 * T(c) -> O(n), S(c) -> O(1)
 */
    public static int search(int[] nums, int target) {
        int n = nums.length;
        for(int i=0;i<n;i++)
        {
            if(nums[i] == target)
            {
                return i;
            }
        }
        return -1;
    }

    /*
     * Using binary search
     * T(c) -> O(logn), S(c) -> O(1)
     */
    public static int searchEfficient(int[] nums, int target) {
        int n = nums.length;
        int low = 0;
        int high = n-1;
        while(low <= high)
        {
            int mid = low + (high-low)/2;
            // found element in mid position
            if(nums[mid] == target)
            {
                return mid;
            }
            else
            {
                // if left part is sorted
                if(nums[low] <= nums[mid])
                {
                    // if element present within low and mid-1
                    if(nums[low] <= target && target < nums[mid])
                    {
                        high = mid-1;
                    }
                    else{
                        low = mid+1;
                    }
                }
                // if right part is sorted
                else{
                    // if element present within mid+1 and high
                    if(nums[mid] < target && target <= nums[high])
                    {
                        low = mid+1;
                    }
                    else{
                        high = mid-1;
                    }
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int nums[] = {4,5,6,7,0,1,2};
        int target = 0;
        System.out.println(search(nums, target));
        System.out.println(searchEfficient(nums, target));
    }    

}
