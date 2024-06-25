public class PeakElement2D {
    
    /*
     * A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the 
     * left, right, top, and bottom. Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find 
     * any peak element mat[i][j] and return the length 2 array [i,j]. You may assume that the entire matrix is 
     * surrounded by an outer perimeter with the value -1 in each cell.
     * 
     * https://leetcode.com/problems/find-a-peak-element-ii/
     * T(c) -> O(logn * m), S(c) -> O(1)
     */

    static public int[] findPeakGrid(int[][] mat) {
        int row = mat.length; //m
        int col = mat[0].length; //n

        int low = 0;
        int high = col-1;
        
        // using binary search column by column
        while(low <= high)
        {
            int mid = (low + high)/2;
            
            // checking max element for each column
            int maxRowIndex = findMaxRowElementIdx(mat, row, mid);
            
            // As we are checking max element in column, no need to check for above and below element, as that is already larger
            int left = mid-1 >= 0 ? mat[maxRowIndex][mid-1] : -1;
            int right = mid+1 < col ? mat[maxRowIndex][mid+1] : -1;
            
            if(mat[maxRowIndex][mid] > left && mat[maxRowIndex][mid] > right) 
            {
                return new int[]{maxRowIndex,mid};              
            }
            else if(left < mat[maxRowIndex][mid])
            {
                low = mid+1;
            }
            else {
                high = mid-1;
            }
        }
        return new int[] {-1, -1};
    }
    
    static int findMaxRowElementIdx(int[][] mat, int row, int col)
    {
        // find max element in each column -> iterate over each row
        int max = -1;
        int rowIdx = 0;
        for(int i=0;i<row;i++)
        {
            if(mat[i][col] > max)
            {
                max = mat[i][col];
                rowIdx = i;
            }
        }
        return rowIdx;
    }

    public static void main(String[] args) {
        int mat[][] = {{10,20,15},{21,30,14},{7,16,32}};
        int res[] = findPeakGrid(mat);
        System.out.println("index = " + res[0] + " " + res[1]);
        System.out.println("Peak element = "+ mat[res[0]][res[1]]);
    } 

}
