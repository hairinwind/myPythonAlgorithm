import argparse
import cProfile, pstats, sys
import logging
from typing import List

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

"""
leetcode 877. stone game
https://leetcode.com/problems/stone-game/
https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E4%B9%8B%E5%8D%9A%E5%BC%88%E9%97%AE%E9%A2%98.md
my understanding https://docs.google.com/spreadsheets/d/1_ND0CsEl4EoC92WEZDQ2lWtw0Wyy7D2rU3RttFALYO4/edit#gid=1593371985
"""


class Solution(object):
    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[(0,0) for x in piles] for x in piles]
        # initialize with one pile only 
        for i in range(0, len(piles)):
            dp[i][i] = (piles[i], 0)
        
        for i in range(1, len(piles)):  #need loop 1 [0,1] [1,2] [2,3] 2 [0,2] [1,3] 3 [0,3]
            x = 0
            y = i
            while y < len(piles):
                right = min(dp[x+1][y][0], dp[x][y-1][0])
                left = sum(piles[x:y+1]) - right
                dp[x][y] = (left, right)
                x += 1
                y += 1
        
        result = dp[0][len(piles)-1]
        return result[0] > result[1]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # arguments ref: https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
    parser.add_argument("--piles", help="piles", nargs='?', type=str, const="5,3,4,5", default="5,3,4,5")
    args = parser.parse_args()
    piles = [int(x) for x in args.piles.split(",")]

    solution = Solution()
    result = solution.stoneGame(piles)
    print("result for piles {} is {}".format(piles, result))