import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class AnagramString {
    
    /*
     * Given two strings s and t, return true if t is an anagram of s, and false otherwise. An Anagram is a word or 
     * phrase formed by rearranging the letters of a different word or phrase, typically using all the original 
     * letters exactly once.
     * 
     * https://leetcode.com/problems/valid-anagram/
     * T(c) -> O(nlogn), S(c) -> O(ns)
     */
    static boolean isAnagram(String s, String t) {
        char sArr[] = s.toCharArray();
        char tArr[] = t.toCharArray();
        
        // sort both character array
        Arrays.sort(sArr);
        Arrays.sort(tArr);
        
        // if same characters, anagram
        return Arrays.equals(sArr, tArr);
    }

    /*
     * T(c) -> O(n), S(c) -> O(n)
     */
    static boolean isAnagramEfficient(String s, String t) {
        Map<Character, Integer> map = new HashMap<>();
        
        // count character frequency for string s
        for(int i=0;i<s.length();i++)
        {
            char ch = s.charAt(i);
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
        
        // decrement frequncy for string t
        for(int i=0;i<t.length();i++)
        {
            char ch = t.charAt(i);
            map.put(ch, map.getOrDefault(ch, 0) - 1);
        }
        
        // check if all frequency are zero in map, anagram
        for(int count: map.values())
        {
            if(count != 0)
            {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        String s = "anagram";
        String t = "nagaram";
        System.out.println(isAnagram(s, t));

        String s1 = "rat";
        String t1 = "car";
        System.out.println(isAnagramEfficient(s1, t1));
    }
}
