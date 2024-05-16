public class SumOfDigitPalindrome {
/*
 * Given a number n. Find if the digit sum(or sum of digits) of n is a Palindrome number or not.
 * https://www.geeksforgeeks.org/problems/sum-of-digit-is-pallindrome-or-not2751/1
 * T(c) -> O(log(n)) or O(d) where d is number of digits, space -> O(1)
 */

    static int isDigitSumPalindrome(int n) {

        int temp = n;
        int sum = 0;
        // finding digit sum
        while(temp > 0)
        {
            int digit = temp%10;
            sum += digit;
            temp = temp/10;
        }
        
        if(isPalindrome(sum))
        {
            return 1;
        }
        else{
            return 0;
        }
    }

    // if reversed, the number stays same as before
    static boolean isPalindrome(int n)
    {
        int temp = n;
        int rev = 0;
        while(temp > 0)
        {
            int digit = temp%10;
            rev = (rev*10)+digit;
            temp = temp/10;
        }  
        
        if(n == rev)
        {
            return true;
        }
        else{
            return false;
        }
    }

    public static void main(String[] args) {
        int N = 56;
        System.out.println("Sum of digits is Palindrome Number? "+ N +" = "+  isDigitSumPalindrome(N));
    }

}
