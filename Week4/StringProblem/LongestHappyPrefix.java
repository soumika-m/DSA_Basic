public class LongestHappyPrefix {
    
    /*
     * A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).
     * Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.
     * 
     * https://leetcode.com/problems/longest-happy-prefix/description/
     * T(c) -> O(n), S(c) -> O(1)
     */
    static String longestPrefix(String s) {
        // using longest prefix suffix array(KMP)
        int n = s.length();
        int[] lp = new int[n];

        // check for max proper prefix
        int len = 0;
        int i = 1;

        lp[0] = 0;

        while(i < n)
        {
            if(s.charAt(i) == s.charAt(len))
            {
                len++;
                lp[i] = len;
                i++;
            }
            else{
                if(len > 0)
                {
                    // check for overlap
                    len = lp[len-1];
                }
                else{
                    lp[i] = 0;
                    i++;
                }   
            }
        }
        return s.substring(0, lp[n-1]);
    }

    public static void main(String[] args) {
        String s = "ababab";
        System.out.println(longestPrefix(s));
    }
}
