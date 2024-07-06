import java.util.Arrays;
import java.util.Collections;

public class ReverseWordInString {
    
    /*
     * Given an input string s, reverse the order of the words. A word is defined as a sequence of non-space 
     * characters. The words in s will be separated by at least one space. Return a string of the words in reverse 
     * order concatenated by a single space.
     * 
     * https://leetcode.com/problems/reverse-words-in-a-string/
     * T(c) -> O(n), S(c) -> O(n)
     */
    static String reverseWords(String s) {
        // discard leading and trailing space
        String[] word = s.trim().split(" +");
        // reverse those array of words
        int start = 0, end = word.length-1;
        while(start<end)
        {
            String temp = word[start];
            word[start] = word[end];
            word[end] = temp;
            start++;
            end--;
        }
        return String.join(" ", word);
    }


    public static void main(String[] args) {
        String s = "the sky is blue";
        System.out.println(reverseWords(s));
    }
}
