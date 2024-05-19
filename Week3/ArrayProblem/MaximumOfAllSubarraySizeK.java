import java.util.ArrayList;

public class MaximumOfAllSubarraySizeK {
/*
 * Given an array arr[] of size N and an integer K. Find the maximum for each and every contiguous 
 * subarray of size K.
 * 
 * https://www.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1
 * T(c) -> O(n-k+1) * O(k) => O(n*k)
 * S(c) -> O(n-k+1) => O(n)
 */

    static ArrayList <Integer> max_of_subarrays(int arr[], int n, int k)
    {
        ArrayList<Integer> subarrayMax = new ArrayList<>();
        
        // left and right pointers will consider the window (number of elements in subarray)
        int left = 0;
        int right = left + k- 1;
        
        while(right<n)
        {
            int maxVal = 0;
            int i = left;
            
            // check maximum in that window with k elements
            while(i<=right)
            {
                maxVal = Math.max(maxVal, arr[i]);
                i++;
            }
            
            subarrayMax.add(maxVal);
            
            // check for next window
            left++;
            right++;
        }
        return subarrayMax;
    }
    
    public static void main(String[] args) {
        int arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6};
        int k = 3;
        ArrayList<Integer> res1 = max_of_subarrays(arr, arr.length, k);
        System.out.println(res1);
    }    
}
