import os
import sys
import datetime
import difflib

from re import search
from colorama import init
from termcolor import colored

# Using colorama to make termcolor work on Windows
init()

# Constant variable initialization
# Where 'datetime.datetime.now().timestamp()' -> is time stamp
# and 'datetime.datetime.fromtimestamp()' -> converts time stamp to
# normal date and time, for example: 2023-01-11 18:40:31.988340
TIME_STAMP = datetime.datetime.fromtimestamp(
    datetime.datetime.now().timestamp())


def clearConsole():
    ''' Clearing up console output '''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def isOnlyDigits(string):
    ''' Returns "True" if 'string' is contains only digits
    "False" - otherwise '''
    if search("\d+", string):
        return True
    else:
        return False


def menu():
    ''' Prints menu and current date and time to terminal. Returns input value '''
    print(f"Time stamp: {TIME_STAMP}")
    print('1. View file\n2. Compare files\n3. Clear output\n4. Exit\nEnter a value: ', end='')
    return input()


def printContentsOfFile(filename):
    ''' Just prints file content to terminal, with "end=''" '''
    with open(filename, 'r') as f:
        for line in f:
            print(line, end='')


def findStringInFile(filename, pattern='^compiler=\w'):
    ''' Returns line which is respond to specified pattern '''
    with open(filename, 'r') as f:
        for line in f.readlines():
            if search(pattern, line):
                return line


def compareFiles(filenames):
    ''' Comparing 2 files like 'diff' linux command. Prints
    results to the terminal, inserted marked with green, deleted - with red,
    neutral lines marked with white '''
    with open(filenames[0], 'r') as f1, \
            open(filenames[1], 'r') as f2:
        if findStringInFile(filenames[0]) == findStringInFile(filenames[1]):
            print(
                colored("The files differ only in the time and place of assembly", 'blue'))
        else:
            diff = difflib.unified_diff(f1.readlines(), f2.readlines())
            for line in diff:
                if line[0] == '+':
                    print(colored(line, 'green'), end='')
                elif line[0] == '-':
                    print(colored(line, 'red'), end='')
                else:
                    print(line, end='')


def loopedMenu(filenames):
    ''' Function same as 'menu()', but looped and processing users input '''
    while True:
        choice = menu()
        if isOnlyDigits(choice):
            if int(choice) == 1:
                while True:
                    print('Which of file do you want to view?\n1. {0}\n2. {1}\nEnter a number: '.format(
                        filenames[0], filenames[1]), end='')
                    choice = input()
                    if isOnlyDigits(choice):
                        if int(choice) == 1:
                            printContentsOfFile(filenames[0])
                            break
                        elif int(choice) == 2:
                            printContentsOfFile(filenames[1])
                            break
                        else:
                            print(colored('Error! Incorrect input', 'red'))
                    else:
                        print(
                            colored('Your input is invalid! You entered not only digits', 'red'))
            elif int(choice) == 2:
                compareFiles(filenames)
            elif int(choice) == 3:
                clearConsole()
            elif int(choice) == 4:
                print('Exiting ...')
                break
            else:
                print(colored('Error! Incorrect input', 'red'))
        else:
            print(colored('Your input is invalid! You entered not only digits', 'red'))


def main():
    # Getting names of files which are been passed to CLI
    # by command "python3 script.py <file1> <file2>"
    filenames = sys.argv[1:]
    loopedMenu(filenames)


main()
