public class MaxNestingDepthOfParanthesis {
    
    /*
     * Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of 
     * nested parentheses.
     * 
     * https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
     * T(c) -> O(n^2), S(c) -> O(1)
     */
    static int maxDepth(String s) {
        int max_nest_bracket = 0;
        for(int i=0;i<s.length();i++)
        {
            int open_bracket = 0;
            int close_bracket = 0;
            
            for(int j=0;j<i;j++)
            {
                if(s.charAt(j) == '(')
                {
                    open_bracket++;
                }
                else if(s.charAt(j) == ')')
                {
                    close_bracket++;
                }
            }
            // number of left bracket before it - number of right bracket after it
            max_nest_bracket = Math.max(max_nest_bracket, (open_bracket - close_bracket));
        }
        return max_nest_bracket;
    }


    /*
     * T(c) -> O(n), S(c) -> O(1)
     */
    static int maxDepthEfficient(String s) {
        int max_nest_bracket = 0;
        int count = 0;
        for(int i=0;i<s.length();i++)
        {
            if(s.charAt(i) == '(')
            {
                count++;
                // finding max opening brackets, for max depth
                max_nest_bracket = Math.max(max_nest_bracket, count);
            }
            else if(s.charAt(i) == ')')
            {
                count--;
            }
        }
        return max_nest_bracket;
    }


    public static void main(String[] args) {
        String S = "(1+(2*3)+((8)/4))+1";
        System.out.println(maxDepth(S));
        S = "()(())((()()))";
        System.out.println(maxDepthEfficient(S));
    }

}
