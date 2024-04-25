public class RotateArray {

/*
 * Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
 * eg. nums = [-1,-100,3,99], k = 2 ==> [3,99,-1,-100]
 * https://leetcode.com/problems/rotate-array/
 * T(c) -> O(n), S(c) -> O(1)
 */
    static void rotateRight(int[] nums, int k) {
        /* using reversal operation, without using extra array */
        int arrLen = nums.length;
        /* to discard index out of bound error */
        int key = k % arrLen; 

        int pos = arrLen - key;

        /* reversing first part */
        reversal(nums, 0, pos-1);
        /* reversing second part */
        reversal(nums, pos, arrLen-1);
        /* reversing complete array */
        reversal(nums, 0, arrLen-1);
    }
    
    static void reversal(int arr[], int posFrom, int posTo)
    {
        for(int i=posFrom,j=posTo; i<j; i++,j--)
        {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    static void displayArr(int arr[])
    {
        for(int i=0;i<arr.length;i++)
        {
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int arr[] = {1,2,3,4,5,6,7};
        int k = 3;
        displayArr(arr);
        System.out.println("Rotating array to right for "+ k +" steps => ");
        rotateRight(arr, k);
        displayArr(arr);
    }
}
