public class InsertionSort {
/*
 * The task is to complete the insert() function which is used to implement Insertion Sort.
 * https://www.geeksforgeeks.org/problems/insertion-sort/1
 * T(c) -> O(n^2)  // bast case -> O(n)
 * S(c) -> O(1)
 * Stable sort - A sorting algorithm is considered stable if it preserves the relative order of equal elements in the sorted output as they were in the original input. 
 */
    static void insert(int arr[],int i)
    {
        int temp = arr[i];
        int j = i-1;
        
        // check temp with left sorted array to find correct position
        while(j>=0 && arr[j]>temp)
        {
        // shift element 1 place right
            arr[j+1] = arr[j];
            j--;
        }
        // put temp in correct position
        arr[j+1]  = temp;
    }

    /* Function to sort the array using insertion sort algorithm. */
    public static void insertionSort(int arr[], int n)
    {
        //code here
        for(int i=1;i<n;i++)
        {
            insert(arr,i);
        }
    }

    /* 
    * Recursive insertion sort
    * T(c) -> O(n^2), S(c) -> O(1) 
     */
    public static void insertionSortRecursive(int arr[], int n)
    {
        //  base case
        if(n == 1)
        {
            return;
        }
    
        int lastIndex = n-1;
        // call insertion sort with one less element -> we reduce the size of the array by 1 until the base case is reached.
        insertionSortRecursive(arr, n-1);
        // insert that element
        insert(arr, lastIndex);
    }

    public static void main(String[] args) {
        int arr[] = {4,3,2,1};
        // insertionSort(arr, arr.length);
        insertionSortRecursive(arr, arr.length);

        for(int k=0;k<arr.length;k++)
        {
            System.out.print(arr[k]+" ");
        }
    }
}
