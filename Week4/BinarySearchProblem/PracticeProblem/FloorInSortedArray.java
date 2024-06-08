class FloorInSortedArray{

    /*
     * Given a sorted array arr[] of size N without duplicates, and given a value x. Floor of x is defined as the largest 
     * element K in arr[] such that K is smaller than or equal to x. Find the index of K(0-based indexing). 
     * Return -1 if there isn't any such number.
     * 
     * https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1
     * T(c) -> O(logn), S(c) -> O(1)
     */
    static int findFloor(long arr[], int n, long x)
    {
        int ans = -1;
        int low = 0;
        int high = n-1;
        while(low <= high)
        {
            int mid = low + (high-low)/2;
            // largest number, less than equal to x
            if(arr[mid] > x)
            {
                high = mid-1;
            }
            else
            {
                ans = mid;
                low = mid+1;
            }
        }
        return ans;
    }


    public static void main(String[] args) {
        long arr[] = {1,2,8,10,11,12,19};
        System.out.println(findFloor(arr, arr.length, 5));
    }
}