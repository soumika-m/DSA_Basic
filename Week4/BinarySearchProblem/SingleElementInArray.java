public class SingleElementInArray {

/*
 * You are given a sorted array consisting of only integers where every element appears exactly twice, except for one 
 * element which appears exactly once. Return the single element that appears only once. 
 * 
 * https://leetcode.com/problems/single-element-in-a-sorted-array/description/
 * T(c) -> O(n), S(c) -> O(1)
 */

    static int singleNonDuplicate(int[] nums) {
        int n = nums.length;
        // if array contains single element
        if(n == 1)
        {
            return nums[0];
        }
        
        for(int i=0;i<n;i++)
        {
            // first index
            if(i == 0)
            {
                if(nums[i] != nums[i+1])
                {
                    return nums[0];
                }
            }
            // last index
            else if(i == n-1)
            {
                if(nums[i] != nums[i-1])
                {
                    return nums[n-1];
                }
            }
            else{
                // not matched with previous and next element
                if(nums[i-1] != nums[i] && nums[i] != nums[i+1])
                {
                    return nums[i];
                }
            }
        }
        return -1;
    }

    /*
     * Using binary search
     * T(c) -> O(logn), S(c) -> O(1)
     */
    static int singleNonDuplicateEfficient(int[] nums) {
        int n = nums.length;
        if(n == 1)
        {
            return nums[0];
        }
        
        int low = 0;
        int high = n-1;
        while(low <= high)
        {
            int mid = (low+high)/2;
            // mid points to first index
            if(mid == 0 && nums[mid] != nums[mid+1])
            {
                return nums[0];
            }
            // mid points to last index
            if(mid == n-1 && nums[mid] != nums[mid-1])
            {
                return nums[n-1];
            }
            // mid element not matching with previous and next element
            if(nums[mid] != nums[mid-1] && nums[mid] != nums[mid+1])
            {
                return nums[mid];
            }
            
            // we are on left half, odd even index, go to right half, or even odd index, go to right half
            if((mid%2==1 && nums[mid] == nums[mid-1]) || (mid%2==0 && nums[mid] == nums[mid+1]))
            {
                low = mid+1;
            }
            else{
                high = mid-1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int arr[] ={1,1,2,3,3,4,4,8,8};
        System.out.println(singleNonDuplicate(arr));
        System.out.println(singleNonDuplicateEfficient(arr));
    }
}
