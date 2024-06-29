public class RemoveOutermostParanthesis {
    
    /*
     * A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split 
     * it into s = A + B, with A and B nonempty valid parentheses strings. Return s after removing the 
     * outermost parentheses of every primitive string in the primitive decomposition of s.
     * 
     * https://leetcode.com/problems/remove-outermost-parentheses/
     * T(c) -> O(n), S(c) -> O(n)
     */
    static public String removeOuterParentheses(String s) {
        int openBracket = 0;
        StringBuilder sb = new StringBuilder();
        
        // primitive string means opening and closing brackets count are same
        for(int i=0;i<s.length();i++)
        {
            // if opening bracket, increase the count
            if(s.charAt(i) == '(' && openBracket++ > 0)
            {
                sb.append(s.charAt(i));
            }
            // if closing bracket, decrease the count
            if(s.charAt(i) == ')' && openBracket-- > 1)
            {
                sb.append(s.charAt(i));
            }
        }
        return sb.toString();
    }
    
    public static void main(String args[])
    {
        String s = "(()())(())(()(()))";
        System.out.println(removeOuterParentheses(s));
    }

}
