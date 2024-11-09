import java.util.HashMap;

public class FindDuplicateNumber {

/*
 * Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
 * There is only one repeated number in nums, return this repeated number.
 * You must solve the problem without modifying the array nums and uses only constant extra space.
 * T(c) -> O(n^2), S(c) -> O(1)
 */

    static int findDuplicate(int[] nums) {
        int n = nums.length;
        // check frequency of each number
        for(int i=0;i<n;i++)
        {
            int count = 1;
            for(int j=i+1;j<n;j++)
            {
                if(nums[i] == nums[j])
                {
                    count++;
                }
            }
            
            // if frequency is greater than 1, means duplicate
            if(count > 1)
            {
                return nums[i];
            }
        }
        // by default case, duplicate not found
        return -1;
    }

    /*
     * Using hashing
     * T(c) -> O(n), S(c) -> O(n)
    */
    static int findDuplicateBetter(int[] nums) {
        int n = nums.length;
        
        HashMap<Integer,Integer> map = new HashMap<>();
        
        // check frequency of each number
        for(int i=0;i<n;i++)
        {
            map.put(nums[i], map.getOrDefault(nums[i], 0)+1);
            
            // if frequency is greater than 1, duplicate
            if(map.get(nums[i]) > 1)
            {
                return nums[i];
            }
        }
         
        // by default case, duplicate not found
        return -1;
    }
    
    /*
     * Using floyd's tortoise and hare algo (cycle detection)
     * T(c) -> O(n), S(c) -> O(1)
     */
    static int findDuplicateOptimal(int[] nums) {
        int slow = nums[0];
        int fast = nums[0];
        
        // move fast pointer 2 step and slow pointer 1 step until both meets at one point
        do{
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        while(slow != fast);
        
        /* point fast pointer in the beginning and start to travarse again 
         this  time both slow and fast pointer will go 1 step until both will meet again */
        fast = nums[0];
        while(slow != fast)
        {
            fast = nums[fast];
            slow = nums[slow];
        }
        return fast;
    }


    public static void main(String[] args) {
        int arr[] = {1,3,4,2,2};
        System.out.println("Duplicate = "+findDuplicate(arr));
        System.out.println("Duplicate = "+findDuplicateBetter(arr));
        System.out.println("Duplicate = "+findDuplicateOptimal(arr));
    }

}
