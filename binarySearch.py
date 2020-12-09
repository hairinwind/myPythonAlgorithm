import argparse
import cProfile
import logging

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

def binarySearch(numbers, target):
    if target < numbers[0] or target > numbers[-1]: # the target is not in the array
        return -1
    left = 0
    right = len(numbers) - 1  # the last index
    while (left < right):
        mid = left + (right - left) // 2
        if numbers[mid] == target:
            return mid
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
    parser.add_argument("--numbers", help="provide numbers like 1,2,3,4,5", nargs='?', type=str, const="1,2,3,4,5,6", default="1,2,3,4,5,6,7,8,9")
    parser.add_argument("--target", help="the target to search", nargs='?', type=int, const="4", default="4")
    args = parser.parse_args()
    numbers = [int(i) for i in args.numbers.split(',')] 
    target = args.target

    index = binarySearch(numbers, target)
    logging.info("the index of number %s in array %s is %s", target, numbers, index)

        