# Display the content of a file on screen

import os

def File_Read(FileName):
    if(os.path.exists(FileName)):
        fd = open(FileName, 'r')
        Data = fd.read()
        print("Data from the file is:", Data)
        
        fd.close()

    else:
        print("File is Existing")
        return

def main():
    Name = input("Enter a File Name to display content: ")

    File_Read(Name)

if __name__ == "__main__":
    main()