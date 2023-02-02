# Multiplication of 2 parameters using Lambda Function

Mul1 = lambda A,B : A*B

def main():
    No1 = int(input("Enter 1st number: "))
    No2 = int(input("Enter 2nd number: "))
    No3 = int(input("Enter 1st Number: "))
    No4 = int(input("Enter 2nd number: "))

    Ans1 = Mul1(No1,No2)
    Ans2 = Mul1(No3,No4)

    print("Multiplication of 1st numbers is: ",Ans1)
    print("Multiplication of 2nd numbers is: ",Ans2)

if __name__ == "__main__":
    main()