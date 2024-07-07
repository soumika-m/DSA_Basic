public class SumBeautySubstring {
    
    /*
     * The beauty of a string is the difference in frequencies between the most frequent and least frequent characters. 
     * For example, the beauty of "abaacc" is 3 - 1 = 2. Given a string s, return the sum of beauty of all of its substrings.
     * 
     * https://leetcode.com/problems/sum-of-beauty-of-all-substrings/
     * T(c) -> O(n^2), S(c) -> O(1)
     */
    static int beautySum(String s) {
        int n = s.length();
        int totalBeauty = 0;

        for(int i=0;i<n;i++)
        {
            int[] freq = new int[26];
            // check for each substring
            for(int j=i;j<n;j++)
            {
                // update frequency
                freq[s.charAt(j)-'a'] += 1;
                
                // find maximum and minimum frequency
                int maxFreq = 0;
                int minFreq = Integer.MAX_VALUE;
                for(int f : freq)
                {
                    if(f>0)
                    {
                        if(f > maxFreq)
                        {
                            maxFreq = f;
                        }
                        if(f < minFreq)
                        {
                            minFreq = f;
                        }
                    }
                }
                // calculate beauty, and add it sum of beauty
                totalBeauty = totalBeauty + (maxFreq - minFreq);
            }
        }
        return totalBeauty;
    }


    public static void main(String[] args) {
        String s = "aabcb";
        /*
         * The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
         */
        System.out.println(beautySum(s));
    }
}
