from functools import reduce

def CheckEven(No):
    if (No >= 70) and (No <= 90):
        return No

def Doubles(No):
    return No+10

def Sum(A,B):
    return A*B

def main():
    iSize = int(input("Enter number of elements you want to enter : "))

    Data_Input = []
    print("Please enter the data ")
    for iCnt in range(0,iSize,1):
        iCnt = int(input())
        Data_Input.append(iCnt)
    print("Data is : ",Data_Input)
    
    Data_Filter = list(filter(CheckEven, Data_Input))
    print("Data after filter is : ",Data_Filter)

    Data_Map = list(map(Doubles, Data_Filter))
    print("Data after map is : ",Data_Map)
    
    Output = reduce(Sum, Data_Map)
    print("Result after reduce is : ",Output)

if __name__ == "__main__":
    main()