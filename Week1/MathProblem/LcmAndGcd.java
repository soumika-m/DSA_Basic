public class LcmAndGcd {

/* 
* Find gcd and lcm of 2 number.
* https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1
* T(c) -> O(log(min(A,B)))
*/
    static Long[] lcmAndGcd(Long A , Long B) {

        long divisor = Math.min(A,B);
        long divident = Math.max(A,B);
        
        /* Using Euclidean algorithm or division method to find gcd. */
        while(divident % divisor != 0)
        {
            long remainder = divident % divisor;
            divident = divisor;
            divisor = remainder;
        }
        
        long gcd = divisor;
        
        /* Used property GCD(A,B)×LCM(A,B)=A×B to find the LCM (Least Common Multiple). */
        long lcm = (A*B)/gcd;
        
        Long[] arr = new Long[2];
        arr[0]=lcm;
        arr[1]=gcd;

        return arr;
    }

    public static void main(String args[])
    {
        long A = 14;
        long B = 8;
        Long[] ptr = lcmAndGcd(A,B);
                
        System.out.println("LCM = " + ptr[0] + " , GCD = "+ ptr[1]);

    }
}
