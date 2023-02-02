# Make a list of N numbers and find the frequency of repeated number
def main():
    size4 = int(input("How many Numbers you want to store in this List: "))

    list4 = []
    
    for i in range (1, size4+1):
        i = int(input("Enter your Elements: "))
        list4.append(i)
        
    print("Input Elments: ", list4)
    
    f = int(input("Element to search: "))
    count = 0
    for n in list4:
        if f == n:
            count += 1
    print("Frequency is: ",count)

if __name__ == "__main__":
    main()