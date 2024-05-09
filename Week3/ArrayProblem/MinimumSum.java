import java.util.Arrays;

public class MinimumSum {
/*
 * Given an array Arr of size N such that each element is from the range 0 to 9. Find the minimum possible sum 
 * of two numbers formed using the elements of the array. All digits in the given array must be used to form the 
 * two numbers. Eg. {6, 8, 4, 5, 2, 3} -> The minimum sum is formed by numbers 358 and 246. -> 604
 * 
 * https://www.geeksforgeeks.org/problems/minimum-sum4058/1
 */

    /* it will not work for very big size of n
     * T(c) -> O(n), S(c) -> O(1) 
     */
    static String findMinSum(int[] arr, int n) {
        // sort the array
        Arrays.sort(arr);

        long firstNum = 0;
        long secondNum = 0;

        // create first num by using even index numbers of array, and second number by odd index
        for(int i=0;i<n;i++)
        {
            if(i%2 == 0)
            {
                firstNum *= 10;
                firstNum += arr[i]; 
            }
            else{
                secondNum *= 10;
                secondNum += arr[i];
            }
        }

        return Long.toString(firstNum + secondNum);
    }
   
    public static void main(String[] args) {
        int arr[] = {6, 8, 4, 5, 2, 3};
        System.out.println(findMinSum(arr, arr.length));
        
    }
}
