#!python.exe
import os
import sys
import argparse

currentDay = __file__[__file__.rfind("Day") + 3:__file__.rfind("Solution")]
filePath = os.path.realpath(__file__)

def GetInputLinesList(test = False):
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
                returnList.append(int(line))

    except Exception as e:
        print(f"Could not read input file:\n{e}")

    return returnList


#####################################
def Part1Internal(input):
    containedPairs = 0
    for i in input:
        pairs = i.split(',')
        pair1 = pairs[0]
        pair2 = pairs[1]

        range1End = pair1.find('-')
        range2End = pair2.find('-')

        range1 = range(int(pair1[:range1End]), int(pair1[range1End + 1:]) + 1)
        range2 = range(int(pair2[:range2End]), int(pair2[range2End + 1:]) + 1)

        if set(range1).issubset(range2) or set(range2).issubset(range1):
            containedPairs += 1

    print(containedPairs)

def Part1(test = False):
    Part1Internal(GetInputLinesList(test))

#####################################

#####################################
def Part2Internal(input):
    containedPairs = 0
    for i in input:
        pairs = i.split(',')
        pair1 = pairs[0]
        pair2 = pairs[1]

        range1End = pair1.find('-')
        range2End = pair2.find('-')

        range1 = range(int(pair1[:range1End]), int(pair1[range1End + 1:]) + 1)
        range2 = range(int(pair2[:range2End]), int(pair2[range2End + 1:]) + 1)

        if set(range1).intersection(range2):
            containedPairs += 1

    print(containedPairs)

def Part2(test = False):
    Part2Internal(GetInputLinesList(test))

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
