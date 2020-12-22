import argparse
import cProfile, pstats, sys
import logging
from typing import List

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

"""
leetcode 887. Super egg drop 
https://leetcode.com/problems/super-egg-drop/
https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E9%AB%98%E6%A5%BC%E6%89%94%E9%B8%A1%E8%9B%8B%E8%BF%9B%E9%98%B6.md
my understanding https://docs.google.com/spreadsheets/d/1_ND0CsEl4EoC92WEZDQ2lWtw0Wyy7D2rU3RttFALYO4/edit#gid=0
"""


class Solution(object):
    def superEggDrop(self, K: int, N: int) -> int:
        m = 0 # m is the test times
        dp = [[0 for i in range(0, N+1)] for x in range(0, K+1)] # dp[K+1][N+1]  dp stands for "Dynamic programming"
        while dp[K][m] < N : 
            m +=1 # m 的次数并不确定，所以放在外圈循环，找到第一个超过要求楼层N的时候停止
            for k in range(1, K+1): # K 是鸡蛋个数，是确定的，放内圈循环
                dp[k][m] = dp[k][m - 1] + dp[k - 1][m - 1] + 1
        return m

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # arguments ref: https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
    parser.add_argument("--eggs", help="eggs", nargs='?', type=int, const="3", default="3")
    parser.add_argument("--stories", help="stories", nargs='?', type=int, const="14", default="14")
    args = parser.parse_args()
    eggs = args.eggs
    stories = args.stories

    solution = Solution()
    result = solution.superEggDrop(eggs, stories)
    print("result for eggs {} and stories {} is {}".format(eggs, stories, result))