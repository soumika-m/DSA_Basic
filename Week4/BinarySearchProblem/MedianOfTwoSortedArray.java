public class MedianOfTwoSortedArray {
    
    /*
     * Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
     * https://leetcode.com/problems/median-of-two-sorted-arrays/
     * T(c) -> O(n1+n2) , S(c) -> O(n1+n2)
     */
    static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n1 = nums1.length;
        int n2 = nums2.length;
        int n3 = n1+n2;
        
        int[] buffer = new int[n3];
        // merge both array in sorted order
        int i = 0;
        int j = 0;
        int k = 0;
        while(i<n1 && j<n2)
        {
            if(nums1[i] < nums2[j])
            {
                buffer[k++] = nums1[i++];
            }
            else{
                buffer[k++] = nums2[j++];
            }
        }
        
        while(i<n1)
        {
            buffer[k++] = nums1[i++];
        }
        
        while(j<n2)
        {
            buffer[k++] = nums2[j++];
        }
        
        double ans = -1;
        // if merged array is of odd size, there is only one median
        if(n3 % 2 == 1)
        {
            int mid = n3/2;
            ans  = buffer[mid];
            return ans;
        }
        
        // if merged array is of even size, there will be 2 median
        int mid1 = n3/2;
        int mid2 = mid1-1;
        ans = (double)(buffer[mid1]+buffer[mid2])/2;
        return ans;
    }

    /*
     * Without using extra space
     * T(c) -> O(n1+n2) , S(c) -> O(1)
     */
    static double findMedianSortedArraysBetter(int[] nums1, int[] nums2) {
        int n1 = nums1.length;
        int n2 = nums2.length;
        // cnt will keep track of index as we merge the array by assumption
        int cnt = 0;
        
        int i = 0;
        int j = 0;
        
        // keep track of median index
        int mid2 = (n1+n2)/2;
        int mid1 = mid2-1;
        
        int idx_el1 = -1, idx_el2 = -1;
        
        while(i<n1 && j<n2)
        {
            if(nums1[i] < nums2[j])
            {
                if(cnt == mid1) { idx_el1 = nums1[i]; }
                if(cnt == mid2) { idx_el2 = nums1[i]; }
                cnt++;
                i++;
            }
            else{
                if(cnt == mid1) { idx_el1 = nums2[j]; }
                if(cnt == mid2) { idx_el2 = nums2[j]; }
                cnt++;
                j++;
            }
        }
        
        while(i<n1)
        {
            if(cnt == mid1) { idx_el1 = nums1[i]; }
            if(cnt == mid2) { idx_el2 = nums1[i]; }
            cnt++;
            i++;
        }
        
        while(j<n2)
        {
            if(cnt == mid1) { idx_el1 = nums2[j]; }
            if(cnt == mid2) { idx_el2 = nums2[j]; }
            cnt++;
            j++;
        }
        
        // if n1+n2 array is of odd size, there is only one median
        if((n1+n2) % 2 == 1)
        {
            return (double)idx_el2;
        }
        
        // if n1+n2 array is of even size, there will be two median
        return (double)(idx_el1 + idx_el2)/2.0;
    }

    /*
     * Using binary search
     * T(c) -> O(min(logn1, logn2)), S(c) -> O(1)
     */
    static double findMedianSortedArraysOptimal(int[] nums1, int[] nums2) {
        int n1 = nums1.length;
        int n2 = nums2.length;
        
        if(n1 > n2) {
            return findMedianSortedArrays(nums2,nums1);
        }
        
        int low = 0;
        int high = n1;
        int left = (n1+n2+1)/2;
        int n = n1+n2;
        
        while(low <= high)
        {
            // elements to selct from array1
            int mid1 = (low+high)/2;
            // elements to select from array2
            int mid2 = left-mid1;
            int l1 = Integer.MIN_VALUE, l2 = Integer.MIN_VALUE;
            int r1 = Integer.MAX_VALUE, r2 = Integer.MAX_VALUE;
            
            if(mid1 < n1) { r1 = nums1[mid1]; }
            if(mid2 < n2) { r2 = nums2[mid2]; }
            if(mid1 - 1 >= 0) { l1 = nums1[mid1-1]; }
            if(mid2 - 1 >= 0) { l2 = nums2[mid2-1]; }
            
            if(l1 <= r2 && l2 <= r1)
            {
                // odd size of merged array
                if(n%2 == 1)
                {
                    return (double)Math.max(l1,l2);
                }
                // even size
                else{
                    return (double)(Math.max(l1,l2) + Math.min(r1,r2)) / 2.0;
                }
            }
            // decrement the select value of array1
            else if(l1 > r2)
            {
                high = mid1-1;
            }
            // increment the select value of array1
            else{
                low = mid1+1;
            }
        }
        return 0;
    }

    public static void main(String args[])
    {
        int[] nums1 = {1,3};
        int[] nums2 = {2};
        System.out.println(findMedianSortedArrays(nums1, nums1));

        int[] arr1 = {1,2};
        int[] arr2 = {3,4};
        System.out.println(findMedianSortedArraysBetter(arr1, arr2));
        
        int[] a1 = {1,3};
        int[] a2 = {2,4,5,6};
        System.out.println(findMedianSortedArraysOptimal(a1, a2));
    }
}
