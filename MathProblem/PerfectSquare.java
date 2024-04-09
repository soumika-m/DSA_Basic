public class PerfectSquare {
/* 
* count perfect square -> You are given a number N, you have to count the number of perfect squares less than N
* https://www.geeksforgeeks.org/problems/count-squares3649/155
* T(C) -> O(sqrt(N))
*/
    static int countSquares(int N) {
        // code here
        if(N == 1)
        {
            return 0;
        }
        
        int count = 0;

        /* we need to check till sqrt(N) as sqrt(N)*sqrt(N)= N -> perfect square */
        for(int i=1;i*i<N;i++)
        {
            count++;
        }
        return count;
    }

    public static void main(String args[])
    {
        int N = 9;
        System.out.println(countSquares(N));
    }
}
