class CelebrityProblem {

/*
 * A celebrity is a person who is known to all but does not know anyone at a party. If you go to a party of N people, 
 * find if there is a celebrity in the party or not. A square NxN matrix M[][] is used to represent people at the party 
 * such that if an element of row i and column j  is set to 1 it means ith person knows jth person. Here M[i][i] will 
 * always be 0. Return the index of the celebrity, if there is no celebrity return -1.
 * 
 * https://www.geeksforgeeks.org/problems/the-celebrity-problem/1
 * T(c) -> O(n^2), S(c) -> O(1)
 */

    static int celebrity(int M[][], int n)
    {
    	boolean flag = true;
    	int celebrity = -1;
    	for(int i=0;i<n;i++)
    	{
    	    boolean isCelebrity = true;
    	    /* identify celebrity, celebrity row, celebrity don't know anyone
    	     if not contains all 0, (celebrity knows someone), not a celebrity */
    	    for(int j=0;j<n;j++)
    	    {
    	        // skip where person know himself
    	        if(i!=j && M[i][j] == 1)
    	        {
    	            isCelebrity = false;
        	        break;
    	        }
    	    }
    	    
    	    // if found any celebrity, revalidate it
    	    if(isCelebrity)
    	    {
    	        /* if everyone knows celebrity, celebrity column
    	         if not contains all 1, (everyone don't know celebrity), not a celebrity */
        	    for(int j=0;j<n;j++)
        	    {
        	        // skip where person know himself
        	        if(i!=j && M[j][i] == 0)
        	        {
        	            isCelebrity = false;
        	            break;
        	        }
        	    }
    	    }
    	    
    	    // if that is celebrity, return
    	    if(isCelebrity)
    	    {
    	        return i;
    	    }
    	}
    	return -1;
    }


	/*
	 * T(c) -> O(n), S(c) -> O(1)
	 */
	static int celebrityEfficient(int M[][], int n)
    {
    	int person = 0;
    	// identify celebrity
    	for(int j=1;j<n;j++)
    	{
    	    // if person/celebrity knows j, then that person can not be celebrity
    	    if(M[person][j] == 1)
    	    {
    	        person = j;
    	    }
    	}
    	
    	// verify celebrity
    	for(int i=0;i<n;i++)
    	{
    	    if(i != person)
    	    {
    	        // if celebrity knows someone or someone don't know celebrity, that is not valid
    	        if(M[person][i] == 1 || M[i][person] == 0)
        	    {
        	        return -1;
        	    }
    	    }
    	}
    	return person;
    }


    public static void main(String[] args) {
        int matrix[][] = {
            {0, 1, 0}, 
            {0, 0, 0}, 
            {0, 1, 0}
        };
        System.out.println("Celebrity Index = " + celebrity(matrix, matrix.length));
		System.out.println("Celebrity Index = " + celebrityEfficient(matrix, matrix.length));
    }
    
}