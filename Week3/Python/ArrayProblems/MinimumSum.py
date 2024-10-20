"""
    Given an array Arr of size N such that each element is from the range 0 to 9. Find the minimum possible sum of two 
    numbers formed using the elements of the array. All digits in the given array must be used to form the two numbers.
    Eg. {6, 8, 4, 5, 2, 3} -> The minimum sum is formed by numbers 358 and 246. -> 604

    https://www.geeksforgeeks.org/problems/minimum-sum4058/1
"""

def solve(arr, n):
    """ T(c) -> O(nlogn), S(c) -> O(1) """
    # sort the array
    arr.sort()

    first_num = 0
    second_num = 0
    
    # create first num using even index, second num using odd index
    for i in range(n):
        # even index
        if i % 2 == 0:
            first_num *= 10
            first_num += arr[i]
        # odd index
        else:
            second_num *= 10
            second_num += arr[i]
    
    minimum_sum = first_num + second_num
    return minimum_sum


arr = [6, 8, 4, 5, 2, 3]
print(solve(arr, len(arr)))
