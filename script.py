# Importing libraries to work with system, time, difference of some objects
from re import search
import sys
import datetime
import difflib

# Importing colors library
from colorama import init
from termcolor import colored

# Using colorama to make termcolor work on Windows
init()

# Importing 'search' from regex library
# Constant variable initialization
# Where 'datetime.datetime.now().timestamp()' -> is time stamp
# and 'datetime.datetime.fromtimestamp()' -> converts time stamp to
# normal date and time, for example: 2023-01-11 18:40:31.988340
TIME_STAMP = datetime.datetime.fromtimestamp(
    datetime.datetime.now().timestamp())
print(f"Time stamp: {TIME_STAMP}")

# Defining function that will be show a menu
def menu():
    print('1. View file\n2. Compare files\n3. Exit\nEnter a value: ', end='')
    return int(input())

# Defining function that will print contents of a file
def printContentsOfFile(filename):
    with open(filename, 'r') as f:
        for line in f:
            print(line, end='')

# Emulating 'diff' command
def compareFiles(filenames):
    with open(filenames[0], 'r') as f1:
        with open(filenames[1], 'r') as f2:
            diff = difflib.unified_diff(f1.readlines(), f2.readlines())

            for line in diff:
                if line[0] == '+':
                    print(colored(line, 'green'), end='')
                elif line[0] == '-':
                    print(colored(line, 'red'), end='')
                else:
                    print(line, end='')

# Defining function of looped menu
def loopedMenu(filenames):
    while True:
        choice = menu()
        if choice == 1:
            while True:
                print('Which of file do you want to view?\n1. {0}\n2. {1}\nEnter a number: '.format(
                    filenames[0], filenames[1]), end='')
                choice = input()
                if int(choice) == 1:
                    printContentsOfFile(filenames[0])
                    break
                elif int(choice) == 2:
                    printContentsOfFile(filenames[1])
                    break
                else:
                    print('Incorrect input')

        elif choice == 2:
            compareFiles(filenames)
        elif choice == 3:
            print('Exiting ...')
            break
        else:
            print('Incorrect input')

def main():
    # Getting names of files which are been passed to CLI
    # by command "py script.py <file1> <file2>"
    filenames = sys.argv[1:]
    loopedMenu(filenames)

main()
