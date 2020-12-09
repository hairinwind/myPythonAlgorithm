import argparse
import cProfile
import logging

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

result = []

def backTrackQueen(number, queenPositions): 
    for i in range(0, number * number): 
        x = i % number
        y = i // number
        queenPositions.append((x, y))
        getNextQueen(number, queenPositions)
        queenPositions.remove((x, y))

def getNextQueen(number, queenPositions):
    x = 0
    y = 0
    if len(queenPositions) > 0: # if one queen is already on the board, starting from the first cell of next 
        lastQueenPosition = queenPositions[-1]
        y = lastQueenPosition[1] + 1 # lastQueenPosition is tuples like (x,y)

    # end condition: number is never changed which is the expected queen number
    if len(queenPositions) == number: 
        result.append(queenPositions)
        return
    if y >= number:
        return
    if number - y + 1 < number - len(queenPositions):  # if the left rows is less then the queen needed, it is not valid
        return
    
    while True:
        if isValidForQueen(x, y, queenPositions):
            queenPositions.append((x, y))
            getNextQueen(number, queenPositions.copy())
            # remove the previous position and try the next position
            queenPositions.remove((x, y))    
        x, y = next(x, y, number)
        if y >= number:
            break

def next(x, y, number):
    nextX = x + 1
    if nextX < number:
        return nextX, y
    else:
        return 0, y+1

def isValidForQueen(x, y, queenPositions):
    for queenPosition in queenPositions:
        if queenPosition[0] == x or queenPosition[1] == y: # same row or same column is not valid
            return False
        if abs(queenPosition[0] - x) == abs(queenPosition[1] - y): # 
            return False

    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # arguments ref: https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
    parser.add_argument("--number", help="provide numbers great than 2", nargs='?', type=int, const="4", default="4")
    args = parser.parse_args()
    number = args.number

    queenPositions = []
    # backTrackQueen(number, queenPositions)
    cProfile.run("backTrackQueen(number, queenPositions)")
    logging.debug("len %s", len(result))