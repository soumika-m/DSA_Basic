class FibonacciSeries{

/*
 * You are given an integer n, return the fibonacci series till the nth(0-based indexing) term. 
 * Since the terms can become very large return the terms modulo 109+7.
 * https://www.geeksforgeeks.org/problems/fibonacci-series-up-to-nth-term/1
 * T(c) -> O(n^2) , S(c) -> O(n)
 */
    static int[] Series(int n) {

        int fibArr[] = new int[n+1];
        
        while(n >= 0)
        {
            int num = fibHelper(n);
            fibArr[n] = num;
            n--;
        }
        
        return fibArr;
    }
    
    static int fibHelper(int n)
    {
        // 10^9+7
        int MOD = 1000000007;
        // base case
        if(n == 0 || n == 1)
        {
            return n;
        }
        
        return (fibHelper(n-1) + fibHelper(n-2)) % MOD;
    }

    public static void main(String[] args) {
        int n = 5;
        int fib[] = Series(n);
        for(int i=0;i<n;i++)
        {
            System.out.print(fib[i]+ " ");
        }
    }
}