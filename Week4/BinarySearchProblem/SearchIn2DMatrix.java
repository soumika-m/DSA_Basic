public class SearchIn2DMatrix {
    
    /*
     * You are given an m x n integer matrix matrix with the following two properties: Each row is sorted in 
     * non-decreasing order. The first integer of each row is greater than the last integer of the previous row. 
     * Given an integer target, return true if target is in matrix or false otherwise.
     * 
     * https://leetcode.com/problems/search-a-2d-matrix/description/
     * T(c) -> O(n)*O(logm), S(c) -> O(1)
     */
    static public boolean searchMatrix(int[][] matrix, int target) {
        int row = matrix.length;
        int col = matrix[0].length;
        for(int i=0;i<row;i++)
        {
            // if target is present in that row
            if(matrix[i][0] <= target && target <= matrix[i][col-1])
            {
                return binarySearch(matrix[i], target);
            }
        }
        return false;
    }
    
    static boolean binarySearch(int[] arr, int target)
    {
        int low = 0;
        int high = arr.length-1;
        while(low <= high)
        {
            int mid = (low + high)/2;
            if(arr[mid] == target)
            {
                return true;
            }
            else if(arr[mid] > target)
            {
                high = mid-1;
            }
            else{
                low = mid+1;
            }
        }
        return false;
    }

    /*
     * T(c) -> O(log(m*n)), S(c) -> O(1)
     */
    static public boolean searchMatrixEfficient(int[][] matrix, int target) {
        int r = matrix.length;
        int c = matrix[0].length;
        
        // flatten the array from 2d to 1d by assumtion
        int low = 0;
        int high = (r*c)-1;
        
        // using binary search
        while(low <= high)
        {
            int mid = (low+high)/2;
            // point in 2d co-ordinate
            int row = mid/c;
            int col = mid%c;
            if(matrix[row][col] == target)
            {
                return true;
            }
            else if(matrix[row][col] > target)
            {
                high = mid-1;
            }
            else{
                low = mid+1;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int matrix[][] = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
        int target = 3;
        System.out.println(searchMatrix(matrix, target));
        System.out.println(searchMatrixEfficient(matrix, target));
    }

}
