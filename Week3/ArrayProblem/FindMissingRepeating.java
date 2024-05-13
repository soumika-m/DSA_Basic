public class FindMissingRepeating {

/*
 * Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2,....,N} is missing and 
 * one number 'B' occurs twice in array. Find these two numbers.
 * https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1
 * T(C) -> O(n^2), S(c) -> O(1)
 */

    static int[] findTwoElement(int arr[], int n) {
        int missing = -1;
        int repeating = -1;
        // check for each number
        for(int i=1;i<=n;i++)
        {
            int count = 0;
            // count occurance in array for that number
            for(int j=0;j<n;j++)
            {
                if(arr[j] == i)
                {
                    count++;
                }
            }

            // find missing or repeating number
            if(count == 0)
            {
                missing = i;;
            }
            else if(count == 2)
            {
                repeating = i;
            }

            // both found
            if(missing != -1 && repeating != -1)
            {
                break;
            }
        }
        return new int[]{repeating, missing};
    }

    /*
     * Using hashing
     * T(C) -> O(2n), S(c) -> O(n)
     */
    static int[] findTwoElementBetter(int arr[], int n) {

        int hashArr[] = new int[n+1];

        // counting occurance of elements
        for(int i=0;i<n;i++)
        {
            hashArr[arr[i]]++;
        }
        
        int missing = -1, repeating = -1;
        // finding missing and repeating numbers
        for(int i=1;i<=n;i++)
        {
            // repeated number
            if(hashArr[i] == 2)
            {
                repeating = i;
            }
            // missing number
            else if(hashArr[i] == 0)
            {
                missing = i;
            }
            
            // already found missing and repeating number
            if(missing != -1 && repeating != -1)
            {
                break;
            }
        }
        
        int[] ans = {repeating, missing};
        
        return ans;
    }

    public static void main(String[] args) {
        int arr[] = {1, 3, 3};
        int res1[] = findTwoElement(arr, arr.length);
        System.out.println("Repeating = "+ res1[0]+ ", Missing = " + res1[1]);
        int res2[] = findTwoElementBetter(arr, arr.length);
        System.out.println("Repeating = "+ res2[0]+ ", Missing = " + res2[1]);
    }
    
}
