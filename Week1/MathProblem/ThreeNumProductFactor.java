public class ThreeNumProductFactor {

    /*
     * Given a number n, find it's three factors a, b, c such that a * b * c = n and a != b != c != 1
     * constraint -> N <= 10^9
     */
    static void productOfThreeNumFactor(int n)
    {
        int a = Integer.MAX_VALUE, b = Integer.MAX_VALUE, c = Integer.MAX_VALUE;
        // find first minimum factor a other than 1
        for(int i=2;i*i<=n;i++)
        {
            if(n%i==0)
            {
                a = i;
                break;
            }
        }

        n = n/a;

        // find second factor other than 1 and a and also minimum
        for(int i=2;i*i<=n;i++)
        {
            if(n%i == 0)
            {
                if(i != a)
                {
                    b = Math.min(b, i);
                }
                // check for remaining factor
                if((n/i) != i)
                {
                    if((n/i) != a)
                    {
                        b = Math.min(b, (n/i));
                    }                    
                }
            }
        }

        c = n/b;

        if(a != b && b != c && c != Integer.MAX_VALUE)
        {
            System.out.println("Yes");
            System.out.println(a + ", " + b + ", " + c);
        }
        else{
            System.out.println("No");
        }
    }

    public static void main(String[] args) {
        int n = 64;
        n = 32;
        n = 97;
        n = 2;
        n = 12345;
        productOfThreeNumFactor(n);
    }

}
