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

    /* T(c) ->  O(n log n + n^2) => O(n^2), S(c)-> O(no.of unique triplets) */
    static List<List<Integer>> threeSum2(int[] nums) {
        
        /* Sort the array */
        Arrays.sort(nums);
        
        List<List<Integer>> result = new ArrayList<>();
        
        /* Using two pointer */
        for(int i=0;i<nums.length;i++)
        {
            /* remove duplicate elements of i */
            if(i>0 && nums[i]==nums[i-1]) continue;
            
            /* we will fix i, and move j and k when needed */
            int j=i+1;
            int k = nums.length-1;
            while(j<k)
            {
                int sum = nums[i]+nums[j]+nums[k];
                if(sum > 0)
                {
                    k--;
                }
                else if(sum < 0)
                {
                    j++;
                }
                else{
                    List<Integer> temp = Arrays.asList(nums[i],nums[j],nums[k]);
                    result.add(temp);
                    
                    j++;
                    k--;
                    
                    /* ignore duplicates of j and k */
                    while(j<k && nums[j]==nums[j-1])
                    {
                        j++;
                    }
                    while(j<k && nums[k]==nums[k+1])
                    { 
                        k--;
                    }
                }
            }
        }
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

        System.out.println();

        result = threeSum2(arr);
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