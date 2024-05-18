public class CountSubarrayProductLessThanK {

/*
 * Given an array of positive numbers, the task is to find the number of possible contiguous subarrays having product 
 * less than a given number k.
 * https://www.geeksforgeeks.org/problems/count-the-subarrays-having-product-less-than-k1708/1
 * T(c) -> O(n^2) , S(c) -> O(1)
 */

    static long countSubArrayProductLessThanK(long a[], int n, long k)
    {
        long count = 0;
        for(int i=0;i<n;i++)
        {
            long product = 1;
            // checking product from current element to end of array until it is less than k
            for(int j=i;j<n;j++)
            {
                product *= a[j];
                // if product is less than k, count that subarray
                if(product < k)
                {
                    count++;
                }
                // if product is equal or greater, break it, as it will increase the product further
                else{
                    break;
                }
            }
        }
        return count;
    }

    /*
     * Using sliding window (2 pointer)
     * T(c) -> O(2N), S(c) -> O(1)
     */
    static long countSubArrayProductLessThanKOptimal(long a[], int n, long k)
    {
        long product = 1;
        long count = 0;

        int left = 0;
        int right = 0;
        
        // move right every time
        while(right<n)
        {
            // calculate product
            product *= a[right];
            
            // if product >= k, move left also, and discard that left number
            while(product >= k && left < right)
            {
                product /= a[left];            
                left++; 
            }
            
            // while adjusting the pointer, all subarrays ending at right and starting from left to right are valid
            if(product < k)
            {
                count += (right-left+1);
            }
            
            // check for next element (right pointer)
            right++;
        }
        return count;
    }

    public static void main(String[] args) {
        long arr[] = {7, 5, 3, 4, 2, 8};
        long k = 50;
        System.out.println("Subarray count = "+ countSubArrayProductLessThanK(arr, arr.length, k));
        System.out.println("Subarray count = "+ countSubArrayProductLessThanKOptimal(arr, arr.length, k));
    }
    
}
