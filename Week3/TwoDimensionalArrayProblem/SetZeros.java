import java.util.ArrayList;
import java.util.Arrays;

public class SetZeros {

/*
 * Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
 * https://leetcode.com/problems/set-matrix-zeroes/
 * 
 * T(c) -> (O(m*n) * O(m+n)) + O(m*n) , S(c) -> O(1)
 * 
 * This code will not work if matrix will have negative values
 */
    public static void setZeroes(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        
        //  identify where 0 present, make corresponding row and column values as -1, except 0
        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {
                if(matrix[i][j] == 0)
                {
                    markRow(matrix, i);
                    markColumn(matrix, j);
                }
            }
        }
        
        // resetting those -1 to 0
        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {
                if(matrix[i][j] == -1)
                {
                    matrix[i][j] = 0;
                }
            }
        }
    }
    
    // mark entire row as -1, except 0 values
    static void markRow(int[][] matrix, int rowNum)
    {
        int col = matrix[0].length;
        for(int i=0;i<col;i++)
        {
            if(matrix[rowNum][i] != 0)
            {
                matrix[rowNum][i] = -1;
            } 
        }
    }
    
    // mark entire column as -1, except 0 values
    static void markColumn(int[][] matrix, int columnNum)
    {
        int row = matrix.length;
        for(int i=0;i<row;i++)
        {
            if(matrix[i][columnNum] != 0)
            {
                matrix[i][columnNum] = -1;
            }
        }
    }

    /*
     * Using extra row and column array
     * T(c) -> O(m*n) + O(m*n) => O(2*m*n)
     * S(c) -> O(m+n)
     */
    public static void setZeroesEffiecient(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        
        // for tracking which row index contains 0
        int rowArray[] = new int[row];
        // for tracking which column index contains 0
        int colArray[] = new int[col];
        
        //  identify where 0 present, keep track of row and column number in separate array
        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {
                if(matrix[i][j] == 0)
                {
                    rowArray[i] = 1;
                    colArray[j] = 1;
                }
            }
        }
        
        // iterate matrix, check row and column array to know if need to make 0 or not
        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {
                if(rowArray[i] == 1 || colArray[j] == 1)
                {
                    matrix[i][j] = 0;
                }
            }
        }
    }

    /*
     * Without using extra space, inplace
     * T(c) -> O(n*m) + O(n*m) => O(2*n*m)
     * S(c) -> O(1)
     */
    public static void setZeroesOptimal(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        
        // rowarray -> matrix[0][....]
        // colarray -> matrix[...][0]
        
        // for tracking first column
        int colSpace = 1;
        
        // identifying 0 elements, marking elements in first row, first column and colSpace variable
        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {
                if(matrix[i][j] == 0)
                {
                    // marking in rowarray
                    matrix[i][0] = 0;
                    
                    // marking in colarray
                    if(j != 0)
                    {
                        matrix[0][j] = 0;
                    }
                    else{
                        colSpace = 0;
                    }  
                }
            }
        }
        
        // except first row and column, iterate and make change, by looking at rowarray or colarray
        for(int i=1;i<row;i++)
        {
            for(int j=1;j<col;j++)
            {
                if(matrix[i][j] != 0)
                {
                    if(matrix[i][0] == 0 || matrix[0][j] == 0)
                    {
                        matrix[i][j] = 0;
                    }
                }
            }
        }
        
        // make entire first row as 0
        if(matrix[0][0] == 0)
        {
            for(int i=0;i<col;i++)
            {
                matrix[0][i] = 0;
            }
        }
        
        // make entire first column as 0
        if(colSpace == 0)
        {
            for(int i=0;i<row;i++)
            {
                matrix[i][0] = 0;
            }
        } 
    }


    static void printMatrix(int[][] matrix)
    {
        for(int i=0;i<matrix.length;i++)
        {
            for(int j=0;j<matrix[0].length;j++)
            {
                System.out.print(matrix[i][j]+ " ");
            }
            System.out.println();
        }
    }


    public static void main(String[] args) {
        int matrix1[][] = {{1,1,1},{1,0,1},{1,1,1}};
        System.out.println("Original Matrix = ");
        printMatrix(matrix1);
        setZeroes(matrix1);
        System.out.println("Modified Matrix = ");
        printMatrix(matrix1);

        int matrix2[][] = {{0,1,2,0},{3,4,5,2},{1,3,1,5}};
        System.out.println("Original Matrix = ");
        printMatrix(matrix2);
        setZeroesEffiecient(matrix2);
        System.out.println("Modified Matrix = ");
        printMatrix(matrix2);

        int matrix3[][] = {{0,1,2,0},{3,4,5,2},{1,3,1,5}};
        System.out.println("Original Matrix = ");
        printMatrix(matrix3);
        setZeroesOptimal(matrix3);
        System.out.println("Modified Matrix = ");
        printMatrix(matrix3);
    }

}
