class SearchInsertPosition{

/*
 * Given a sorted array of distinct integers and a target value, return the index if the target is 
 * found. If not, return the index where it would be if it were inserted in order.
 * 
 * https://leetcode.com/problems/search-insert-position/
 * T(c) -> O(logn), S(c) -> O(logn)
 */
    static int searchInsert(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        while(low <= high)
        {
            int mid = low + (high-low)/2;
            // element found
            if(nums[mid] == target)
            {
                System.out.println("Element Found");
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
        // return insert position if element not found
        return low;
    }

    public static void main(String[] args) {
        int arr[] = {1,3,5,6};
        int target = 2;
        System.out.println("Index = " + searchInsert(arr, target));
    }

}