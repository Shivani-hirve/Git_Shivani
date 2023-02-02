def main():
    no = int(input("Enter the Number: "))
    
    for i in range(no+1):
        for j in range(1,i+1, ):
            print(j,end=' ')
        print()

if __name__ == "__main__":
    main()

