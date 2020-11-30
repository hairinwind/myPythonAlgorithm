from math import nan
from memory_profiler import profile

import argparse
import cProfile

# this is the code practice of 
# https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E8%AF%A6%E8%A7%A3%E8%BF%9B%E9%98%B6.md

# this is the dpTable to save the state which can reduce recursive times
dpTable = {}

# this is the method using recursive, from top to bottom
# as it repeats the calculation for the same amount, it is quite slow when the number is big
def getMinCoinNumber(amount, coinOptions):
    # print("try to get coinNumber for amount {}".format(amount))
    minCoin = nan
    for x in coinOptions:
        preAmount = amount-x  # the amount after taking away one coin, in this example, it can take away either 1 or 2 or 5
        if preAmount < 0: 
            continue
        if preAmount == 0: # end recursive condition
            return 1
        minCoin = min(getMinCoinNumber(preAmount, coinOptions), minCoin) 
    minCoin = 1 + minCoin
    # print("coinNumber for amount {} is {}".format(amount, minCoin))    
    return minCoin

# this is the method to remember the previous calculate result
# this method is still from top to bottom
def getMinCoinNumber2(amount, coinOptions):
    minCoin = nan
    for x in coinOptions:
        preAmount = amount-x  # the amount after taking away one coin, in this example, it can take away either 1 or 2 or 5
        if preAmount < 0: 
            continue
        if preAmount == 0:
            saveDpTable(amount, 1)
            return 1
        minCoin = min(getDpMinCoinNumber(preAmount, coinOptions), minCoin)
    minCoin = 1 + minCoin
    saveDpTable(amount, minCoin)
    return minCoin
    
def getDpMinCoinNumber(amount, coinOptions): 
    if amount in dpTable:
        return dpTable[amount]
    if amount == 1:
        saveDpTable(1, 1)
        return dpTable[1]
    minCoin = getMinCoinNumber2(amount, coinOptions)
    return dpTable[amount]

def saveDpTable(index, value):
    dpTable[index] = value
    # print("save dpTable[{}] value {}".format(index, value))

# this is the method to calculate from bottom to top, no recursive call
# for the recursive one, if the number > 2470, there is error "maximum recursion depth exceeded in comparison"
def getMinCoinNumber3(amount, coinOptions):
    for i in range(amount+1):
        if i == 0:
            saveDpTable(i, 0)
            continue
        minCoin = nan
        for x in coinOptions:
            preAmount = i-x
            if preAmount < 0:
                continue
            minCoin = min(dpTable[preAmount], minCoin)
        saveDpTable(i, minCoin+1)    
    return dpTable[amount]

def runGetMinCoinNumber(amount, coinOptions):
    minCoinNumber = getMinCoinNumber(amount, coinOptions)  
    print("====== the minimum coin needed for {} is {}".format(amount, minCoinNumber))

def runGetMinCoinNumber2(amount, coinOptions):
    minCoinNumber = getMinCoinNumber2(amount, coinOptions)  
    print("====== the minimum coin needed for {} is {}".format(amount, minCoinNumber))

def runGetMinCoinNumber3(amount, coinOptions):
    minCoinNumber = getMinCoinNumber3(amount, coinOptions)  
    print("====== the minimum coin needed for {} is {}".format(amount, minCoinNumber))


@profile
# memory profile ref: https://pypi.org/project/memory-profiler/
# if without @profile, to run memory profile: python -m memory_profiler example.py
def runMprofGetMinCoinNumber(amount, coinOptions):
    runGetMinCoinNumber(amount, coinOptions)

@profile
def runMprofGetMinCoinNumber2(amount, coinOptions):
    runGetMinCoinNumber2(amount, coinOptions)

@profile
def runMprofGetMinCoinNumber3(amount, coinOptions):
    runGetMinCoinNumber3(amount, coinOptions)

if __name__ == "__main__":
    coinOptions = [1,2,5]
    parser = argparse.ArgumentParser()
    # arguments ref: https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
    parser.add_argument("--amount", help="Amount", nargs='?', type=int, const=3, default=18)
    args = parser.parse_args()
    amount = args.amount
 
    # cProfile.run("runGetMinCoinNumber(amount, sorted(coinOptions)[::-1])") # descending sorted coinOptions can decrease recursive numbers
    # cProfile.run("runGetMinCoinNumber(amount, coinOptions)")
    # runGetMinCoinNumber(amount, sorted(coinOptions)[::-1])
    
    # runGetMinCoinNumber2(amount, sorted(coinOptions)[::-1])
    # cProfile.run("runGetMinCoinNumber2(amount, sorted(coinOptions)[::-1])") # this function is much master than the prvious one when the number is big
    # runMprofGetMinCoinNumber2(amount, sorted(coinOptions)[::-1]) # result: no diff on mem usages

    # runGetMinCoinNumber3(amount, sorted(coinOptions)[::-1])
    cProfile.run("runGetMinCoinNumber3(amount, sorted(coinOptions)[::-1])")
    # runMprofGetMinCoinNumber3(amount, sorted(coinOptions)[::-1]) # result: no diff on mem usages