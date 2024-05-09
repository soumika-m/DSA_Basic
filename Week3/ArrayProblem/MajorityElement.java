import java.util.HashMap;
import java.util.Map;

public class MajorityElement {
/*
 * Given an array nums of size n, return the majority element.
 * The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
 * always exists in the array.
 * https://leetcode.com/problems/majority-element/
 * T(c) -> O(n^2), S(c) -> O(1)
 */

    static int majorityElement(int[] nums) {
        int cnt = 0;
        for(int i=0;i<nums.length;i++)
        {
            // checking count of each element
            for(int j=0;j<nums.length;j++)
            {
                if(nums[i] == nums[j])
                {
                    cnt++;
                }
            }

            if(cnt > nums.length/2)
            {
                return nums[i];
            }
            
            // meking count 0, for checking next element
            cnt = 0;
        }
        return -1;
    }

    /*
     * Using hash map
     * T(c) -> O(n), S(c) -> O(n)
     */
    static int majorityElementEfficient(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i=0;i<nums.length;i++)
        {
            // increment the count
            map.put(nums[i], (map.getOrDefault(nums[i],0)+1));
        }
        
        int majority = -1;
        for(Map.Entry<Integer, Integer> entry: map.entrySet()){
            if(entry.getValue() > nums.length/2)
            {
                majority = entry.getKey();
                return majority;
            }
        }
        return majority;
    }

    /*
     * Using moore's voting algo
     * T(c) -> O(n), S(c) -> O(1)
     */
    static int majorityElementOptimal(int[] nums) {
        int cnt = 0;
        int majorityElem = -1;
        for(int i=0;i<nums.length;i++)
        {
            // if cnt = 0, check for next element in the array
            if(cnt == 0)
            {
                majorityElem = nums[i];
            }
            // if number matched with majorityElem, increase count
            if(nums[i] == majorityElem)
            {
                cnt++;
            }
            // otherwise decrease count
            else{
                cnt--;
            }
        }
        // count will be always > 0 for this element
        return majorityElem;
    }


    public static void main(String[] args) {
        int arr1[] = {2,2,1,1,1,2,2};
        System.out.println(majorityElementEfficient(arr1));
        System.out.println(majorityElement(arr1));
        int arr2[] = {8,8,7,7,7};
        System.out.println(majorityElementOptimal(arr2));
    }
    
}
