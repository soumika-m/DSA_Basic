public class PrintNto1 {
/*
 * Print numbers from N to 1 (space separated) without the help of loops.
 * https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/1
 * T(N)=T(N−1)+O(1) ==> T(c) -> O(N) , S(c) -> O(N)
 * The space complexity of the recursive function depends on the maximum depth of the recursive call stack. 
 */
    static void printNo1(int N) {
        // Base case
        if(N < 1)
        {
            return;
        }
        
        System.out.print(N + " ");
        
        printNo1(N-1);
    }

    public static void main(String[] args) {
        int N = 10;
        printNo1(N);
    }

}
