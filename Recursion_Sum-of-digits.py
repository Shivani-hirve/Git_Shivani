# write a recursive program which accepts number from user and return summation of its digits

def main():
    no = int(input("Enter the Numbers: "))
    sum = 0
    while (no > 0):
        i = no % 10
        sum = sum  + i
        no = no//10
    print("Summation is: ", sum)

main()
print()

num = int(input("Enter Number: "))
def digit( n ):
    if n == 0:
        return 0
    return (n % 10 + digit(int(n / 10)))
result = digit(num)
print("Summation is", result)
print()