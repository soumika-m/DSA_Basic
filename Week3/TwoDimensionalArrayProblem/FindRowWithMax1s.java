public class FindRowWithMax1s {

/*
 * Given a boolean 2D array of n x m dimensions, consisting of only 1's and 0's, where each row is sorted. Find the 
 * 0-based index of the first row that has the maximum number of 1's.  If no such row exists, return -1.
 * 
 * https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1
 * T(c) -> O(n*m), S(c) -> O(1)
 */
    static int rowWithMax1s(int arr[][], int n, int m) {
        int maxNum = 0;
        int rowIndex = -1;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                // when 1 found, as array is already sorted, calculate count of 1 and break
                if(arr[i][j] == 1 && m-j > maxNum)
                {
                    maxNum = m-j;
                    rowIndex = i;
                    break;
                }
            }
        }
        return rowIndex;
    }
   

    public static void main(String[] args) {
        int matrix[][] =  {
            {0, 1, 1, 1},
            {0, 0, 1, 1},
            {1, 1, 1, 1},
            {0, 0, 0, 0}
        };

        System.out.println("Row contains max 1s = " + rowWithMax1s(matrix, matrix.length, matrix[0].length));
    }
    
}
