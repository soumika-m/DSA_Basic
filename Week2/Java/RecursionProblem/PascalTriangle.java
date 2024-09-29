import java.util.ArrayList;

public class PascalTriangle {
/*
 * Given a positive integer N, return the Nth row of pascal's triangle.
 * Pascal's triangle is a triangular array of the binomial coefficients formed by summing up the elements of previous row.
 * The elements can be large so return it modulo 109 + 7.
 * https://www.geeksforgeeks.org/problems/pascal-triangle0652/1
 * T(c) -> O(n^2), S(c) -> O(n)
 */    
    static ArrayList<Long> nthRowOfPascalTriangle1(int n) {
        // 10^9 + 7
        int MOD = 1000000007;
        ArrayList<Long> result = new ArrayList<>();
        // 1st row will only contain 1
        result.add(1L);

        for(int row=2;row<=n;row++)
        {
            ArrayList<Long> currentList = new ArrayList<>();
            // 1st element will be always 1
            currentList.add(1L);
            for(int col=0;col<result.size()-1;col++)
            {
                // result will contain previous row elements
                currentList.add((result.get(col) + result.get(col+1)) % MOD);
            }
            // last element will be always 1
            currentList.add(1L);
            
            result = currentList;
        }
        return result;
    }

    /* 
    * It will not work for large numbers
    * T(c) -> O(n), S(c) -> O(n)
     */
    static ArrayList<Long> nthRowOfPascalTriangle2(int n) {
        ArrayList<Long> result = new ArrayList<>();
        long res = 1;
        result.add(res);
        // using formula = (row-col)/col derived from pattern ncr
        for(int col=1;col<n;col++)
        {
            res = res*(n-col);
            res = res/col;
            result.add(res);
        }
        return result;
    }

    public static void main(String[] args) {
        int n = 5;
        ArrayList<Long> arr1 = nthRowOfPascalTriangle1(n);
        ArrayList<Long> arr2 = nthRowOfPascalTriangle2(n);
        for(Long i:arr1)
        {
            System.out.print(i + " ");
        }
        System.out.println();

        for(Long i:arr2)
        {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}

