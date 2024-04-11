import java.util.ArrayList;
import java.util.Arrays;

class PrimeNumber
{
/* (1)
    * Return 0 for not prime, 1 for prime
    * https://www.geeksforgeeks.org/problems/prime-number2314/1
    * T(c) -> o(N)
*/
    static int isPrime(int N)
    {
        if(N == 0 || N == 1)
        {
            return 0;
        }
        
        for(int i=2;i<N;i++)
        {
            /* if divisible by any number other than 1 and N, it is not prime */
            if(N%i == 0)
            {
                return 0;
            }
        }
        return 1;
    }

    /* return 0 if number is not prime, 1 for prime , T(c) -> O(sqrt(N)) */
    static int isPrimeEfficient(int N)
    {
        if(N <= 1)
        {
            return 0;
        }
        
        /* check till sqrt(N) -> For any non-prime number N, it must have at least one divisor less than or equal to √N */
        for(int i=2;i*i<=N;i++)
        {
            // if divisible by any number other than 1 and N, it is not prime
            if(N%i == 0)
            {
                return 0;
            }
        }
        return 1;
    }

/* (2)
 * Sum of all prime numbers between 1 and N.
 * https://www.geeksforgeeks.org/problems/sum-of-all-prime-numbers-between-1-and-n4404/1
 * T(c) -> O(n sqrt(n)) , space -> O(n)
 */

    public static long prime_Sum(int n)
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
     * T(c) -> O(n log(logn)), space -> O(n)
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
        System.out.println("IsPrime 5? = "+ isPrime(5));
        System.out.println("IsPrime 9? = "+ isPrime(9));
        int n = 10;
        System.out.println("Sum of primes till "+ n + " = " + prime_Sum(n));
        System.out.println("Sum of primes (efficient) till "+ n + " = " + primeSumEfficient(n));
    }
}