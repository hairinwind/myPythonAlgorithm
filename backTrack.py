# this is the practice code of "back track" or "all permutation" or "decision tree"
# give you n different numbers and need you return all permutation


from memory_profiler import profile
import argparse
import cProfile
import logging

result = set()

def backTrack(numbers, track):
    if len(numbers) == 0: # end condition, no more numbers available
        logging.debug("tracks append %s", track)
        result.add(''.join(track))
        return 
    
    for i in numbers:
        print("track is {} and next number is {}".format(track, i))
        track.append(i)
        subNumbers = numbers.copy() # the code was changed a bit to support duplicated numbers 
        subNumbers.remove(i)
        logging.debug("subNumbers %s", subNumbers)
        backTrack(subNumbers, track)
        # recover to previous state
        track.pop()
    
@profile
def runBackTrack(numbers, track):
    backTrack(numbers, track) 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # arguments ref: https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
    parser.add_argument("--numbers", help="provide numbers like 1,2,3", nargs='?', type=str, const="1,2,3", default="1,2,3")
    args = parser.parse_args()
    numbers = args.numbers.split(',')

    track = []

    # runBackTrack(numbers, track)
    backTrack(numbers, track)
    # cProfile.run("backTrack(numbers, track)")
    print("len {} and result {}".format(len(result), result))