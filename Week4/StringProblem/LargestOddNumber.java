public class LargestOddNumber {
    
    /*
     * You are given a string num, representing a large integer. Return the largest-valued odd integer 
     * (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists. 
     * A substring is a contiguous sequence of characters within a string.
     * 
     * https://leetcode.com/problems/largest-odd-number-in-string/
     * T(c) -> O(n) , S(c) -> O(1)
     */
    static public String largestOddNumber(String num) {
        // if last digit is odd, return
        if((int)(num.charAt(num.length()-1)) % 2 == 1)
        {
            return num;
        }
        
        for(int i=num.length()-1;i>=0;i--)
        {
            int ch = num.charAt(i);
            // current digit is odd number
            if(ch % 2 != 0)
            {
                return num.substring(0,i+1);
            }
            // if current digit is even, go to previous digit
        }
        return "";
    }


    public static void main(String[] args) {
        String s = "52746";
        System.out.println(largestOddNumber(s));  
    }
}
