import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class FourSum {
/*
 * Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] 
 * such that: 0 <= a, b, c, d < n. 
 * a, b, c, and d are distinct. 
 * nums[a] + nums[b] + nums[c] + nums[d] == target. You may return the answer in any order.
 * 
 * https://leetcode.com/problems/4sum/
 * T(c) -> O(n^4) , S(c) -> 2*n , for set and list data structure
 * Gave TLE
 */

    static List<List<Integer>> fourSum(int[] nums, int target) {
        int n = nums.length;
        
        // for storing unique arrays
        Set<List<Integer>> hset = new HashSet<>();
        
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                for(int k=j+1;k<n;k++)
                {
                    for(int l=k+1;l<n;l++)
                    {
                        long sum = (long)nums[i] + nums[j];
                        sum += nums[k];
                        sum += nums[l];
                        if(sum == target)
                        {
                            List<Integer> temp = Arrays.asList(nums[i], nums[j], nums[k], nums[l]);
                            // before storing in set, sort array
                            Collections.sort(temp);
                            hset.add(temp);
                        }
                    }
                }
            }
        }
        
        // creating list from set data structure
        List<List<Integer>> result = new ArrayList<>(hset);
        return result;
    }

    /*
     * Using hashset for finding 4th element
     * T(c) -> O(N3*log(M)), where N = size of the array, M = no. of elements in the set.
     * S(c) -> O(2 * no. of the quadruplets)+O(N) , set data structure and a list to store the quads, set data structure to store the array elements.
     */
    static List<List<Integer>> fourSum(int[] nums, int target) {
        int n = nums.length;
        
        // for storing unique arrays
        Set<List<Integer>> hset = new HashSet<>();
        
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                HashSet<Integer> tempSet = new HashSet<>();
                for(int k=j+1;k<n;k++)
                {
                    int fourth = target - (nums[i] + nums[j] + nums[k]);
                    if(tempSet.contains(fourth)) 
                    {
                        long sum = (long)nums[i] + nums[j];
                        sum += nums[k];
                        sum += fourth;
                        
                        if(sum == target)
                        {
                            List<Integer> tempList = Arrays.asList(nums[i], nums[j], nums[k], fourth);
                            // before storing in set, sort array
                            Collections.sort(tempList);
                            hset.add(tempList);
                        }
                    }
                    
                    // add in hashset
                    tempSet.add(nums[k]);
                }
            }
        }
        
        // creating list from set data structure
        List<List<Integer>> result = new ArrayList<>(hset);
        return result;
    }

    public static void main(String[] args) {
        int arr[] = {1,0,-1,0,-2,2};
        int target = 0;
        /* [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]] */
        List<List<Integer>> ans = fourSum(arr, target);
        System.out.println(ans);
    }
    
}
