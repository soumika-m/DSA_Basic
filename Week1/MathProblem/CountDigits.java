public class CountDigits {

/*
 * Count the number of digits in N which evenly divide N.
 * Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided.
 * https://www.geeksforgeeks.org/problems/count-digits5716/1
 * T(c) -> O(logN)
 */

    static int evenlyDivides(int N){
        // code here
        int temp = N;
        int count = 0;
        while(temp > 0)
        {
            int rem = temp%10;
            /* evenly divisible */
            if(rem != 0 && N % rem == 0)
            {
                count++;
            }
            temp = temp/10;
        }
        return count;
    }

    public static void main(String[] args) {
        int N = 12;
        System.out.println("Evenly Divides? = "+ evenlyDivides(N));
    }
}
