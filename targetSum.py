import argparse
import cProfile, pstats, sys
import logging
from typing import List

"""
leetcode 494. Target Sum
https://leetcode.com/problems/target-sum/
"""

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        zeros = [x for x in nums if x == 0] # get all zeros from nums
        nums = [x for x in nums if x != 0] # now nums has no zero

        startNodes = [0]
        targetNodes = [S] # bfs bidirection
        nodes = [startNodes, targetNodes]

        for num in nums:
            nodes = self.sortByItemNumbers(nodes[0], nodes[1])
            nodes[0] = self.nextNodes(nodes[0], num)

        #now check the match items in nodes[0] and nodes[1]
        result = 0
        for num in nodes[0]:
            numInOtherNodes = [x for x in nodes[1] if x == num]
            result += len(numInOtherNodes)

        # every 0 need double the result
        return result * pow(2, len(zeros))

    """
    input two lists 
    return an array which sorted by list item numbers
    for exmple, if nodes0 items is less than or equal to items of nodes1 return [nodes0, nodes1]
    """
    def sortByItemNumbers(self, nodes0, nodes1):
        if len(nodes0) > len(nodes1): 
            return [nodes1, nodes0]
        return [nodes0, nodes1]

    """
    input nums: [1,2], number 1
    return [2,0,1,3]
    """
    def nextNodes(self, nums, number):
        result = []
        for num in nums:
            result.append(num + number)
            result.append(num - number)
        return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # arguments ref: https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
    parser.add_argument("--numbers", help="numbers", nargs='?', type=str, const="1,2,3,4,5", default="1,2,3,4,5")
    parser.add_argument("--target", help="the target sum", nargs='?', type=int, const="1", default="1")
    args = parser.parse_args()
    numbers = [int(i) for i in args.numbers.split(',')] 
    target = args.target

    print(numbers)
    print(target)

    solution = Solution()
    totalWays = solution.findTargetSumWays(numbers, target)
    print("total ways: {}".format(totalWays))