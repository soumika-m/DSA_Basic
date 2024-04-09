class PrimeNumber
{
    /* Return 0 for not prime, 1 for prime
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

    public static void main(String args[])
    {
        System.out.println("IsPrime 5? = "+ isPrime(5));
        System.out.println("IsPrime 9? = "+ isPrime(9));
    }
}