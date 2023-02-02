def fact():
    No = int(input("Enter Number: "))
    i = 1
    while No > 0:
        i = i * No
        No = No - 1
    print("result is: ", i)

fact()

print()
# Recursion

No = int(input("Enter Number: "))
def Factorial(No):
    if No <= 0:
        return 1
    else:
        return (Factorial(No - 1)* No)

Ans = Factorial(No)
print("Factorials are: ", Ans)
print()
