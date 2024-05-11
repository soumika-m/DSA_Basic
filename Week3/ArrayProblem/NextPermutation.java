public class NextPermutation {

/*
 * A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
 * The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
 * If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
 * 
 * https://leetcode.com/problems/next-permutation/
 * T(c) - > O(n), S(c) -> O(1)
 */
    static void nextPermutation(int[] nums) {
        int n = nums.length;
        int breakIdx = -1;
        
        // find breakpoint, first index i from the back of the given array where arr[i] < arr[i+1]
        for(int i=n-2;i>=0;i--)
        {
            if(nums[i]<nums[i+1])
            {
                breakIdx = i;
                break;
            }
        }

        // if there is no decrement/break point, reverse the whole array
        if(breakIdx == -1)
        {
            for(int i=0,j=n-1; i<j; i++,j--)
            {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
        // if breakpoint found
        else{
            // find some number from right side which is small but greater than that number, swap
            for(int i=n-1;i>breakIdx;i--)
            {
                if(nums[i]>nums[breakIdx])
                {
                    // swap numbers
                    int temp = nums[i];
                    nums[i] = nums[breakIdx];
                    nums[breakIdx] = temp;
                    break;
                }
            }
            
            // sort/reverse remaining numbers (right side of that break point index)
            for(int i=breakIdx+1,j=n-1; i<j; i++,j--)
            {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
    }

    public static void main(String[] args) {
        int arr[] = {1,2,3};
        nextPermutation(arr);
        for(int i=0;i<arr.length;i++)
        {
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }
}
