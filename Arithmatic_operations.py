# Que1: Arithmatic operations

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
 
def Add(num1,num2):
    Add = num1 + num2
    print ("Addition is: ", Add)
 
def Sub(num1,num2):
    Sub =  num1 - num2
    print ("Subtraction is: ", Sub)

def Mult(num1,num2):
    Mult = num1 * num2
    print ("Multiplication is: ", Mult)
 
def Div(num1,num2):
    Div = num1 / num2
    print ("Division is: ", Div)

if __name__ == "__main__":
    Add(num1,num2)
    Sub(num1,num2)
    Mult(num1,num2)
    Div(num1,num2)