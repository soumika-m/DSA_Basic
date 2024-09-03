import java.util.ArrayList;

public class MultiplicationTable {

/*
 * Create the multiplication table of a given number N and return the table as an array.
 * https://www.geeksforgeeks.org/problems/print-table0303/1
 * T(c) -> O(1), S(c) -> O(1)
 */

    static ArrayList<Integer> getTable(int N){
        // code here
        ArrayList<Integer> numList = new ArrayList<>();
        for(int i=1;i<=10;i++)
        {
            numList.add(N*i);
        }
        return numList;
    }

    public static void main(String[] args) {
        int N = 5;
        ArrayList<Integer> table = getTable(N);
        System.out.println(table); 
    }
    
}
