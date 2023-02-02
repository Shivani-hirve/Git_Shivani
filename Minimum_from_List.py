# Make a list and find the minimum number from that list

def main():
    size3 = int(input("How many Numbers you want to store in this List: "))

    list3 = []
    for i in range (1, size3+1):
        i = int(input("Enter your Elements: "))
        list3.append(i)
    print("Data is: ", list3)

    print("Minimum number: ", min(list3))

if __name__ == "__main__":
    main()