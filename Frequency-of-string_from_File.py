# Check the Frequecy of string from File

import os
import sys

def CreateFile(FileName, str):
    f = open(FileName, "r")
    str = str.split()
    str2 = []

    for i in str:
        if i not in str2:
            str2.append(i)
        for i in range(0, len(str2)):
            print("Frequncy of", str2[i], 'is:', str.count(str2[i]))

    f.close()

def main():
    Name = input("Enter a File Name to check: ")
    Char = input("Enter the string: ")

    CreateFile(Name, Char)

if __name__ == "__main__":
    main()
