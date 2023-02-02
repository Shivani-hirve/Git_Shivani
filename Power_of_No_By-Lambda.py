# Power of 2 number using Lambda Function

power1 = lambda A : (A ** 2)
power2 = lambda B : (B ** 2)

def main():
    No1 = int(input("Enter 1st Number: "))
    No2 = int(input("Enter 2nd Number: "))
    
    Ans1 = power1(No1)
    Ans2 = power2(No2)

    print("Power of 1st number is: ", Ans1)
    print("Power of 2st number is: ", Ans2)    
        
if __name__ == "__main__":
    main()