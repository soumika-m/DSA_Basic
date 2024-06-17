class PeakElement{

    /*
     * A peak element is an element that is strictly greater than its neighbors. Given a 0-indexed integer array nums, 
     * find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the 
     * peaks. You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be 
     * strictly greater than a neighbor that is outside the array.
     * 
     * https://leetcode.com/problems/find-peak-element/
     * T(c) -> O(logn), S(c) -> O(1)
     */
    static public int findPeakElement(int[] nums) {
        int n = nums.length;
        
        // if array contains only one element
        if(n == 1)
        {
            return 0;
        }
        
        // if first index is pick element
        if(nums[0] > nums[1])
        {
            return 0;
        }
        
        // if last element is pick element
        if(nums[n-1] > nums[n-2])
        {
            return n-1;
        }
        
        int low = 1;
        int high = n-1;
        while(low <= high)
        {
            int mid = low + (high-low)/2;
            // element is peak
            if(nums[mid-1] < nums[mid] && nums[mid] > nums[mid+1])
            {
                return mid;
            }
            // if in increasing slop (peak is on right)
            else if(nums[mid-1] < nums[mid])
            {
                low = mid+1;
            }
            // if in decreasing slop (peak is on left)
            else if(nums[mid-1] > nums[mid])
            {
                high = mid-1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int arr[] = {1,2,1,3,5,6,4};
        int idx = findPeakElement(arr);
        System.out.println("Peak element index = "+ idx +", element = "+ arr[idx]);
    }

}