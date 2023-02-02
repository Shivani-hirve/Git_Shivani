def numbers_while():
    No = int(input("Enter Number: "))
    while No >= 1:
        print(No, end=' ')
        No -= 1

numbers_while()
print()
# Recursion

No = int(input("Enter Number: "))
def Number(No):
    if No > 0:
        print(No, end=' ')
        Number(No-1) 

Number(No)
print()
