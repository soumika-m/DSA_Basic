class MaximumProductSubarray {

/*
 * Given an integer array nums, find a subarray that has the largest product, and return the product.
 * The test cases are generated so that the answer will fit in a 32-bit integer.
 * https://leetcode.com/problems/maximum-product-subarray/
 * T(c) -> O(n^2), S(c) -> O(1)
 */

    static int maxProduct(int[] nums) {
        int n = nums.length;
        int maxProduct = Integer.MIN_VALUE;
        // find every subarray product
        for(int i=0;i<n;i++)
        {
            int product = 1;
            for(int j=i;j<n;j++)
            {
                product *= nums[j];
                // find maximum product
                maxProduct = Math.max(maxProduct, product);
            }
        }
        return maxProduct;
    }

    /*
     * Using observation, array can contains either of these - 
     * all positives -> just multiply
     * even negatives, others positives -> just mutiply, as negative and negative will become positives
     * odd negatives, others positives -> discard one negative, will calculate prefix and suffix product
     * contains zeros -> calculate subarray product without including 0 as element 
     * 
     * T(c) -> O(n), S(c) -> O(1) 
     */
    static int maxProductOptimal(int[] nums) {
        int n = nums.length;
        int maxProduct = Integer.MIN_VALUE;
        
        int prefix = 1;
        int suffix = 1;
        
        // iterate through each array element
        for(int i=0;i<n;i++)
        {
            // if number becomes 0, no need to carry forward it 
            if(prefix == 0)
            {
                prefix = 1;
            }
            if(suffix == 0)
            {
                suffix = 1;
            }

            //calculate prefix product from front of the array
            prefix *= nums[i];
            // calculate suffix product from back of the array
            suffix *= nums[n-1-i];
            
            // max product will be maximum of suffix and prefix
            maxProduct = Math.max(maxProduct, Math.max(suffix,prefix));
        }
        
        return maxProduct;
    }


    public static void main(String[] args) {
        int arr1[] = {2,3,-2,4};
        /* [2,3] has the largest product 6 */ 
        System.out.println("Maximum Product = "+ maxProduct(arr1));
        int arr2[] = {-2,3,-4};
        /* [-2,3,-4] has the largest product 24 */
        System.out.println("Maximum Product = "+ maxProductOptimal(arr2));
    }

}