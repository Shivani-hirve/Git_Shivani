#print("*"*5)
def star():
    no = int(input("Enter Number: "))
    i = 1
    while i <= no:
        print("*", end=" ")
        i+=1
star()

print()

#Recursion

no = int(input("Enter Number: "))
def pattern1(no):
    if no > 0:
        pattern1(no - 1)
        print("*", end=" ")
        
pattern1(no)
print()
