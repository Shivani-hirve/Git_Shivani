from functools import reduce

def main():
    Data_Input = []
    Size = int(input("Enter number of elements you want to enter : "))
    
    for i in range(0,Size,1):
        i = int(input("Please enter the data "))
        Data_Input.append(i)
    print("Data is : ",Data_Input)
    
    Data_Filter = list(filter(lambda No : No % 2 == 0, Data_Input))
    print("Data after filter is : ",Data_Filter)

    Data_Map = list(map(lambda No : No**2, Data_Filter))
    print("Data after map is : ",Data_Map)
    
    Output = reduce(lambda A,B : A+B ,Data_Map)
    print("Result after reduce is : ",Output)

if __name__ == "__main__":
    main()