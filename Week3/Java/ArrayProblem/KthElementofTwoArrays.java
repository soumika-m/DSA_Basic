import java.util.ArrayList;

public class KthElementofTwoArrays {

/*
 * Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K. The task is to find the element 
 * that would be at the kth position of the final sorted array.
 * 
 * https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1
 * T(c) -> O(min(n,m)) + O(n) + O(m) => O(n+m)
 * S(c) -> O(n+m)
 */

    static long kthElement( int arr1[], int arr2[], int n, int m, int k) {
        // merge the array and return the kth element from merged array
        ArrayList<Integer> mergedArr = new ArrayList<>();
        int i=0, j=0;
        // if arr1 and arr2 both are present
        while(i<n && j<m)
        {
            if(arr1[i] <= arr2[j])
            {
                mergedArr.add(arr1[i]);
                i++;
            }
            else{
                mergedArr.add(arr2[j]);
                j++;
            }
        }
        
        // if remaining of arr1
        while(i<n)
        {
            mergedArr.add(arr1[i]);
            i++;
        }
        
        // or if remaining of arr2
        while(j<m)
        {
            mergedArr.add(arr2[j]);
            j++;
        }
        
        return (long)mergedArr.get(k-1);
    }

    public static void main(String[] args) {
        int a[] = {100, 112, 256, 349, 770};
        int b[] = {72, 86, 113, 119, 265, 445, 892};
        int k = 7;
        /* Final sorted array is - 72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892 */
        System.out.println(k+"th element after merging array = "+ kthElement(a, b, a.length, b.length, k));
    }
    
}
