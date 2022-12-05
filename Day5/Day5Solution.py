#!python.exe
import os
import sys
import argparse
import re

currentDay = __file__[__file__.rfind("Day") + 3:__file__.rfind("Solution")]
filePath = os.path.realpath(__file__)

def GetCargoStacks():
    stacks = [[] for i in range(9)]

    try:
        with open(fr"{filePath}\..\Input.txt", 'r') as f:
            lines = f.readlines()
            for i in range(0, 8):
                for j in range(1, len(stacks) + 1):
                    currentCargo = lines[i][4 * j - 3]
                    if currentCargo != ' ':
                        stacks[j - 1].append(currentCargo)

    except Exception as e:
        print(f"Could not read input file:\n{e}")

    return stacks

def GetInstructions():
    instructionsList = []

    try:
        with open(fr"{filePath}\..\Input.txt", 'r') as f:
            lines = f.readlines()
            for i in range(10, len(lines)):
                nums = re.findall(r'\d+', lines[i])
                instructionsList.append(nums)

    except Exception as e:
        print(f"Could not read input file:\n{e}")

    return instructionsList

def WriteSolution(part, output, path = None):
    if path == None:
        path = fr"{filePath}\..\Output{part}.txt"

    try:
        with open(path, 'w') as f:
            f.write(output)
    except Exception as e:
        print(f"Could not write output file:\n{e}")

#####################################
def Part1Internal(stacks, instructions):
    # solution processing
    for i in instructions:
        moveCount = int(i[0])
        moveFrom = int(i[1]) - 1
        moveTo = int(i[2]) - 1

        for j in range(0, moveCount):
            currentCargo = stacks[moveFrom][0]
            stacks[moveFrom].pop(0)
            stacks[moveTo].insert(0, currentCargo)

    output = ""
    for i in stacks:
        output += i[0]

    return output

def Part1(test = False):
    soln = Part1Internal(GetCargoStacks(), GetInstructions())
    WriteSolution(1, soln)

#####################################

#####################################
def Part2Internal(stacks, instructions):
    # solution processing
    print(instructions[0])
    print(stacks)
    for i in instructions:
        moveCount = int(i[0])
        moveFrom = int(i[1]) - 1
        moveTo = int(i[2]) - 1

        toMove = []
        for j in range(0, moveCount):
            currentCargo = stacks[moveFrom][0]
            stacks[moveFrom].pop(0)
            toMove.insert(0, currentCargo)

        for j in toMove:
            stacks[moveTo].insert(0, j)

    output = ""
    for i in stacks:
        output += i[0]

    return output


def Part2(test = False):
    soln = Part2Internal(GetCargoStacks(), GetInstructions())
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
