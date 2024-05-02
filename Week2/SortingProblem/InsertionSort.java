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
        
        while(j>=0 && arr[j]>temp)
        {
        // shift element 1 place right
            arr[j+1] = arr[j];
            j--;
        }
        
        arr[j+1]  = temp;
    }

    //Function to sort the array using insertion sort algorithm.
    public static void insertionSort(int arr[], int n)
    {
        //code here
        for(int i=1;i<n;i++)
        {
            int j = i-1;
            int temp = arr[i];
            while(j>=0 && arr[j]>temp)
            {
            //  shift element 1 place right
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1]  = temp;
        }
    }

    public static void main(String[] args) {
        int arr[] = {4,3,2,1};
        insertionSort(arr, arr.length);

        for(int k=0;k<arr.length;k++)
        {
            System.out.print(arr[k]+" ");
        }
    }
}
