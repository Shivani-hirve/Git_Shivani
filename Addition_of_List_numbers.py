# Make a list and addition of elements contains n=in list.

def main():
    size = int(input("How many elements you want to store in this List: "))

    list1 = []
    for i in range (1, size+1):
        i = int(input("Enter your Elements: "))
        list1.append(i)
    print("Data is: ", list1)

    Ans = print("Addition is: ", sum(list1))


if __name__ == "__main__":
    main()