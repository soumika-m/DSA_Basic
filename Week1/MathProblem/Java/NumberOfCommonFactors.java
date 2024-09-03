public class NumberOfCommonFactors {

/*
 * Given two positive integers a and b, return the number of common factors of a and b.
 * An integer x is a common factor of a and b if x divides both a and b.
 * T(c) -> O(min(a,b)), space -> O(1)
 */
    public static int commonFactors(int a, int b) {
        int min = Math.min(a,b);
        int count = 0;
        for(int i=1;i<=min;i++)
        {
            // finding common factors
            if(a%i == 0 && b%i == 0)
            {
                count++;
            }
        }
        return count;
    }


    public static void main(String args[])
    {
        int a = 12, b = 6;  // factors are 1,2,3,6
        System.out.println("Common Factor count of "+a+", "+b+" = "+commonFactors(a,b));

    }
}
