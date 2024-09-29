import java.util.HashMap;
class TwoSum {
/*
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order.
 * https://leetcode.com/problems/two-sum/
 * T(c) -> O(n), S(c) -> O(n)
 */
    static int[] twoSum(int[] nums, int target) {
        int result[] = new int[2];
        /* using hash map */
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i=0;i<nums.length;i++)
        {
            int currentNum = nums[i];
            int moreNeeded = target - nums[i];
            if(map.containsKey(moreNeeded))
            {
                result[0] = i;
                result[1] = map.get(moreNeeded);
                break;
            }
            map.put(nums[i], i);
        }
        return result;
    }

    public static void main(String[] args) {
        int nums[] = {2,7,11,15};
        int target = 9;
        int res[]= twoSum(nums, target);
        System.out.println(res[0]+ " " +res[1]);
    }
}