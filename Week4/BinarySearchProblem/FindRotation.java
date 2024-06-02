public class FindRotation {

/*
 * You are given an array 'arr' having 'n' distinct integers sorted in ascending order. The array is right rotated 
 * 'r' times. Find the value of 'r'.
 * 
 * T(c) -> O(logn), S(c) -> O(1)
 */

    static int findRotation(int[] nums)
    {
        int n = nums.length;
        int low = 0;
        int high = n-1;
        int idx = -1;
        int minValue = Integer.MAX_VALUE;
        while(low <= high)
        {
            int mid = (low+high)/2;
            // left sorted part
            if(nums[low] <= nums[mid])
            {
                if(nums[low] < minValue)
                {
                    minValue = nums[low];
                    idx = low;
                }
                low = mid+1;
            }
                // right sorted part
            else{
                if(nums[mid] < minValue)
                {
                    minValue = nums[mid];
                    idx = mid;
                }
                high = mid-1;
            }
        }
        return idx;
    }

    public static void main(String[] args) {
        int arr1[] = {2, 3, 4, 1};
        // int arr1[] = {1,2,3};
        System.out.println(findRotation(arr1));
    }
    
}
