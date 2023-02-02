from functools import reduce

def main():
    List = []
    Numbers = int(input("Enter how many number you want: "))
    for i in range (0, Numbers, 1):
        i = int(input("Enter number: "))
        List.append(i)
    print("Data is: ", List)
    
    # i = 0
    # while i <= no:
    #     i = int("Enter numbers: ")
    #     L.append(i)
    # print("Data is: ", List)

    FilterX = list(filter(lambda x : all(x%y!=0 for y in range(2,x)), List))
    print("Data After Filterd: ",FilterX)

    MapX = list(map(lambda x,y=2 : x*y, FilterX))
    print("Data after Mapped: ",MapX)

    ReduceX = reduce(lambda x, y: x if (x > y) else y, MapX)
    print("Final Outout: ", ReduceX)

if __name__ == "__main__":
    main()