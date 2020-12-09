import argparse
import cProfile
import logging

result = []

def findNQueen(number):
    for y in range(0, number):
        for x in range(0, number):  
            board = getInitialBoard(number)
            queenCell = board[y*number + x]
            queenCell.value = 'Q'
            queens = [queenCell]
            findNextQueen(number, board, queens)

def getInitialBoard(number): 
    board = []
    for y in range(0, number):
        for x in range(0, number):    
            board.append(Cell(x, y))
    return board

def findNextQueen(number, availableCells, queens):
    # print("availableCells {} and queens {}".format(availableCells, queens))
    if number == len(queens): 
        result.append(queens.copy())
        return
    nextAvailableCells = getAvailableCells(availableCells, queens)
    if len(nextAvailableCells) < number - len(queens): # the left available cells is less than the left queens, no need to continue
        return 
    for cell in nextAvailableCells:
        queens.append(cell)
        findNextQueen(number, nextAvailableCells, queens)
        # remove to try the next available cell
        queens.remove(cell)


def getAvailableCells(availableCells, queens):
    lastQueen = queens[-1]
    result = []
    for cell in availableCells:
        # only consider the cells after the last queen
        if cellIndexCompare(cell, lastQueen) <= 0: 
            continue
        # not conflict with last queen   
        if cell.x != lastQueen.x and cell.y != lastQueen.y \
            and abs(cell.x - lastQueen.x) != abs(cell.y - lastQueen.y): 
            result.append(cell)
    return result

def cellIndexCompare (cell1, cell2):
    if cell1.x == cell2.x and cell1.y == cell2.y:
        return 0
    if cell1.y < cell2.y or (cell1.y == cell2.y and cell1.x < cell2.x): 
        return -1
    return 1  

class Cell: 
    def __init__(self, x, y, value='E'):  #value: E - empty, Q - queen, N - not available
        self.x = x
        self.y = y
        self.value = value

    def __str__(self): # this mehtod is like toString in java class
        return "{},{} {}".format(self.x, self.y, self.value)
    
    def __repr__(self): # this method is to print object in array prettily
        return str(self)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # arguments ref: https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
    parser.add_argument("--number", help="provide numbers great than 2", nargs='?', type=int, const="4", default="4")
    args = parser.parse_args()
    number = args.number

    # board = [[Cell(i, j) for i in range(number)] for j in range(number)]
    # print(board)

    # findNQueen(number)
    cProfile.run("findNQueen(number)")
    print("for number {}, the result is {}".format(number, len(result)))
    # print("result {}".format(result))