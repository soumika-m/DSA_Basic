import java.util.ArrayList;
import java.util.Arrays;

public class FloorAndCeilArray {

    /*
     * Given an unsorted array Arr[] of N integers and an integer X, find floor and ceiling of X in Arr[0..N-1]. 
     * Floor of X is the largest element which is smaller than or equal to X. Floor of X doesn’t exist if X is 
     * smaller than smallest element of Arr[]. Ceil of X is the smallest element which is greater than or equal to X. 
     * Ceil of X doesn’t exist if X is greater than greatest element of Arr[].
     * 
     * https://www.geeksforgeeks.org/problems/ceil-the-floor2802/1
     * T(c) -> O(nlogn) + O(logn), S(c)-> O(1)
     */
    static ArrayList getFloorAndCeil(int[] arr, int n, int x) {
        // sort the array to apply binary search
        Arrays.sort(arr);
        int floor = -1;
        int ceil = -1;
        
        int low = 0;
        int high = n-1;
        while(low <= high)
        {
            int mid = (low+high)/2;
            // ceil -> smallest number, greater than x
            if(arr[mid] > x)
            {
                ceil = arr[mid];
                high = mid-1;
            }
            // floor -> largest number, smaller than x
            else if(arr[mid] < x)
            {
                floor = arr[mid];
                low = mid+1;
            }
            // found both floor ceil (equal element)
            else{
                floor = ceil = arr[mid];
                return new ArrayList<>(Arrays.asList(floor,ceil));
            }
        }
        /* return new Pair(floor,ceil); */
        return new ArrayList<>(Arrays.asList(floor,ceil));
    }

    public static void main(String[] args) {
        int arr[] = {5, 6, 8, 9, 6, 5, 5, 6};
        int x = 7;
        System.out.println(getFloorAndCeil(arr, arr.length, x));
    }
    
}
