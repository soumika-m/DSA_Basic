class MultiplyTwoStrings {

/*
 * Given two numbers as strings s1 and s2. Calculate their Product. 
 * The numbers can be negative and You are not allowed to use any built-in function or convert the strings to integers. 
 * There can be zeros in the begining of the numbers. You don't need to specify '+' sign in the begining of positive numbers.
 * https://www.geeksforgeeks.org/problems/multiply-two-strings/1
 * T(c) -> O(n1 * n2 + n1 + n2), S(c) -> O(n1 + n2)
 */
    static String multiplyStrings(String s1,String s2)
    {
        boolean isNegative = false;

        /* checking if strings are negative */
        if(s1.charAt(0) == '-')
        {
            isNegative = !isNegative;
            /* removing minus sign if present */
            s1 = s1.substring(1);
        }
        if(s2.charAt(0) == '-')
        {
            isNegative = !isNegative;
            /* removing minus sign if present */
            s2 = s2.substring(1);
        }
        
        /* To handle overflow of big numbers we are taking array instead of int or long */
        int resultArr[] = new int[s1.length()+s2.length()]; 
        
        /* multiplication logic -> iterates from right to left(similar to manual process) */
        for(int i=s1.length()-1;i>=0;i--)
        {
            for(int j=s2.length()-1;j>=0;j--)
            {
                int digit1 = s1.charAt(i) - '0';
                int digit2 = s2.charAt(j) - '0';
                int product = digit1 * digit2;
                int sum = product + resultArr[i+j+1];
                /* handling carry */
                resultArr[i+j] += sum / 10;
                /* placing multiplication digit in correct position */
                resultArr[i+j+1] = sum % 10;
            }
        }
        
        StringBuilder sb = new StringBuilder();

        /* dicarding leading zeros and appending those digits in string */
        for(int digit:resultArr)
        {
            if(!(sb.length() == 0 && digit == 0))
            {
                sb.append(digit);
            }
        }
        
        /* Prepend negative sign if necessary */
        if(isNegative && sb.length() != 0)
        {
            sb.insert(0,'-');
        }
        
        return sb.length() == 0 ? "0" : sb.toString();
    }

    public static void main(String args[])
    {
        String s1 = "984";
        String s2 = "24";
        System.out.println(multiplyStrings(s1, s2));
        s1 = "342857466747623190253535915582654079729535249666495366204751947309612861759399743340838318159436477709808";
        s2 = "4471335218251938463464417392810911901096513109096223883606949011331588570391782354624160500218170491853613331964401401436877119247304542334868677958787620083249";
        System.out.println(multiplyStrings(s1, s2));
        
    }
}