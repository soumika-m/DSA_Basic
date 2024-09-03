""""
    Given an integer N, print all the divisors of N in the ascending order.

    https://practice.geeksforgeeks.org/problems/all-divisors-of-a-number/1
"""

def print_divisors(N):
    """ T(c) -> O(sqrt(N) log(sqrt(N))), space -> O(sqrt(N)) """
    res = []
    i = 1
    # iterate from 1 to sqrt(N)
    while i*i <= N:
        # found factor
        if N%i == 0:
            res.append(i)
            # if both factors are same number, exclude duplicate
            if i != N//i:
                res.append(N//i)
        i += 1
            
    # sort the list
    res.sort()

    # print the numbers
    for i in res:
        print(i, end=" ")


def print_divisors_efficient(N):
    """ T(c) -> O(sqrt(N)), space -> O(sqrt(N)) """
    # contains divisors up to sqrt(N)
    smaller_divisor = []
    # contains divisors more than sqrt(N)
    greater_divisor = []
    i = 1
    # go till sqrt(N)
    while i*i <= N:
        # found factor
        if N%i == 0:
            smaller_divisor.append(i)
            # if both factors are same number, exclude duplicate
            if i != N//i:
                greater_divisor.append(N//i)
        i += 1

    # print all divisors in ascending order
    for d in smaller_divisor:
        print(d, end=" ")
    
    for d in reversed(greater_divisor):
        print(d, end=" ")


N = 20
# 20 is completely divisible by 1, 2, 4, 5, 10 and 20
print_divisors(N)
print()
print_divisors_efficient(N)
