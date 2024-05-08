import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class SortArrayWithSquares{
/*
 * Given a sorted array A containing N integers both positive and negative.
 * You need to create another array containing the squares of all the elements in A and return it in non-decreasing order.
 * https://www.interviewbit.com/problems/sort-array-with-squares/
 * T(c) -> O(nlogn), S(c) -> O(n)
 */
    static ArrayList<Integer> sortWithSquares(ArrayList<Integer> A) {
        ArrayList<Integer> result = new ArrayList<>();
        
        for(int i=0;i<A.size();i++)
        {
            int num = A.get(i);
            int square = num * num;
            result.add(i,square);
        }
        Collections.sort(result);
        return result;
    }

    /*
     * check from both end of array and insert in result accordingly
     * T(c) -> O(n), S(c) -> O(n)
     */
    static ArrayList<Integer> sortWithSquaresEfficient(ArrayList<Integer> A) {
        int n = A.size();
        ArrayList<Integer> result = new ArrayList<>(Collections.nCopies(n,0));
        
        int left = 0;
        int right = n-1;
        int i = n-1;
        
        while(left <= right)
        {
            int leftSquare = A.get(left) * A.get(left);
            int rightSqaure = A.get(right) * A.get(right);
            if(rightSqaure > leftSquare)
            {
                result.set(i--,rightSqaure);
                right--;
            }
            else{
                result.set(i--,leftSquare);
                left++;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<>(List.of(-6, -3, -1, 2, 4, 5));
        System.out.println(sortWithSquares(arr));
        System.out.println(sortWithSquaresEfficient(arr));
    }
}