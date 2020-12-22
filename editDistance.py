import argparse
import cProfile, pstats, sys
import logging
from typing import List

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

"""
leetcode 72. Edit distance
https://leetcode.com/problems/edit-distance/
https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E7%BC%96%E8%BE%91%E8%B7%9D%E7%A6%BB.md
"""

dpStackTrace = []

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def dp(i, j):
            dpStackTrace.append((i, j)) #save the parameters to see how many duplicated calls were triggered
            # base case
            if i == -1: return j + 1
            if j == -1: return i + 1
            
            if word1[i] == word2[j]:
                return dp(i - 1, j - 1)  # 啥都不做
            else:
                return min(
                    dp(i, j - 1) + 1,    # 插入
                    dp(i - 1, j) + 1,    # 删除
                    dp(i - 1, j - 1) + 1 # 替换
                )
    
        # i，j 初始化指向最后一个索引
        return dp(len(word1) - 1, len(word2) - 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # arguments ref: https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
    parser.add_argument("--words", help="words", nargs='?', type=str, const="horse,ros", default="horse,ros")
    args = parser.parse_args()
    words = args.words.split(',')

    print(words)

    solution = Solution()
    result = solution.minDistance(words[0], words[1])
    print("result: {}".format(result))
    dpStackTrace.sort()
    print(dpStackTrace) # duplicated calls
    # a lot of duplicated calls, it would be slow. For high performance, using memo to remeber the result already calculated.
    # see editDistanceMemo.py