import java.util.ArrayList;

public class TravarseMatrixSpirally {

/*
 * Given a matrix of size r*c. Traverse the matrix in spiral form.
 * https://www.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1
 * T(c) -> O(r*c), S(c) -> O(r*c) // for storing element in answer array 
 */

    static ArrayList<Integer> spirallyTraverse(int matrix[][], int r, int c)
    {
        ArrayList<Integer> result = new ArrayList<>();
        int left = 0, right = c-1;
        int top = 0, down = r-1;
        
        while(top <= down && left <= right)
        {
            // going left to right
            for(int i=left;i<=right;i++)
            {
                result.add(matrix[top][i]);
            }
            top++;
            
            // going top to down
            for(int i=top;i<=down;i++)
            {
                result.add(matrix[i][right]);
            }
            right--;
            
            // check if more row present (consider if only one row present)
            if(top <= down)
            {
                // going right to left
                for(int i=right;i>=left;i--)
                {
                    result.add(matrix[down][i]);
                }
                down--;
            }
            
            // check if more column present
            if(left <= right)
            {
                // going down to top
                for(int i=down;i>=top;i--)
                {
                    result.add(matrix[i][left]);
                }
                left++;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        int matrix[][] = {
            {1, 2, 3, 4},
            {5, 6, 7, 8},
            {9, 10, 11, 12},
            {13, 14, 15,16}
        };

        ArrayList<Integer> result = spirallyTraverse(matrix, 4, 4);
        System.out.println(result);

        int matrix1[][] = {{22, 3, 21, 2}};
        System.out.println(spirallyTraverse(matrix1, 1, 4));

    }
    
}
