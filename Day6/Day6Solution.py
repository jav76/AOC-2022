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

def WriteSolution(part, output, path = None):
    if path == None:
        path = fr"{filePath}\..\Output{part}.txt"

    try:
        with open(path, 'w') as f:
            f.write(output)
    except Exception as e:
        print(f"Could not write output file:\n{e}")

#####################################
def Part1Internal(input):
    # solution processing
    for i in range(0, len(input) - 3):
        currentWindow = input[i:i+4]
        charRepeated = False
        for j in currentWindow:
            if currentWindow.count(j) > 1:
                charRepeated = True

        if charRepeated == False:
            return str(i + 4)




def Part1(test = False):
    soln = Part1Internal(GetInputRaw(test))
    WriteSolution(1, soln)

#####################################

#####################################
def Part2Internal(input):
    # solution processing
    for i in range(0, len(input) - 13):
        currentWindow = input[i:i+14]
        charRepeated = False
        for j in currentWindow:
            if currentWindow.count(j) > 1:
                charRepeated = True

        if charRepeated == False:
            return str(i + 14)

def Part2(test = False):
    soln = Part2Internal(GetInputRaw(test))
    WriteSolution(2, soln)

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
