"""
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return 
    an array of the non-overlapping intervals that cover all the intervals in the input.
    Eg. intervals = [[1,3],[2,6],[8,10],[15,18]] => [[1,6],[8,10],[15,18]]

    https://leetcode.com/problems/merge-intervals/
"""

def merge(intervals):
    """ T(c) -> O(nlogn) + O(n), S(c) -> O(n) """

    n = len(intervals)
    # if array contains only one element
    if n <= 1:
        return intervals
    
    # sort arrays using first index
    intervals = sorted(intervals, key=lambda x:x[0])
    
    result = []
    
    i = 0
    while i < n:
        start = intervals[i][0]
        end = intervals[i][1]
        # if both array are overlapping, first element of second array is in between first array elements, merge it
        if result and start <= result[-1][1]:
            result[-1][1] = max(end, result[-1][1])
        # otherwise add current array elements directly
        else:
            result.append([intervals[i][0], intervals[i][1]])
        i += 1            
        
    return result


arr = [[1,3],[2,6],[8,10],[15,18]]
print(arr)
print(merge(arr))
