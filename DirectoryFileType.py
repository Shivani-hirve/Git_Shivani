import os
from sys import *
from pathlib import Path
import fnmatch

def Directory_Watcher(path, extension):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for foldername, subfolder, Filenames in os.walk(path):
            for filen in Filenames:
                if filen.lower().endswith(extension):
                    print(filen)

    else:
        print("Invalid Path")

def main():
    print("Directory watcher application")

    if(argv[1] == "-h"):
        print("This script will travel the directory and display the name of all entries")
        exit()

    if(argv[1]== "-u"):
        print("Usage : Application_name Directory_Name")
        exit()
    
    if(len(argv)<3):
        print("Insufficient argument")
        exit()

    Directory_Watcher(argv[1], argv[2])


if __name__ == "__main__":
    main()