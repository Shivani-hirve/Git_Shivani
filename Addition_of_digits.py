# Display Addition of given multiple numbers

def main():
    no = int(input("Enter the Numbers: "))
    sum = 0
    while (no > 0):
        i = no % 10
        sum = sum  + i
        no = no//10
    print("Addition is: ", sum)

if __name__ == "__main__":
    main()


# given number : 12345 = 1+2+3+4+5= 15 

no = int(input("Enter the Numbers: "))
sum = 0
for i in range(1, no):
    i = no % 10
    sum = sum  + i
    no = no//10
print("Addition is: ", sum)