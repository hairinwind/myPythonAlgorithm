import argparse
import cProfile, pstats, sys
import logging
from typing import List

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

"""
leetcode 28. implement strStr()
https://leetcode.com/problems/implement-strstr/
https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E4%B9%8BKMP%E5%AD%97%E7%AC%A6%E5%8C%B9%E9%85%8D%E7%AE%97%E6%B3%95.md
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x = 0 # shadow status
        dp = [[0 for x in range(0,256)] for x in needle]
        # base case
        dp[0][ord(needle[:1])] = 1
        for j in range(1, len(needle)):
            for c in range(0, 256):
                if ord(needle[j:j+1]) == c:
                    dp[j][c] = j + 1
                else:
                    dp[j][c] = dp[x][c]
                if dp[j][c] != 0:
                    print("... dp[{}][{}] is {}".format(j, c, dp[j][c]))
            print("x changed ... j={}, x={}, dp[{}][{}]={}".format(j,x, x, needle[j:j+1], dp[x][ord(needle[j:j+1])]))
            x = dp[x][ord(needle[j:j+1])]
            print("-") 
        # now the dp table (status moving table) is ready

        j = 0
        for index, c in enumerate(haystack):
            j = dp[j][ord(c)]
            if j == len(needle):
                return index - len(needle) + 1 
        return -1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # arguments ref: https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
    parser.add_argument("--haystack", help="haystack", nargs='?', type=str, const="abaaababc", default="abaaababc")
    parser.add_argument("--needle", help="needle", nargs='?', type=str, const="ababc", default="ababc")
    args = parser.parse_args()
    haystack = args.haystack
    needle = args.needle

    print(haystack)
    print(needle)

    solution = Solution()
    result = solution.strStr(haystack, needle)
    print("result: {}".format(result))