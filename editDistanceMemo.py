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
        dp = []
        for i in range(0, len(word1) + 1): 
            dp.append([0 for x in word2+"0"])
        
        for i in range(0, len(dp[0])):
            dp[0][i] = i
        for i in range(0, len(dp)):
            dp[i][0] = i
        print(dp)

        for i in range(0, len(word1)):
            dp_row_index = i + 1
            for j in range(0, len(word2)):
                dp_col_index = j + 1
                if word1[i] == word2[j]:
                    dp[dp_row_index][dp_col_index] = dp[i][j]
                else:
                    dp[dp_row_index][dp_col_index] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
        return dp[len(word1)][len(word2)]
       

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