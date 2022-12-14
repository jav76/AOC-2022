#!python.exe
import os
import queue
import sys
import argparse
import math

currentDay = __file__[__file__.rfind("Day") + 3:__file__.rfind("Solution")]
filePath = os.path.realpath(__file__)

def GetInputLinesDict(test = False):
    path = ""
    if test:
        path = fr"{filePath}\..\Input.test.txt"
    else:
        path = fr"{filePath}\..\Input.txt"

    try:
        with open(path, 'r') as f:
            return f.read().splitlines()
    except Exception as e:
        print(f"Could not read input file:\n{e}")

def GetInputRaw(test = False):
    path = ""
    if test:
        path = fr"{filePath}\..\Input.test.txt"
    else:
        path = fr"{filePath}\..\Input.txt"

    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"Could not read input file:\n{e}")

def GetInputNumbersList(test = False):
    path = ""
    if test:
        path = fr"{filePath}\..\Input.test.txt"
    else:
        path = fr"{filePath}\..\Input.txt"
    returnList = []

    try:
        with open(path, 'r') as f:
            for line in f.read().splitlines():
                if len(line) == 0:
                    returnList.append("*")
                else:
                    returnList.append(int(line))
            returnList.append("*")

    except Exception as e:
        print(f"Could not read input file:\n{e}")

    return returnList


#####################################
def Part1Internal(input):
    # solution processing
    highestCal = 0
    currentElf = 0
    for i in input:
        if i != '*':
            currentElf = currentElf + i
        else:
            if currentElf > highestCal:
                highestCal = currentElf
            currentElf = 0

    print(highestCal)
def Part1(test = False):
    Part1Internal(GetInputNumbersList(test))
#####################################

#####################################
def Part2Internal(input):
    # solution processing
    highestCalsQ = queue.PriorityQueue(3)
    currentElf = 0
    for i in input:
        if i != '*':
            currentElf = currentElf + i
        else:
            if (highestCalsQ.qsize() < 3):
                highestCalsQ.put(currentElf)
                currentElf = 0
                continue

            currentLowest = highestCalsQ.get()
            if currentElf > currentLowest:
                highestCalsQ.put(currentElf)
            else:
                highestCalsQ.put(currentLowest)
            currentElf = 0

    highestSum = 0
    for i in range(0, highestCalsQ.qsize()):
        current = highestCalsQ.get()
        highestSum = highestSum + current
    print(highestSum)


def Part2(test = False):
    Part2Internal(GetInputNumbersList(test))

#####################################


if __name__ == "__main__":
    # This file can be called directly, if not being accessed through main
    if len(sys.argv) == 1:
        Part1()
        Part2()
        sys.exit(0)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "part",
        type = int,
        help = "Run the solution for the specified part"
    )
    parser.add_argument(
        "-t",
        "--test",
        action = argparse.BooleanOptionalAction,
        help = "Run against the test input for the specified part."
    )

    args = parser.parse_args()

    if args.part:
        if args.part == 1:
            Part1(args.test)
        elif args.part == 2:
            Part2(args.test)


