public class SortColors {

/*
 * Given an array nums with n objects colored red, white, or blue, sort them in-place so that 
 * objects of the same color are adjacent, with the colors in the order red, white, and blue.
 * We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
 * You must solve this problem without using the library's sort function.
 * 
 * https://leetcode.com/problems/sort-colors/description/
 * 
 * T(c) -> O(n), S(c) -> O(1)
 */
    static void sortColors(int[] nums) {
        int cnt0 = 0, cnt1 = 0, cnt2 = 0;
        
        // counting how many 0, 1, 2 are there
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i] == 0)
            {
                cnt0++;
            }
            else if(nums[i] == 1)
            {
                cnt1++;
            }
            else{
                cnt2++;
            }
        }
        
        // adding 0, 1 , 2 back to array in corresponding positions based on count
        for(int j=0;j<nums.length;j++)
        {
            if(cnt0 > 0)
            {
                nums[j] = 0;
                cnt0--;
            }
            else if(cnt1 > 0)
            {
                nums[j] = 1;
                cnt1--;
            }
            else{
                nums[j] = 2;
                cnt2--;
            }
        }
    }

    /* 
    * using dutch national flag algorithm
    * T(c) -> O(n) , S(c) -> O(1)
    */
    static void sortColorsEfficient(int[] nums) {

        int low = 0;
        int mid = 0;
        int high = nums.length-1;
        
        while(mid <= high)
        {
            // if 0 found, swap low with mid and increase low and mid pointer
            if(nums[mid] == 0)
            {
                int temp = nums[low];
                nums[low] = nums[mid];
                nums[mid] = temp;

                mid++;
                low++;
            }
            // if 1 found, nothing to do, just increase mid pointer
            else if(nums[mid] == 1)
            {
                mid++;   
            }
            // if 2 found, swap high with mid, decrease high
            else{
                int temp = nums[high];
                nums[high] = nums[mid];
                nums[mid] = temp;
                
                high--;
            }
        }
    }

    public static void main(String[] args) {
        int nums1[] = {2,0,2,1,1,0};
        sortColors(nums1);
        for(int i=0;i<nums1.length;i++)
        {
            System.out.print(nums1[i] + " ");
        }
        System.out.println();

        int nums2[] = {2,0,1};
        sortColorsEfficient(nums2);
        for(int i=0;i<nums2.length;i++)
        {
            System.out.print(nums2[i] + " ");
        }
        System.out.println();
    }
    
}
