class SearchInRotatadSortedArray2 {

/*
 * There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values). Before being 
 * passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting 
 * array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, 
 * [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4]. 
 * Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is 
 * not in nums.
 * 
 * https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
 * T(c) -> O(logn) // average , O(n/2) // worst
 * S(c) -> O(1)
 */
    public boolean search(int[] nums, int target) {
        int n = nums.length;
        int low = 0;
        int high = n-1;
        while(low <= high)
        {
            int mid = (low + high)/2;
            // if element found in mid
            if(nums[mid] == target)
            {
                return true;
            }
            
            // due to duplicates and rotated, difficult to understand sorted part, discard duplicates
            if(nums[low] == nums[mid]  && nums[mid] == nums[high])
            {
                // srink search space
                low++;
                high--;
                continue;
            }
            
            // in between left and right, one part will be always sorted
            // check if left part is sorted
            if(nums[low] <= nums[mid])
            {
                // element found in that range
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
                // element found is that range
                if(nums[mid] < target && target <= nums[high])
                {
                    low = mid+1;
                }
                else{
                    high = mid-1;
                }
            }
        }
        return false;
    }
    
    public static void main(String[] args) {
        // int arr[] = {2,5,6,0,0,1,2};
        int arr[] = {1,0,1,1,1};
        int target = 0;
        System.out.println(search(arr, target));
    }

}
