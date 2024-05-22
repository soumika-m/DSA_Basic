public class ReversePairs {

/*
 * Given an integer array nums, return the number of reverse pairs in the array.
 * A reverse pair is a pair (i, j) where: 0 <= i < j < nums.length and nums[i] > 2 * nums[j].
 * 
 * https://leetcode.com/problems/reverse-pairs/description/
 * T(c) -> O(n^2), S(c) -> O(1)
 */

    static int reversePairs(int[] nums) {
        int n = nums.length;
        int count = 0;
        for(int i=n-1;i>=0;i--)
        {
            for(int j=i+1;j<n;j++)
            {
                // convert to long, as integer can overflow after multiply
                if(nums[i] > (long)2*nums[j])
                {
                    count++;
                }
            }
        }
        return count;
    }


    /*
     * Using merge sort
     * T(c) -> O(nlogn) + O(n) + O(n) => O(2nlogn)
     * S(c) -> O(n) 
     */

    public static int reversePairsEfficient(int[] nums) {
        return mergeSort(nums, 0, nums.length-1);
    }
    
    static int mergeSort(int[] nums, int low, int high)
    {
        int cnt = 0;
        // run until one or no element left
        if(low<high)
        {
            int mid = (low+high)/2;
            // left part
            cnt += mergeSort(nums, low, mid);
            // right part
            cnt += mergeSort(nums, mid+1, high);
            // count reverse pairs
            cnt += countReversePairs(nums, low, mid, high);
            // merge both parts
            merge(nums, low, mid, high);
        }  
        return cnt;
    }
    
    static void merge(int[] nums, int low, int mid, int high)
    {
        int i = low;
        int j = mid+1;
        int k = 0;
        
        int temp[] = new int[high-low+1];  
        
        // both part elements present
        while(i<=mid && j<=high)
        {
            if(nums[i] <= nums[j])
            {
                temp[k++] = nums[i++];
            }
            else{
                temp[k++] = nums[j++];
            }
        }
        
        // remaining elements in first part
        while(i<=mid)
        {
            temp[k++] = nums[i++];
        }
        
        // remaining elements in second part
        while(j<=high)
        {
            temp[k++] = nums[j++];
        }
        
        // copy elements from temp array to original array
        for(int p=low;p<=high;p++)
        {
            nums[p] = temp[p-low];
        }
    }
    
    static int countReversePairs(int nums[], int low, int mid, int high)
    {
        int count = 0;
        int right = mid+1;
        for(int i=low; i<=mid; i++)
        {
            // check 2nd part elements with 1st part element
            while(right <= high && nums[i] > 2L*nums[right])
            {
                right++;
            }
            count+= right-(mid+1);
        }
        return count;
    } 


    public static void main(String[] args) {
        int arr1[] = {1,3,2,3,1};
        /* (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1 
        (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1 */
        System.out.println("Number of reverse pairs = "+ reversePairs(arr1));
        int arr2[] = {2147483647,2147483647,2147483647,2147483647,2147483647,2147483647};
        System.out.println("Number of reverse pairs = "+ reversePairsEfficient(arr2));
    }
    
}
