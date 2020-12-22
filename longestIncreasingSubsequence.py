import argparse
import cProfile, pstats, sys
import logging
from typing import List

"""
leetcode 300. Longest increasing subsequence
https://leetcode.com/problems/longest-increasing-subsequence/
"""

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for x in nums] # init, the minimun length of subsequence is 1 which is itself
        for i in range(0, len(nums)):
            for j in range(0, i): 
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # arguments ref: https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
    parser.add_argument("--numbers", help="numbers", nargs='?', type=str, const="10,9,2,5,3,7,101,18", default="10,9,2,5,3,7,101,18")
    args = parser.parse_args()
    numbers = [int(i) for i in args.numbers.split(',')]

    print(numbers)

    solution = Solution()
    length = solution.lengthOfLIS(numbers)
    print("total ways: {}".format(length))