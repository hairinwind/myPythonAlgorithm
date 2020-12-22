import argparse
import cProfile, pstats, sys
import logging
from typing import List

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

"""
leetcode 887. Super egg drop 
https://leetcode.com/problems/super-egg-drop/
https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E9%AB%98%E6%A5%BC%E6%89%94%E9%B8%A1%E8%9B%8B%E9%97%AE%E9%A2%98.md
"""


class Solution(object):
    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()
        
        def dp(K, N) -> int:
            if K == 1: return N
            if N == 0: return 0
            
            if (K,N) in memo:
                return memo[(K,N)]

            result = float('INF')
            for i in range(1, N+1):  # i 代表第一个鸡蛋在第i层扔
                numberIfBroken = dp(K - 1, i - 1) # 碎
                numberIfNotBroken = dp(K, N - i) # 没碎
                dpMax = max(  # 在碎和没碎两种情况下，分别求其个需要测试多少次，取最大值，也就是最坏结果
                            numberIfBroken, numberIfNotBroken     
                        ) + 1 # 在第 i 楼扔了一次
                result = min(result, dpMax) # result 是之前各个楼层的最少尝试次数

            # 用二分搜索代替线性搜索
            # lo, hi = 1, N
            # while lo <= hi:
            #     mid = (lo + hi) // 2
            #     broken = dp(K - 1, mid - 1) # 碎
            #     not_broken = dp(K, N - mid) # 没碎
            #     # res = min(max(碎，没碎) + 1)
            #     if broken > not_broken:
            #         hi = mid - 1
            #         result = min(result, broken + 1)
            #     else:
            #         lo = mid + 1
            #         res = min(result, not_broken + 1)

            memo[(K, N)] = result
            return result
        
        result = dp(K, N)
        print(memo)
        return result
       

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