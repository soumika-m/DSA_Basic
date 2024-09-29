public class QuickSort {
/*
 * Quick Sort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot.
 * Given an array arr[], its starting position is low (the index of the array) and its ending position is high(the index of the array).
 * Implement quick sort algorithm.
 * Note: The low and high are inclusive.
 * https://www.geeksforgeeks.org/problems/quick-sort/1
 * T(c) -> O(n^2) // best case -> O(nlogn)
 * S(c) -> O(longn)
 */

    //Function to sort an array using quick sort algorithm.
    static void quickSort(int arr[], int low, int high)
    {
        if(low >= high)
        {
            return;
        }
        
        // find partition element
        int p = partition(arr, low, high);
        // apply quicksort on left part
        quickSort(arr, low, p-1);
        // apply quicksort on right part
        quickSort(arr, p+1, high);
    }

    static int partition(int arr[], int low, int high)
    {
        int pivot = arr[low];
        
        int count = 0;
        // counting all minimum elements present after pivot
        for(int i=low+1;i<=high;i++)
        {
            if(arr[i]<=pivot)
            {
                count++;
            }
        }
        
        // placing pivot element to correct place, swap elements
        int pivotIndex = low+count;
        int temp = arr[low];
        arr[low] = arr[pivotIndex];
        arr[pivotIndex] = temp;
        
        // make left side less than, and right side greater than pivot element
        while(low<pivotIndex && high>pivotIndex)
        {
            while(arr[low]<=pivot)
            {
                low++;
            }
            while(arr[high]>pivot)
            {
                high--;
            }

            if(low<pivotIndex && high>pivotIndex)
            {
                // swap elements
                temp = arr[low];
                arr[low] = arr[high];
                arr[high] = temp;
            }
        }
        
        return pivotIndex;
    } 
   
    public static void main(String[] args) {
        int arr[] = {4,1,3,9,7};
        quickSort(arr, 0, arr.length-1);
        for(int i=0;i<arr.length;i++)
        {
            System.out.print(arr[i] + " ");
        }
    }

}
