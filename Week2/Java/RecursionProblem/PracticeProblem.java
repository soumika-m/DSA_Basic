public class PracticeProblem {
    
    /* 1. find nth fibonacci number */
    static int fibonacci(int n)
    {
        // base case
        if(n == 0 || n == 1)
        {
            return n;
        }

        return fibonacci(n-1) + fibonacci(n-2);

    }

    /* 2. to reach n from 0, we can go 1 step or 2 step, return total number of ways we can go */
    static int countNstairs(int N)
    {
        // for negative stairs no ways
        if(N < 0)
        {
            return 0;
        }

        // for 0th step, only 1 way to reach (0 to 0)
        if(N == 0)
        {
            return 1;
        }

        // to reach nth stairs either we can take last step or last to last step
        return countNstairs(N-1) + countNstairs(N-2);
    }

    /* 3. Given 134 -> print one three four */
    static void sayDigit(int N)
    {
        String arr[] = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};

        if(N == 0)
        {
            return;
        }

        int temp = N%10;
        sayDigit(N/10);
        System.out.println(arr[temp]);
    }

    public static void main(String[] args) {
        int n = 5;
        printNto1(n);
        System.out.println();
        System.out.println(fibonacci(6));
        System.out.println(countNstairs(3));
        System.out.println();
        sayDigit(123);
    }
}
