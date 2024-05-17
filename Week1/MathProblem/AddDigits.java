public class AddDigits {

/*
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
        // if number is 0, return 0
        if(num == 0)
        {
            return 0;
        }

        // using digital root formula - dr(n)=n%9 or dr(n)=1+(n-1)%9
        // if number is divisible by 9, we need to return 9 instead of 0
        if(num % 9 == 0)
        {
            return 9;
        }
        else{
            return num % 9;
        }
    }

    public static void main(String[] args) {
        int N = 2147483647;  // 2^31-1
        System.out.println("After adding digits of "+ N +" repeatedly this single digit generated = "+  addDigits(N));
    }

}
