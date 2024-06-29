import java.util.Arrays;

public class AggressiveCows {
    
    /*
     * You are given an array consisting of n integers which denote the position of a stall. You are also 
     * given an integer k which denotes the number of aggressive cows. You are given the task of assigning 
     * stalls to k cows such that the minimum distance between any two of them is the maximum possible. 
     * The first line of input contains two space-separated integers n and k. 
     * The second line contains n space-separated integers denoting the position of the stalls.
     * 
     * https://www.geeksforgeeks.org/problems/aggressive-cows/0
     * T(c) -> O(max-min)*O(n) -> O(n^2) , S(c) -> O(1)
     */
    public static int solve(int n, int k, int[] stalls) {
        // sort the array
        Arrays.sort(stalls);
        
        int max = findMax(stalls, n);
        int min = findMin(stalls, n);
        
        // distance range can be [1, (max-min)] between 2 cows
        for(int i=1; i<=(max-min); i++)
        {
            // if placing all k cows possible
            if(isPlacingCowsPossible(stalls, i, k))
            {
                continue;
            }
            else{
                return i-1;
            }
        }
        return 0;
    }
    
    static int findMax(int[] stalls, int n)
    {
        int maxVal = 0;
        for(int i=0;i<n;i++)
        {
            maxVal = Math.max(maxVal, stalls[i]); 
        }
        return maxVal;
    }
    
    static int findMin(int[] stalls, int n)
    {
        int minVal = 0;
        for(int i=0;i<n;i++)
        {
            minVal = Math.min(minVal, stalls[i]); 
        }
        return minVal;
    }
    
    static boolean isPlacingCowsPossible(int[] stalls, int distance, int cows)
    {
        int cowsCnt = 1;
        // place where we placed last cow
        int lastCordinate = stalls[0];
        
        for(int i=1;i<stalls.length;i++)
        {
            // if distance is >= mindistance
            if(stalls[i] - lastCordinate >= distance)
            {
                cowsCnt++;
                lastCordinate = stalls[i];
                // if all cows placed with distance >= mindistance between them
                if(cowsCnt == cows)
                {
                    return true;
                }
            }
        }
        return false;
    }

    /*
     * Using binary search
     * T(c) -> O(nlogn) + O(log(max-min))*O(n) => O(nlogn) + O(log(n-1-0))*O(n) 
     * S(c) -> O(1)
     */
    public static int solveEfficient(int n, int k, int[] stalls) {
        // sort the array
        Arrays.sort(stalls);
        
        // distance range can be [1, (max-min)] between 2 cows
        int low = 1;
        int high = stalls[n-1] - stalls[0];
        int ans = 0;
        
        while(low <= high)
        {
            int mid = (low + high)/2;
            // if placing all k cows possible, find highest (right)
            if(isPlacingCowsPossible(stalls, mid, k))
            {
                ans = mid;
                low = mid+1;
            }
            else{
                high = mid-1;
            }
        }
        return ans;
    }


    public static void main(String[] args) {
        int stalls[] = {10, 1, 2, 7, 5};
        int cows = 3;
        /*
         * The first cow can be placed at stalls[0], the second cow can be placed at stalls[1] and 
         * the third cow can be placed at stalls[4]. The minimum distance between cows, in this case, is 4, 
         * which also is the largest among all possible ways.
         */
        System.out.println(solve(stalls.length, cows, stalls));
        System.out.println(solve(stalls.length, cows, stalls));
    }

}
