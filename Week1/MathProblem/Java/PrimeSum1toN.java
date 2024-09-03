import java.util.ArrayList;
import java.util.Arrays;

public class PrimeSum1toN {

/*
 * Sum of all prime numbers between 1 and N.
 * https://www.geeksforgeeks.org/problems/sum-of-all-prime-numbers-between-1-and-n4404/1
 * T(c) -> O(n*sqrt(n)) , space -> O(n)
 */
    public static long primeSum(int n)
    {
        // code here
        ArrayList<Integer> primeNumbers = new ArrayList<>();
        for(int i=2;i<=n;i++)
        {
            if(is_prime(i))
            {
                primeNumbers.add(i);
            }
        }
        
        // calculating sum of prime numbers
        long sum = 0;
        for(int i=0;i<primeNumbers.size();i++)
        {
            sum += primeNumbers.get(i);
        }
        return sum;
    }
    
    static boolean is_prime(int n)
    {
        for(int i=2;i*i<=n;i++)
        {
            if(n%i == 0)
            {
                return false;
            }
        }
        return true;
    }

    /* 
     * Using sieve of eratosthenes algorithm
     * T(c) -> O(n*log(logn)), space -> O(n)
     */
    public static long primeSumEfficient(int n)
    {
        boolean[] primes = new boolean[n+1];
        Arrays.fill(primes, true);
        // 0 and 1 are not prime, marking that as false
        primes[0] = false;
        primes[1] = false;
        
        // running loop till sqrt(n)
        for(int i=2;i*i<=n;i++)
        {
            // if current number is prime
            if(primes[i])
            {
                // marking all multiples of i as false(non prime)
                for(int j=i*i;j<=n;j+=i)
                {
                    primes[j]=false;
                }
            }
        }
        
        long sum = 0;
        for(int i=2;i<=n;i++)
        {
            // if prime, add in sum
            if(primes[i])
            {
                sum += i;
            }
        }
        return sum;
    }
    
    public static void main(String args[])
    {
        int n = 10;
        System.out.println("Sum of primes till "+ n + " = " + primeSum(n));
        System.out.println("Sum of primes (efficient) till "+ n + " = " + primeSumEfficient(n));
    }

}
