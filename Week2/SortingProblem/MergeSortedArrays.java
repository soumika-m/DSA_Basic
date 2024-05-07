class MergeSortedArrays{
/*
 * You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
 * representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted 
 * in non-decreasing order. The final sorted array should not be returned by the function, but instead be stored inside
 * the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that
 * should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
 * 
 * https://leetcode.com/problems/merge-sorted-array/
 * T(c) -> O(m+n), S(c) -> O(m+n)
 */

    static void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = 0, j = 0, k = 0;
        int res[] = new int[m+n];
        // compare elements and put in result array
        while(i<m && j<n)
        {
            // put num1 element in array
            if(nums1[i] <= nums2[j])
            {
                res[k++] = nums1[i++];
            }
            // put num2 element in array
            else {
                res[k++] = nums2[j++];
            }
        }
        
        // put remaining elements of nums1
        while(i<m)
        {
            res[k++] = nums1[i++];
        }
        
        // put remaining elements of nums2
        while(j<n)
        {
            res[k++] = nums2[j++];
        }
        
        // copy back elements from result array to nums1
        for(int l=0;l<m+n;l++)
        {
            nums1[l] = res[l];
        }
    }

    /* 
    * merge 2 arrays without using extra space
    * T(c) -> O(m+n), S(c) -> O(1)
    */
    public void mergeInplace(int[] nums1, int m, int[] nums2, int n) {
        int i = m-1;
        int j = n-1;
        int k = m+n-1;

        // using 2 pointers algo
        while(j>=0)
        {
            // compare elements from the end of both array and place larger element at the end of nums1 array
            if(i>=0 && nums1[i] > nums2[j])
            {
                nums1[k--] = nums1[i--];
            }
            else{
                nums1[k--] = nums2[j--];
            }
        }
    }


    public static void main(String[] args) {
        int nums1[] = {1,2,3,0,0,0};
        int m = 3;
        int nums2[] = {2,5,6};
        int n = 3;
        merge(nums1, m, nums2, n);
        for(int i=0;i<nums1.length;i++)
        {
            System.out.print(nums1[i]+" ");
        }
        System.out.println();
        mergeInplace(nums1, m, nums2, n);
        for(int i=0;i<nums1.length;i++)
        {
            System.out.print(nums1[i]+" ");
        }
        System.out.println();
    }
}