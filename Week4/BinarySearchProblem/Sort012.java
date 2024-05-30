public class Sort012 {

/*
 * Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same 
 * color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to 
 * represent the color red, white, and blue, respectively. You must solve this problem without using the library's 
 * sort function.
 * 
 * https://leetcode.com/problems/sort-colors/
 * T(c) -> O(n), S(c) -> O(1)
 */

    static void sortColors(int[] nums) {
        // using dutch national flag algo
        int n = nums.length;
        int low = 0;
        int mid = 0;
        int high = n-1;
        
        while(mid <= high)
        {
            // push to left, swap with low
            if(nums[mid] == 0)
            {
                int temp = nums[mid];
                nums[mid] = nums[low];
                nums[low] = temp;
                low++;
                mid++;
            }
            // push to right, swap with high
            else if(nums[mid] == 2)
            {
                int temp = nums[mid];
                nums[mid] = nums[high];
                nums[high] = temp;
                high--;
            }
            // for element 1, skip (assuming it is in correct position, i.e, middle)
            else{
                mid++;
            }
        }
    }

    public static void main(String[] args) {
        int arr[]= {2,0,2,1,1,0};
        sortColors(arr);
        for(int i=0;i<arr.length;i++)
        {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

}
