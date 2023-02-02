# Make a list and find the maximum number from that list

def main():
    size2 = int(input("How many elements you want to store in this List: "))

    list2 = []
    for i in range (1, size2+1):
        i = int(input("Enter your Elements: "))
        list2.append(i)
    print("Data is: ", list2)

    print("Maximum number: ", max(list2))

if __name__ == "__main__":
    main()