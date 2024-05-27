class RotateImage{

/*
 * You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
 * 
 * https://leetcode.com/problems/rotate-image/
 * T(c) -> O(n^2), S(c) -> O(n^2)
 */
    static void rotate(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        int result[][] = new int[row][col];
        
        int i = row-1;
        int k = 0;
        
        // take elements, start from last row and put that in result array in correct place
        while(i>=0 && k<col)
        {
            for(int j=0;j<col;j++)
            {
                result[j][k] = matrix[i][j];
            }
            i--;
            k++;
        }
        
        // copying back element to original matrix
        for(int p=0;p<row;p++)
        {
            for(int j=0;j<col;j++)
            {
                matrix[p][j] = result[p][j];
            }
        }
    }


    /*
     * Using inplace method, transpose and reverse
     * T(c) -> O(n*n) + O(n*n)
     * S(c) - > O(1)
     */
    static void rotateEfficient(int[][] matrix) {
        int n = matrix.length;
        
        // transpose matrix
        for(int i=0;i<n-1;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                // swap elements from top diagonal with bottom diagonal
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        
        // take every row and reverse it
        for(int i=0;i<n;i++)
        {
            for(int j=0,k=n-1;j<k;j++,k--)
            {
                //swap elements
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][k];
                matrix[i][k] = temp;
            }
        }
    }

    static void printMatrix(int[][] matrix)
    {
        for(int i=0;i<matrix.length;i++)
        {
            for(int j=0;j<matrix[0].length;j++)
            {
               System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }


    public static void main(String[] args) {
        int matrix1[][] = {
            {1, 2, 3, 4},
            {5, 6, 7, 8},
            {9, 10, 11, 12},
            {13, 14, 15,16}
        };
        rotate(matrix1);
        printMatrix(matrix1);

        int matrix2[][] = {{1,2,3},{4,5,6},{7,8,9}};
        rotate(matrix2);
        printMatrix(matrix2);
    }
}