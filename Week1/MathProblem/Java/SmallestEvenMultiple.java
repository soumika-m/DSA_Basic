public class SmallestEvenMultiple {

/*
 * Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
 * T(c) -> O(n)
 */
    public static int smallestEvenMultiple(int n) {
        int i = 1;
        int j = 1;
        // if multiple of 2 and multiple of n are not matching 
        while(2*i != n*j)
        {
            // if multiple of 2 is greater than multiple of n, we will check for next multiple of n
            if((2*i) > (n*j))
            {
                j++;
            }
            // if multiple of 2 is equal to multiple of n, that is the smallest integer
            if((2*i) == (n*j))
            {
                return (2*i);
            }
            // we will check for next multiple of 2 in each iteration
            i++;
        }
        // out of while loop means both multiples are matching
        return (2*i);
    }

    /* 
    * checking if number even or odd, and returing appropriate result
    * T(c) -> O(1)
     */
    public static int smallestEvenMultipleEfficient(int n) {
        // if n is even, smallest multiple of 2 and n will be n itself.
        if(n % 2 == 0)
        {
            return n;
        }
        // if n is odd, smallest multiple of both 2 and n will be 2*n 
        else{
            return n*2;
        }
    }

    public static void main(String[] args) {
        int N = 5;
        System.out.println("Smallest Even Multiple of "+ N+ " = "+ smallestEvenMultiple(N));
        System.out.println("Smallest Even Multiple (efficient) of "+ N+ " = "+ smallestEvenMultiple(N));
    }
    
}
