import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class LongestConsecutiveSequence{

/*
 * Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
 * https://leetcode.com/problems/longest-consecutive-sequence/description/
 * T(c) -> O(nlogn) + O(n) , S(c) -> O(1)
 */

    static int longestConsecutive(int[] nums) {
        int n = nums.length;
        int currentCnt = 0;
        // keep track of longest count
        int longestCnt = 0;
        // keep track of previous number of current number sequence
        int previousNum = Integer.MIN_VALUE;
        
        // sort the array
        Arrays.sort(nums);
        
        // travarse each element and check if that is belongs to a sequence or not
        for(int i=0;i<n;i++)
        {
            int currentNum = nums[i];
            
            // it is in sequence
            if(currentNum - 1 == previousNum)
            {
                currentCnt += 1;
                previousNum = currentNum;
                
            }
            // not in sequence, not duplicate (unique number)
            else if(currentNum != previousNum){
                currentCnt = 1;
                previousNum = currentNum;
            }
            
            longestCnt = Math.max(longestCnt, currentCnt);
        }
        return longestCnt;
    }

    /* 
     * Using hash set
     * T(c) -> O(n) + O(2*n), the set will be traversed at most twice in the worst case.
     * S(c) -> O(n)
     */
    static int longestConsecutiveOptimal(int[] nums) {
        int n = nums.length;
        int currentCnt = 0;
        int longestCnt = 0;
        
        Set<Integer> set = new HashSet<Integer>();
        
        // add all elements of array to one set to avoid duplicates and searching will be easy
        for(int i=0;i<n;i++)
        {
            set.add(nums[i]);
        }
        
        // check for each element in set, if previous element present in set, that is not starting point
        for(int elem : set)
        {
            int previousElem = elem - 1;
            // if previous element not present inside set, that is the starting point
            if(!set.contains(previousElem))
            {
                currentCnt = 1;
                int nextElem = elem + 1;
                // if all consecutive next element is present in set, count it
                while(set.contains(nextElem))
                {
                    currentCnt++;
                    nextElem = nextElem + 1;
                }
                // find longest count
                longestCnt = Math.max(longestCnt, currentCnt);
            }
        }
        return longestCnt;
    }


    public static void main(String[] args) {
        int arr[] = {0,3,7,2,5,8,4,6,0,1};
        /* 0 1 2 3 4 5 6 7 8 */
        System.out.println("Longest count = " + longestConsecutive(arr));
        System.out.println("Longest count = " + longestConsecutiveOptimal(arr));
    }
}