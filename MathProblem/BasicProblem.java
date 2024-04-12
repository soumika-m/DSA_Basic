import java.util.ArrayList;
import java.util.Collections;
public class BasicProblem {

/* (1)
* Count the number of digits in N which evenly divide N.
* https://www.geeksforgeeks.org/problems/count-digits5716/1
* T(c) -> O(logN)
*/

    static int evenlyDivides(int N){
        // code here
        int temp = N;
        int count = 0;
        while(temp > 0)
        {
            int rem = temp%10;
            /* evenly divisible */
            if(rem != 0 && N % rem == 0)
            {
                count++;
            }
            temp = temp/10;
        }
        return count;
    }

/* (2)
* Return "Yes" if it is a armstrong number else return "No".
* https://practice.geeksforgeeks.org/problems/armstrong-numbers2727/1
* T(c) -> O(1) // as n will be always 3 digit number (constant)
* if n is not constant (variable in nature), T(c) -> O(logn)
*/    
    static String armstrongNumber(int n){

        int temp = n;
        int cubeSum = 0;
        while(temp > 0)
        {
            int digit = temp%10;
            cubeSum += Math.pow(digit,3);
            temp = temp/10;
        }
        
        if(cubeSum == n)
        {
            return "Yes";
        }
        else{
            return "No";
        }
    }

/* (3)
 * Given a mathematical equation that contains only numbers and +, -, *, /. 
 * Print the equation in reverse, such that the equation is reversed, but the numbers remain the same.
 * https://practice.geeksforgeeks.org/problems/reversing-the-equation2205/1
 * T(c) -> O(N) / O(|S|)
 */

    static String reverseEqn(String S)
    {
        StringBuilder res = new StringBuilder();
        StringBuilder number = new StringBuilder();
        // your code here
        for(int i=S.length()-1; i>=0; i--)
        {
            char ch = S.charAt(i);
            // numbers
            if(ch >= '0' && ch <='9')
            {
                number.append(ch);
            }
            // operators
            else{
                number.reverse();
                res.append(number.toString());
                res.append(ch);
                number.setLength(0);
            }
        }
        number.reverse();
        res.append(number.toString());

        return res.toString();
    }

/* (4)
 * Given an integer N, print all the divisors of N in the ascending order.
 * https://practice.geeksforgeeks.org/problems/all-divisors-of-a-number/1
 * T(c) -> sqrt(N), space -> sqrt(N)
 */
    public static void printDivisors(int n) {
        // code here
        ArrayList<Integer> divisors = new ArrayList<>();
        // run loop till sqrt(n)
        for(int i=1;i*i<=n;i++)
        {
            // if i is divisors of n, add that to list
            if(n%i == 0)
            {
                divisors.add(i);
                // if another number(multiple) is not same as i, add to list
                if(i != n/i)
                {
                    divisors.add(n/i);
                }
            }
        }
        
        // sort the list
        Collections.sort(divisors); 
    
        // print the divisors
        for(int divisor:divisors)
        {
            System.out.print(divisor + " ");
        }
    }

/* (5)
 * Given a number n.Find if the digit sum(or sum of digits) of n is a Palindrome number or not.
 * https://www.geeksforgeeks.org/problems/sum-of-digit-is-pallindrome-or-not2751/1
 * T(c) -> O(log(n)) or O(d) where d is number of digits, space -> O(1)
 */

    static int isDigitSumPalindrome(int n) {
        // code here
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
        
        // if reversed, the number stays same as before
        if(n == rev)
        {
            return true;
        }
        else{
            return false;
        }
    }

/* (6)
 * Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
 * https://leetcode.com/problems/add-digits/
 * T(c) -> O(log(n)) or O(d) where d is number of digits, space -> O(1)
 */ 

    static int addDigits(int num) {
        while(num>=10)
        {
            num = digitSum(num); 
        }
        return num;
    }
    
    static int digitSum(int num)
    {
        int temp = num;
        int sum = 0;
        while(temp > 0)
        {
            int digit = temp%10;
            sum += digit;
            temp = temp/10;
        }
        return sum;
    }

    /* 
    * T(c) -> O(1) 
    */
    public int addDigitsEfficient(int num) {
    //  if number is 0, return 0
        if(num == 0)
        {
            return 0;
        }

    //  using digital root formula - dr(n)=n%9 or dr(n)=1+(n-1)%9
    //  if number is divisible by 9, we need to return 9 instead of 0
        if(num % 9 == 0)
        {
            return 9;
        }
        else{
            return num % 9;
        }
    }

/* (7)
 * Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
 * T(c) -> O(n)
 */
    public static int smallestEvenMultiple(int n) {
        int i = 1;
        int j = 1;
        // if multiple of 2 and multiple of n are not matching 
        while(2*i != n*j)
        {
            // if multiple of 2 is greater than multiple of n, we will check for next multiple of n
            if((2*i) > (n*j))
            {
                j++;
            }
            // if multiple of 2 is equal to multiple of n, that is the smallest integer
            if((2*i) == (n*j))
            {
                return (2*i);
            }
            // we will check for next multiple of 2 in each iteration
            i++;
        }
        // out of while loop means both multiples are matching
        return (2*i);
    }

    /* 
    * checking if number even or odd, and returing appropriate result
    * T(c) -> O(1)
     */
    public static int smallestEvenMultipleEfficient(int n) {
        // if n is even, smallest multiple of 2 and n will be n itself.
        if(n % 2 == 0)
        {
            return n;
        }
        // if n is odd, smallest multiple of both 2 and n will be 2*n 
        else{
            return n*2;
        }
    }

/* (8)
 * Given two positive integers a and b, return the number of common factors of a and b.
 * An integer x is a common factor of a and b if x divides both a and b.
 * T(c) -> O(min(a,b)), space -> O(1)
 */
    public static int commonFactors(int a, int b) {
        int min = Math.min(a,b);
        int count = 0;
        for(int i=1;i<=min;i++)
        {
            // finding common factors
            if(a%i == 0 && b%i == 0)
            {
                count++;
            }
        }
        return count;
    }


    public static void main(String args[])
    {
        int N = 12;
        System.out.println("Evenly Divides? = "+ evenlyDivides(N));
        N = 157;
        System.out.println("Armstrong Number? "+ N +" = "+  armstrongNumber(N));
        String eq1 = "20-3+5*2";
        System.out.println("Reverse Equation? "+ eq1 +" = "+  reverseEqn(eq1));
        N = 20;
        System.out.print("Printing Divisors of "+ N +" = ");
        printDivisors(N);
        System.out.println();
        N = 56;
        System.out.println("Sum of digits is Palindrome Number? "+ N +" = "+  isDigitSumPalindrome(N));
        N = 2147483647;  // 2^31-1
        System.out.println("After adding digits of "+ N +" repeatedly this single digit generated = "+  addDigits(N));
        N = 5;
        System.out.println("Smallest Even Multiple of "+ N+ " = "+ smallestEvenMultiple(N));
        System.out.println("Smallest Even Multiple (efficient) of "+ N+ " = "+ smallestEvenMultiple(N));
        int a = 12, b = 6;  // factors are 1,2,3,6
        System.out.println("Common Factor count of "+a+", "+b+" = "+commonFactors(a,b));
    }
}
