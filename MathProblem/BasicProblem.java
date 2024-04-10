public class BasicProblem {

/* (1)
* Count the number of digits in N which evenly divide N.
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

/* (2)
* Return "Yes" if it is a armstrong number else return "No".
* T(c) -> O(1) // as n will be always 3 digit number (constant)
* if n is not constant (variable in nature), T(c) -> O(logn)
*/    
    static String armstrongNumber(int n){

        int temp = n;
        int cubeSum = 0;
        while(temp > 0)
        {
            int digit = temp%10;
            cubeSum += Math.pow(digit,3);
            temp = temp/10;
        }
        
        if(cubeSum == n)
        {
            return "Yes";
        }
        else{
            return "No";
        }
    }

/* (3)
 * Given a mathematical equation that contains only numbers and +, -, *, /. 
 * Print the equation in reverse, such that the equation is reversed, but the numbers remain the same.
 * T(c) -> O(N) / O(|S|)
 */

    static String reverseEqn(String S)
    {
        StringBuilder res = new StringBuilder();
        StringBuilder number = new StringBuilder();
        // your code here
        for(int i=S.length()-1; i>=0; i--)
        {
            char ch = S.charAt(i);
            // numbers
            if(ch >= '0' && ch <='9')
            {
                number.append(ch);
            }
            // operators
            else{
                number.reverse();
                res.append(number.toString());
                res.append(ch);
                number.setLength(0);
            }
        }
        number.reverse();
        res.append(number.toString());

        return res.toString();
    }

    public static void main(String args[])
    {
        int N = 12;
        System.out.println("Evenly Divides? = "+ evenlyDivides(N));
        N = 157;
        System.out.println("Armstrong Number? "+ N +" = "+  armstrongNumber(N));
        String eq1 = "20-3+5*2";
        System.out.println("Reverse Equation? "+ eq1 +" = "+  reverseEqn(eq1));
    }
}
