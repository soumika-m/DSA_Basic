public class Print1toN {

/*
 * Print numbers from 1 to N without the help of loops.
 * https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1
 * T(c) - > O(N), S(c) -> O(N)
 */
    static void print1oN(int N)
    {
        // Base case
        if(N == 0)
        {
            return;
        }
        
        // Recursion function
        print1oN(N-1);
        
        System.out.print(N+" ");
    }

    public static void main(String[] args) {
        int N = 10;
        print1oN(N);
    }
    
}
