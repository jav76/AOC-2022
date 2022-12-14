#!python.exe
import math
import os
import sys
import argparse
import re

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

def WriteSolution(day, output, path = None):
    if path == None:
        path = fr"{filePath}\..\Output{day}.txt"

    try:
        with open(path, 'w') as f:
            f.write(output)
    except Exception as e:
        print(f"Could not write output file:\n{e}")


class directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = {}
        self.dirSize = 0

    def addFile(self, fileName, size):
        self.files[fileName] = size

    def hasChild(self, directory):
        for i in self.children:
            if i.name == directory.name:
                return True
        return False

    def getFilesSize(self):
        directorySize = 0
        for file, size in self.files.items():
            directorySize += size
        return directorySize

    def __eq__(self, other): # Directory can't have two children with the same name
        return isinstance(other, directory) and self.name == other.name and self.parent == other.parent


def getDirectorySize(directory, level, size, limit=100000000000000):
    #print(directory.name, size)
    currentDirFileSize = directory.getFilesSize()
    if len(directory.children) == 0:
        if currentDirFileSize < limit:
            return size + currentDirFileSize
        else:
            return size
    childrenSize = 0
    for i in directory.children:
        currentDirSize = getDirectorySize(i, level + 1, 0)
        i.dirSize = currentDirSize
        #print(i.name, currentDirSize)
        if currentDirSize < limit:
            #print(f"LeveL {level} Child size of {i.name}: {currentDirSize}")
            #print(f"adding {currentDirSize} to {childrenSize}")
            childrenSize += currentDirSize
            #print(childrenSize)
    if currentDirFileSize < limit:
        size += currentDirFileSize

    #print(f"CUR SIZE: {size} child size: {childrenSize}")
    if childrenSize < limit:
        directory.dirSize = size + childrenSize
        return size + childrenSize
    else:
        directory.dirSize = size
        return size


#####################################
def Part1Internal(input):
    # solution processing
    directories = []
    currentDir = None

    for i in range(0, len(input)):
        currentLine = input[i]
        print(currentLine)
        if currentLine[0] == "$": # This is a command line

            if currentLine[2:4] == "cd":
                dirName = currentLine[5:]
                if dirName == "..":
                    if currentDir.parent != None:
                        currentDir = currentDir.parent
                        print(f"Switching directories to {currentDir}")
                else:
                    if currentDir != None:
                        directoryExists = False
                        for dir in currentDir.children:
                            if dir.name == dirName:
                                directoryExists = True
                                currentDir = dir
                                print(f"Switching to directory: {currentDir.name}")
                                break
                        newDir = directory(dirName, currentDir)
                        if not directoryExists and not currentDir.hasChild(newDir):
                            directories.append(newDir)
                            currentDir.children.append(newDir)
                            currentDir = newDir

                    else:

                        directoryExists = False
                        for dir in directories:
                            if dir.name == dirName:
                                directoryExists = True
                                currentDir = dir
                                print(f"Switching to directory: {currentDir.name}")
                                break
                        if not directoryExists:
                            newDir = directory(dirName, currentDir)
                            directories.append(newDir)
                            currentDir = newDir
                            print(f"Added new directory: {currentDir.name}")
        else:
            if currentLine[0:3] == "dir":
                dirName = currentLine[4:]
                directoryExists = False
                for dir in currentDir.children:
                    if dir.name == dirName:
                        directoryExists = True
                        break
                newDir = directory(dirName, currentDir)
                if not directoryExists:
                    directories.append(newDir)
                if not currentDir.hasChild(newDir):
                    currentDir.children.append(newDir)

                    print(f"Added new directory: {newDir.name}")
            else:
                fileSizeExpression = re.match(r"^[^\d]*(\d+)", currentLine)
                if fileSizeExpression is not None:
                    sizeSpan = fileSizeExpression.span()
                    fileSize = int(currentLine[sizeSpan[0]:sizeSpan[1]])
                    fileName = currentLine[sizeSpan[1] + 1:]
                    currentDir.addFile(fileName, fileSize)
                    print(f"Added file {fileName} - {fileSize} to directory: {currentDir.name}")

    getDirectorySize(directories[0], 0, 0)
    for i in directories:
        print(i.name)
        for j in i.children:
            print(f"\t{j.name} : {j.dirSize}")
        print(f"\t{i.files}")
        print(f"\t{i.dirSize}")


    sum = 0
    for i in directories:
        if i.dirSize <= 100000:
            sum += i.dirSize

    print(sum)
    return str(sum)


def Part1(test = False):
    soln = Part1Internal(GetInputLinesList(test))
    WriteSolution(1, soln)

#####################################

#####################################
def Part2Internal(input):
    # solution processing
    directories = []
    currentDir = None

    for i in range(0, len(input)):
        currentLine = input[i]
        print(currentLine)
        if currentLine[0] == "$":  # This is a command line

            if currentLine[2:4] == "cd":
                dirName = currentLine[5:]
                if dirName == "..":
                    if currentDir.parent != None:
                        currentDir = currentDir.parent
                        print(f"Switching directories to {currentDir}")
                else:
                    if currentDir != None:
                        directoryExists = False
                        for dir in currentDir.children:
                            if dir.name == dirName:
                                directoryExists = True
                                currentDir = dir
                                print(f"Switching to directory: {currentDir.name}")
                                break
                        newDir = directory(dirName, currentDir)
                        if not directoryExists and not currentDir.hasChild(newDir):
                            directories.append(newDir)
                            currentDir.children.append(newDir)
                            currentDir = newDir

                    else:

                        directoryExists = False
                        for dir in directories:
                            if dir.name == dirName:
                                directoryExists = True
                                currentDir = dir
                                print(f"Switching to directory: {currentDir.name}")
                                break
                        if not directoryExists:
                            newDir = directory(dirName, currentDir)
                            directories.append(newDir)
                            currentDir = newDir
                            print(f"Added new directory: {currentDir.name}")
        else:
            if currentLine[0:3] == "dir":
                dirName = currentLine[4:]
                directoryExists = False
                for dir in currentDir.children:
                    if dir.name == dirName:
                        directoryExists = True
                        break
                newDir = directory(dirName, currentDir)
                if not directoryExists:
                    directories.append(newDir)
                if not currentDir.hasChild(newDir):
                    currentDir.children.append(newDir)

                    print(f"Added new directory: {newDir.name}")
            else:
                fileSizeExpression = re.match(r"^[^\d]*(\d+)", currentLine)
                if fileSizeExpression is not None:
                    sizeSpan = fileSizeExpression.span()
                    fileSize = int(currentLine[sizeSpan[0]:sizeSpan[1]])
                    fileName = currentLine[sizeSpan[1] + 1:]
                    currentDir.addFile(fileName, fileSize)
                    print(f"Added file {fileName} - {fileSize} to directory: {currentDir.name}")

    getDirectorySize(directories[0], 0, 0)
    for i in directories:
        print(i.name)
        for j in i.children:
            print(f"\t{j.name} : {j.dirSize}")
        print(f"\t{i.files}")
        print(f"\t{i.dirSize}")

    spaceNeeded = directories[0].dirSize - (70000000 - 30000000)

    canDelete = []
    for i in directories:
        if i.dirSize >= spaceNeeded:
            canDelete.append(i)

    lowest = math.inf

    for i in canDelete:
        print(f"Delete candidate: {i.name}, {i.dirSize}, current lowest: {lowest}")
        if i.dirSize < lowest:
            lowest = i.dirSize
            print(f"New lowest: {i.name}, {i.dirSize}")

    print(lowest)
    return str(lowest)

def Part2(test = False):
    soln = Part2Internal(GetInputLinesList(test))
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
