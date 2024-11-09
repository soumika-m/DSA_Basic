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
     * T(c) -> O(nlogn), S(c) -> O(1) 
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

    /* 
    * using string
    * T(c) -> O(nlogn), S(c) -> O(n)
    */
    static String findMinSumEfficient(int[] arr, int n) {
        // sort the array
        Arrays.sort(arr);

        StringBuilder firstNum = new StringBuilder();
        StringBuilder secondNum = new StringBuilder();

        // create first num by using even index numbers of array, and second number using odd index
        for(int i=0;i<n;i++)
        {
            if(i%2 == 0)
            {
                firstNum.append(arr[i]);
            }
            else{
                secondNum.append(arr[i]);
            }
        }

        int j = firstNum.length()-1;
        int k = secondNum.length()-1;

        StringBuilder ans = new StringBuilder();
        int carry = 0;

        // if any of the number digits present while doing addition, or we have carry
        while(j >= 0 || k >= 0 || carry > 0)
        {
            int sum = carry;
            // if only firstnumber is left
            if(j >= 0)
            {
                sum += (firstNum.charAt(j--) - '0');
            }
            // if only secondnumber is left
            if(k >= 0)
            {
                sum += (secondNum.charAt(k--) - '0');
            }
            ans.append(sum % 10);
            carry = sum / 10;
        }

        // reverse final string as we are appending number from left to right
        ans.reverse();

        // to remove leading zeros which will appear ahead of our sum, if all zeros keep last one
        while(ans.length() > 1 && ans.charAt(0) == '0')
        {
            ans.deleteCharAt(0);
        }

        return ans.toString();
    }
   
    public static void main(String[] args) {
        int arr1[] = {6, 8, 4, 5, 2, 3};
        System.out.println(findMinSum(arr1, arr1.length));
        int arr2[] = {0, 0, 0, 0, 0};
        System.out.println(findMinSumEfficient(arr2, arr2.length));
    }
}

/* 
carry = 0

 [2,3,4,5,6,8]
  2 4 6
+ 3 5 8
 ----------
  6 0 4

 12/10 = 1
 12%10 = 2 
*/

