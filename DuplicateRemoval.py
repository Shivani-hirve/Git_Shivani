#Automation script which accepts directory name from user and Remove Duplicate files from that directory.
from sys import *
import os
import hashlib
import time

def Deletefiles(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    icnt = 0

    if len(results) > 0:
        for result in results:
            for subresult in result:
                icnt +=1
                if icnt >= 2:
                    os.remove(subresult)

    else:
        print("No duplicate files found>")
        
def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

def FindDuplicate(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}
    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            print("Currect folder is: "+ dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups
    else:
        print("Invalid Path")

def PrintResult(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results) > 0:
        print("Duplicates Found:")
        print("The following files are dplicate.")
        for result in results:
            for subresult in result:
                print('\t\t%s'%subresult)
        else:
            print("No duplicate files found.")

def main():
    print("Application Name:"+argv[0])

    if(len(argv) != 2):
        print("Error: Invalid number of arguments")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script us used to traverse specific directory and display checksum of files")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage: Application Name AbsolutePath_of_Director Extension")
        exit()

    try:
        arr = {}
        startTime = time.time()
        arr = FindDuplicate(argv[1])
        PrintResult(arr)
        Deletefiles(arr)
        endTime = time.time()

        print('Took %s Second to evaluate'%(endTime - startTime))

    except ValueError:
        print("Error: Inavalid datatype of input")

    except Exception as E:
        print("Error: Invalid input", E)

if __name__ == "__main__":
    main()