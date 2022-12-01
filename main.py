#!python.exe
import importlib
import os
import sys
import requests
import argparse
import html
from shutil import copyfile
from datetime import datetime
from urllib.request import urlopen

CURRENT_YEAR = 2022


def GetSSID(path = None):
    if path == None:
        try:
            with open("SSID.secret", 'r') as f:
                content = f.read()
                return content
        except Exception as e:
            print(f"Could not open SSID.secret:\n{e}")
    else:
        try:
            with open(path, 'r') as f:
                content = f.read()
                return content
        except Exception as e:
            print(f"Could not open {path}:\n{e}")

def GetInput(day, SSID):
    url = f'https://adventofcode.com/{CURRENT_YEAR}/day/{int(day)}/input'
    cookies = dict(session = SSID)

    try:
        data = requests.get(url, cookies = cookies)
    except Exception as e:
        print(f"Error with request:{e}")
        return None

    if data.status_code == 200:
        dataText = data.text

        try:
            os.makedirs(f"Day{day}", exist_ok = True)
            with open(f"Day{day}/Input.txt", 'w') as f:
                f.write(dataText)

            with open(f"Day{day}/Input.test.txt", 'w') as f:
                f.write(GetTestInput(day))

            if not os.path.exists(f"Day{day}/Day{day}Solution.py"):
                InitializeDay(day)

        except Exception as e:
            print(f"Could not write input data:\n{e}")
    else:
        print(f"Error requesting AOC data:\n{data.status_code} - {data.reason}")

def InitializeDay(day):
    os.makedirs(f"Day{day}", exist_ok=True)
    copyfile("solutionBase.py", f"Day{day}/Day{day}Solution.py")

def GetTestInput(day):
    url = f"https://adventofcode.com/{CURRENT_YEAR}/day/{int(day)}"
    page = urlopen(url)
    html_bytes = page.read()
    htmltext = html_bytes.decode("utf-8")
    htmltext = html.unescape(htmltext)
    element = "<pre><code>"

    elementPosStart = htmltext.find(element)
    if elementPosStart != -1:
        elementPosEnd = htmltext.find("</code></pre>")
        inputText = htmltext[elementPosStart + len(element):elementPosEnd]

        return inputText

def RunSolution(day, part = None):
    if os.path.isdir(f"Day{day}"):
        if os.path.exists(f"Day{day}/Day{day}Solution.py"):
            # Add specified day directory to path and import it
            solnDir = f"{os.path.dirname(os.path.realpath(__file__))}/Day{day}"
            sys.path.insert(0, solnDir)
            soln = importlib.import_module(f"Day{day}Solution")

            if part == 1:
                soln.Part1()
            elif part == 2:
                soln.Part2()
            elif part == None:
                soln.Part1()
                soln.Part2()
        else:
            print(f"No solution exists yet for day {day}.")
            response = input(f"Initialize a new solution now for day {day}? (Y/N)")
            if response.rstrip().lower() == "y":
                InitializeDay(day)
    else:
        print("No directory exists yet for day {day}.")
        response = input(f"Initialize a new directory now for day {day}? (Y/N)")
        if response.rstrip().lower() == "y":
            InitializeDay(day)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "day",
        type = int
    )
    parser.add_argument(
        "-s",
        "--solution",
        type = int,
        help = "Run the solution for the specified part"
    )
    parser.add_argument(
        "-i",
        "--input",
        action = argparse.BooleanOptionalAction,
        help = "Get the input file for the specified day"
    )
    parser.add_argument(
        "-t",
        "--test",
        action = argparse.BooleanOptionalAction,
        help = "Run against the test input for the specified day."
    )

    args = parser.parse_args()

    day = args.day

    if args.input:
        SSID = GetSSID()
        GetInput(day, SSID)

    RunSolution(day, args.solution)

