class MergeSort {
/*
 * Given an array arr[], its starting position l and its ending position r. Sort the array using merge sort algorithm.
 * https://www.geeksforgeeks.org/problems/merge-sort/1
 * T(c) -> O(nlogn), S(c) -> O(n)
 */
    static void mergeSort(int arr[], int l, int r)
    {
        if(l<r)
        {
            int mid = (l + r) / 2;
            // break left part into subpart
            mergeSort(arr, l, mid);
            // break right part into subpart
            mergeSort(arr, mid+1, r);
            // merge both left and right part
            merge(arr, l, mid, r);
        }
    }

    static void merge(int arr[], int l, int m, int r)
    {
        int i = l;
        int j = m+1;
        int k = 0;
        
        //  this array needed for merging both subarrays
        int B[] = new int[r-l+1];
        
        while(i<=m && j<=r)
        {
            //  merge array in sorted way
            if(arr[i] <= arr[j])
            {
                B[k++] = arr[i++];
            }
            else{
                B[k++] = arr[j++];
            }
        }
         
        //  add if anything present in left array
        while(i<=m)
        {
            B[k++] = arr[i++];
        }
        
        // add if anything present in right array
        while(j<=r)
        {
            B[k++] = arr[j++];
        }
        
        // copy back elements from B to arr
        for(int p=0;p<k;p++)
        {
            arr[p+l] = B[p];
        }
    }

    public static void main(String[] args) {
        int arr[] = {4,1,3,9,7};
        mergeSort(arr, 0, arr.length-1);
        for(int i=0;i<arr.length;i++)
        {
            System.out.print(arr[i] + " ");
        }
    }
}