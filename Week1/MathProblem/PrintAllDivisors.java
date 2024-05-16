import java.util.ArrayList;
import java.util.Collections;

public class PrintAllDivisors {

/*
 * Given an integer N, print all the divisors of N in the ascending order.
 * https://practice.geeksforgeeks.org/problems/all-divisors-of-a-number/1
 * T(c) -> sqrt(N), space -> sqrt(N)
 */

    public static void printDivisors(int n) {
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

    public static void main(String[] args) {
        int N = 20;
        System.out.print("Printing Divisors of "+ N +" = ");
        printDivisors(N);
        System.out.println();
    }

}
