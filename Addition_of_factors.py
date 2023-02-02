# Display addition of factors of given numbers

def main():
    no = int(input("Enter Number: "))
    
    i = 1
    sum = 0
    while (i <= no/2):
        if (no % i == 0):
            sum = sum + i
        i = i + 1
    print("Addition of the Factors is: ",sum)    
        
if __name__ == "__main__":
    main()