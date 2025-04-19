"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

https://leetcode.com/problems/merge-intervals/description/
"""

from typing import List


def mergeIntervals(intervals: List[List[int]]) -> List[List[int]]:
    """ T(C) -> O(NlogN) + O(2N), S(C) -> O(N) """

    # sort array
    intervals.sort()
    # print(intervals)

    res = []
    # iterate each intervals
    for i in range(len(intervals)):
        start = intervals[i][0]
        end = intervals[i][1]
        # don't consider if interval is already belongs to last one
        if len(res) != 0 and end <= res[-1][1]:
            continue
        for j in range(i+1, len(intervals)):
            # if current interval's first element belongs to recent interval's end, that is overlapping, update interval
            if intervals[j][0] <= end:
                end = max(end, intervals[j][1])
            # otherwise it is not sub interval, break the loop
            else:
                break

        # update in result
        res.append([start, end])

    return res


def mergeIntervalsOptimal(intervals):
    """ T(C) -> O(NlogN) + O(N), S(C) -> O(N) """

    # sort array
    intervals.sort()

    res = []

    # iterate through each intervals
    for i in range(len(intervals)):
        # if result is empty or current interval's start don't belongs to array interval's end, create new sub interval
        if len(res) == 0 or intervals[i][0] > res[-1][1]:
            res.append(intervals[i])

        # if current interval's start element belongs to array interval's end element, merge the intervals (intervals[i][0] <= res[-1][1])
        else:
            # update in result array
            res[-1][1] = max(res[-1][1], intervals[i][1])

    return res


if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]
    print(intervals)
    ### Since intervals [1,3] and [2,4] and [2,6] overlap, merge them into [1,6].
    print(mergeIntervals(intervals))
    print(mergeIntervalsOptimal(intervals))