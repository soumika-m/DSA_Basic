import java.util.HashMap;

class LongestSubArrayWithSumK{
/*
* Given an array containing N integers and an integer K. Your task is to find the length of the longest Sub-Array 
* with the sum of the elements equal to the given value K.
* https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1
* T(c) -> O(N^2), S(c) -> O(1)
 */
    static int lenOfLongSubarr_BruteForce(int A[], int N, int K) {
        int sum = 0;
        int maxLen = 0;
        
        for(int i=0;i<N;i++)
        {
            for(int j=i;j<N;j++)
            {
                sum += A[j];
                int currentSubarrLen = (j - i) + 1;
                if(sum == K && currentSubarrLen > maxLen)
                {
                    maxLen = currentSubarrLen;
                }
            }
            /* reset sum for finding next subarray */
            sum = 0;
        }
        return maxLen;
    }


    /* 
    * T(c) -> O(N), S(c) -> O(N)
     */
    public static int lenOfLongSubarr_Efficient(int A[], int N, int K) {
        /* using hashing */
        /* hashmap will store sum with index */
        HashMap<Integer, Integer> map = new HashMap<>();
        int sum = 0;
        int maxLen = 0;
        
        for(int i=0;i<N;i++)
        {
            sum += A[i];
            /* when we will find the first subarray, calculate that length */
            if(sum == K)
            {
                maxLen = Math.max(maxLen, i+1);
            }
            
            /* calculate sum of remaining part, x-k */
            int prefixSum = sum - K;
            if(map.containsKey(prefixSum))
            {
                int len = i - map.get(prefixSum);
                maxLen = Math.max(maxLen, len);
            }
            
            /* if sum is not present in map, update that */
            if(!map.containsKey(sum))
            {
                map.put(sum,i);
            }
        }
        return maxLen;
    }


    public static void main(String[] args) {
        int arr[] = {10, 5, 2, 7, 1, 9};
        int k = 15;
        System.out.println(lenOfLongSubarr_BruteForce(arr, arr.length, k));
        int arr1[] = {1, 4, 3, 3, 5, 5};
        k = 16;
        System.out.println(lenOfLongSubarr_Efficient(arr1, arr1.length, k));
    }
}