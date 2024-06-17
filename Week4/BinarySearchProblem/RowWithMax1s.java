public class RowWithMax1s {
    
    /*
     * Given a integer 2D array of n x m dimensions, consisting of only 1's and 0's, where each row is 
     * sorted. Find the 0-based index of the first row that has the maximum number of 1's.
     * 
     * https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1
     * T(c) -> O(n*m), S(c) -> O(1)
     */
    static int rowWithMax1s(int arr[][], int n, int m) {
        int maxcnt = 0;
        int rowIdx = -1;
        for(int i=0;i<n;i++)
        {
            int count = 0;
            for(int j=0;j<m;j++)
            {
                // as subarray contains 1 and 0, sum will act as counting 1's
                count += arr[i][j];
            }
            
            if(count > maxcnt)
            {
                maxcnt = count;
                rowIdx = i;
            }
        }
        return rowIdx;
    }

    /*
     * Using binary search
     * T(c) -> O(n * logm), S(c) -> O(1)
     */
    static int rowWithMax1sUsingBS(int arr[][], int n, int m) {
        int maxcnt = 0;
        int rowIdx = -1;
        for(int i=0;i<n;i++)
        {
            int countOnes = m - findFirstOccurance(arr[i], m, 1);
            
            if(countOnes > maxcnt)
            {
                maxcnt = countOnes;
                rowIdx = i;
            }
        }
        return rowIdx;
    }
    
    static int findFirstOccurance(int arr[], int n, int target)
    {
        // consider element is present after last index of array
        int firstIdx = n;
        int low = 0;
        int high = n-1;
        while(low <= high)
        {
            int mid = low + (high-low)/2;
            if(arr[mid] == target)
            {
                firstIdx = mid;
                high = mid-1;
            }
            else{
                low = mid+1;
            }
        }
        return firstIdx;
    }



    public static void main(String[] args) {
        int arr[][] = {{0, 1, 1, 1},
        {0, 0, 1, 1},
        {1, 1, 1, 1},
        {0, 0, 0, 0}};
        System.out.println("Row number where max 1's present = "+ rowWithMax1s(arr, arr.length, arr[0].length));
        System.out.println("Row number where max 1's present = "+ rowWithMax1sUsingBS(arr, arr.length, arr[0].length));
    }

}
