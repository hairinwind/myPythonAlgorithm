import argparse
import cProfile, pstats, sys
import logging
from typing import List

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

"""
leetcode 121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E5%9B%A2%E7%81%AD%E8%82%A1%E7%A5%A8%E9%97%AE%E9%A2%98.md
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = float('inf')
        max = 0
        balance = 0

        for i in prices:
            if i > max: 
                max = i
            if i < min:
                min = i
                max = 0 # 发现新的一个数小于前一个数，重置 max, 确保总是用 min 之后的 max 计算 balance
            newBalance = max - min
            if newBalance > balance:
                balance = newBalance
            print("min, max, balance are {}, {}, {}".format(min, max, balance))

        return balance

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # arguments ref: https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
    parser.add_argument("--prices", help="prices", nargs='?', type=str, const="7,1,5,3,6,4", default="7,6,4,3,1")
    args = parser.parse_args()
    prices = [int(x) for x in args.prices.split(",")]

    print(prices)

    solution = Solution()
    result = solution.maxProfit(prices)
    print("result: {}".format(result))