import argparse
import cProfile, pstats, sys
import logging
from typing import List

"""
leetcode 300. Longest increasing subsequence
https://leetcode.com/problems/longest-increasing-subsequence/
使用牌堆二分法
https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E8%AE%BE%E8%AE%A1%EF%BC%9A%E6%9C%80%E9%95%BF%E9%80%92%E5%A2%9E%E5%AD%90%E5%BA%8F%E5%88%97.md
"""

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tops = [nums[0]] # the minimum number in each pile

        for i in range(1, len(nums)):
            tops = self.putNum(nums[i], tops) 

        return len(tops)

    def putNum(self, num, tops):
        # 二分法
        left = 0
        right = len(tops)
        while left < right:
            i = left + int((right - left) / 2)
            if num <= tops[i]:
                right = i
            else:
                left = i + 1
        
        if left < len(tops):
            tops[left] = num
        else: 
            tops.append(num)
        return tops
          

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