def numbers_while():
    No = int(input("Enter Number: "))
    i = 1
    while i <= No:
        print(i, end=' ')
        i += 1

numbers_while()
print()
#Recusrion

No = int(input("Enter Number: "))
def Number(No):
    if No > 0:
        Number(No-1) 
        print(No, end=' ')

Number(No)
print()
