# Copy content fron 1 file to another file
import os

def File_Read():
    first_file = "Demo.txt"
    second_file = input("Enter the File Name: ")

    file1 = open(first_file, "r")
    Data = file1.read()
    file1.close()

    with open(second_file, 'w') as file1:
        file1.write(Data)

    print("Completed")

    
def main():

    File_Read()
       
if __name__ == "__main__":
    main()