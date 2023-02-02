# Display 12345 as 5:5

def main():
    no = int(input("Enter the Number: "))
    
    for i in range(no):
        for j in range(1,no+1):
            print(j,end=' ')
        print()

if __name__ == "__main__":
    main()