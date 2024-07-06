class LongestPalindromeSubstring{

    /*
     * Given a string s, return the longest palindromic substring in s.
     * https://leetcode.com/problems/longest-palindromic-substring/
     * T(c) -> O(n^3), S(c)-> O(1)
     */
    static public String longestPalindrome(String s) {
        String longestsubstr = "";
        
        // find each substring and check for palindrome
        for(int i=0;i<s.length();i++)
        {
            for(int j=i;j<s.length();j++)
            {
                String substr = s.substring(i, j+1);
                // find longest substring
                if(isPalindrome(substr) && substr.length() > longestsubstr.length())
                {
                    longestsubstr = substr;
                }
            }
        }
        return longestsubstr;
    }
    
    static boolean isPalindrome(String s)
    {
        int i = 0;
        int j = s.length()-1;
        while(i < j)
        {
            if(s.charAt(i) != s.charAt(j))
            {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    /*
     * T(c) -> O(n^2), S(c) -> O(1)
     * Using expand around center algo
     */
    static public String longestPalindromeEfficient(String s) {
        int start = 0;
        int maxLen = 1;
        
        // using expand around center algorithm
        for(int i=0;i<s.length();i++)
        {
            // odd length palindrome
            int left = i-1;
            int right = i;
            while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right))
            {
                if(right-left+1 > maxLen)
                {
                    maxLen = right-left+1;
                    start = left;
                }
                left--;
                right++;
            }
            
            // even length palindrome
            left = i-1;
            right = i+1;
            while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right))
            {
                if(right-left+1 > maxLen)
                {
                    maxLen = right-left+1;
                    start = left;
                }
                left--;
                right++;
            } 
        }
        return s.substring(start, start+maxLen);
    }

    public static void main(String[] args) {
        String s = "babad";
        System.out.println(longestPalindrome(s));
        s = "cbbd";
        System.out.println(longestPalindromeEfficient(s));
    }
}