public class CountInversion {

/*
 * Given an array of integers. Find the Inversion Count in the array. For an array, inversion count indicates how 
 * far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
 * If an array is sorted in the reverse order then the inversion count is the maximum. 
 * Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
 * 
 * https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
 * T(c) -> O(n^2), S(c) -> O(1)
 */
    static long inversionCount(long arr[], long N)
    {
        long count = 0;
        for(int i=0;i<N;i++)
        {
            for(int j=i+1;j<N;j++)
            {
                if(arr[i]>arr[j])
                {
                    count++;
                }
            }
        }
        return count;
    }


    /* 
    * Using mergesort algo to check a[i]>a[j] while merging
    * T(c) -> O(nlogn), S(c) -> O(n)
     */
    static long inversionCountEfficient(long arr[], long N)
    {
        return mergeSort(arr, 0, arr.length-1);
    }
    
    static long mergeSort(long arr[], int low, int high)
    {
        long count = 0;
        // continue until one or no element is remaining
        if(low < high)
        {
            int mid = (low+high)/2;
            count += mergeSort(arr, low, mid);
            count += mergeSort(arr, mid+1, high);
            count += merge(arr, low, mid, high);
        }
        return count;
    }
    
    static long merge(long arr[], int low, int mid, int high)
    {
        int i = low;
        int j = mid+1;
        int k = 0;
        
        // for counting the pairs
        long cnt = 0;
        
        // for storing elements after merging
        long B[] = new long[high-low+1];
        
        // if left and right both array contains elements
        while(i<=mid && j<=high)
        {
            if(arr[i] <= arr[j])
            {
                B[k++] = arr[i++];
            }
            // inversion found, from that index till last index , all can form the pair
            else{
                B[k++] = arr[j];
                cnt += (mid-i+1);
                j++;
            }
        }
        
        // if only left array still contains elements
        while(i<=mid)
        {
            B[k++] = arr[i++];
        }
        
        // if only right array still contains elements
        while(j<=high)
        {
            B[k++] = arr[j++];
        }
        
        // shifting elements from B to arr
        for(int l=0;l<k;l++)
        {
            arr[l+low] = B[l];
        }
        
        return cnt;
    }


    public static void main(String[] args) {
        long arr[] = {2, 4, 1, 3, 5};
        /*  The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3) */
        System.out.println("Inversion Count = "+ inversionCount(arr, arr.length));
        System.out.println("Inversion Count = "+ inversionCountEfficient(arr, arr.length));
    }
    
}
