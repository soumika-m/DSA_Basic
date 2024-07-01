import java.util.HashMap;

class IsomorphicString{

    /*
     * Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the 
     * characters in s can be replaced to get t. All occurrences of a character must be replaced with another 
     * character while preserving the order of characters. No two characters may map to the same character, but a 
     * character may map to itself.
     * 
     * https://leetcode.com/problems/isomorphic-strings/
     * T(c) -> O(n^2), S(c) -> O(n)
     */
    static boolean isIsomorphic(String s, String t) {        
        HashMap<Character, Character> hm = new HashMap<>();
        
        for(int i=0;i<s.length();i++)
        {   
            if(hm.containsKey(s.charAt(i)))
            {
                // if mapping present, but wrong, return false
                if(hm.get(s.charAt(i)) != t.charAt(i))
                {
                    return false;
                }
            }
            else{
                // check if value is already mapped with some other character
                if(hm.containsValue(t.charAt(i)))
                {
                    return false;
                }
                
                // if mapping not present, add it
                hm.put(s.charAt(i), t.charAt(i));
            }
        }
        return true;
    }

    /*
     * T(c) -> O(n), S(c) -> O(n)
     */
    static boolean isIsomorphicBetter(String s, String t) {
        
        HashMap<Character, Character> s_to_t_map = new HashMap<>();
        HashMap<Character, Character> t_to_s_map = new HashMap<>();
        
        for(int i=0;i<s.length();i++)
        {
            char s_ch = s.charAt(i);
            char t_ch = t.charAt(i);
            
            // map characters accordingly
            if(s_to_t_map.containsKey(s_ch))
            {
                if(s_to_t_map.get(s_ch) != t_ch)
                {
                    return false;
                }
            }
            else{
                s_to_t_map.put(s_ch, t_ch);
            }
            
            if(t_to_s_map.containsKey(t_ch))
            {
                if(t_to_s_map.get(t_ch) != s_ch)
                {
                    return false;
                }
            }
            else{
                t_to_s_map.put(t_ch, s_ch);
            }
        }
        return true;
    }

    public static void main(String[] args) {
        String s = "babc";
        String t = "baba";
        System.out.println(isIsomorphic(s, t));
        System.out.println(isIsomorphicBetter(s, t));
    }

}