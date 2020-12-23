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
        def isOverLap(interval1, interval2): 
            if interval1[0] >= interval2[1] or interval1[1] <= interval2[0]:
                return 0
            elif (interval1[0]-interval2[0])*(interval1[1]-interval2[1]) <= 0: 
                return 2
            else:
                return 1

        def dpCleanUp(dp): # clean up until all row sum is 0
            if len(dp) <= 1:
                return 0
            dpRowSum = [sum(x) for x in dp]
            maxDpRowSum = max(dpRowSum)
            if maxDpRowSum == 0:
                return 0
            maxIndex = dpRowSum.index(maxDpRowSum)
            removeCount = 1
            # clean up row
            dp[maxIndex] = [0 for x in intervals]
            # clean up column
            for dpItem in dp:
                dpItem[maxIndex] = 0 
            removeCount += dpCleanUp(dp)
            return removeCount

        def removeDuplicated(intervals):
            result = []
            for item in intervals: 
                if item not in result:
                    result.append(item)
            return result

        # remove duplicated items from Intervals
        newIntervals = removeDuplicated(intervals)
        removeCount = len(intervals) - len(newIntervals)
        intervals = newIntervals
        dp = [[ 0 for x in intervals] for x in intervals]
        
        for i in range(0, len(intervals)): 
            for j in range(i+1, len(intervals)):
                dp[i][j] += isOverLap(intervals[i], intervals[j])
                dp[j][i] = dp[i][j]

        removeCount += dpCleanUp(dp)
        return removeCount

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