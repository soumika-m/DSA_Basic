public class SelectionSort {
/*
 * Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.
 * https://www.geeksforgeeks.org/problems/selection-sort/1
 * T(c) -> O(n^2)  // best case -> O(n^2)
 * S(c) -> O(1)
 * Unstable sort
 */
    static int select(int arr[], int i)
	{
        // code here such that selectionSort() sorts arr[]
        int minIndex = i;
        
        for(int j=i+1;j<arr.length;j++)
        {
            // find minimum element/index
            if(arr[minIndex] > arr[j])
            {
                minIndex = j;
            }
        }
        
        return minIndex;
	}
	
	static void selectionSort(int arr[], int n)
	{
	    // number of passes
	    for(int i=0;i<n-1;i++)
	    {
	        int minIndex = select(arr,i);
	        
	        // if current element and minimum element are not same
	        if(minIndex != i)
	        {
	           //swap minimum index element with i index
	           int temp = arr[minIndex];
	           arr[minIndex] = arr[i];
	           arr[i] = temp;
	        }
	    }
	}

    public static void main(String[] args) {
        int arr[] = {4,3,1,2};
        selectionSort(arr, arr.length);
        for(int k=0;k<arr.length;k++)
        {
            System.out.print(arr[k]+" ");
        }
    }

}
