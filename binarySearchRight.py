"""
this is the practice to use binary search to find the most right matched item
the binary search can only be used on sorted array
"""

import argparse
import cProfile
import logging
import math

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

def binarySearch(numbers, target):
    if target < numbers[0] or target > numbers[-1]: # the target is not in the array
        return -1
    left = 0
    right = len(numbers) - 1  # the last index
    while (left < right):
        mid = left + math.ceil((right - left) / 2)  # if two in the middle, pick up the right one
        if numbers[mid] == target:
            left = mid
            logging.debug("left = %s", left)
        elif numbers[mid] < target:
            left = mid + 1
            logging.debug("left = %s", left)
        elif numbers[mid] > target:
            right = mid - 1
            logging.debug("rignt = %s", right)
        
    return left

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # arguments ref: https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
    parser.add_argument("--numbers", help="provide numbers like 1,2,3,4,5", nargs='?', type=str, const="1,2,2,2,2,3", default="1,2,2,2,2,2,3")
    parser.add_argument("--target", help="the target to search", nargs='?', type=int, const="2", default="2")
    args = parser.parse_args()
    numbers = [int(i) for i in args.numbers.split(',')] 
    target = args.target

    index = binarySearch(numbers, target)
    logging.info("the most right index of number %s in array %s is %s", target, numbers, index)

        