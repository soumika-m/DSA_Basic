public class SecondLargestElement {
/*
 * Given an array Arr of size N, print the second largest distinct element from an array. 
 * If the second largest element doesn't exist then return -1.
 * https://www.geeksforgeeks.org/problems/second-largest3735/1
 * T(c) -> O(n) , S(c) -> O(1)
 */
    static int print2largest(int arr[], int n) {

        int largest = Integer.MIN_VALUE;
        int secondLargest = -1;

        /* find largest number */
        for(int i=0;i<n;i++)
        {
            if(arr[i] > largest)
            {
                largest = arr[i];
            }
        }

        /* find second largest number */
        for(int i=0;i<n;i++)
        {
            if(arr[i]>secondLargest && arr[i]<largest)
            {
                secondLargest = arr[i];
            }
        }
        
        /* second largest number is available or not */
        if(largest != secondLargest)
        {
            return secondLargest;
        }
        else{
            return -1;
        }
    }

    /* using one for loop T(c) -> O(n), S(c) -> O(1) */
    static int print2largestMethod2(int arr[], int n) {

        int largest = Integer.MIN_VALUE;
        int secondLargest = Integer.MIN_VALUE;

        /* find second largest number */
        for(int i=0;i<n;i++)
        {
            if(arr[i] > largest)
            {
                secondLargest = largest;
                largest = arr[i];
            }
            else if(arr[i] > secondLargest && arr[i] != largest)
            {
                secondLargest = arr[i];
            }
        }
        
        /* second largest number is available or not */
        if(secondLargest != Integer.MIN_VALUE)
        {
            return secondLargest;
        }
        else{
            return -1;
        }
    }

    public static void main(String[] args) {
        int arr1[] = {12, 35, 1, 10, 34, 1};
        System.out.println(print2largest(arr1, arr1.length));
        int arr2[] = {10, 10, 10};
        System.out.println(print2largestMethod2(arr2, arr2.length));
    }
}
