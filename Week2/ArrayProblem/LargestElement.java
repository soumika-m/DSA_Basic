public class LargestElement{
/*
 * Given an array A[] of size n. The task is to find the largest element in it.
 * https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1
 * T(c) -> O(n), S(c) -> O(1)
 */
    static int largest(int arr[], int n)
    {
        int max = Integer.MIN_VALUE;
        for(int i=0;i<n;i++)
        {
            if(arr[i] > max)
            {
                max = arr[i];
            }
        }
        return max;
    }

    public static void main(String[] args) {
        int arr[] = {10,5,4,13};
        System.out.println(largest(arr, arr.length));
    }   
}