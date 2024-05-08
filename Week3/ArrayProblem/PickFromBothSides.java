import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class PickFromBothSides {
/*
 * Given an integer array A of size N.
 * You have to pick exactly B elements from either left or right end of the array A to get the maximum sum.
 * Find and return this maximum possible sum.
 * Suppose B = 4 and array A contains 10 elements then, You can pick the first four elements or can pick the last four elements 
 * or can pick 1 from the front and 3 from the back etc. you need to return the maximum possible sum of elements you can pick. 
 * 
 * https://www.interviewbit.com/problems/pick-from-both-sides/
 * T(c) -> O(B), S(c) -> O(1)
 */

    static int maxSumFromBothSide(ArrayList<Integer> A, int B) {
        int n = A.size();
        int currentSum = 0;
        // calculate sum of left side of array (B elements)
        for(int i=0;i<B;i++)
        {
            currentSum += A.get(i);
        }
        int maxSum = currentSum;
        
        // using sliding window take elements from end of right side and remove elements from left side end, find maximum
        for(int j=0;j<B;j++)
        {
            currentSum += A.get(n-1-j) - A.get(B-1-j);
            maxSum = Math.max(maxSum, currentSum);
        }
        
        return maxSum;
    }

    public static void main(String[] args) {
        ArrayList<Integer> A1 = new ArrayList<>(List.of(5, -2, 3 , 1, 2));
        int B = 3;
        System.out.println(maxSumFromBothSide(A1, B));
        ArrayList<Integer> A2 = new ArrayList<>(List.of(-533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35));
        B = 48;
        System.out.println(maxSumFromBothSide(A2, B));
    }
}
