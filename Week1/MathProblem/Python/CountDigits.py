"""
    Count the number of digits in N which evenly divide N.
    Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided.
    https://www.geeksforgeeks.org/problems/count-digits5716/1
"""
def evenlyDivides (N):
    """ T(c) -> O(logN) , S(c) -> O(1) """
    count = 0
    num = N
    while num > 0:
        digit = num % 10
        
        # if N is evenly divisible by digit
        if digit != 0 and N % digit == 0:
            count += 1
            
        num = num//10
    
    return count


N = 12072
print("Number of digits which can evenly divide N =", evenlyDivides(N))
