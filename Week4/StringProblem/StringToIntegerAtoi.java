public class StringToIntegerAtoi {
    
    /*
     * Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer. 
     * For edge case refer problem statement.
     * https://leetcode.com/problems/string-to-integer-atoi/
     * T(c) -> O(n), S(c) -> O(1)
     */
    static int myAtoi(String s) {
        // for empty string
        if(s.length() == 0) return 0;
        
        long ans = 0;
        int sign = 1;
        
        int i = 0;
        // ignore leading white space ,trim takes O(n) time, so better to use manual way
        while(i<s.length() && s.charAt(i) == ' ')
        {
            i++;
        }
        
        // if + or - sign is present
        if(i<s.length())
        {
            if(s.charAt(i) == '-')
            {
                sign = -1;
                i++;
            }
            else if(s.charAt(i) == '+')
            {
                sign = 1;
                i++;
            }
        }
        
        while(i<s.length())
        {
            char ch = s.charAt(i);
            
            // if digit found
            if(ch >= '0' && ch <= '9')
            {
                ans = ans * 10 + (ch-'0');
            }
            // if whitespace or non digit found, break or return
            else{
                break;
            }
            
            // handle overflow
            if(sign == -1 && ans*-1 < Integer.MIN_VALUE)
            {
                return Integer.MIN_VALUE;
            }
            else if(sign == 1 && ans > Integer.MAX_VALUE)
            {
                return Integer.MAX_VALUE;
            }
            i++;
        }
        
        return (int)(ans*sign);
    }

    public static void main(String args[])
    {
        String s = "1337c0d3";
        System.out.println(myAtoi(s));
        s = "   -042";
        System.out.println(myAtoi(s));
        s = "0-1";
        System.out.println(myAtoi(s));
        s = "words and 987";
        System.out.println(myAtoi(s));
    }
}
