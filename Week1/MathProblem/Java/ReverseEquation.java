public class ReverseEquation {

/*
 * Given a mathematical equation that contains only numbers and +, -, *, /. 
 * Print the equation in reverse, such that the equation is reversed, but the numbers remain the same.
 * Eg. "20-3+5*2" -> "2*5+3-20" 
 * 
 * https://practice.geeksforgeeks.org/problems/reversing-the-equation2205/1
 * T(c) -> O(N) / O(|S|)
 */
    static String reverseEqn(String S)
    {
        StringBuilder res = new StringBuilder();
        StringBuilder number = new StringBuilder();

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

    public static void main(String[] args) {
        String eq1 = "20-3+5*2";
        System.out.println("Reverse Equation? "+ eq1 +" = "+  reverseEqn(eq1));
    }

}
