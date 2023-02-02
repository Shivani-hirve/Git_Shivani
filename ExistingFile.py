# Check whether the file is exist or not in current directory

import os

def CreateFile(FileName):
    if(os.path.exists(FileName)):
        print("File is already existing")
        return
    else:
        open(FileName, "w")

def main():
    Name = input("Enter a File Name to check: ")

    CreateFile(Name)

if __name__ == "__main__":
    main()
