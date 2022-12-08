#!python.exe
import os
import sys
import argparse

currentDay = __file__[__file__.rfind("Day") + 3:__file__.rfind("Solution")]
filePath = os.path.realpath(__file__)

def GetInputLinesTup(test = False):
    path = ""
    if test:
        path = fr"{filePath}\..\Input.test.txt"
    else:
        path = fr"{filePath}\..\Input.txt"

    lines = []
    try:
        with open(path, 'r') as f:
            lines = f.read().splitlines()
    except Exception as e:
        print(f"Could not read input file:\n{e}")

    result = []
    for i in lines:
        result.append(i.split(" "))

    return result

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

# I was going to re-write this day's solution to be better but I don't really care anymore
def Part1Internal(input):
    # solution processing
    score = 0
    for pair in input:
        opponent = pair[0]
        response = pair[1]

        match opponent:
            case 'A': # Rock
                if response == 'Y': # Paper
                    score = score + 6
                    score = score + 2
                elif response == 'X': # Rock
                    score = score + 3
                    score = score + 1
                else:
                    score = score + 3

            case 'B': # Paper
                if response == 'Y': # Paper
                    score = score + 3
                    score = score + 2
                elif response == 'Z': # Scissors
                    score = score + 6
                    score = score + 3
                else:
                    score = score + 1

            case 'C': # Scissors
                if response == 'X': # Rock
                    score = score + 6
                    score = score + 1
                elif response == 'Z':
                    score = score + 3
                    score = score + 3
                else:
                    score = score + 2

        print(pair, score)

    print(score)

def Part1(test = False):
    Part1Internal(GetInputLinesTup(test))

#####################################

#####################################
def Part2Internal(input):
    score = 0
    for pair in input:
        opponent = pair[0]
        response = pair[1]

        match opponent:
            case 'A':  # Rock
                if response == 'X': # Lose
                    score = score + 3
                elif response == 'Y': # Draw
                    score = score + 3
                    score = score + 1
                else:
                    score = score + 6
                    score = score + 2

            case 'B':  # Paper
                if response == 'X': # Lose
                    score = score + 1
                elif response == 'Y': # Draw
                    score = score + 3
                    score = score + 2
                else:
                    score = score + 6
                    score = score + 3

            case 'C':  # Scissors
                if response == 'X': # Lose
                    score = score + 2
                elif response == 'Y': # Draw
                    score = score + 3
                    score = score + 3
                else:
                    score = score + 6
                    score = score + 1

        print(pair, score)

    print(score)

def Part2(test = False):
    Part2Internal(GetInputLinesTup(test))

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
