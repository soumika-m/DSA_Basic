class MinimumInRotatedSortedArray {

/*
 * Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array 
 * nums = [0,1,2,4,5,6,7] might become: [4,5,6,7,0,1,2] if it was rotated 4 times.
 * [0,1,2,4,5,6,7] if it was rotated 7 times. Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time 
 * results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]]. Given the sorted rotated array nums of unique elements, 
 * return the minimum element of this array.
 * 
 * https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
 * T(c) -> O(logn), S(c) -> O(1)
 */

    static int findMin(int[] nums) {
        int n = nums.length;
        int low = 0;
        int high = n-1;
        int minValue = Integer.MAX_VALUE;
        while(low <= high)
        {
            int mid = (low+high)/2;
            
            // if whole array is already sorted
            if(nums[low] <= nums[high])
            {
                minValue = Math.min(minValue, nums[low]);
                break;
            }
            
            // left part is sorted, equals is for checking single element
            if(nums[low] <= nums[mid])
            {
                minValue = Math.min(minValue, nums[low]);
                low = mid+1;
            }
            // right part is sorted
            else{
                minValue = Math.min(minValue, nums[mid]);
                high = mid-1;
            }
        }
        return minValue;
    }


    public static void main(String[] args) {
        int arr[] = {4,5,6,7,0,1,2};
        System.out.println(findMin(arr));
    }
    
}
