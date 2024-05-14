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

    /*
     * Using math equations - 
     * First, find out the values of S and Sn and then calculate S - Sn
     * Then, find out the values of S2 and S2n and then calculate S2 - S2n.
     * After performing above, we will be having the values of X + Y and X - Y. Now, by substitution of values, 
     * we can able to find the values of X and Y.
     * 
     * T(c) -> O(n), S(c) -> O(1)
    */
    static int[] findTwoElementOptimal(int arr[], int n) {
        // convert n to long due to integer overflow issue
        long N = n;
        // sum of first n natural number
        long sN = (N*(N+1))/2;
        // sum of sqaures of first n natural number
        long s2N = (N*(N+1)*(2*N+1))/6;
        
        // calculating sum of array number, sum of square of array numbers
        long sum = 0;
        long sum2 = 0;
        for(int i=0;i<n;i++)
        {
            sum += arr[i];
            sum2 += (long)(arr[i])*(long)(arr[i]);
        }
        
        // Sum-Sn = X-Y
        long val1 = sum - sN;
        // Sum2-S2n = X^2-Y^2
        long val2 = sum2 - s2N;
        // Find X+Y = (X^2-Y^2)/(X-Y)
        val2 = val2/val1;
        // repeating
        long x = (val1+val2)/2;
        // misssing
        long y = x - val1;
        
        return new int[] {(int)x, (int)y};
    }

    public static void main(String[] args) {
        int arr[] = {1, 3, 3};
        int res1[] = findTwoElement(arr, arr.length);
        System.out.println("Repeating = "+ res1[0]+ ", Missing = " + res1[1]);
        int res2[] = findTwoElementBetter(arr, arr.length);
        System.out.println("Repeating = "+ res2[0]+ ", Missing = " + res2[1]);
        int res3[] = findTwoElementOptimal(arr, arr.length);
        System.out.println("Repeating = "+ res3[0]+ ", Missing = " + res3[1]);
    }
    
}
