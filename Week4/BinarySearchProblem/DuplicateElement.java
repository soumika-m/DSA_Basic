public class DuplicateElement {
    
/*
 * Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive. 
 * There is only one repeated number in nums, return this repeated number.
 * You must solve the problem without modifying the array nums and uses only constant extra space.
 * https://leetcode.com/problems/find-the-duplicate-number/
 * T(c) -> O(n* logn), S(c) -> O(1)
 */
    static public int findDuplicate(int[] nums) {
        // performing binary search on value range rather than array index
        int n = nums.length;
        int low = 0;
        int high = n-1;
        while(low < high)
        {
            int mid = low + (high-low)/2;
            int cnt = 0;
            // count elements <= mid
            for(int i=0;i<n;i++)
            {
                if(nums[i] <= mid)
                {
                    cnt++;
                }
            }
            
            if(cnt > mid)
            {
                // duplicate is on the left half
                high = mid;
            }
            else{
              //  duplicate is on the right half
                low = mid+1;
            }  
        }
        // at the end low and high will point to same element
        return low;
    }
    
    public static void main(String[] args) {
        int arr[] = {3,1,3,4,2};
        System.out.println("Duplicate number in array = "+findDuplicate(arr));
    }

}
