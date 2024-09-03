public class LargestPrimeFactor {
    
/*
 * Given a number N, the task is to find the largest prime factor of that number.
 * For eg, 24 = 2*2*2*3 , so output is 3
 * https://www.geeksforgeeks.org/problems/largest-prime-factor2601/1
 * T(c) - > O(sqrt(n)), S(c) -> O(1)
 */

    static long largestPrimeFactor(int N) {
        
        int largestPrime = 1;
        
        /* for non prime number we will have atleast one multiple <= sqrt(n) */
        for(int i=2;i*i<=N;i++)
        {
            /* check if i divides N evenly, do until n becomes 1 */
            while(N%i == 0)
            {
                /* update largest prime factor */
                largestPrime = N;
                /* divide N by i */
                N=N/i;
            }
        }
        
        /* if N is greater than 1, means N is itself prime, then we need to update it as largestPrime */
        if(N>1)
        {
            largestPrime = N;
        }
        
        return largestPrime;
    }

    public static void main(String[] args) {
        int N = 24;
        System.out.println("Largest prime factor for = "+ largestPrimeFactor(N));
        N = 17;
        System.out.println("Largest prime factor for = "+ largestPrimeFactor(N));
    }
}
