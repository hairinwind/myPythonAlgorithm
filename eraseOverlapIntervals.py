import argparse
import cProfile, pstats, sys
import logging
from typing import List

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

"""
leetcode 435. Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/

"""


class Solution(object):
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        currentInterval = None
        overlapCount = 0
        for interval in intervals:
            if currentInterval is None:
                currentInterval = interval
                continue
            if interval[0] <= currentInterval[1]:
                overlapCount += 1
            else:
                currentInterval = interval
        
        return overlapCount

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # arguments ref: https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
    parser.add_argument("--intervals", help="intervals", nargs='?', type=str, const="1-2,2-3,3-4,1-3", default="1-2,2-3,3-4,1-3")
    args = parser.parse_args()
    intervals = [x.split("-") for x in args.intervals.split(",")]
    #test
    intervals = [[1,100],[11,22],[1,11],[2,12]]
    print(intervals)

    solution = Solution()
    result = solution.eraseOverlapIntervals(intervals)
    print("result is {}".format(result))