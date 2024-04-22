import java.util.List;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Set;
import java.util.Arrays;

class ThreeSum {
/*
 * Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
 * and nums[i] + nums[j] + nums[k] == 0.  Solution set must not contain duplicate triplets.
 * https://leetcode.com/problems/3sum/
 * T(c) -> O(N^2 * log(no. of unique triplets)) // time required for storing inside set datastructure.
 * S(c) -> O(2 * no. of the unique triplets) + O(N)  // first is for list and set, 2nd is for set.
 */
    static List<List<Integer>> threeSum(int[] nums) {
        /* for storing unique arrays */
        Set<List<Integer>> hashset = new HashSet<>();
        
        for(int i=0;i<nums.length;i++)
        {
            Set<Integer> tempSet = new HashSet<>();
            for(int j=i+1;j<nums.length;j++)
            {
                /* calculating third element, i+j+k = 0 => k = -i-j => k = -(i+j) */
                int third = -(nums[i]+nums[j]);
                
                /* if hashset contains that element */
                if(tempSet.contains(third))
                {
                    List<Integer> tempList = Arrays.asList(nums[i],nums[j],third);
                    Collections.sort(tempList);
                    hashset.add(tempList);
                }
                /* add number in hashset */
                tempSet.add(nums[j]);
            }
        }
        
        List<List<Integer>> result = new ArrayList<>(hashset);
        return result;
    }


    public static void main(String[] args) {
        int arr[] = {-1,0,1,2,-1,-4};
        List<List<Integer>> result = threeSum(arr);
        for(List<Integer> res:result)
        {
            for(int elem: res)
            {
                System.out.print(elem+" ");
            }
            System.out.println();
        }
    }
}