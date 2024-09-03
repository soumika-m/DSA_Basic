import java.util.Arrays;

public class CountPrime {

/*
 * Given an integer n, return the number of prime numbers that are strictly less than n.
 * https://leetcode.com/problems/count-primes/
 * T(c) -> O(n*log(logn)), space -> O(n)
 */
    
    static int countPrimes(int n) {
        /* not prime */
        if(n == 0 || n == 1)
        {
            return 0;
        }
        
        /* using sieve of eratosthenes algorithm */
        boolean primeArr[] = new boolean[n];
        
        Arrays.fill(primeArr, true);
        
        /* 0 and 1 are not prime, marking that as false */
        primeArr[0] = false;
        primeArr[1] = false;
        
        /* running loop till sqrt(n) */
        for(int i=2;i*i<=n;i++)
        {
            /* if number is prime */
            if(primeArr[i])
            {
                /* mark all multiples of i as not prime(false) till n-1 */ 
                for(int j=i*i;j<n;j+=i)
                {
                    primeArr[j] = false;
                }
            }
        }
        
        int count = 0;
        /* counting all prime numbers less than n */
        for(int i=2;i<n;i++)
        {
            if(primeArr[i])
            {
                count++;
            }
        }
        
        return count;
    }

    public static void main(String[] args) {
        int n = 10;
        System.out.println("Primes count less than "+ n +" is = " + countPrimes(n));
        n = 1;
        System.out.println("Primes count less than "+ n +" is = " + countPrimes(n));
    }
}
