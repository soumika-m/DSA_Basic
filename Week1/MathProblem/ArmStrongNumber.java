public class ArmStrongNumber {

/*
 * For a given 3 digit number, find whether it is armstrong number or not. 
 * An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the 
 * number itself. Return "Yes" if it is a armstrong number else return "No".
 * 
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

    public static void main(String[] args) {
        int N = 157;
        System.out.println("Armstrong Number? "+ N +" = "+  armstrongNumber(N));
        N = 153;
        System.out.println("Armstrong Number? "+ N +" = "+  armstrongNumber(N));
    }
    
}
