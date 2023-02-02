# Comparison of 2 files
import os
import filecmp

def File_Read():
    first_file = input("Enter the 1st File Name: ")
    second_file = input("Enter the 2nd File Name: ")
    with open(first_file) as f1:
        with open(second_file) as f2:
            if f1.read() == f2.read():
                print("Success")
            else:
                print("Failuare")

def main():

    File_Read()
       
if __name__ == "__main__":
    main()