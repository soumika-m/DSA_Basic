import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MergeIntervals {
/*
 * Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return 
 * an array of the non-overlapping intervals that cover all the intervals in the input.
 * Eg. intervals = [[1,3],[2,6],[8,10],[15,18]] => [[1,6],[8,10],[15,18]]
 * 
 * https://leetcode.com/problems/merge-intervals/description/
 * T(c) -> O(nlogn) + O(2n) , S(c) -> O(n) 
 */

    static int[][] mergeIntervals(int[][] intervals) {
        // sort arrays based on start index of array element
        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0],b[0]));
        
        List<List<Integer>> result = new ArrayList<>();
        
        // check each element
        for(int i=0;i<intervals.length;i++)
        {
            int start = intervals[i][0];
            int end = intervals[i][1];
            
            // skip all merge intervals
            if(!result.isEmpty() && end <= result.get(result.size()-1).get(1))
            {
                continue;
            }
            
            // check the rest of the intervals
            for(int j=i+1;j<intervals.length;j++)
            {
                int currentStartIndex = intervals[j][0];
                int currentEndIndex = intervals[j][1];
                // found merge intervals
                if(currentStartIndex <= end)
                {
                    end = Math.max(end, currentEndIndex);
                }
                else{
                    break;
                }
            }
                        
            result.add(Arrays.asList(start,end));
        }
        
        // convert arraylist to int[][]
        int j = 0;
        int[][] ans = new int[result.size()][2];
        for(List<Integer> a : result){
            ans[j][0] = a.get(0);
            ans[j][1] = a.get(1);
            j++;
        }
        
        return ans;
    }

    /*
     * Using single loop
     * T(c) -> O(nlogn) + O(n) , S(c) -> O(n)
    */
    static int[][] mergeIntervalsEfficient(int[][] intervals) {
        // sort arrays based on start index of array element
        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0],b[0]));
        
        List<List<Integer>> result = new ArrayList<>();
        
        // check each element
        for(int i=0;i<intervals.length;i++)
        {
            int start = intervals[i][0];
            int end = intervals[i][1];
            
            // found merge interval
            if(!result.isEmpty() && start <= result.get(result.size()-1).get(1))
            {
                // check maximum of last element of result array and current start index
                end = Math.max(end, result.get(result.size()-1).get(1));
                // update last element in result array
                result.get(result.size()-1).set(1, end);
            }
            else{
                result.add(Arrays.asList(start,end));
            }
        }
        
        // convert arraylist to int[][]
        int j = 0;
        int[][] ans = new int[result.size()][2];
        for(List<Integer> a : result){
            ans[j][0] = a.get(0);
            ans[j][1] = a.get(1);
            j++;
        }
        
        return ans;
    }


    public static void main(String[] args) {
        int[][] arr = {{1,3},{2,6},{8,10},{15,18}};

        int[][] res1 = mergeIntervals(arr);
        for(int i=0;i<res1.length;i++)
        {
            for(int j=0;j<res1[i].length;j++)
            {
                System.out.print(res1[i][j]+" ");
            }
            System.out.println();
        }

        System.out.println();

        int[][] res2 = mergeIntervalsEfficient(arr);
        for(int i=0;i<res2.length;i++)
        {
            for(int j=0;j<res2[i].length;j++)
            {
                System.out.print(res2[i][j]+" ");
            }
            System.out.println();
        }
    }

}
