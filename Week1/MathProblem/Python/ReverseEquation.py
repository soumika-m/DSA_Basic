"""
    Given a mathematical equation that contains only numbers and +, -, *, /. 
    Print the equation in reverse, such that the equation is reversed, but the numbers remain the same.
    Eg. "20-3+5*2" -> "2*5+3-20" 

    https://practice.geeksforgeeks.org/problems/reversing-the-equation2205/1
"""

def reverseEqn(s):
    """ T(c) -> O(N) / O(|S|), S(c) -> O(N) """
    # holds final string
    newstr = ""
    # hold number
    num = ""
    # start iteration from last to first
    for char in s[::-1]:
        # if number add it into num variable to reverse it later
        if char >= '0' and char <='9':
            num += char
        # for operators, add the number at first after reversing, then add operator
        else:
            newstr += num[::-1]
            num = ""
            newstr += char
    
    # add last number which is remaining, after reversal
    newstr += num[::-1]
    
    return newstr


if __name__ == "__main__":
    eq = "5+2*56-2/4"
    print(eq + " => " + reverseEqn(eq))