class BubbleSort{
/*
 * Given an Integer N and a list arr. Sort the array using bubble sort algorithm.
 * https://www.geeksforgeeks.org/problems/bubble-sort/1
 * T(c) -> O(n^2)  // Best case -> O(n)
 * S(c) -> O(1)
 * Stable sort
 */
	static void bubbleSort(int arr[], int n)
    {
        // number of passes
        for(int i=0;i<n-1;i++)
        {
            boolean swap = false;
            // number of comparisons
            for(int j=0;j<n-1-i;j++)
            {
                if(arr[j] > arr[j+1])
                {
                    // swap elements
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;

                    swap = true;
                }
            }

            // array already sorted
            if(swap == false)
            {
                break;
            }
        }
    }   
    
    public static void main(String[] args) {
        int arr[] = {4,3,2,1};
        bubbleSort(arr, arr.length);
        for(int k=0;k<arr.length;k++)
        {
            System.out.print(arr[k]+" ");
        }
    }

}